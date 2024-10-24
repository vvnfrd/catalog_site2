from django.shortcuts import render

def catalog_list(request):
    return render(request, 'catalog/index.html')