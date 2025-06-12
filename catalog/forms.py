import re

from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
FORBIDDEN_PATTERN = re.compile(r'\b(' + '|'.join(FORBIDDEN_WORDS) + r')\b', re.IGNORECASE)


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    is_published = BooleanField(label="Опубликовать", required=False)

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price < 0:
            raise ValidationError('Цена введена неправильно')
        return purchase_price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if FORBIDDEN_PATTERN.search(name):
            raise ValidationError('Неуместное наименование товара')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if FORBIDDEN_PATTERN.search(description):
            raise ValidationError('Неуместное описание товара')
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            extension = image.name.split('.')[-1].lower()
            if extension not in ['jpg', 'jpeg', 'png']:
                raise ValidationError('Допустимы только форматы JPEG и PNG.')

            max_size = 5 * 1024 * 1024  # 5MB
            if image.size > max_size:
                raise ValidationError('Размер изображения не должен превышать 5MB.')
        return image

    class Meta:
        model = Product
        fields = ['name', 'description', 'purchase_price', 'category']
