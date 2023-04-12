from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm, AddEmailForm


class MyAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(MyAddEmailForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({'class': 'form-control'})


class MyCustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        self.fields["email"].widget.attrs.update({'class': 'form-control'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control'})


class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget.attrs.update({'class': 'form-control'})
        self.fields["password"].widget.attrs.update({'class': 'form-control'})
        # self.fields["remember"].widget.attrs.update({'class': 'checkbox-inline'})


class MyCustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields["oldpassword"].widget.attrs.update({'class': 'form-control'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control'})
