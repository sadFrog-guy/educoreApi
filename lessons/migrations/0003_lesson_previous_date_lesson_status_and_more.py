# Generated by Django 5.1.3 on 2024-11-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lessonstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='previous_date',
            field=models.DateTimeField(blank=True, help_text='Если урок перенесён, укажите дату, с которой он был перенесён.', null=True, verbose_name='Предыдущая дата'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Запланирован'), ('in_progress', 'В процессе'), ('completed', 'Проведён'), ('canceled', 'Отменён'), ('not_held', 'Не состоялся'), ('rescheduled', 'Перенесён')], default='scheduled', max_length=20, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='lessonstudent',
            name='reason',
            field=models.TextField(blank=True, null=True, verbose_name='Причина (если указана)'),
        ),
        migrations.AddField(
            model_name='lessonstudent',
            name='status',
            field=models.CharField(choices=[('pending', 'Ожидается'), ('present', 'Присутствует'), ('absent', 'Отсутствует без причины'), ('sick', 'Отсутствует по болезни'), ('late', 'Опоздал'), ('excused', 'Освобожден'), ('removed', 'Удалён'), ('other', 'Другое')], default='pending', max_length=20, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='lessonstudent',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время записи'),
        ),
    ]
