from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, GenericAPIView

from data.models import Record, Variable
from data.serializers import RecordSerializer, VariableSerializer


class VariableViewSet(viewsets.ModelViewSet):
    search_fields = ["name"]
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer


class RecordApiView(ListCreateAPIView):
    filterset_fields = {
        "created_at": ["gte", "lte", "exact", "gt", "lt"],
        "variable__name": ["exact"],
    }
    queryset = Record.objects.order_by("created_at").all()
    serializer_class = RecordSerializer


class LastRecordsApiView(GenericAPIView):
    serializer_class = RecordSerializer

    def get(self, request, *args, **kwargs):
        variables = Variable.objects.all()
        last_records = []
        for variable in variables:
            last_record = (
                Record.objects.filter(variable=variable).order_by("-created_at").first()
            )
            if last_record:
                last_records.append(last_record)
        return Response(self.get_serializer(last_records, many=True).data)
