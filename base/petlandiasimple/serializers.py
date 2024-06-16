from rest_framework import serializers
import datetime
from .models import MedicalHistory, CustomUser
class CustomDateFormatField(serializers.DateField):
    def to_internal_value(self, value):
        try:
            # Parse the input date in 'YYYY/MM/DD' format
            date_obj = datetime.datetime.strptime(value, '%Y/%m/%d').date()
            return date_obj
        except ValueError:
            raise serializers.ValidationError("Invalid date format. Please use 'YYYY/MM/DD'.")
class CreateMedicalHistorySerializer(serializers.ModelSerializer):
    pets_birthday = CustomDateFormatField()
    last_vaccination_date = CustomDateFormatField()
    last_deworming_date = CustomDateFormatField()
    date_hospitalized = CustomDateFormatField ()
    followup_checkup_date = CustomDateFormatField()
    class Meta:
        model = MedicalHistory
        fields = [
            
            'parents_name',
            'parents_address',
            'parents_contact_number',
            'parents_occupation',
            'pets_name',
            'pets_species',
            'pets_breed',
            'pets_color_or_markings',
            'pets_sex',
            'pets_birthday',
            'chief_complaint',
            'medication_given_prior_to_check_up',
            'last_vaccination_given',
            'last_vaccination_date',
            'last_vaccination_brand',
            'last_deworming_given',
            'last_deworming_date',
            'last_deworming_brand',
            'is_transferred_from_other_clinic',
            'name_of_clinic',
            'case',
            'date_hospitalized',
            'diet',
            'weight',
            'initial_temp',
            'heart_rate',
            'respitory_rate',
            'abnormal_findings',
            'is_cbc',
            'is_skin_scrape',
            'is_xray',
            'is_dfs',
            'is_urinalysis',
            'is_vaginal_smear',
            'tentative_diagnosis',
            'prognosis',
            'treatment_given',
            'take_home_meds',
            'recommendations',
            'followup_checkup_date',
        ]

class DisplayMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
        

class ViewProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = [ 'name', 'username', 'email']