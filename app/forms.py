from django import forms
from app.models import Login


class aForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class aFormfromhome(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    classroom = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput())

    def clean_message(self):
        user = self.cleaned_data.get("email")

        dbuser = Login.objects.filter(email = user)

        if not dbuser:
            raise forms.ValidationError("USER DOES NOT EXISTS IN OUR DB!")
        return user

    def clean_message_pass(self):
        passw = self.cleaned_data.get('password')

        dbpass = Login.objects.filter(password = passw)

        if not dbpass:
            raise forms.ValidationError("INVALID EMAIL OR PASSWORD!")
        return passw


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    school_id = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)
