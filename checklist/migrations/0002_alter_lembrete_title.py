# Generated by Django 4.1.5 on 2023-01-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lembrete',
            name='title',
            field=models.CharField(default='NotATitle', max_length=17),
        ),
    ]
