from django.utils import simplejson
from django.http import HttpResponse

from .forms import NicEditImageForm


def upload(request):
    if not request.user.is_authenticated():
        json = simplejson.dumps({
            'success': False,
            'errors': {'__all__': 'Authentication required'}})
        return HttpResponse(json, mimetype='application/json')
    form = NicEditImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        image = form.save()
        json = simplejson.dumps({
            'success': True,
            'upload': {
                'links': {
                    'original': image.image.url},
                'image': {
                    'width': image.image.width,
                    'height': image.image.height}
            }
        })
    else:
        json = simplejson.dumps({
            'success': False, 'errors': form.errors})
    return HttpResponse(json, mimetype='application/json')
