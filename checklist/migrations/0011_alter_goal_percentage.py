# Generated by Django 4.1.5 on 2023-02-02 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0010_goal_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='percentage',
            field=models.CharField(default='0%', max_length=6),
        ),
    ]
