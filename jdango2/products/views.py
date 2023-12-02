from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView

from jdango2.products.forms import FormModelForm
from jdango2.products.models import ProductModel, CategoryModel


def index_page(request):
    # products = ProductModel.objects.all().filter(title__icontains="Iphone12")
    # products = ProductModel.objects.all().order_by('-id')

    return render(request, 'index.html', )


# def shop_page(request):
#     products = ProductModel.objects.all()
#     return render(request, 'shop.html', {'product': products})

# CBV - Class Based Views
class ShopPageView(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            qs = qs.filter(category_id=category)


        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()

        return context


class ShopDetailView(DetailView):
    template_name = 'shop-details.html'
    model = ProductModel
    context_object_name = 'products'


class AboutPageView(TemplateView):
    template_name = 'about.html'


# context ={}
#
#     # add the dictionary during initialization
#     form = GeeksForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context['form']= form
#     return render(request, "create_view.html", context)
def send_form(request):
    context = {}

    form = FormModelForm(request.POST)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'forms.html', context)


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        else:
            # Пользователь с таким именем уже существует, выполните обработку ошибки или сообщение
            return redirect('/')

    return render(request, 'account/signup.html')

