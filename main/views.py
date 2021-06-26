from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, View
from .models import Post, Brand, Phones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse


class MainIndex(ListView):
    model = Phones
    template_name = "main/index.html"

    def phone_carusel(self, request):
        return render(request, 'widgets/_carusel.html', {
            'phones': Phones.objects.all()
        })

    def phone_carusel_phone(self, request):
        phones = Phones.objects.get(id=request.GET.get('id1'))
        return render(request, 'widgets/_carusel.html', {
            'p': phones
        })


class CompareOne(View):
    def get(self, request, id):
        try:
            d = Phones.objects.get(id=id)
        except Phones.DoesNotExist:
            return redirect('main:compare-phones')

        # m = Phones.objects.filter(id=d.id)
        return render(request, "main/compare-one.html", {
            'one': d
        })

# def main_ajax(request):
#     Brand.objects.all()
#
#     # apple = Brand(name="Apple")
#     # apple.save()
#     # samsung = Brand(name="Samsung")
#     # samsung.save()
#     #
#     # Brand(parent=apple, name="iPhone 5").save()
#     # Brand(parent=apple, name="iPhone 6").save()
#     # Brand(parent=apple, name="iPhone 12").save()
#     #
#     # Brand(parent=samsung, name="Galaxy S20").save()
#     # Brand(parent=samsung, name="Galaxy S21").save()
#     # Brand(parent=samsung, name="Galaxy S5").save()
#     #
#     return render(request, 'widgets/ajax.html', {
#         'brands': Brand.objects.filter(parent__isnull=True).all()
#     })
#
#
# def main_child(request, pid):
#     return HttpResponse("".join(["<option value='{}'>{}</option>".format(row.id, row.name)
#                                 for row in Brand.objects.filter(parent_id=pid).order_by('id').all()]))
#

# class CompareIndex(ListView):
#     model = Phones
#     template_name = "main/compare.html"
#
#     def phone_compare(self, request):
#         return render(request, {
#             'phones': Phones.objects.all()
#         })


def ComaprePhones(request):
    if request.method == "POST":
        return redirect('main:compare-phones', i1=request.POST.get('i1'), i2=request.POST.get('i2'))

    return render(request, 'main/compare.html', {
        'phones': Phones.objects.all(),
        'brandes': Brand.objects.all()
    })




def Compare_Phones(request, i1, i2):
    phone1 = Phones.objects.get(id=i1)
    phone2 = Phones.objects.get(id=i2)
    return render(request, 'main/compare-phones.html', {
        'p1': phone1,
        'p2': phone2,

    })

# class PhoneIndex(ListView):
#     model = Phones
#     template_name = 'main/compare.html'
#
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(id=id)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('subject', 'content', 'image')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Maqola qo'shish"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user_id = self.request.user.id
        post.save()

        messages.success(self.request, "Maqola muvaffaqiytli qo'shildi.")

        return redirect('main:index')


class PhoneCreateView(LoginRequiredMixin, CreateView):
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




class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('main:index')








