# Generated by Django 5.0.7 on 2024-11-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0003_remove_slider_email_remove_slider_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(default='default_image.jpg', upload_to='slides/'),
        ),
    ]
