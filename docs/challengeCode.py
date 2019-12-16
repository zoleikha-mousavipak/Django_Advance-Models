#
# ###### IBAN Field
# Write a Django custom Field model to store IBANs. The Field must meet the following requirements:
# 1. The stored value should never be fully visible - given an IBAN like "GR96 0810 0010 0000 0123 4567 890",
#    the value should be displayed as "---7890" everywhere
# 2. Superusers should be able to see the full value when needed
#
# ###### Address deduplication
# Consider an Address model defined as follows:
#
# class UserAddress(models.Model):
#    user = models.ForeignKey(User)
#    name = models.CharField(max_length=255)
#    street_address = models.CharField(max_lenght=255)
#    street_address_line2 = models.CharField(max_lenght=255, blank=True, null=True)
#    zipcode = models.CharField(max_length=12, blank=True, null=True)
#    city = models.CharField(max_length=64)
#    state = models.CharField(max_length=64, blank=True, null=True)
#    country = models.CharField(max_length=2)
#    full_address = models.TextField(blank=True)
#
#    def save(*args, **kwargs):
#        streetdata = f"{self.street_address}\n{self.street_address_line2}"
#        self.full_address = f"{streetdata}\n{self.zipcode} {self.city} {self.state} {self.country}"
#        super().save(*args, **kwargs)
#
# A UserAddress is saved every time the user changes something in the form, provided the form is valid.
# The task is devising a way of removing partial addresses that are entirely a subset of the current address.
# For example, assuming the following addresses are entered in the form(all belonging to the same user) in sequence:
#
# add1 = UserAddress(name="Max", city="Giventown")
# add2 = UserAddress(name="Max Mustermann", street_address="Randomstreet", city="Giventown")
# add3 = UserAddress(name="Max Mustermann", street_address="456 Randomstreet", city="Giventown")
# add4 = UserAddress(name="Max Mustermann", street_address="789 Otherstreet", city="Giventown", country="NL")
#
# The expected result would be that only add3 and add4 are left in the DB at the end of the sequence