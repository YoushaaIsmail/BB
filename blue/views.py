from django.shortcuts import render
from .models import Contact

from .models import AboutUs,profile

# def app(request):
#     about_us = AboutUs.objects.first()  # استرداد أول كائن "AboutUs" من قاعدة البيانات
#     return render(request, 'app.html', {'about_us': about_us})
from .models import categoriesPRODUCT

def app(request):
    about_us = AboutUs.objects.first()
    profile_obj = profile.objects.first()
    categories = categoriesPRODUCT.objects.all()  # استرداد جميع كائنات الفئات من قاعدة البيانات
    return render(request, 'app.html', {'about_us': about_us, 'profile': profile_obj, 'categories': categories})
def success(request):
    return render(request , 'success.html')


from django.shortcuts import render
from .models import categoriesPRODUCT, Product

def category(request, category_id):
    category = categoriesPRODUCT.objects.get(id=category_id)
    products = Product.objects.filter(categories1=category)
    categories = categoriesPRODUCT.objects.all()
    # return render(request, 'list.html', {'products': products, 'categories': categories})
    return render(request, 'category.html', {'category': category, 'products': products, 'categories': categories})



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        return render(request, 'success.html')
    return render(request, 'contact.html')

# def list(request):
#     return render(request , 'list.html')

from .models import Product

def list(request):
    products = Product.objects.all()
    categories = categoriesPRODUCT.objects.all()
    return render(request, 'list.html', {'products': products, 'categories': categories})
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, get_object_or_404
from .models import Product


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'details.html', {'product': product})





   
from django.shortcuts import render
# from .models import Product

# def details(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     return render(request, 'details.html', {'product': product})