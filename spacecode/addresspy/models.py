from django.contrib.auth.models import User
from django.db import models
from django.db.models import F, Value, CharField


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    street_address = models.TextField(blank=True, null=True)
    street_address_line2 = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    full_address = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        streetdata = f"{self.street_address}\n{self.street_address_line2}"
        self.full_address = f"{streetdata}\n{self.zipcode} {self.city} {self.state} {self.country}"

        UserAddress.objects.annotate(temp_field=Value(self.street_address, output_field=CharField())).filter(
            temp_field__icontains=F('street_address')).delete()
        t = UserAddress.objects.filter(street_address__contains=self.street_address).count()
        if t == 0:
            super().save(*args, **kwargs)