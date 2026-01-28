from django.shortcuts import render
from . import forms
import qr_code
import os
from django.conf import settings


def products(request):
    if request.method == "POST":
        form = forms.QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['res_name']
            url = form.cleaned_data['url']

            # generate
            qr = qr_code.make(url)
            file_name = res_name.replace(' ', '_').lower()+'_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)
            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            return render(request, 'qrcode.html', {"qr_url": qr_url, 'rn': res_name, 'file_name': file_name})
    else:

        form = forms.QRCodeForm()

        return render(request, 'products.html', {'form': form})
