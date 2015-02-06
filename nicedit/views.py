try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponse

from .forms import NicEditImageForm


def upload(request):
    if not request.user.is_authenticated():
        json_data = json.dumps({
            'success': False,
            'errors': {'__all__': 'Authentication required'}})
        return HttpResponse(json_data, mimetype='application/json')
    form = NicEditImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        image = form.save()
        json_data = json.dumps({
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
        json_data = json.dumps({
            'success': False, 'errors': form.errors})
    return HttpResponse(json_data, mimetype='application/json')
