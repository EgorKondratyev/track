from allauth.account.forms import LoginForm


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'special'})
        self.fields['login'].widget.attrs.update({'class': 'special'})
        self.fields['remember'].widget.attrs.update({'class': 'special'})
