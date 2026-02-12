from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ["titulo", "descripcion", "precio", "categoria"]

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
        }


    def clean_precio(self):
        precio = self.cleaned_data.get("precio")

        if precio is None:
            raise forms.ValidationError("Debes introducir un precio.")

        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")

        return precio

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")

        if not descripcion:
            raise forms.ValidationError("La descripción es obligatoria.")

        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")

        return descripcion
