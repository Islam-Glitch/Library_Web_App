# Generated by Django 5.0.6 on 2024-05-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_user_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
