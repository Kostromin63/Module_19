from django.shortcuts import render
from .forms import UsrRegister
from django.views.generic import TemplateView
from task1.models import Buyer, Game

# /////////////////////////////////////////////////////////////////////////////////
# // Регистрация

# users = ['Anton', 'Andre', 'Simon', 'Marya', 'Tereza', 'Fransua', 'Izabel', 'Ilia']
def sign_up_by_django(request):
    print(request.method)
    info = {}
    if request.method == 'POST':
        form = UsrRegister(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if Buyer.objects.filter(name=str(username)):
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            # elif int(age) < 18:
            #     info['error'] = 'Вы должны быть старше 18'
            else:
                new_buyer = Buyer(name=f"{username}", balance=0, age=age)
                new_buyer.save()
                info['salut'] = f'Приветствуем, {username}!'
    else:
        form = UsrRegister()

    info['form'] = form

    return render(request, 'registration_page.html', context=info)


# /////////////////////////////////////////////////////////////////////////////////
# // Магазин, Корзина  и Домашняя страница

class ClassHome(TemplateView):
    template_name = 'task1/platform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['title'] = 'Главная'
        return context


class ClassShop(TemplateView):
    template_name = 'task1/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        games = Game.objects.all()
        context['title'] = 'Игры'
        context['products'] = games
        return context


class ClassBasket(TemplateView):
    template_name = 'task1/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['title'] = 'Корзина'
        context['products'] = (['AtomicHeart', 'Cyberpunc 2077', 'PayDay 2'])
        return context