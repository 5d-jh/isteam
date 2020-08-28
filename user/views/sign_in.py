from django.views.generic import FormView
from django.contrib.auth import authenticate, login

from user.forms.sign_in import SignInForm
from user.models import Member


class SignIn(FormView):
    form_class = SignInForm

    template_name = 'sign_in.html'

    success_url = '/groupware/activities'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '로그인'
        return context

    def form_valid(self, form):
        nickname = form.data['nickname']
        password = form.data['password']
        member = authenticate(self.request, username=nickname, password=password)

        if member is not None and member.did_sign_up:
            login(self.request, member)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
