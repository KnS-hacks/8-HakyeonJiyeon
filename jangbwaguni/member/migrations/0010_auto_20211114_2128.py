# Generated by Django 3.2.9 on 2021-11-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_auto_20211114_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cus_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='고객 이름'),
        ),
        migrations.AddField(
            model_name='user',
            name='cus_pw',
            field=models.CharField(blank=True, max_length=20, verbose_name='고객 비밀번호'),
        ),
    ]