# Generated by Django 2.2.1 on 2020-01-30 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0005_auto_20200130_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='refpost',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.Subject'),
        ),
    ]