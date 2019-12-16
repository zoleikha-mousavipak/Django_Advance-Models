from django.db import models


class MyIBANField(models.Field):
    def db_type(self, connection):
        return 'char(25)'

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class MyIBANModel(models.Model):
    _iban = MyIBANField()
    
    @property 
    def iban(self):
        return self._iban

    @iban.setter
    def iban(self, value):
        self._iban = value

    def __str__(self):
        return self.iban


