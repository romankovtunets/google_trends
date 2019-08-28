from django.shortcuts import render
from pytrends.request import TrendReq

from .forms import KeyWords


def get_keywords(request):

    if request.method == 'POST':
        form = KeyWords(request.POST)

        if form.is_valid():
            # process data
            keywords = form.cleaned_data['keywords'].split()
            pytrend = TrendReq()
            pytrend.build_payload(kw_list=keywords)
            interest_over_time = pytrend.interest_over_time()
            interest_html = interest_over_time.to_html()
            return render(request, 'index.html', {'data':
                                                  interest_html,
                                                  'form': form})
    else:
        form = KeyWords()

    return render(request, 'index.html', {'form': form})
