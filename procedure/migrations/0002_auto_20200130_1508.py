# Generated by Django 2.2.1 on 2020-01-30 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refpost',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.Subject'),
        ),
    ]
