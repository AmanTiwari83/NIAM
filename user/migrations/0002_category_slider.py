# Generated by Django 3.2.4 on 2023-09-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('cpic', models.ImageField(null=True, upload_to='ststic/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spic', models.ImageField(null=True, upload_to='static/slider/')),
                ('sdate', models.DateField()),
            ],
        ),
    ]
