from rest_framework import serializers
from .models import User
from .models import SignIn
from .models import ChangePassword
from .models import ForgetPassword



class UserSerializers(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'




class SignInSerializer(serializers.ModelSerializer):

    class Meta:

        model = SignIn
        fields = '__all__'






class ChangePasswordSerializers(serializers.ModelSerializer):

    class Meta:

        model = ChangePassword
        fields = '__all__'






class ForgetPasswordSerializers(serializers.ModelSerializer):

    class Meta:

        model = ForgetPassword
        fields = '__all__'