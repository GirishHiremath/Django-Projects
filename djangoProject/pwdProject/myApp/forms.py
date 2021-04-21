from django import forms

class SignUpForm(forms.Form):
    name=forms.CharField()
    pwd=forms.CharField(widget=forms.PasswordInput)
    rpwd=forms.CharField(label="re-enter the pwd",widget=forms.PasswordInput)
    email=forms.EmailField()

    def clean(self):
        pwd=self.cleaned_data['pwd']
        rpwd=self.cleaned_data['rpwd']
        if(pwd!=rpwd):
            raise Exception("password mismatch...!")
