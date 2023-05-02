import os
import requests
import pandas as pd
from .models import PrimeNumber
import time
import datetime


performance_log_path = './performance_log.csv'

def log_performance():
    res = requests.get('http://web:8000/api/monitor/?k=1')
    performance = res.json()[0]
    print('loging')
    performance['timestamp'] = datetime.datetime.now()

    if not os.path.exists(performance_log_path):
        os.makedirs(os.path.dirname(performance_log_path), exist_ok=True)
        log = pd.DataFrame(data=[performance])
        log.to_csv(performance_log_path, index=False)
    else:
        logs = pd.read_csv(performance_log_path)
        new_log = pd.DataFrame(data=[performance])
        updated_logs = pd.concat([logs, new_log], ignore_index=True, axis=0)
        updated_logs.to_csv(performance_log_path, index=False)

def periodic(interval, func):
    while True:
        time.sleep(interval)
        func()

def fetch_primes():
	res = requests.get('http://web:8000/api/get/').json()
	for num in res:
		try:
			PrimeNumber.objects.create(number=num['number'])
		except Exception as e:
			pass
			# print(e)
		
	res = requests.get('http://web-1:8000/api/get/').json()
	for num in res:
		try:
			PrimeNumber.objects.create(number=num['number'])
		except Exception as e:
			pass
			# print(e)
		
	res = requests.get('http://web-2:8000/api/get/').json()
	for num in res:
		try:
			PrimeNumber.objects.create(number=num['number'])
		except Exception as e:
			pass
			# print(e)