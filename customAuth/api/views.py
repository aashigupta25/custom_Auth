from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customAuth import CustomAuthentication

class PersonModelViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
