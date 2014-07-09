# utility views

import json

from django.http import HttpResponse


class JSONResponseMixin(object):
    def json_response(self, context, **kwargs):
        return HttpResponse(
            json.dumps(context),
            content_type='text/json',
            **kwargs)
