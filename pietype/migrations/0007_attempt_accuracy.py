# Generated by Django 4.0.4 on 2022-05-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pietype', '0006_alter_attempt_sentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='accuracy',
            field=models.IntegerField(default=0, verbose_name='Accuracy'),
            preserve_default=False,
        ),
    ]