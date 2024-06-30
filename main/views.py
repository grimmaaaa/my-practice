from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import View, ListView

from .forms import RegisterForm, LoginForm, CustomUserChangeForm, WeaponForm
from .models import RentPlace

from products.models import Product, RentOrder


User = get_user_model()


class MainView(View):

    def get(self, request):
        context = {
            'products': Product.objects.all()[:5]
        }
        context['ru_count'] = RentPlace.objects.filter(location=RentPlace.LocationCountries.russia).count()
        context['br_count'] = RentPlace.objects.filter(location=RentPlace.LocationCountries.brasil).count()
        context['it_count'] = RentPlace.objects.filter(location=RentPlace.LocationCountries.italy).count()
        context['kn_count'] = RentPlace.objects.filter(location=RentPlace.LocationCountries.kenia).count()
        context['nz_count'] = RentPlace.objects.filter(location=RentPlace.LocationCountries.new_zeland).count()
        context['zb_count'] = RentPlace.objects.filter(location=RentPlace.LocationCountries.zimbabve).count()

        return render(request, 'main/index.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('main:home')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            print(f'valid form: {form.cleaned_data}')
            user = form.get_user()
            login(request, user)
            return redirect('main:home')
        else:
            print(f'{form.errors}, {form.data}')
            return render(request, 'main/login.html', {'form': form})
    else:
        return render(request, 'main/login.html', {'form': LoginForm()})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:home')  # Redirect to a home page or any other page after successful registration
    else:
        form = RegisterForm()

    return render(request, 'main/register.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'main/user_page.html'
    success_url = reverse_lazy('main:user_page')

    def get_object(self):
        return self.request.user


class WeaponApplicationView(CreateView):
    form_class = WeaponForm
    template_name = 'main/application.html'

    def form_valid(self, form: WeaponForm) -> HttpResponse:
        application = form.save(commit=False)
        application.user = self.request.user
        application.save()

        return redirect('main:home')


class PlacesView(ListView):
    template_name = 'main/places.html'
    context_object_name = 'places'

    def get_queryset(self) -> QuerySet:
        location = self.kwargs['location']

        if location == 'all':
            return RentPlace.objects.all()

        return RentPlace.objects.filter(location=location)


class BookView(View, LoginRequiredMixin):

    def get(self, request, pk):
        try:
            place = RentPlace.objects.get(pk=pk)
        except Exception as e:
            return Http404()
        
        RentOrder.objects.create(
            user=self.request.user,
            place=place
        )

        return redirect('products:orders')
