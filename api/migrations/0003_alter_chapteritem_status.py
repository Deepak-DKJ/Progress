# Generated by Django 5.0.6 on 2024-05-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_chapteritem_pos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapteritem',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
