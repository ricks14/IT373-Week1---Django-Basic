from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
		'course': 'IT373 - Websys and Technologies 2',
		'week': 1,
	}
	return render(request, 'pages/home.html', context)

def hello(request):
	return render(request, 'pages/hello.html')

def about(request):
	return render(request, 'pages/about.html')