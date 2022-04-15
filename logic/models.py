import datetime

import dateparser
from django.db import models


# Create your models here.
from django.utils import timezone


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Rank(models.TextChoices):
    """Звания, которые могут быть у курируемых"""
    ONE = '01', _('Рядовой соботыльник')
    TWO = '02', _('Младший сержант бота')
    THREE = '03', _('Сержант олимпиад')
    FOUR = '04', _('Старшина перечней')
    FIVE = '05', _('Товарищ прапорщик')
    SIX = '06', _('Старший соботыльник')
    SEVEN = '07', _('Лейтенант учёбы')
    EIGHT = '08', _('Капитан региона')
    NINE = '09', _('Майор тайм-менеджмента')
    TEN = '10', _('Полковник-бвишник')
    ELEVEN = '11', _('Генерал всерос(с)а')
    TWELVE = '12', _('Магистр книг и пособий')
    THIRTEEN = '13', _('Повелитель бота')
    FOURTEEN = '14', _('Император всея Бота и Учёбы')


class WeekDay(models.TextChoices):
    """День недели"""
    MONDAY = '1', _('понедельник')
    TUESDAY = '2', _('вторник')
    WEDNESDAY = '3', _('среда')
    THURSDAY = '4', _('четверг')
    FRIDAY = '5', _('пятница')
    SATURDAY = '6', _('суббота')
    SUNDAY = '7', _('воскресенье')


class Group(models.TextChoices):
    """Группа"""
    PRO = 'P', _('Pro')
    LITE = 'L', _('Lite')


class Curator(models.Model):
    """
        Профиль куратора (для того, чтобы не возится с User тут лежит вся нужная инфа)
        user.username - Имя на сайте (не ник в телеге)
        user.first_name - имя
        user.last_name - фамилия
        user.email - мыло (хз зачем, но оно есть)
        user.password - хэш и метаданные о пароле (обязательное поле)
        user.is_staff - булево, False
        user.is_active - булево, на будущее
        user.is_superuser - не трогать, на будущее
        user.last_login - не трогать, на будущее
        user.date_joined - дата создания аккаунта
    """

    chat_id = models.IntegerField('id чата в телеге', null=True, editable=False)
    username = models.CharField('ник', max_length=32)

    notes = models.TextField('заметки', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='сuratorProfile', null=True)

    def __str__(self):
        return f'{self.username} {self.user.get_full_name()}'

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


class Padawan(models.Model):
    chat_id = models.IntegerField('id чата в телеге', null=True, editable=False)
    username = models.CharField('ник', max_length=32)

    telephone = models.CharField('телефон', max_length=16, blank=True)
    notes = models.TextField('заметки', blank=True)
    rank = models.CharField('звание', choices=Rank.choices, default=Rank.ONE, max_length=2)
    off_date = models.DateField('окончание оплаченного периода', auto_now_add=True)
    weekend = models.CharField('выходной', choices=WeekDay.choices, default=WeekDay.SUNDAY, max_length=1)
    group = models.CharField('группа', choices=Group.choices, default=Group.LITE, max_length=1)
    utc = models.IntegerField('временной сдвиг', default=3, validators=[MinValueValidator(-12), MaxValueValidator(12)])
    rating = models.IntegerField('рейтинг', default=0, validators=[MinValueValidator(-20)])
    curator = models.ForeignKey(Curator, on_delete=models.SET_NULL, related_name='padawans', null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Подаван'
        verbose_name_plural = 'Подваны'
        ordering = ["-off_date"]

    @staticmethod
    def search(chat_id: int):
        return Padawan.objects.get(chat_id=chat_id)

    def create_task(self, description: str):
        text = ''
        for i in range(len(description)):
            if description[i] != '|':
                text = text + description[i]
            else:
                break
            description = description[1:]
        description = description[1:]
        task = self.tasks.create(text=text, end=dateparser.parse(description))
        task.save()
        return task


class Code(models.Model):
    days = models.IntegerField('время', default=31, validators=[MinValueValidator(0)])
    activations = models.IntegerField('активации', default=0, validators=[MinValueValidator(0)])
    text = models.SlugField('текст')
    users = models.ManyToManyField(Padawan, blank=True, related_name='codes')

    def __str__(self) -> str:
        return f'{self.text} на {self.days} сталось: {self.activations - len(self.users.all())}'

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'
        ordering = ["-days"]


class Task(models.Model):
    text = models.SlugField('описание')
    end = models.DateTimeField('дата сдачи')
    padawan = models.ForeignKey(Padawan, on_delete=models.CASCADE, related_name='tasks')
    start = models.DateTimeField('дата создания задачи', auto_now_add=True, null=True)
    proof = models.ImageField('пруф', null=True)

    def __str__(self) -> str:
        return f'{self.padawan}: {self.text} | {self.end}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
