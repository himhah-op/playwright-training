import pytest
import csv

with open('logins.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

@pytest.mark.parametrize("row", data)
def test_eval(row):
    print (row)