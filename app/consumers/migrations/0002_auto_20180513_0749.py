# Generated by Django 2.0.5 on 2018-05-13 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumer',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='consumer',
            name='email',
            field=models.EmailField(help_text='Your Email', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='name',
            field=models.CharField(help_text='Your Name', max_length=300, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4,}$')]),
        ),
    ]