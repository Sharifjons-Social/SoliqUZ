# Generated by Django 4.2.5 on 2023-11-05 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserSoliq', '0001_initial'),
        ('PaymentSoliq', '0003_remove_payment_pay_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pay_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSoliq.usermodel'),
        ),
    ]