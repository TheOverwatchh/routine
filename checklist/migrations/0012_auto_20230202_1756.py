# Generated by Django 3.1.7 on 2023-02-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0011_alter_goal_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lembrete',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='minigoal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
