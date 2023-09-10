# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorsSerializer, MeasurementsSerializer, SensorsDetailSerializer


class SensorsView(APIView):
    def get(self, request):
        sensor = Sensor.objects.all()
        ser = SensorsSerializer(sensor, many=True)
        return Response(ser.data)

    def post(self, request):
        req = request.data
        q = Sensor(name=req.get('name'), description=req.get('description'))
        q.save()
        return Response({'status': 'OK'})


class SensorsDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsDetailSerializer

    def patch(self, request, pk):
        req = request.data
        sensor = Sensor.objects.filter(id=pk)[0]
        if req.get('name'):
            sensor.name = req.get('name')
        if req.get('description'):
            sensor.description = req.get('description')
        sensor.save()
        return Response({'status': 'OK'})


class MeasurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer

    def post(self, request):
        req = request.data
        sensor = Sensor.objects.filter(id=req.get('sensor'))
        q = Measurement(sensor=sensor[0],
                        temperature=req.get('temperature'))
        q.save()
        return Response({'status': 'OK'})
