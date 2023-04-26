from django.shortcuts import render
from rest_framework. views import APIView
from rest_framework.response import Response
# from . models import applicationDataModel
# from . serializers import applicationDataSeria
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated #for class based veiw
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.

# class applicationData(APIView):
#     application = applicationDataModel.objects.all()
    
#     def get(self, request, format=None):
#         stu = applicationDataModel.objects.all()
#         serializers = applicationDataSeria(stu, many=True)
        
            
#         return Response({serializers})
        

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])        
def applicationData(request):

    return HttpResponse({"Here is our Home Page"})


from .serializers import showProfileSerializer

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication



class ShowProfile(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		serializer = showProfileSerializer(request.user)
		return Response(serializer.data)