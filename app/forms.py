from django import forms
from app.models import Login


class aForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class aFormfromhome(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    classroom = forms.CharField(max_length=50)


class ClassroomForm(forms.Form):
    room_name = forms.CharField(max_length=50)
    time_start = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])
    time_end = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])
    days = forms.CharField(max_length=10)
    date_start = forms.DateField()
    date_end = forms.DateField()
    year_start = forms.CharField(max_length=4)
    semester = forms.CharField(max_length=25)
    headerpix = forms.ImageField()


class JoinClassroomForm(forms.Form):
    token = forms.CharField(max_length=50)


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


class EditClassroomForm(forms.Form):
    room_name = forms.CharField(max_length=50)
    time_start = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])
    time_end = forms.TimeField(input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])
    days = forms.CharField(max_length=10)
    date_start = forms.DateField()
    date_end = forms.DateField()
    year_start = forms.CharField(max_length=4)
    semester = forms.CharField(max_length=25)

class EditHeaderForm(forms.Form):
    headerpix = forms.ImageField()


class EditAccountForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class AddLectureForm(forms.Form):
    no = forms.FloatField()
    title = forms.CharField()
    file_loc = forms.FileField()