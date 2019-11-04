from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from app.forms import aForm, aFormfromhome, LoginForm, RegisterForm
from app.models import Classroom, Professor, Student, Post, Lecture, Event, Message, Login, Account
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
import datetime
import random
import string
from django.core.mail import send_mail
from project import settings

#VIEW FOR LOGIN PAGE
def login(request):
    if not request.session.is_empty():
        return render(request, 'redir.html', {})
    else:
        return render(request, "index.html", {})

#PROCESS FOR LOGGING IN
def makelogins(request):
    MyLoginForm = LoginForm(request.POST)

    if MyLoginForm.is_valid():
        email = MyLoginForm.clean_message()
        password = MyLoginForm.cleaned_data['password']
        login = Login.objects.get(email=email)

        if not pbkdf2_sha256.verify(password, login.password):
            return HttpResponse('wrong password')
        if login.category == "STUDENT":
            context = {
                'posts': Post.objects.all(),
                'events': Event.objects.all(),
                'account': Student.objects.select_related().get(account__login__email=email),
                'students': Student.objects.all(),
            }
            
        elif login.category == "PROFESSOR":
            context = {
                'posts': Post.objects.all(),
                'events': Event.objects.all(),
                'account': Professor.objects.select_related().get(account__login__email=email),
                'students': Student.objects.all(),
            }

        request.session['start'] = True
        request.session['email'] = email
        request.session['category'] = login.category
        request.session.save()

    else:
        return HttpResponse('form invalid')

    if not login.verified:
        return render(request, 'verification.html', context)

    else:
        return render(request, 'redir.html', {})

#VIEW FOR HOME PAGE
def home(request):
    if request.session.is_empty():
        return redirect('/')

    email_session = request.session.get('email')

    if email_session == None:
        return redirect('/logout/')

    login = Login.objects.get(email=email_session)
    
    if login.category == "STUDENT":
        context = {
            'posts': Post.objects.all(),
            'events': Event.objects.all(),
            'account': Student.objects.select_related().get(account__login__email=email_session),
            'students': Student.objects.all(),
        }
    elif login.category == "PROFESSOR":
        context = {
            'posts': Post.objects.all(),
            'events': Event.objects.all(),
            'account': Professor.objects.select_related().get(account__login__email=email_session),
            'students': Student.objects.all(),
        }

    return render(request, "home.html", context)

#VIEW FOR DASHBOARD PAGE
def dashboard(request):
    if request.session.is_empty():
        return redirect('/')

    email_session = request.session.get('email')

    if email_session == None:
        return redirect('/logout/')

    login = Login.objects.get(email=email_session)
    
    if login.category == "STUDENT":
        context = {
            'posts': Post.objects.all(),
            'events': Event.objects.all(),
            'account': Student.objects.select_related().get(account__login__email=email_session),
            'students': Student.objects.all(),
        }
    elif login.category == "PROFESSOR":
            context = {
                'posts': Post.objects.all(),
                'events': Event.objects.all(),
                'account': Professor.objects.select_related().get(account__login__email=email_session),
                'students': Student.objects.all(),
            }


    return render(request, 'dashboard.html', context)
    
# THIS FUNCTION CREATE POST AND SEND IT TO DATABASE
def help(request):
    myform = aForm(request.POST)
    if myform.is_valid():
        text = myform.cleaned_data['text']
        return HttpResponse(text)

    else:
        return HttpResponse(myform.errors['hello'])

#RANDOM STRING GENERATOR
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#PROCESS FOR REGISTERING FOR STUDENTS
def registerstudent(request):
    MyRegisterForm = RegisterForm(request.POST)

    if request.method == "POST":
        if MyRegisterForm.is_valid():
            email = MyRegisterForm.cleaned_data['email']
            password = MyRegisterForm.cleaned_data['password']
            category = "STUDENT"
            school_id = MyRegisterForm.cleaned_data['school_id']
            first_name = MyRegisterForm.cleaned_data['first_name']
            last_name = MyRegisterForm.cleaned_data['last_name']


            obj = Login.objects.all()
            for objs in obj:
                if email == objs.email:
                    return HttpResponse("Email already exists")

            login = Login()

            login.category = category
            login.email = email
            login.password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
            login.verification_string = randomString(10)
            login.verified = False
            login.save()

            send_mail(
                'Your QuickLynx Verification Code',
                login.verification_string,
                settings.EMAIL_HOST_USER,
                [login.email]
            )

            account = Account()
            
            account.first_name = first_name
            account.last_name = last_name
            account.school_id = school_id
            account.login = login
            account.save()

            student = Student()
            student.account = account
            student.save()

        else:
            return HttpResponse("FORM INVALID")

    return redirect('/')


