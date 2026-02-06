from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/", views.lista_productos, name="lista_productos"),
    path("producto/<int:pk>/", views.detalle_producto, name="detalle_producto"),
    path("mis-productos/", views.mis_productos, name="mis_productos"),
    path("producto/nuevo/", views.ProductoCreateView.as_view(), name="producto_nuevo"),
    path("producto/<int:pk>/editar/", views.ProductoUpdateView.as_view(), name="producto_editar"),
    path("producto/<int:pk>/eliminar/", views.ProductoDeleteView.as_view(), name="producto_eliminar"),
    
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

]
