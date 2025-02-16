# Generated by Django 5.1.3 on 2024-11-25 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='status',
            field=models.CharField(choices=[('RECRUITING', 'Набирается'), ('ACTIVE', 'Учится'), ('COMPLETED', 'Завершена'), ('INACTIVE', 'Неактивна')], default='RECRUITING', max_length=100),
        ),
    ]
