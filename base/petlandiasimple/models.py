from django.db import models

    

    
class MedicalHistory(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    parents_name = models.CharField(max_length=100)
    parents_address = models.CharField(max_length=100)
    parents_contact_number= models.CharField (max_length= 100)
    parents_occupation = models.CharField(max_length=100)
    pets_name = models.CharField(max_length=100)
    pets_species = models.CharField(max_length=100)
    pets_breed = models.CharField(max_length=100)
    pets_color_or_markings = models.CharField(max_length=100)
    sex_choices = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    pets_sex = models.CharField(max_length=1, choices=sex_choices)
    
    pets_birthday = models.DateField()
    chief_complaint = models.TextField()
    medication_given_prior_to_check_up = models.TextField()
    last_vaccination_given = models.CharField(max_length=100)
    last_vaccination_date = models.DateField()
    last_vaccination_brand = models.CharField(max_length=100)
    last_deworming_given = models.CharField(max_length=100)
    last_deworming_date = models.DateField()
    last_deworming_brand = models.CharField(max_length=100)
    is_transferred_from_other_clinic = models.BooleanField()
    name_of_clinic = models.CharField(max_length=100, blank=True, null=True)
    case = models.TextField()
    date_hospitalized = models.DateField()
    diet = models.TextField()
    weight = models.FloatField()
    initial_temp = models.FloatField()
    heart_rate = models.CharField(max_length=100)
    respitory_rate = models.CharField(max_length=100)
    abnormal_findings = models.TextField()
    is_cbc = models.BooleanField()
    is_skin_scrape = models.BooleanField()
    is_xray = models.BooleanField()
    is_dfs = models.BooleanField()
    is_urinalysis = models.BooleanField()
    is_vaginal_smear = models.BooleanField()
    tentative_diagnosis = models.TextField()
    prognosis = models.TextField()
    treatment_given = models.TextField()
    take_home_meds = models.TextField()
    recommendations = models.TextField()
    followup_checkup_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



