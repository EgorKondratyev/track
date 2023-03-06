from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'home/main_page.html', context)
