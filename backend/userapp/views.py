from rest_framework.viewsets import ModelViewSet
from .models import BackUser
from .serializers import BackUserSerializer


class BackUserViewSet(ModelViewSet):
    serializer_class = BackUserSerializer
    queryset = BackUser.objects.all()
