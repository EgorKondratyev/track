from django.shortcuts import render

from home.forms import TrackSearchForm
from home.utils import get_tracks


def main_page(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'home/main_page.html', context)


def track_search(request):
    tracks = None
    if request.POST:
        form = TrackSearchForm(request.POST)
        print(request.POST)
        if form.is_valid():
            shipped_to, shipped_from, state, senders_zip = form.cleaned_data['shipped_to'], \
                                                           form.cleaned_data['shipped_from'], \
                                                           form.cleaned_data['state'], \
                                                           form.cleaned_data['senders_zip']
            if state and senders_zip:
                pass
            elif state:
                pass
            elif senders_zip:
                pass
            else:
                print(shipped_from, shipped_to)
                tracks = get_tracks(shipped_from=shipped_from,
                                    shipped_to=shipped_to)
    else:
        form = TrackSearchForm()

    context = {
        'title': 'My track',
        'form': form,
        'tracks': tracks
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
