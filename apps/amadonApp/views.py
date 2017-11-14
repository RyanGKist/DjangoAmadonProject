from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if 'total' in request.session:
		return render(request,"amadonApp/index.html")
	else:
		request.session['items'] = 0
		request.session['total'] = 0
		return render(request,"amadonApp/index.html")

def purchase(request):
	if request.method == 'POST':
		if request.POST['price'] == "111":
			request.session['current_purchase']   = 19.99 * int(request.POST['quantity'])
			request.session['total'] += request.session['current_purchase']
			request.session['items'] += int(request.POST['quantity'])
		if request.POST['price'] == '222':
			request.session['current_purchase']  = 29.99 * int(request.POST['quantity'])
			request.session['total'] += request.session['current_purchase']
			request.session['items'] += int(request.POST['quantity'])
		if request.POST['price'] == '333':
			request.session['current_purchase']  = 4.99 * int(request.POST['quantity'])
			request.session['total'] += request.session['current_purchase']
			request.session['items'] += int(request.POST['quantity'])
		if request.POST['price'] == '444':
			request.session['current_purchase'] = 49.99 * int(request.POST['quantity'])
			request.session['total'] += request.session['current_purchase']
			request.session['items'] += int(request.POST['quantity'])
		return render(request,'amadonApp/success.html')

def clear(request):
	request.session['total'] = 0
	request.session['items'] = 0
	return redirect('/')

def return_S(request):
	return redirect('/')
# Create your views here.
