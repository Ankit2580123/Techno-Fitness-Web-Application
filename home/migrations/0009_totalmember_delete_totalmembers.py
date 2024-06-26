# Generated by Django 5.0.4 on 2024-05-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_totalmembers_date_of_admissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fathers_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=12)),
                ('age', models.IntegerField(default=18)),
                ('plan', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=300)),
                ('date_of_admissions', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TotalMembers',
        ),
    ]
