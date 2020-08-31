import json

from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse

from recruit.forms.question import QuestionForm
from recruit.models import Recruitment, Question, Applicant, Answer


class QuestionFormView(FormView):
    form_class = QuestionForm

    template_name = 'recruit/question.html'

    success_url = '/'

    applicant_profile = {}

    def form_valid(self, form):
        recruitment = Recruitment.objects.order_by('year', 'semester').first()

        ids = list(form.data.keys())[1:]

        questions = Question.objects.filter(id__in=map(int, ids), recruitment=recruitment)
        questions = list(questions)

        applicant = Applicant(
            recruitment=recruitment,
            name=self.applicant_profile['username'],
            student_id=self.applicant_profile['student_id'],
            email=self.applicant_profile['email'],
            phone_number=self.applicant_profile['phone_number'],
            passed=False
        )
        applicant.save()

        answers = []
        for q in questions:
            answers.append(
                Answer(
                    question=q,
                    answer=str(form.data[str(q.pk)]),
                    applicant=applicant
                )
            )
        Answer.objects.bulk_create(answers)

        return super().form_valid(form)

    def get(self, *args, **kwargs):
        try:
            profile = self.request.COOKIES.get('profile')
            profile = json.loads(profile)

            for key in ('username', 'student_id', 'email', 'phone_number'):
                if type(profile[key]) is not str:
                    raise Exception()
                else:
                    self.applicant_profile[key] = profile[key]
            
            return super().get(*args, **kwargs)
        except:
            return HttpResponseRedirect(reverse('recruit'))
