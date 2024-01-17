from django.db import models

    

    
class MedicalHistory(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    parents_name = models.CharField(max_length=100)
    parents_address = models.CharField(max_length=100)
    parents_contact_number= models.CharField (max_length= 100)
    parents_occupation = models.CharField(max_length=100, null= True)
    pets_name = models.CharField(max_length=100)
    pets_species = models.CharField(max_length=100)
    pets_breed = models.CharField(max_length=100)
    pets_color_or_markings = models.CharField(max_length=100, null =True)
    sex_choices = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    pets_sex = models.CharField(max_length=1, choices=sex_choices)
    
    pets_birthday = models.DateField(null=True)
    chief_complaint = models.TextField(null=True)
    medication_given_prior_to_check_up = models.TextField(null=True)
    last_vaccination_given = models.CharField(max_length=100, null=True)
    last_vaccination_date = models.DateField(null =True)    
    last_vaccination_brand = models.CharField(max_length=100, null=True)
    last_deworming_given = models.CharField(max_length=100, null = True)
    last_deworming_date = models.DateField(null =True)
    last_deworming_brand = models.CharField(max_length=100)
    is_transferred_from_other_clinic = models.BooleanField(null=True)
    name_of_clinic = models.CharField(max_length=100, blank=True, null=True)
    case = models.TextField(null =True)
    date_hospitalized = models.DateField(null =True)
    diet = models.TextField(null =True)
    weight = models.FloatField(null=True)
    initial_temp = models.FloatField(null =True)
    heart_rate = models.CharField(max_length=100, null =True)
    respitory_rate = models.CharField(max_length=100, null =True)
    abnormal_findings = models.TextField(null =True)
    is_cbc = models.BooleanField(null =True)
    is_skin_scrape = models.BooleanField(null =True)
    is_xray = models.BooleanField(null =True)
    is_dfs = models.BooleanField(null =True)
    is_urinalysis = models.BooleanField(null =True)
    is_vaginal_smear = models.BooleanField(null =True)
    tentative_diagnosis = models.TextField(null =True)
    prognosis = models.TextField(null =True)
    treatment_given = models.TextField(null =True)
    take_home_meds = models.TextField(null =True)
    recommendations = models.TextField(null =True)
    followup_checkup_date = models.DateField(null =True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)




