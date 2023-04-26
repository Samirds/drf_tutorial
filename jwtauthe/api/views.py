
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework. views import APIView
from django.http import HttpResponse
from . serializers import LoginSerializers, RegistrationSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from rest_framework import views
from rest_framework import permissions
from . import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class Registration(APIView):
    def post(self, request, format=None):
        serializers = RegistrationSerializers(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            token = get_tokens_for_user(user)
            return Response({'msg': 'Registration Succesfull', "token":token}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        #return HttpResponse({'msgss': 'Registration Succesfull'})



# class Login(APIView):
#     def post(self, request, format=None):
#         serializers = LoginSerializers(data=request.data)
#         if serializers.is_valid():
#             return Response({'msg': 'login Succesfull',}, status=status.HTTP_201_CREATED)
#         return Response({'msg': 'login unsucesful',}, status=status.HTTP_400_BAD_REQUEST)
#         #return HttpResponse({'msgss': 'Registration Succesfull'})





class Login(APIView):
    def post(self, request, format=None):
        serializers = LoginSerializers(data=request.data, )
        if serializers.is_valid():
            email = serializers.data.get('email')
            password = serializers.data.get('password')
            print("\n\n")
            print(email)
            print(password)
            
            print("\n\n")
            user = authenticate(email = email, password = password)
            print(user)
            if user is not None:
            #serializers.save()
                return Response({"msg": "Login Successful"}, 
                        status=status.HTTP_200_OK)
            return Response("msg" : "user is None")
        
        return Response({"msg" : "in valid"}, status=status.HTTP_401_UNAUTHORIZED,)


# class Login(APIView):
#     #permission_classes = [AllowAny]
#     def get(self, request, format=None):
#         serializers = DisplaySerializers(data=request.user)
#         if serializers.is_valid():
        
#             return Response(serializers._data,
#                             status=status.HTTP_200_OK)
        
#         return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)


# class Login(APIView):
#     def post(self, request, format=None):
#         serializers = LoginSerializer(data=request.data)
#         if serializers.is_valid():
#             email = serializers.data.get('email')
#             password = serializers.data.get('password')
#             user = authenticate( email = email, password = password)
#             if user is not None:
#                 login(request, user)
#                 return Response( serializers.data)
            
#             else:
#                 return Response({"msg": "Un Successfull"})
            
        
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


# class Login(views.APIView):
#     # This view should be accessible also for unauthenticated users.
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = serializers.LoginSerializer(data=self.request.data,
#             context={ 'request': self.request })
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response(None, status=status.HTTP_202_ACCEPTED)




# class Login(APIView):
#     def post(self, request):
#         email=request.data["email"]
#         password=request.data["password"]
#         user = authenticate(request, email=email, password=password)
#         if user is None:
#             return Response({"response":"No User exist"})
#         else:
#             return Response({"response":"correct Password"})