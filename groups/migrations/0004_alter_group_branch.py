# Generated by Django 5.1.3 on 2024-11-26 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_alter_branch_options_branch_created_at_and_more'),
        ('groups', '0003_group_end_date_group_start_date_group_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='branches.branch'),
        ),
    ]
