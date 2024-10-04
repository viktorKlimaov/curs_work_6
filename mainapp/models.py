from django.db import models

class Mailing(models.Model):

    STARTED = 'started'
    CREATED = 'created'
    COMPLETED = 'completed'

    STATES_CHOICES = {
        STARTED: 'Запущена',
        CREATED: 'Создана',
        COMPLETED: 'Завершена'
    }

    ONCE_DAY = "once_day"
    ONCE_MONTH = "once_month"
    ONCE_WEEK = "once_week"

    PERIODICITY_CHOICES = {
        ONCE_DAY: "Раз в день",
        ONCE_WEEK: "Раз в неделю",
        ONCE_MONTH: "Раз в месяц",
    }

    data_time = models.DateTimeField(verbose_name='Дата и время первой отправки рассылки', blank=True, null=True)
    periodicity = models.CharField(verbose_name='Периодичность', max_length=10,
                                   choices=PERIODICITY_CHOICES, default=ONCE_DAY)

    status = models.CharField(verbose_name='Статус рассылки', max_length=9, choices=STATES_CHOICES, default=CREATED)
    client = models.ManyToManyField(to='Client', verbose_name='Клиенты')
    message = models.ForeignKey(to='Message',on_delete=models.CASCADE, verbose_name='Сообщение')


    class Meta:
        verbose_name = 'Рассылка '
        verbose_name_plural = 'Рассылки'


################################################

class Message(models.Model):
    subject_letter = models.CharField(max_length=350, verbose_name='Тема письма')
    body_letter = models.TextField(verbose_name='Тело письма')

    class Meta:
        verbose_name = 'Письмо '
        verbose_name_plural = 'Письма'

    def __str__(self):
        return f'{self.subject_letter}'

################################################

# class MailingLog(models.Model):
#     data_time = models.DateTimeField(verbose_name='Дата и время первой отправки рассылки', blank=True, null=True)
#     is_attempt = models.BooleanField(default=True, verbose_name='Признак публикации')
#     email_answer = models

################################################


class Client(models.Model):
    email = models.EmailField(verbose_name='Почта',unique=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=True, null=True)
    father_name = models.CharField(max_length=150, verbose_name='Отчество', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    class Meta:
        verbose_name = 'Клиент '
        verbose_name_plural = 'Клиенты'


    def __str__(self):
        return f'{self.email}'

















