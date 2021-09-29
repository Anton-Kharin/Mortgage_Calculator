# Generated by Django 3.2.5 on 2021-09-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_loan', models.IntegerField(default=0)),
                ('min_down_payment', models.IntegerField(default=0)),
                ('loan_term', models.IntegerField(default=0)),
                ('rates', models.ManyToManyField(to='banks.Rate')),
            ],
        ),
    ]
