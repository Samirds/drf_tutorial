from rest_framework import serializers
from . models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        # password2 = serializers.CharField(style={
        #     'input_type': 'password'
        # }, write_only=True)
        model = CustomUser
        fields  =  ["first_name", "last_name", "password", "email",]
        # extra_kwargs = {
        #     'password': {'write_only':True}
        # }


    def validate(self, data):
         password = data.get("password")
         special_charecter = ["@", "&", "#", "$", "%", "_"]

         if (len(password) >= 8 and  bool(any(i in password for i in special_charecter))):
            return data
         else:
          raise ValidationError("Password must have a symbol and total length of 8")


    # def create(self, validate_data):  # here we are using custome user mdoel so we have to override the create method
    #         return User.objects.create_user(**validate_data   )

    def create(self, validated_data):  # here we are using custome user mdoel so we have to override the create method
        user = CustomUser.objects.create_user(email=validated_data['email'], first_name=validated_data['first_name'], password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class LoginSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ["email", "password"]

        # def validate(self, data):

        #     email = data.get("email")
        #     password = data.get("password")
        #     user = authenticate(email = email, password = password)
        #     print("\n\n\n")
        #     print("ldfhaodsifhodifhdiofhdoifhiosdhfodhfiodfhoidhfoidhfoihdfoidhsfoihdf")
        #     print(user)
        #     if user is not None:
        #         return data
        #     else:
        #         raise ValidationError("Password or Email not valid")




class ProfileSerializers(serializers.ModelSerializer):
    #email = serializers.EmailField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ["email", "password"]



class logoutSerializers(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    

    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
            

        except TokenError:
            self.fail("bad token")
