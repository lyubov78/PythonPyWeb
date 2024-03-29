from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        # TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer2 = None  # Entry.objects.annotate(author=Count('author').order_by('-author').first()

        # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer3 = None  # Entry.objects.filter(Q(tags='Кино') | Q(tags='Музыка'))

        # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = Author.objects.filter(gender='ж').count()

        # TODO Какой процент авторов согласился с правилами при регистрации?
        agree = Author.objects.filter(status_rule=True).count()
        total_authors = Author.objects.count()
        self.answer5 = round(agree * 100 / total_authors)

        # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1, 5))

        # TODO Какой автор имеет наибольший возраст?
        self.answer7 = Author.objects.order_by('age').first()

        # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()

        # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = Author.objects.filter(age__lt=25)

        # TODO Сколько статей написано каждым автором?
        self.answer10 = None  # Entry.objects.annotate(number_of_entries=Count('author')).values('author', 'number_of_entries')

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
