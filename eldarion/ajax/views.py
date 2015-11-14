from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic.edit import BaseCreateView, BaseUpdateView, BaseFormView


class EldarionAjaxResponseMixin(object):

    template_fragment = None
    response_class = JsonResponse
    encoder_class = DjangoJSONEncoder
    safe = True

    def render_html(self, context):
        return render_to_string(
            self.template_fragment,
            RequestContext(self.request, context)
        )

    def render_location(self, url):
        return {
            "location": url
        }

    def render_to_response(self, context, **response_kwargs):
        data = {
            "html": self.render_html(context)
        }
        return self.response_class(
            data=data,
            encoder=self.encoder_class,
            safe=self.safe
        )


class EldarionAjaxCreateView(EldarionAjaxResponseMixin, BaseCreateView):

    def redirect(self):
        return self.response_class(
            data=self.render_location(self.get_success_url()),
            encoder=self.encoder_class,
            safe=self.safe
        )

    def form_valid(self, form):
        self.object = form.save()
        return self.redirect()


class EldarionAjaxUpdateView(EldarionAjaxResponseMixin, BaseUpdateView):

    def redirect(self):
        return self.response_class(
            data=self.render_location(self.get_success_url()),
            encoder=self.encoder_class,
            safe=self.safe
        )

    def form_valid(self, form):
        self.object = form.save()
        return self.redirect()


class EldarionAjaxFormView(EldarionAjaxResponseMixin, BaseFormView):

    def redirect(self):
        return self.response_class(
            data=self.render_location(self.get_success_url()),
            encoder=self.encoder_class,
            safe=self.safe
        )

    def form_valid(self, form):
        raise NotImplementedError("method needs to be defined by sub-class")
