# Generated by Django 4.0.4 on 2022-05-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pietype', '0007_attempt_accuracy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='sentence',
            field=models.CharField(max_length=4000, verbose_name='Sentence'),
        ),
    ]