from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework. views import APIView
from django.http import HttpResponse
from . seralizers import RegistrationSerializers, LoginSerializers, ProfileSerializers, logoutSerializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework import views
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


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

            user = authenticate(email = email, password = password)
           
            if user is not None:
            #serializers.save()
                login(request, user)
                first_name = user.first_name
                last_name = user.last_name
                user_email = user.email
                return Response( {'first_name' : first_name, "Last": last_name, "email": user_email},
                        status=status.HTTP_200_OK)
            return Response({"Email or Password is not exist in admin panel"})
        
        return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED,)
    


class Profile(APIView):

    def get(self, request, format=None):
        serializers = ProfileSerializers(data=request.user)
        if serializers.is_valid():
        
            return Response(serializers.data,
                            status=status.HTTP_200_OK)
        
        return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)
    


class Signout(APIView):
    def post(self, request, format=None):
        try:
            token = RefreshToken(request.data.get('refresh'))
            print(token)
            token.blacklist()
            return Response({"msg": "Logout Successfull"}, status=status.HTTP_200_OK)
        except Exception as e:
             return Response(e, status=status.HTTP_400_BAD_REQUEST)
        



        

class HomePage(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return HttpResponse("Here is our Home Page")

        


class newLogout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializers = logoutSerializers(data=request.data)
        serializers.is_valid()
        serializers.save()

        return Response({"Logout Successfull"})
    



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            print("\n\n")
            print(refresh_token)
            token = RefreshToken(refresh_token)
            print("\n\n")
            print(token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        






