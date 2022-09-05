from django.contrib import admin

from daiyn_zhauaptar.core.models import Book, Answer, MainBooks, Subscription


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'clas')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('number', 'photo', 'book')


@admin.register(MainBooks)
class MainBooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'book')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
