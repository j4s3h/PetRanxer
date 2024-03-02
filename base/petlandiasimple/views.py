from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateMedicalHistorySerializer, DisplayMedicalHistorySerializer, ViewProfileSerializer
from .models import MedicalHistory
from petlandiasimple.utils.generate_uid import generate_uuid
from petlandiasimple.utils.constant import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
class CreateMedicalRecord(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
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
        return Response({"message": "Error!",  "errors": errors}, status)

class DisplayMedicalRecordsViews(APIView):
    permission_classes = [IsAuthenticated]
    
    authentication_classes = [JWTAuthentication]
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
            'followup_checkup_date'
        )
        
        data = medical_history
        status = "ok"
        message = 'Success'
        return Response({"Message": message, "data": data, "status": status})
    

class DisplayMedicalRecordViewsIndiv(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
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
        message = {}
        data = {}
        status = bad_request
        errors = serializer.errors
        return Response({"message": message, "data": data, "status": status, "errors": errors})

class DeleteMedicalRecords(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

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
        return Response({"message": message, "data": data, "status": status, "errors": errors})
class LoginView(APIView):
    
    
    permission_classes = [AllowAny]
        
    def post(self, request, format=None):
        errors = {}
        data = {}
        status = None
        username= request.data['username']
        password = request.data['password']


        user = User.objects.filter(Q(username=username)).first()

        if user is None:
            raise AuthenticationFailed('No user found with the given email/username.')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')

        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = RefreshToken.for_user(serializer.user)
            data = {
                'access_token': str(serializer.validated_data['access']),
                'refresh_token': str(refresh_token)
            }
            message =  'Successfully Login'
            status = ok
            return Response ({"message": message, "data": data, "status": status, "errors": errors })
        status = unauthorized
        return Response(serializer.errors, status=status)




class ViewProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        user = request.user
        is_admin = user.is_staff
        serializer = ViewProfileSerializer(user)
        serialized_data = serializer.data
        message = 'Successful'
        serialized_data['role'] = "owner" if is_admin else "staff"
        status_code = ok
        errors = {}
        
        return Response({
            "message": message,
            "data": serialized_data,
            "status": status_code,
            "errors": errors,
             
        })