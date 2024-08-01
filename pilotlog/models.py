from django.db import models


class AircraftManager(models.Manager):
    def filter_by_criteria(self, make=None, model=None, active=True):
        """
        Filters aircraft based on make, model, and activity status.
        Allows for flexible querying with optional parameters.
        """
        queryset = self.get_queryset()
        if make:
            queryset = queryset.filter(make__iexact=make)
        if model:
            queryset = queryset.filter(model__iexact=model)
        return queryset.filter(active=active)


class Aircraft(models.Model):
    user_id = models.IntegerField()
    guid = models.CharField(max_length=100, unique=True)
    fin = models.CharField(max_length=100, blank=True, null=True)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(default=0)
    make = models.CharField(max_length=100, blank=True, null=True)
    run2 = models.BooleanField(default=False)
    class_type = models.IntegerField(default=0, db_column="class")
    model = models.CharField(max_length=100)
    power = models.IntegerField(default=1)
    seats = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    complex = models.BooleanField(default=False)
    cond_log = models.IntegerField(default=0)
    fav_list = models.BooleanField(default=False)
    category = models.IntegerField(default=0)
    high_perf = models.BooleanField(default=False)
    sub_model = models.CharField(max_length=100, blank=True, null=True)
    aerobatic = models.BooleanField(default=False)
    ref_search = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    tailwheel = models.BooleanField(default=False)
    default_app = models.IntegerField(default=0)
    default_log = models.IntegerField(default=0)
    default_ops = models.IntegerField(default=0)
    device_code = models.IntegerField(default=0)
    aircraft_code = models.CharField(max_length=100)
    default_launch = models.IntegerField(default=0)
    record_modified = models.DateTimeField()

    objects = AircraftManager()

    def __str__(self):
        return f"{self.make} {self.model} ({self.guid})"
