import json

from django.http import HttpResponse
from django.views import generic

from mark_map.models import Coordinates
import logging

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = 'mark_map/index.html'


def save_coordinates(request):
    if 'coordinates' in request.POST and request.method == 'POST':
        coordinates = request.POST['coordinates']
        try:
            # raise Exception
            Coordinates.objects.create(coordinate=coordinates)
            result = {'success': True, 'message': "Coordinate well inserted."}
        except Exception as ex:
            # logger.error('Something went wrong!')
            result = {'success': False,
                      'message': "Something wrong have happened the Coordinate could not be processed."}
    else:
        result = {'success': False, 'message': "Bad request."}
    return HttpResponse(json.dumps(result), content_type='application/json')


def reset_data(request):
    if request.method == 'POST':
        Coordinates.objects.all().delete()
        result = {'success': True, 'message': "All the data were erased."}
    else:
        result = {'success': False, 'message': "Bad request."}
    return HttpResponse(json.dumps(result), content_type='application/json')
