from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def index(request):
    productos = Producto.objects.all()[:3]
    return render(request, "productos/index.html", {"productos": productos})



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista_productos.html", {"productos": productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "productos/detalle_producto.html", {"producto": producto})


@login_required
def mis_productos(request):
    productos = Producto.objects.filter(vendedor=request.user)
    return render(request, "productos/mis_productos.html", {"productos": productos})


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy("mis_productos")

    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super().form_valid(form)


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/producto_form.html"
    success_url = reverse_lazy("mis_productos")

    def get_queryset(self):
        return Producto.objects.filter(vendedor=self.request.user)


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("mis_productos")

    def get_queryset(self):
        return Producto.objects.filter(vendedor=self.request.user)



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")
