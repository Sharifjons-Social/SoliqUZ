# Generated by Django 4.2.5 on 2023-11-03 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserSoliq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user2', models.CharField(max_length=300, unique=True)),
                ('where', models.CharField(max_length=255)),
                ('total', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('pay_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSoliq.usermodel')),
            ],
        ),
    ]