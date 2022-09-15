from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from datetime import datetime
from daiyn_zhauaptar.core.forms import UserRegistrationForm
from daiyn_zhauaptar.core.models import Book, MainBooks, Subscription, Answer, ImageAnswer
from daiyn_zhauaptar.users.models import User


def side_block_dict(request):
    subject_dict = {}
    subject_info = Book.objects.values('clas', 'name').order_by('clas').distinct()
    for i in subject_info:
        clas = i['clas']
        name_list = []
        for j in subject_info:
            if j['clas'] == clas:
                name_list.append(j['name'])
        subject_dict[clas] = set(name_list)
    return subject_dict.items()


def register_request(request):
    user_form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        check_username = User.objects.filter(username=request.POST.get('username'))

        if user_form.is_valid() and not check_username:
            new_user = user_form.save()
            login(request, new_user)
            return redirect('index')

    return render(request, 'registration/registration.html', {'form': user_form})


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'not_exists': True})
    return render(request, 'registration/login.html')


def logout_request(request):
    logout(request)
    return redirect('index')


def password_reset_request(request):
    if request.method == "POST":

        data = request.POST['email']
        associated_users = User.objects.filter(Q(email=data))
        if associated_users.exists():
            for user in associated_users:
                subject = "Password Reset Requested"
                email_template_name = "registration/password_reset_email.txt"
                c = {
                    "email": user.email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'admin@zhauap.kz', [user.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('index')

    return render(request=request, template_name="registration/password_reset_form.html", )


def payment(request):
    return render(request, 'pages/payment.html')


def subscription(request):
    subs_list = sorted(list(
        Subscription.objects.filter(expiration_date__gt=datetime.now())
        .filter(user_id=request.user.id).values_list('class_number', 'activation_date',
                                                     'expiration_date')))

    return render(request, 'pages/subscription.html',
                  {'subs_list': subs_list})


def index(request):
    main_book_dict = dict(MainBooks.objects.values_list('book_id', 'photo'))
    book_dict = {}
    for book_id, photo in main_book_dict.items():
        book_name = Book.objects.get(id=book_id).name
        subject_info = Book.objects.filter(name__contains=book_name).values('clas').order_by('clas').distinct()
        book_detail_dict = {'subject_info': subject_info, 'photo': photo}
        book_dict[book_name] = book_detail_dict

    return render(request, 'index.html',
                  {'book_dict': book_dict,
                   'subject_dict': side_block_dict(request)})


def render_html_detail(request, book_info, clas):
    # answer_list = sorted(list(Answer.objects.filter(book_id=book_info[0][0]).values_list('number')))
    answer_list = sorted(list(
        ImageAnswer.objects.select_related('answer').filter(answer__book_id=book_info[0][0]).values_list(
            'answer__number',
            'image')))

    expiration_date = Subscription.objects.filter(user_id=request.user.id, class_number=clas)
    expire = True

    if expiration_date:
        date = expiration_date.values_list('expiration_date').first()[0]
        if date >= timezone.now():
            expire = False

    answer_number_list = []
    count = 0
    for answer in answer_list:
        if answer[0] != count:
            count = answer[0]
            answer_number_list.append(answer[0])

    return render(request, 'pages/detail.html',
                  {
                      'book_name': book_info[0][1],
                      'book_clas': book_info[0][2],
                      'book_description': book_info[0][3],
                      'book_author': book_info[0][4],
                      'book_image': book_info[0][5],
                      'book_publisher': book_info[0][6],
                      'book_year_published': book_info[0][7],
                      'answer_list': answer_list,
                      "answer_number_list": answer_number_list,
                      'subject_dict': side_block_dict(request),
                      'expire': expire
                  }
                  )


def detail_book_by_id(request, book_id, clas):
    book = Book.objects.filter(id=book_id)
    book_info = list(
        book.values_list('id', 'name', 'clas', 'description', 'author', 'image', 'publisher', 'year_published',
                         'language'))
    return render_html_detail(request, book_info, clas)


def detail(request, book_name, clas):
    book = Book.objects.filter(name__contains=book_name, clas=clas)
    book_info = list(
        book.values_list('id', 'name', 'clas', 'description', 'author', 'image', 'publisher', 'year_published',
                         'language'))

    if len(book) > 1:
        return render(request, 'pages/many_book.html', {
            'subject_dict': side_block_dict(request),
            'book_info': book_info
        })
    return render_html_detail(request, book_info, clas)
