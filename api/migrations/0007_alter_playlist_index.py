# Generated by Django 3.2.6 on 2021-09-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210922_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
