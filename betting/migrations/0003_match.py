# Generated by Django 3.2.12 on 2023-03-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0002_auto_20230301_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(default='team1', max_length=100)),
                ('team2', models.CharField(default='team2', max_length=100)),
                ('team1_goals', models.IntegerField(default=0, max_length=10)),
                ('team2_goals', models.IntegerField(default=0, max_length=10)),
            ],
        ),
    ]
