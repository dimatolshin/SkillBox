from django.db import models


class Image(models.Model):
    name = models.CharField()
    image = models.ImageField(upload_to='')
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'name:{self.name}'

    class Meta:
        verbose_name = '01. Фото'
        verbose_name_plural = '01. Фото'


class CardForPage8(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="Фото студета ")
    description = models.TextField(verbose_name='Отзыв студента ')
    old_job = models.CharField(verbose_name='Предыдущее место работы ')
    new_job = models.CharField(verbose_name='Новое место работы ')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},description:{self.description}'

    class Meta:
        verbose_name = '04. Карточка для страница 8'
        verbose_name_plural = '04. Карточки для страница 8'


class CardForPage13(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="Фото навыка ")
    description = models.CharField(verbose_name='Описание навыка')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},description:{self.description}'

    class Meta:
        verbose_name = '07. Карточка для страница 13'
        verbose_name_plural = '07. Карточки для страница 13'


class CardForPage14(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="Фото")
    description = models.CharField(verbose_name='Имя Фамилия')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},description:{self.description}'

    class Meta:
        verbose_name = '09. Карточка для страница 14'
        verbose_name_plural = '09. Карточки для страница 14'


class CardForPage15(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="Фото")
    description = models.CharField(verbose_name='Описание')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},description:{self.description}'

    class Meta:
        verbose_name = '11. Карточка для страница 15'
        verbose_name_plural = '11. Карточки для страница 15'


class CardForPage16(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name="Фото")
    title = models.CharField(verbose_name='Заголовок')
    description = models.CharField(verbose_name='Описание')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},title:{self.title}'

    class Meta:
        verbose_name = '13. Карточка для страница 16'
        verbose_name_plural = '13. Карточки для страница 16'


class Page5(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(default='Сколько ты хотел(а) б зарабатывать, чтобы удовлетворить свои потребности?',
                             editable=False)
    price1 = models.IntegerField(verbose_name='Первая цена')
    price2 = models.IntegerField(verbose_name='Вторая цена')
    price3 = models.IntegerField(verbose_name='Третья цена')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},price1:{self.price1},price2:{self.price2},price3:{self.price3}'

    class Meta:
        verbose_name = '02. Страница 5'
        verbose_name_plural = '02. Страницы 5'


class Page6(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(default='Насколько ты согласен(на) со следующим утверждением:', editable=False)
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},text:{self.text}'

    class Meta:
        verbose_name = '03. Страница 6'
        verbose_name_plural = '03. Страницы 6'


class Page8(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='У 106+ тысяч студентов уже получилось, а значит и ты сможешь изменить свою жизнь в лучшую сторону!',
        editable=False)

    cards = models.ManyToManyField(CardForPage8, related_name='page8', null=True, blank=True, verbose_name='Карточки')

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name}'

    class Meta:
        verbose_name = '05. Страница 8'
        verbose_name_plural = '05. Страницы 8'


class Page11(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='Как думаешь, какими бы вышли твои дизайны, начни ты прямо сейчас?',
        editable=False)
    head = models.TextField(verbose_name='Заголовок')
    collect_image = models.ManyToManyField(Image, related_name='page11',verbose_name="Коллеция Фото")

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name},head:{self.head}'

    class Meta:
        verbose_name = '06. Страница 11'
        verbose_name_plural = '06. Страницы 11'


class Page13(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='Какие навыки ты бы хотел(а) освоить за прохождение курса?',
        editable=False)
    cards = models.ManyToManyField(CardForPage13, related_name='page13', verbose_name="Коллеция Навыков")

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name}'

    class Meta:
        verbose_name = '08. Страница 13'
        verbose_name_plural = '08. Страницы 13'


class Page14(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='Вот какого результата добились студенты курса',
        editable=False)
    cards = models.ManyToManyField(CardForPage14, related_name='page14', verbose_name="Коллеция Карточек")

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name}'

    class Meta:
        verbose_name = '10. Страница 14'
        verbose_name_plural = '10. Страницы 14'


class Page15(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='Что привлекает в курсе?',
        editable=False)
    cards = models.ManyToManyField(CardForPage15, related_name='page15',  verbose_name="Коллеция Карточек")

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name}'

    class Meta:
        verbose_name = '12. Страница 15'
        verbose_name_plural = '12. Страницы 15'


class Page16(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='Что привлекает в курсе?',
        editable=False)
    head = models.TextField(verbose_name='Заголовок')
    cards = models.ManyToManyField(CardForPage16, related_name='page16', verbose_name="Коллеция Карточек")

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name}'

    class Meta:
        verbose_name = '14. Страница 16'
        verbose_name_plural = '14. Страницы 16'


class Page22(models.Model):
    course_name = models.CharField(verbose_name='Название курса')
    title = models.TextField(
        default='Стоимость курса',
        editable=False)
    full_price = models.IntegerField(verbose_name='Полная стоимость')
    discount = models.IntegerField(verbose_name='Скидка')
    month = models.IntegerField(verbose_name="Месяцев")

    def __str__(self):
        return f'id:{self.id},course_name:{self.course_name}'

    class Meta:
        verbose_name = '15. Страница 22'
        verbose_name_plural = '15. Страницы 22'


class Сourse(models.Model):
    name = models.CharField(verbose_name='Название курса')
    direction = models.CharField(verbose_name='Под направление',null=True,blank=True)
    page5 = models.ForeignKey(Page5, related_name='page5', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 5')
    page6 = models.ForeignKey(Page6, related_name='page6', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 6')
    page8 = models.ForeignKey(Page8, related_name='page8', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 8')
    page11 = models.ForeignKey(Page11, related_name='page11', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 11')
    page13 = models.ForeignKey(Page13, related_name='page13', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 13')
    page14 = models.ForeignKey(Page14, related_name='page14', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 14')
    page15 = models.ForeignKey(Page15, related_name='page15', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 15')
    page16 = models.ForeignKey(Page16, related_name='page16', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 16')
    page22 = models.ForeignKey(Page22, related_name='page22', on_delete=models.SET_NULL,null=True, blank=True, verbose_name='Страница 22')
    url_link= models.URLField(verbose_name='Ссылка для копирования',null=True,blank=True)

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'

    class Meta:
        verbose_name = '16. Курс'
        verbose_name_plural = '16. Курсы'