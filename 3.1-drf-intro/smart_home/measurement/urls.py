from django.urls import path

from django.contrib import admin
from django.urls import path

from .views import SensorsView, SensorsDetailView, MeasurementsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorsDetailView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]