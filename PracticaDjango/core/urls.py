from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, catalogo, nosotros, contacto, registro, mostrar_clientes, form_clientes,form_productos, form_mod_clientes,form_mod_productos, form_del_clientes, mostrar_productos, form_del_productos

urlpatterns = [
    path('', home,name='home'),
    path('catalogo/', catalogo,name='catalogo'),
    path('nosotros/', nosotros,name='nosotros'),
    path('contacto/', contacto,name='contacto'),
    path('registro/', registro,name='registro'),
    path('mostrar_clientes/', mostrar_clientes,name='mostrar_clientes'),
    path('mostrar_productos/', mostrar_productos,name='mostrar_productos'),
    path('form_clientes/', form_clientes,name='form_clientes'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('form_productos/', form_productos,name='form_productos'),
    path('form_mod_clientes/<id>', form_mod_clientes,name='form_mod_clientes'),
    path('form_mod_productos/<id>',form_mod_productos,name='form_mod_productos'),
    path('form_del_clientes/<id>', form_del_clientes,name='form_del_clientes'),
    path('form_del_productos/<id>', form_del_productos,name='form_del_productos'),
]   
