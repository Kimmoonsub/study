# Generated by Django 5.0.6 on 2024-05-18 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0004_fcuser_useremail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_dttm', models.DateField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 게시글',
                'verbose_name_plural': '패스트캠퍼스 게시글',
                'db_table': 'fastcampus_board',
            },
        ),
    ]
