# Generated by Django 5.1.3 on 2024-11-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kick', '0005_alter_equipment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='pincode',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
