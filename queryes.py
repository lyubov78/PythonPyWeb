import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы
    print(Entry.objects.get(id__exact=2))
    print(Entry.objects.filter(headline__contains='пут'))
    print(Entry.objects.filter(id__in=[3, 4]))
    print(Entry.objects.filter(rating__gte=5))
    print(Author.objects.filter(email__endswith='com'))
    print(AuthorProfile.objects.filter(bio__isnull=True))
    print(Author.objects.count())


    obj = Entry.objects.filter(author__name__contains='author')
    print(obj)












