from django.shortcuts import render
from django.core.paginator import Paginator

from home.forms import TrackSearchForm
from home.utils import get_tracks


def main_page(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'home/main_page.html', context)


def track_search(request):
    tracks = None
    tracks_copied = []
    # Filters
    shipped_to = None
    shipped_from = None
    state = None
    senders_zip = 0
    paginator = None
    page_obj = []

    if request.POST:
        form = TrackSearchForm(request.POST)
        if form.is_valid():
            shipped_to, shipped_from, state, senders_zip = form.cleaned_data['shipped_to'], \
                                                           form.cleaned_data['shipped_from'], \
                                                           form.cleaned_data['state'], \
                                                           form.cleaned_data['senders_zip']
            tracks_copied = request.POST.get('tracks_copied')
            tracks = get_tracks(shipped_from=shipped_from,
                                shipped_to=shipped_to,
                                starting_from=0,
                                end_before=100,
                                state=state, senders_zip=senders_zip)
            paginator = Paginator(tracks, 20)
            num_page = request.POST.get('page', 1)
            page_obj = paginator.get_page(num_page)
    else:
        form = TrackSearchForm()
        if request.GET.get('page'):
            shipped_from = request.GET.get('shipped_from')
            shipped_to = request.GET.get('shipped_to')
            state = request.GET.get('state', None)
            senders_zip = request.GET.get('senders_zip', 0)
            tracks = get_tracks(shipped_from=shipped_from,
                                shipped_to=shipped_to,
                                starting_from=0,
                                end_before=100,
                                state=state, senders_zip=senders_zip)
            paginator = Paginator(tracks, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

    base_context = {
        'title': 'My track',
        'form': form,
        'tracks': tracks,
        'tracks_copied': tracks_copied
    }
    filter_context = {
        'shipped_to': str(shipped_to),
        'shipped_from': str(shipped_from),
        'state': state,
        'senders_zip': senders_zip if senders_zip else 0,
    }
    pagination_context = {
        'paginator': paginator,
        'page_obj': page_obj
    }
    return render(request, 'home/track_search.html', base_context | filter_context | pagination_context)


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
