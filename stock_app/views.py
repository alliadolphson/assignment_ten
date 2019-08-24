from django.shortcuts import render
#Imports
from .models import Stock
from django.views.decorators.csrf import csrf_exempt
from .functions import *

# Create your views here.
@csrf_exempt
def index(request):
	"""The Home Page for Stock App"""
	selected_checkboxes = request.POST.getlist('selected_stocks', [])
	#Query a Stock
	stocks = Stock.objects.all()
	#Call Get_Chart function
	chart = Plot_Chart(stocks, selected_checkboxes)
	#Pass Stock Info to HTML Template
	context = {'stocks':stocks, 'selected_checkboxes':selected_checkboxes, 'chart':chart}
	return render(request, 'stock_app/index.html', context)
	
	
