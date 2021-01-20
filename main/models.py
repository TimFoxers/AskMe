from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    birthday = models.DateField(verbose_name='Дата рождения')
    avatar = models.ImageField(verbose_name='Аватар', upload_to='static/img/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']


class Article(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    likes = models.IntegerField(verbose_name='Лайки', default=0)
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.TextField(verbose_name='Текст')
    likes = models.IntegerField(verbose_name='Лайки', default=0)
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    correct = models.BooleanField(verbose_name='Правильно', default=0)
    article = models.ForeignKey('Article', on_delete=models.CASCADE,
                                related_name = "answers",
                                related_query_name = "answer")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'