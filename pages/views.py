from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'pages/home.html')

def about(request):
	context = {
		'college': 'Eastern Visayas State University',
		'course': 'BSIT',
		'name': 'Ricky L. Rulida Jr.',
		'id': '2023-10680',
	}
	return render(request, 'pages/about.html', context)