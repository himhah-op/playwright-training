import pytest
import csv
import random
from faker import Factory
class employee ():
    def __init__(self):
        fakerFR = Factory.create('fr_FR')
        self.last_name=fakerFR.first_name()
        self.first_name=fakerFR.last_name()
        self.id=str(random.randrange (100000, 999999))
        self.birthday = fakerFR.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d")

@pytest.fixture
def test_data():
    with open('logins.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

