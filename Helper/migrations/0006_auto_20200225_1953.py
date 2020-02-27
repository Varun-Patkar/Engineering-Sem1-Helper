# Generated by Django 3.0.3 on 2020-02-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0005_auto_20200225_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pdf',
            name='subject',
            field=models.CharField(choices=[('Maths', 'Maths'), ('Bee', 'BEE'), ('MECHANICS', 'Mechanics'), ('PHYSICS', 'Physics'), ('CHEMISTRY', 'Chemistry')], default=0, max_length=9),
            preserve_default=False,
        ),
    ]
