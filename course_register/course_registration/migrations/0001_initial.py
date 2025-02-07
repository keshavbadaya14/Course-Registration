# Generated by Django 5.1.5 on 2025-02-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('previous_spi', models.FloatField()),
                ('previous_cpi', models.FloatField()),
                ('semester_applying_for', models.CharField(choices=[('1', 'Semester 1'), ('2', 'Semester 2'), ('3', 'Semester 3'), ('4', 'Semester 4'), ('5', 'Semester 5'), ('6', 'Semester 6'), ('7', 'Semester 7'), ('8', 'Semester 8')], max_length=2)),
                ('selected_courses', models.TextField(help_text='Comma-separated list of selected courses')),
                ('program_electives', models.TextField(help_text='Comma-separated list of program electives')),
                ('open_electives', models.TextField(help_text='Comma-separated list of open electives')),
                ('college_fee_proof', models.FileField(upload_to='fee_documents/')),
                ('hostel_fee_proof', models.FileField(upload_to='fee_documents/')),
                ('loan_refund_form', models.FileField(blank=True, null=True, upload_to='fee_documents/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
