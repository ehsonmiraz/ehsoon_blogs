from django import forms

class SignUpForm(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailInput()
    password=forms.PasswordInput()
    confrim_password=forms.PasswordInput()

    def confirm_password(self):
        return self.password==self.confrim_password