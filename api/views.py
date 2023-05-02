import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view((['Get']))
def other(request):
	res = requests.get('http://localhost:12345/api/get').json()
	return Response(res)

