from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import *
from django.utils.translation import gettext_lazy as _


class CityFilter(admin.SimpleListFilter):
    # For filtering attorney's from different states
    # the filter displays the states for which attorney
    # data is present
    parameter_name = 'city'
    title = _('City')

    def lookups(self, request, model_admin):
        list_tuple = []
        # getting distinct states using the attorney info model
        for record in Patient.objects.order_by().values('city').distinct():
            list_tuple.append((record.get('city'), record.get('city')))
        return list_tuple

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(city=self.value())
        else:
            return queryset


class AdminPatient(admin.ModelAdmin):

    def address(self, obj):
        house = obj.flat_no_or_house_name
        street = obj.street
        city = obj.city
        district = obj.district
        state = obj.state

        address_string = "{0},<br>{1}, {2},<br>{3}, {4}".format(house, street, city, district, state)
        return format_html(address_string)

    def patient_records(self, obj):

        query_url_for_record_data = "/PatientLedger/patientrecord/?q=&patient_id="
        links = "<a href = '{0}{1}'>View Record</a>" \
            .format(query_url_for_record_data, obj.id)

        return format_html(links)

    def latest_patient_image(self, obj):
        try:
            image = ImageBox.objects.filter(patient=obj).last().image
            latest_image = '<img src="{0}" width="150"/>'.format(image.url)

            links = "<a href = '{0}{1}'>{2}</a>".format('/PatientLedger/imagebox/?q=&patient_id=', obj.id, latest_image)

            return format_html(links)
        except:
            return None

    list_display = ['name', 'age', 'dob', 'gender', 'address', 'phone_number', 'patient_records',
                    'latest_patient_image']
    list_filter = ('gender', CityFilter)
    search_fields = ['name', 'phone_number']


class AdminPatientRecord(admin.ModelAdmin):
    list_display = ['patient', 'condition', 'medical_history', 'other_medicines', 'dermatology_treatment_history',
                    'dermatology_treatment_plan', 'prescription', 'next_review', 'consultation_fee', 'other_details']

    search_fields = ['patient']

    list_filter = ['next_review']


class AdminImageBox(admin.ModelAdmin):

    def image_tag(self, obj):
        return mark_safe('<img src="{0}" width="150"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ['patient', 'image_tag', 'created_date', ]


admin.site.site_title = "Patient Ledger"
admin.site.site_header = "THE SKIN CLINIC"

admin.site.register(Patient, AdminPatient)
admin.site.register(PatientRecord, AdminPatientRecord)
admin.site.register(ImageBox, AdminImageBox)
