from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    CHOICE_TUPLE = (('M', "Male"), ('F', "Female"))
    gender = models.CharField(max_length=2, choices=CHOICE_TUPLE, null=False, blank=False)
    flat_no_or_house_name = models.CharField(max_length=150, null=True, blank=True)
    street = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=False, default='Mangalore')
    district = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True, default='Karnataka')
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Patient Entry'

    def __str__(self):
        return '%s' % self.name


class ImageBox(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='patient_images', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Image Store'

    def __str__(self):
        return '%s' % self.patient


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    condition = models.CharField(max_length=250, null=False, blank=False)
    medical_history = models.TextField(null=True, blank=True)
    other_medicines = models.TextField(null=True, blank=True)
    dermatology_treatment_history = models.TextField(null=True, blank=True)
    dermatology_treatment_plan = models.TextField(null=True, blank=True)
    prescription = models.TextField(null=True, blank=True)
    image_box = models.ForeignKey(ImageBox, on_delete=models.DO_NOTHING)
    next_review = models.DateField(null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)
    consultation_fee = models.SmallIntegerField(null=False, blank=False, default=300)

    class Meta:
        verbose_name_plural = 'Patient Ledger'
