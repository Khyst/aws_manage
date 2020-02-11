# Generated by Django 2.2.1 on 2020-01-31 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0007_auto_20200130_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='author',
        ),
        migrations.AlterField(
            model_name='refpost',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.Subject'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
