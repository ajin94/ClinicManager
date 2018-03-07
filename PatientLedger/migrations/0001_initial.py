# Generated by Django 2.0.1 on 2018-03-07 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='patient_images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Image Store',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('flat_no_or_house_name', models.CharField(blank=True, max_length=150, null=True)),
                ('street', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(default='Mangalore', max_length=150)),
                ('district', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(blank=True, default='Karnataka', max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Patient Entry',
            },
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=250)),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('other_medicines', models.TextField(blank=True, null=True)),
                ('dermatology_treatment_history', models.TextField(blank=True, null=True)),
                ('dermatology_treatment_plan', models.TextField(blank=True, null=True)),
                ('prescription', models.TextField(blank=True, null=True)),
                ('next_review', models.DateField(blank=True, null=True)),
                ('other_details', models.TextField(blank=True, null=True)),
                ('consultation_fee', models.SmallIntegerField(default=300)),
                ('image_box', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PatientLedger.ImageBox')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PatientLedger.Patient')),
            ],
            options={
                'verbose_name_plural': 'Patient Ledger',
            },
        ),
        migrations.AddField(
            model_name='imagebox',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PatientLedger.Patient'),
        ),
    ]