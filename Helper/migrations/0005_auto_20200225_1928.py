# Generated by Django 3.0.3 on 2020-02-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0004_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='upload',
            field=models.FileField(upload_to='media'),
        ),
    ]
