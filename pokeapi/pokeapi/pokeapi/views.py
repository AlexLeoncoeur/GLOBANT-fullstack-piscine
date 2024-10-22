from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import requests

def index(request):
	return render(request, 'index.html')

def login_with_oauth(request):
	oauth_url = (
		"http://localhost:8000/o/authorize"
		"?response_type=code"
		"&client_id=1YMfyvo2eUFFJl5InW1puPUooY1Bu7IdWMDWoKuI"
		"&redirect_uri=http://localhost:8000/callback/"
		"&scope=read"
	)
	return HttpResponseRedirect(oauth_url)

def oauth_callback(request):

	code = request.GET.get('code')
	if not code:
		return HttpResponse("Error: No authorization code provided.")
	token_url = 'http://localhost:8000/o/token'
	token_data = {
		'grant_type': 'authorization_code',
		'code': code,
		'redirect_uri': 'http:localhost:8000/callback/',
		'client_id': '1YMfyvo2eUFFJl5InW1puPUooY1Bu7IdWMDWoKuI',
		'client_secret': 'pbkdf2_sha256$600000$NB48tMZsnSj55PakgmhZSj$LOjohF0AohgfWtQyeVFRcmw/acbvu2LZvpCI5LUu+F8=',

	}

	response = requests.post(token_url, data=token_data)
	token_json = response.json()
	if 'access_token' in token_json:
		access_token = token_json['access_token']
		request.session['access_token'] = access_token
		return HttpResponse(f"Successfull authentification. Access toke: {access_token}")
	else:
		error_description = token_json.get('error_description', 'Unknown error')
		return HttpResponse(f"Failed to obtain token: {error_description}")