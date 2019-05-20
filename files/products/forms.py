from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
        title       = forms.CharField(label = '',widget = forms.TextInput(attrs = {"placeholder":"Your Title"}))
        description = forms.CharField(required = False, widget = forms.Textarea(
                                                                attrs = {
                                                                "placeholder":"Your Title",
                                                                "class": "new-class-name two",
                                                                "rows" : 20,
                                                                "cols" : 15,
                                                                "id"   : "my-id-for-textarea",
                                                                }
                                                                            )

                                        )
        price       = forms.DecimalField(initial = 199.99)
        class Meta:
            model = Product
            fields = [
            'title',
            'description',
            'price',
        ]

        def clean_title(self,*arg,**kwargs):
            title = self.cleaned_data.get("title")

            if "CFE" in title :
                return title
            else:
                raise forms.ValidationError("This is not a valid title ")   





class RawProduct(forms.Form):
    title       = forms.CharField(label = '',widget = forms.TextInput(attrs = {"placeholder":"Your Title"}))
    description = forms.CharField(required = False, widget = forms.Textarea(
                                                            attrs = {
                                                            "placeholder":"Your Title",
                                                            "class": "new-class-name two",
                                                            "rows" : 20,
                                                            "cols" : 15,
                                                            "id"   : "my-id-for-textarea",
                                                            }
                                                                        )

                                    )
    price       = forms.DecimalField(initial = 199.99)
