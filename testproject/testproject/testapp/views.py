from django.shortcuts import render

from .forms import MessageForm


__all__ = ('index',)


def index(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(
        request,
        'testapp/index.html',
        {'form': form}
    )
