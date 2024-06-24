from django.urls import path
from rest_framework.routers import SimpleRouter

from data.views import RecordApiView, VariableViewSet

router = SimpleRouter()
router.register("variables", VariableViewSet, basename="variables")


urlpatterns = [
    path("records", RecordApiView.as_view(), name="records"),
]

urlpatterns += router.urls
