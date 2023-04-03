from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView

from account.forms import UserSignUpForm, LoginForm, UserProfileForm


class UserSignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')

        user = get_user_model().objects.filter(username=username).only('id').first()
        if user is not None:
            user.is_active = True
            user.save(update_fields=['is_active'])

        url = super().get_redirect_url(*args, **kwargs)
        return url


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')
    model = get_user_model()
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user


'''
1. email + password + confirm password (get email)
2. email (get email) + password + confirm
3. email (get email) 7 days
4. phone, passport, id, code(confirm) password
5. admin -> (user get email) -> user signs up
Create User Form
email
password
password_confirm
Send email
Activate
/account/activate/<key>/
'''


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