#PROCESS FOR REGISTERING AS PROFESSOR
def registerprofessor(request):
    MyRegisterForm = RegisterForm(request.POST)

    if request.method == "POST":
        if MyRegisterForm.is_valid():
            email = MyRegisterForm.cleaned_data['email']
            password = MyRegisterForm.cleaned_data['password']
            category = "PROFESSOR"
            school_id = MyRegisterForm.cleaned_data['school_id']
            first_name = MyRegisterForm.cleaned_data['first_name']
            last_name = MyRegisterForm.cleaned_data['last_name']


            obj = Login.objects.all()
            for objs in obj:
                if email == objs.email:
                    return HttpResponse("Email already exists")

            login = Login()

            login.category = category
            login.email = email
            login.password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
            login.verification_string = 'eakdkvieoppaldkfklalebdk'
            login.verified = False
            login.save()

            account = Account()
            
            account.first_name = first_name
            account.last_name = last_name
            account.school_id = school_id
            account.login = login
            account.save()

            professor = Professor()
            professor.account = account
            professor.save()

        else:
            return HttpResponse(MyRegisterForm.errors)

    return redirect('/')

#VIEW FOR REGISTER PAGE FOR STUDENTS
def register_as_student(request):
    return render(request, "register-students.html", {})

#VIEW FOR REGISTER PAGE FOR PROFESSORS
def register_as_professor(request):
    return render(request, "register-prof.html", {})

#VIEW FOR VERIFICATION PAGE
def verification(request):
    return render(request, "verification.html", {})

#PROCESS FOR VERFICATIONS
def makeverifications(request):
    email_session = request.session.get('email')
    email = email_session
    login = Login.objects.get(email=email_session)
    login.verified = True
    login.save()

    return render(request, 'redir.html', {})

#PROCESS FOR LOGGING OUT
@never_cache
def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')

#CLASSROOM VIEW
def classroom(request, room_name):
    if request.session.is_empty():
        return redirect('/')

    email_session = request.session.get('email')

    if email_session == None:
        return redirect('/logout/')

    login = Login.objects.get(email=email_session)
    
    if login.category == "STUDENT":
        context = {
            'posts': Post.objects.all(),
            'events': Event.objects.all(),
            'account': Student.objects.select_related().get(account__login__email=email_session),
            'students': Student.objects.all(),
            'classroom': Classroom.objects.get(room_name=room_name)
        }
    elif login.category == "PROFESSOR":
            context = {
                'posts': Post.objects.all(),
                'events': Event.objects.all(),
                'account': Professor.objects.select_related().get(account__login__email=email_session),
                'students': Student.objects.all(),
                'classroom': Classroom.objects.get(room_name=room_name)
            }

    return render(request, 'classroom.html', context)

def makepost(request, room_name):
    email = request.session.get('email')
    category = request.session.get('category')
    if category == 'STUDENT':
        acct = Student.objects.select_related().get(account__login__email=email)
    elif category == 'PROFESSOR':
        acct = Professor.objects.select_related().get(account__login__email=email)

    MyPostForm = aForm(request.POST)
    if request.method == "POST":
        if MyPostForm.is_valid():
            text = MyPostForm.cleaned_data['text']

            post = Post()

            post.text = text
            post.date = datetime.datetime.now()
            account = acct.account
            post.account = account
            post.classroom = Classroom.objects.get(room_name=room_name)
            post.save()
    
    return redirect('/classroom/{}'.format(room_name))

def makepostfromhome(request):
    email = request.session.get('email')
    category = request.session.get('category')
    if category == 'STUDENT':
        acct = Student.objects.select_related().get(account__login__email=email)
    elif category == 'PROFESSOR':
        acct = Professor.objects.select_related().get(account__login__email=email)

    MyPostForm = aFormfromhome(request.POST)
    if request.method == "POST":
        if MyPostForm.is_valid():
            print('the form is valid')
            text = MyPostForm.cleaned_data['text']
            classroom = MyPostForm.cleaned_data['classroom']

            post = Post()

            post.text = text
            post.date = datetime.datetime.now()
            account = acct.account
            post.account = account
            post.classroom = Classroom.objects.get(room_name=classroom)
            post.save()
        else:
            return HttpResponse("select a classroom")
    return redirect('/home/')