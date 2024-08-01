from django.shortcuts import render
from .models import Aircraft
from rest_framework import viewsets
from .serializers import AircraftSerializer

# view to use custom manager


def list_active_cessna_aircraft(request):
    aircraft_list = Aircraft.objects.filter_by_criteria(make="Cessna", active=True)
    return render(request, "aircraft/list.html", {"aircraft_list": aircraft_list})


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
