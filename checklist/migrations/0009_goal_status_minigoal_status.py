# Generated by Django 4.1.5 on 2023-02-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0008_alter_goal_title_minigoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='status',
            field=models.CharField(default='undone', max_length=6),
        ),
        migrations.AddField(
            model_name='minigoal',
            name='status',
            field=models.CharField(default='undone', max_length=6),
        ),
    ]