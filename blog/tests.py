from django.test import TestCase

# Create your tests here.
from pytils.translit import slugify


s = 'Привет Мир'
new_slug = slugify(s)

print(new_slug)

