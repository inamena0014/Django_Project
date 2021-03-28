# Generated by Django 3.1.6 on 2021-02-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0002_delete_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Name', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Request_Date', models.DateField()),
                ('Date_Board_Resolution', models.DateField()),
                ('Evaluation_Date', models.DateField()),
                ('Due_Date', models.DateField()),
                ('Position_On_The_Request', models.CharField(max_length=100)),
                ('Execution_Status', models.CharField(max_length=100)),
            ],
        ),
    ]
