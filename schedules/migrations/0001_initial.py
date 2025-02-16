# Generated by Django 5.1.3 on 2024-11-26 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0002_alter_branch_options_branch_created_at_and_more'),
        ('groups', '0005_alter_group_branch'),
        ('rooms', '0003_alter_room_branch'),
        ('teachers', '0004_alter_teacher_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('day_of_week', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], verbose_name='Day of Week')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branch')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_schedules', to='groups.group', verbose_name='Group')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_schedules', to='rooms.room', verbose_name='Room')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly_schedules', to='teachers.teacher', verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Weekly Schedule',
                'verbose_name_plural': 'Weekly Schedules',
                'ordering': ['day_of_week', 'start_time'],
                'constraints': [models.UniqueConstraint(fields=('room', 'day_of_week', 'start_time'), name='unique_schedule')],
            },
        ),
    ]
