# Generated by Django 3.2.9 on 2022-01-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('walk_count', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'activity',
                'ordering': ['-date_created'],
            },
        ),
    ]
