# utility views

import json

from django.http import HttpResponse


class JSONResponseMixin(object):
    def json_response(self, context, **kwargs):
        return HttpResponse(
            json.dumps(context),
            content_type='text/json',
            **kwargs)


class JSONFormMixin(JSONResponseMixin):

    def render_form(self, form):
        raise Exception('form render function must be defined')

    def handle_form(self, form):
        # TODO: see if we should call form.handle()
        return {"status": True}

    def form_invalid(self, form):
        form_html = self.render_form(form)

        response = super(JSONResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            data = {
                "html": form_html,
                "success": False
            }
            return self.json_response(data, status=200)
        else:
            return response

    def form_valid(self, form):
        response = super(JSONFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = self.handle_form(form)
            return self.json_response(data)
        else:
            return response
