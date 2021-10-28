import os
import sys
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    
p = Person
p.name = "Tom"
p.description = "Dobrý muž"

print(p);
