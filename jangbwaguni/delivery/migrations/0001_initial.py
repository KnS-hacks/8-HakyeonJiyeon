# Generated by Django 3.2.9 on 2021-11-12 06:26

from django.db import migrations, models
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=20, verbose_name='주문자')),
                ('cus_address', models.CharField(max_length=250, verbose_name='주문자 주소')),
                ('order_product', multiselectfield.db.fields.MultiSelectField(choices=[('N', 'Null'), ('E', 'Egg'), ('M', 'Milk'), ('R', 'Rice'), ('W', 'Water')], max_length=9, verbose_name='주문 목록')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='주문 요청 시간')),
                ('cus_call', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='안심번호')),
                ('order_message', models.TextField(max_length=1000, verbose_name='요청사항')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_id', models.CharField(max_length=10, verbose_name='라이더 아이디')),
                ('rider_pw', models.CharField(max_length=20, verbose_name='라이더 비밀번호')),
                ('rider_name', models.CharField(max_length=20, verbose_name='라이더 이름')),
                ('rider_intro', models.TextField(blank=True, max_length=100, verbose_name='라이더 소개')),
                ('rider_area', models.CharField(choices=[('GG', 'Gyeonggi'), ('SL', 'Seoul'), ('CC', 'Chungcheong'), ('GS', 'Gyeongsang'), ('GW', 'Gangwon'), ('JL', 'Jeolla'), ('JJ', 'Jeju')], max_length=2, verbose_name='배달 지역')),
                ('rider_vehicle', multiselectfield.db.fields.MultiSelectField(choices=[('NL', 'Null'), ('CR', 'Car'), ('BC', 'Bicycle'), ('AB', 'Autobicycle')], max_length=11, verbose_name='배달 수단')),
                ('min_delivery_amount', models.IntegerField(verbose_name='최소 주문 금액')),
                ('bankbook', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='통장 사본 유무')),
                ('license', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='면허증 여부')),
                ('recommended_person', models.CharField(blank=True, max_length=20, verbose_name='추천인')),
                ('speed', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3')], max_length=1, verbose_name='스피드')),
                ('fresh', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3')], max_length=1, verbose_name='신선도')),
                ('accuracy', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3')], max_length=1, verbose_name='정확도')),
            ],
            options={
                'db_table': 'rider',
            },
        ),
    ]
