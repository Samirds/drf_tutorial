from rest_framework import serializers
from . models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        # password2 = serializers.CharField(style={
        #     'input_type': 'password'
        # }, write_only=True)
        model = User
        fields  =  ["first_name", "last_name", "password", "email", "age"]
        # extra_kwargs = {
        #     'password': {'write_only':True}
        # }


    def validate(self, data):
         password = data.get("password")
         print("\n\n")
         print(password)
         special_charecter = ["@", "&", "#", "$", "%", "_"]

         #bool(any(i in ps for i in special_charecter))  this gives true false that a field present in list
         # if any(substring in ps for substring in special_charecter):
        #     # 👇️ this runs
        #     print('The string contains at least one element from the list')
        # else:
        #     print('The string does NOT contain any of the elements in the list')

         if (len(password) >= 8 and  bool(any(i in password for i in special_charecter))):
            return data
         else:
          raise ValidationError("Password must have a symbol and total length of 8")


    # def create(self, validate_data):  # here we are using custome user mdoel so we have to override the create method
    #         return User.objects.create_user(**validate_data   )

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], first_name=validated_data['first_name'], age=validated_data['age'], password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]


#         def validate(self, data):
#             # Take username and password from request
#             email = data.get('email')
#             password = data.get('password')

#             if email and password:
#                 # Try to authenticate the user using Django auth framework.
#                 user = authenticate(request=self.context.get('request'),
#                                     email=email, password=password)
#                 if not user:
#                     # If we don't have a regular user, raise a ValidationError
#                     msg = 'Access denied: wrong username or password.'
#                     raise serializers.ValidationError(msg, code='authorization')
#             else:
#                 msg = 'Both "username" and "password" are required.'
#                 raise serializers.ValidationError(msg, code='authorization')
#             # We have a valid user, put it in the serializer's validated_data.
#             # It will be used in the view.
#             data['user'] = user
#             return data









        # def validate(self, data):

        #     email = data.get("email")
        #     password = data.get("password")
        #     user = authenticate(email = email, password = password)
        #     if user is not None:
        #         return data
        #     else:
        #         raise ValidationError("Password or Email not valid")
            





# class LoginSerializer(serializers.ModelSerializer):
#     # email = serializers.EmailField(max_length=128 )
#     # password = serializers.CharField(max_length = 50)
#     class Meta:
#         model = User
#         fields = ["email", "password"]