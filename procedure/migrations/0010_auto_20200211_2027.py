# Generated by Django 2.1.1 on 2020-02-11 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0009_auto_20200202_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refpost',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.Subject'),
        ),
    ]
