from rest_framework.serializers import ModelSerializer

from .models import BackUser


class BackUserSerializer(ModelSerializer):
    class Meta:
        model = BackUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
