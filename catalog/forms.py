#
# from django import forms
# from .models import Product
#
#
# FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
#
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'price')
#
#     def clean_name(self):
#         name = self.cleaned_data['name'].lower()
#         for word in FORBIDDEN_WORDS:
#             if word in name:
#                 raise forms.ValidationError(f"Название не может содержать слово '{word}'")
#         return self.cleaned_data['name']
#
#     def clean_description(self):
#         description = self.cleaned_data['description'].lower()
#         for word in FORBIDDEN_WORDS:
#             if word in description:
#                 raise forms.ValidationError(f"Описание не может содержать слово '{word}'")
#         return self.cleaned_data['description']
#
# #

from django import forms
from .models import Product


FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError(f"Название не может содержать слово '{word}'")
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError(f"Описание не может содержать слово '{word}'")
        return self.cleaned_data['description']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price
