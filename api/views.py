import requests
import math
import threading
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PrimeNumber
from .tasks import log_performance, fetch_primes, periodic
from .serializers import PrimeNumberSerializer



@api_view((['Get']))
def other(request):
	res = requests.get('http://web:8000/api/get').json()
	return Response(res)

@api_view((['Get']))
def generate(request):
	prime_range = math.floor(10**3/3)

	url = 'http://web:8000/api/generate'
	params = {'from': 1, 'to': prime_range}
	requests.get(url, params=params)

	url = 'http://web-1:8000/api/generate'
	params = {'from': prime_range+1, 'to': prime_range*2}
	requests.get(url, params=params)

	url = 'http://web-2:8000/api/generate'
	params = {'from': prime_range*2+1, 'to': prime_range*3+1}
	requests.get(url, params=params)

	thread = threading.Thread(target=periodic, args=(60, log_performance))
	thread.daemon = True
	thread.start()

	thread1 = threading.Thread(target=periodic, args=(120, fetch_primes()))
	thread1.daemon = True
	thread1.start()

	return Response({'response' : 'Master Service Invoked.....'})

@api_view(['Get'])
def get(request):
	nums = PrimeNumber.objects.all().order_by('number')
	serializer = PrimeNumberSerializer(nums, many=True)
	return Response(serializer.data)

