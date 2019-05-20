from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .forms import ProductForm,RawProduct

from .models import Product

# Create your views here.
# def product_create_view(request):

#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()


#     context = {
#         "form" : form
#     }
#     return render(request, "products/products_create.html" , context)

# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     my_new_title = request.POST.get('title')
#     #really bad method of saving data
#     print(my_new_title)
#     context = {}
# #     return render(request, "products/products_create.html" , context)
# #
#
# def product_create_view(request):
#     myform = RawProduct(request.GET)
#     if request.method == "POST":
#         myform = RawProduct(request.POST)
#         if myform.is_valid():
#             print("DATA TIME")
#             print(myform.cleaned_data)
#             # Product.objects.create(title = my_new_title)
#             Product.objects.create(**myform.cleaned_data)
#         else:
#             print("ERROR TIME")
#             print(myform.errors)
#             #form already renders bad input
#     context = {
#         "form": myform
#     }
#     return render(request, "products/products_create.html" , context)
#
#

# def product_create_view(request):
#     my_form = RawProduct(request.GET)
#     if request.method == "POST":
#         my_form = RawProduct(request.POST)
#         if my_form.is_valid():
#             print("CLEAN DAAt")
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(" ERROR TIME form itself renders out the problem ")
#             print(my_form.errors)
#     context = {
#         "form" : my_form
#     }
#     return render(request,"products/products_create.html",context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     # 'title': obj.title,
#     # 'description' : obj.description
#     #
#     # }
#     context = {
#         "object" : obj
#     }
#     return render(request, "products/details.html" , context)


def render_initial_data(request):
    ini_data = {
        'title' : "My this awesome title"
    }
    obj = Product.objects.get(id = 1)

    # form = RawProduct(request.POST or None,initial = ini_data)
    form = ProductForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
    contxt = {
        'form':form 
    }

    return render(request,"products/products_create.html",contxt)


def dynamic_lookup_view(request,my_id):
    # obj = Product.objects.get(id = my_id)
    
    
    # try:
    #     obj = Product.objects.get(id = my_id)
    #     contxt = {
    # "object":obj,
    # }
    # except:
    #     obj = "NON EXISTING PRODUCT"
    #     contxt = {"object":obj,}

    # try:
    #     obj = Product.objects.get(id = my_id)
    # except Product.DoesNotExist :
    #     raise Http404



    obj = get_object_or_404(Product, id = my_id)
    contxt = { "object":obj, }


          
    return render(request,"products/details.html",contxt)


def product_dele_view(request,my_id):
    obj = get_object_or_404(Product, id = my_id)
    if  request.method == 'POST':
        obj.delete()
        return redirect('../')
    contxt = {
        "object":obj,
    }
    return render(request,"products/product_delete.html",contxt)

def product_lit_vew(request):
    queryset = Product.objects.all()
    contxt = {
        "objet_list" : queryset
    }
    return render(request,"products/product_lit.html",contxt)
