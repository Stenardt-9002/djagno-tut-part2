from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request,*args,**kwargs):
    print(request.user)
    # return HttpResponse("<h1>HelloWorld </h1>")
    return render(request,"home.html",{})
    #returning html file
      #url


def citaact(request,*args,**kwargs):
    # return HttpResponse("<h1>This is the contact page</h1>")
    return render(request,"cunty.html",{})

    #url

def about_view(request):
    my_ctext = {
        "my_text": "This is about the product",
        "my_no" : 123,
        "my_lit" : ['ad',' ','is']
        #logic shuld be hand;ed here
    }#any datatype
    return render(request,"about.html",my_ctext)
