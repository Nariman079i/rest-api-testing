from rest_framework.serializers import *
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDataSerializer(ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'


class LocateSerializer(ModelSerializer):
    class Meta:
        model = Locate
        fields = '__all__'


class IndustrialSerializer(ModelSerializer):
    class Meta:
        model = Industrial
        fields = '__all__'

