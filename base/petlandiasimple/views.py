from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateMedicalHistorySerializer, DisplayMedicalHistorySerializer
from .models import MedicalHistory
from petlandiasimple.utils.generate_uid import generate_uuid
from petlandiasimple.utils.constant import *
from django.http import Http404
class CreateMedicalRecord(APIView):
    
    def post(self, request):
        serializer = CreateMedicalHistorySerializer(data=request.data)
        data = {}
        errors = {}
        status = None
        message = None

        if serializer.is_valid():
            uid = generate_uuid()
            medical_history = MedicalHistory.objects.create(id=uid, **serializer.validated_data)

            
            data = {
                'id': medical_history.id,
                'created': medical_history.created,
                'modified': medical_history.modified,
                **serializer.data
            }

            status = created
            message = 'Successfully Created'
            return Response({"message": message, "data": data, "status": status, "errors": errors})

        errors = serializer.errors
        status = bad_request
        return Response({"message": "Error!", "status": status, "errors": errors})

class DisplayMedicalRecordsViews(APIView):
    def get(self, request): 
        medical_history = MedicalHistory.objects.all().values(
            'id',
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
            'is_HR',
            'is_RR',
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
            'followup_checkup_date'
        )
        
        data = medical_history
        status = "ok"
        message = 'Success'
        return Response({"Message": message, "data": data, "status": status})
    

class DisplayMedicalRecordViewsIndiv(APIView):
    def get_medical_record(self, pk):
        try: 
            return MedicalHistory.objects.get(pk=pk)
        except MedicalHistory.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        
        medical_record = self.get_medical_record(pk)
        serializer = DisplayMedicalHistorySerializer(medical_record)
        data =serializer.data
        status = ok
        message = 'Results'
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors})
class EditMedicalRecords(APIView):
    def get_medical_record(self, pk):
        try: 
            return MedicalHistory.objects.get(pk=pk)
        except MedicalHistory.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        medical_record = self.get_medical_record(pk)
        serializer = CreateMedicalHistorySerializer(medical_record, data=request.data)

        if serializer.is_valid():
            serializer.save()
            status = ok
            data =serializer.data 
            errors = None
            message = 'Edited Successfully'
            return Response({"message": message, "data": data, "status": status, "errors": errors})
        status = bad_request
        errors = serializer.errors
        return Response({"message": message, "data": data, "status": status, "errors": errors})

class DeleteMedicalRecords(APIView):
    def get_medical_record(self, pk):
        try: 
            return MedicalHistory.objects.get(pk=pk)
        except MedicalHistory.DoesNotExist:
            raise Http404
    def delete(self, request, pk):
        errors = {}
        data = {}
        status = None
        medical_record = self.get_medical_record(pk)
        medical_record.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors })
    
    
