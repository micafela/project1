from django import forms


class QRCodeForm(forms.Form):
    res_name = forms.CharField(
        max_length=50, label="Resturant Name",
        widget=forms.TextInput(attrs={
            'class': 'm-2 block ',
            'placeholder': ' Enter Restaurant name'
        }))

    url = forms.URLField(
        max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class': 'm-2 block border-gray-500',
            'placholder': 'Enter Restaurant Url'
        })
    )
