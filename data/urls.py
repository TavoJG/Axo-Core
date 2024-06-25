from django.urls import path
from rest_framework.routers import SimpleRouter

from data.views import RecordApiView, VariableViewSet, LastRecordsApiView

router = SimpleRouter()
router.register("variables", VariableViewSet, basename="variables")


urlpatterns = [
    path("records", RecordApiView.as_view(), name="records"),
    path("records/last", LastRecordsApiView.as_view(), name="last_records"),
]

urlpatterns += router.urls
