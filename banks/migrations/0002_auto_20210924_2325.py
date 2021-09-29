# Generated by Django 3.2.5 on 2021-09-24 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_loan', models.IntegerField(default=0)),
                ('min_down_payment', models.IntegerField(default=0)),
                ('loan_term', models.IntegerField(default=0)),
                ('banks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bank')),
                ('rates', models.ManyToManyField(to='banks.Rate')),
            ],
        ),
        migrations.DeleteModel(
            name='Banks',
        ),
    ]
