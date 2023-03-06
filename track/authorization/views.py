from allauth.account.views import (
    LoginView, SignupView,
    LogoutView, PasswordChangeView,
    EmailVerificationSentView, ConfirmEmailView,
    PasswordResetView, PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView, PasswordResetDoneView,
    EmailView
)
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        return context


class UserSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super(UserSignupView, self).get_context_data(**kwargs)
        return context


class UserLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
        context = super(UserLogoutView, self).get_context_data(**kwargs)
        return context


class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_change_done')

    def get_context_data(self, **kwargs):
        context = super(UserPasswordChangeView, self).get_context_data(**kwargs)
        return context


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'home/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super(UserPasswordChangeDoneView, self).get_context_data(**kwargs)
        return context


class UserEmailVerificationSentView(EmailVerificationSentView):
    def get_context_data(self, **kwargs):
        context = super(EmailVerificationSentView, self).get_context_data(**kwargs)
        return context


class UserEmailConfirmationView(ConfirmEmailView):
    def get_context_data(self, **kwargs):
        context = super(UserEmailConfirmationView, self).get_context_data(**kwargs)
        return context


class UserPasswordResetView(PasswordResetView):
    def get_context_data(self, **kwargs):
        context = super(UserPasswordResetView, self).get_context_data(**kwargs)
        return context


class UserPasswordResetFromKeyView(PasswordResetFromKeyView):
    def get_context_data(self, **kwargs):
        context = super(UserPasswordResetFromKeyView, self).get_context_data(**kwargs)
        return context


class UserPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    def get_context_data(self, **kwargs):
        context = super(UserPasswordResetFromKeyDoneView, self).get_context_data(**kwargs)
        return context


class UserPasswordResetDoneView(PasswordResetDoneView):
    def get_context_data(self, **kwargs):
        context = super(UserPasswordResetDoneView, self).get_context_data(**kwargs)
        return context


class UserEmailView(EmailView):
    def get_context_data(self, **kwargs):
        context = super(UserEmailView, self).get_context_data(**kwargs)
        return context
