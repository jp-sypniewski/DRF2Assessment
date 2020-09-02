# Generated by Django 3.1.1 on 2020-09-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_author', models.CharField(max_length=120)),
                ('quote_body', models.TextField()),
                ('context', models.CharField(max_length=120, null=True)),
                ('source', models.CharField(max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
