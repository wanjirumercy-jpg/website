# Generated by Django 5.0.7 on 2024-11-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0005_alter_slider_slider_btn_alter_slider_slider_head_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('icon_class', models.CharField(max_length=100)),
            ],
        ),
    ]