from django.shortcuts import render

from home.forms import TrackSearchForm


def main_page(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'home/main_page.html', context)


def track_search(request):
    if request.POST:
        form = TrackSearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = TrackSearchForm()
    print(form)
    context = {
        'title': 'My track',
        'form': form
    }
    return render(request, 'home/track_search.html', context)


def payment(request):
    context = {
        'title': 'Payment'
    }
    return render(request, 'home/payment.html', context)


def my_track(request):
    context = {
        'title': 'My track'
    }
    return render(request, 'home/my_track.html', context)
