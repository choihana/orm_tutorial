# Generated by Django 4.2.4 on 2023-08-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_department_alter_employee_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='compensations',
            field=models.ManyToManyField(to='hr.compensation'),
        ),
    ]