# Generated by Django 2.2.17 on 2021-01-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]