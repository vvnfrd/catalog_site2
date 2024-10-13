from django.shortcuts import render

def catalog_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, {email}, {message}')
    return render(request, 'catalog/index.html')