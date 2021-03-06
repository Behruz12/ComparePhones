from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, View
from .models import Post, Brand, Phones
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages


class MainIndex(ListView):
    """
    Telefonlarni asosiy pageda chiqazadi
    """
    model = Phones
    template_name = "main/index.html"

    def phone_carusel(self, request):
        """
        Telfinni carusle qilib chiqazadi
        """
        return render(request, 'widgets/_carusel.html', {
            'phones': Phones.objects.all()
        })


    def phone_carusel_phone(self, request):
        """
        Har bir telfoni idsini compare-on pagega bervorishga
        """
        phones = Phones.objects.get(id=request.GET.get('id1'))
        return render(request, 'widgets/_carusel.html', {
            'p': phones
        })



class CompareOne(View):
    """
    Carusledegi telfoni ozini xaraktrikani chiqazadi
    """
    def get(self, request, id):
        try:
            d = Phones.objects.get(id=id)
        except Phones.DoesNotExist:
            return redirect('main:compare-phones')

        return render(request, "main/compare-one.html", {
            'one': d
        })


def ComaprePhones(request):
    """
    Telfonlarnin tanlab solishtirish
    """
    if request.method == "POST":
        return redirect('main:compare-phones', i1=request.POST.get('i1'), i2=request.POST.get('i2'))

    return render(request, 'main/compare.html', {
        'phones': Phones.objects.all()
    })


def Compare_Phones(request, i1, i2):
    """
    Ikkla telfoni malumotlarni olib htmlga bervoradi
    """
    phone1 = Phones.objects.get(id=i1)
    phone2 = Phones.objects.get(id=i2)
    return render(request, 'main/compare-phones.html', {
        'p1': phone1,
        'p2': phone2,

    })


class PhoneCreateView(LoginRequiredMixin, CreateView):
    """
    Yengi telefon qoshish
    """
    model = Phones
    fields = ('name', 'datetime', 'dimensions', 'weight', 'colors', 'Approximate_price', 'display_dioganal', 'display_type', 'memory_type', 'battery_type', 'brand_id', 'ram_type', 'image')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Phone qo'shish"

    def form_valid(self, form):
        phone = form.save(commit=False)
        phone.user_id = self.request.user.id
        phone.save()

        messages.success(self.request, "Maqola muvaffaqiytli qo'shildi.")

        return redirect('main:index')












