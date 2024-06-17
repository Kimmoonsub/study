# Generated by Django 5.0.6 on 2024-05-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_alter_fcuser_options_alter_fcuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@email.com', max_length=128, verbose_name='사용자 이메일'),
            preserve_default=False,
        ),
    ]