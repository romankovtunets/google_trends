from django.shortcuts import render
from .forms import KeyWords


def get_keywords(request):

    if request.method == 'POST':
        form = KeyWords(request.POST)

        if form.is_valid():
            # process data
            data = form.cleaned_data['keywords']
            return render(request, 'index.html', {'data': data, 'form': form})
    else:
        form = KeyWords()

    return render(request, 'index.html', {'form': form})
