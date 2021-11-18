# Generated by Django 3.2.9 on 2021-11-18 04:15

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_auto_20211116_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_id', models.CharField(blank=True, max_length=10, unique=True, verbose_name='고객 아이디')),
                ('cus_pw', models.CharField(blank=True, max_length=200, verbose_name='고객 비밀번호')),
                ('cus_nickname', models.CharField(blank=True, max_length=20, unique=True, verbose_name='고객 별명')),
                ('cus_address', models.TextField(blank=True, max_length=100, verbose_name='고객 주소')),
                ('cus_sig_data', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date signup costomer')),
                ('recommended_person', models.CharField(blank=True, max_length=20, verbose_name='추천인')),
            ],
            options={
                'verbose_name': '고객 가입 정보',
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(blank=True, max_length=100, verbose_name='라이더 이름')),
                ('rider_intro', models.TextField(blank=True, max_length=100, verbose_name='라이더 소개')),
                ('rider_area', models.CharField(blank=True, choices=[('GG', '경기도'), ('SL', '서울시'), ('CC', '충청도'), ('GS', '경상도'), ('GW', '강원도'), ('JL', '전라도'), ('JJ', '제주도')], max_length=2, verbose_name='배달 지역')),
                ('rider_vehicle', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('NL', '뚜벅이'), ('CR', '차'), ('BC', '자전거'), ('AB', '오토바이')], max_length=11, verbose_name='배달 수단')),
                ('min_delivery_amount', models.IntegerField(blank=True, verbose_name='최소 주문 금액')),
                ('bankbook', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='통장 사본')),
                ('license', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='면허증 사본')),
                ('recommended_person', models.CharField(blank=True, max_length=20, verbose_name='추천인')),
            ],
            options={
                'db_table': 'rider',
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
