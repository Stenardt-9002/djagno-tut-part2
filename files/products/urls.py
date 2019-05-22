#urls for app itself

from django.urls import path
from .views import (
    render_initial_data,
    dynamic_lookup_view,
    product_dele_view,
    product_lit_vew,

)

app_name = 'products'
urlpatterns = [
      
    #path('create/',product_create_view,name = 'create'),
    path('create/',render_initial_data,name = 'create'),
    # path('product/',product_detail_view,name='product'),
    path('product/',render_initial_data,name='product'),
    path('productlist/',product_lit_vew,name='product-list'),
    path('no=<int:my_id>/',dynamic_lookup_view,name='product-dtail'),
    path('<int:my_id>/delete/',product_dele_view,name = 'product-delete')

]