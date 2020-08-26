from django.views.generic import FormView
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseServerError, HttpResponseNotAllowed
from django.utils.encoding import force_bytes
from django.db.models import Q

from user.models import Member
from user.forms.sign_up import SignUpForm
from user.tokens import account_activation_token
from user.utils.email import build_template_email


class SignUp(FormView):
    form_class = SignUpForm    

    template_name = 'sign_up.html'

    success_url = '/'

    def create_template_email_context(self, form, member):        
        return {
            'user': member,
            'domain': get_current_site(self.request).domain,
            'uid': urlsafe_base64_encode(force_bytes(member.id)),
            'token': account_activation_token.make_token(member)
        }

    # 이 메소드는 POST 요청일 때만 실행됨 
    def form_valid(self, form):
        try:
            member = Member.objects.get(
                Q(student_id=form.data['student_id']) &
                Q(first_name=form.data['name'][1:]) &
                Q(last_name=form.data['name'][:1])
            )
            member.username = form.data['nickname']
            member.email = form.data['email']
            member.password = make_password(form.data['password'])
            member.did_sign_up = True
            member.save()
        except:
            return HttpResponseNotAllowed("부원으로 등록되어 있지 않습니다. 관리자에게 문의하여 주십시오.")

        try:
            email = build_template_email(
                title='계정 활성화 확인 이메일', 
                template_name='email_body/activation.html', 
                context=self.create_template_email_context(form.data, member),
                to=form.data['email']
            )
            email.send()
            return super().form_valid(form)
        except:
            member.delete()
            return HttpResponseServerError("500 내부 서버 오류. 이메일 전송에 실패하였습니다. 회원가입을 다시 진행해 주세요.")
