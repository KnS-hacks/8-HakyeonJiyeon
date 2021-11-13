# Generated by Django 3.2.9 on 2021-11-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_id', models.CharField(max_length=10, verbose_name='고객 아이디')),
                ('cus_pw', models.CharField(max_length=20, verbose_name='고객 비밀번호')),
                ('cus_name', models.CharField(max_length=20, verbose_name='고객 이름')),
                ('cus_address', models.TextField(max_length=100, verbose_name='고객 주소')),
            ],
        ),
    ]