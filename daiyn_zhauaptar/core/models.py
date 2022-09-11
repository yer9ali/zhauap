import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Model, DateTimeField
from django.utils.translation import gettext_lazy as _

from daiyn_zhauaptar.users.models import User


class AbstractDateTime(Model):
    datetime_created = DateTimeField("Время создания", auto_now_add=True)
    datetime_updated = DateTimeField("Время обновления", auto_now=True)

    class Meta:
        abstract = True


class Payment(AbstractDateTime):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'payment'


class Subscription(AbstractDateTime):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    class_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    activation_date = models.DateTimeField(_('activation_date'))
    expiration_date = models.DateTimeField(_('expiration_date'))

    payment = models.ForeignKey(Payment, db_column='payment_id', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'subscription'


class Book(AbstractDateTime):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('описание'), max_length=10000, blank=True)
    author = models.CharField(_('автор'), max_length=100, blank=True)
    publisher = models.CharField(_('издатель'), max_length=100, blank=True)

    clas = models.IntegerField(_('класс'), validators=[MinValueValidator(1), MaxValueValidator(12)])
    year_published = models.CharField(_('год публикации'), max_length=4, blank=True, default='')
    image = models.FileField(_('картинка'), upload_to='content/', blank=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f'{self.name} - {self.clas}'


# class CustomUser(AbstractUser):
#     id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
#     username = models.CharField(_('username'), unique=True, max_length=100, null=False)
#     email = models.EmailField(_('email'), unique=True, max_length=100, null=False)
#     password = models.CharField(_('password'), max_length=100)
#
#     is_staff = models.BooleanField(_('is_staff'), default=True)
#     is_active = models.BooleanField(_('is_active'), default=True)
#     is_superuser = models.BooleanField(_('is_superuser'), default=False)
#
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(default=timezone.now)
#
#     books = models.ManyToManyField('Book', through='UserBook')
#
#     USERNAME_FIELD = 'username'
#
#     class Meta:
#         db_table = 'custom_user'


class UserBook(AbstractDateTime):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, db_column="user_id", related_name="user", on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, db_column="book_id", on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_book'


class Answer(AbstractDateTime):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, verbose_name=_('книга'), db_column='book_id', on_delete=models.CASCADE)
    number = models.IntegerField(_('номер ответа'), blank=True)
    photo = models.FileField(_('картинка'), upload_to='content/', blank=True)

    class Meta:
        db_table = 'answer'


class MainBooks(AbstractDateTime):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.FileField(_('картинка'), upload_to='content/', blank=True)
    book = models.OneToOneField(Book, unique=True, verbose_name=_('книга'),
                                db_column='book_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'main_book'
