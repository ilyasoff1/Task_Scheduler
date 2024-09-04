from django.test import TestCase

from django.db import models
from datetime import timedelta, datetime


today = datetime.today()
print(today)
start_datetime = datetime.combine(today, start_time)
stop_datetime = datetime.combine(today, stop_time)

# Check if the stop_time is less than start_time (indicating a crossover past midnight)
if stop_time < start_time:
	stop_datetime += timedelta(days=1)  # Adjust stop_time to the next day
result = stop_datetime - start_datetime


