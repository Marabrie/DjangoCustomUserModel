# Generated by Django 3.2.7 on 2021-10-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafkan_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kafkan',
            name='id',
        ),
        migrations.AddField(
            model_name='kafkan',
            name='name',
            field=models.CharField(default='Kafkan', max_length=250, primary_key=True, serialize=False),
        ),
    ]