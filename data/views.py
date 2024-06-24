from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from data.models import Record, Variable
from data.serializers import RecordSerializer, VariableSerializer


class VariableViewSet(viewsets.ModelViewSet):
    search_fields = ["name"]
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer


class RecordApiView(ListCreateAPIView):
    filterset_fields = ["created_at", "variable__name"]
    queryset = Record.objects.order_by("created_at").all()
    serializer_class = RecordSerializer
