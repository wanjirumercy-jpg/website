# Generated by Django 5.0.7 on 2024-11-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0002_service_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='email',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='message',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='subject',
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_btn',
            field=models.CharField(default='Get Started', max_length=50),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_head',
            field=models.CharField(default='Default Slider Head', max_length=100),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_image',
            field=models.ImageField(default='default_image.jpg', upload_to='sliders/'),
        ),
    ]