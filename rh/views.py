from django.views.defaults import ERROR_500_TEMPLATE_NAME
from django.views.decorators.csrf import requires_csrf_token
from django.template import TemplateDoesNotExist, loader
from django import http
from sekizai.context import SekizaiContext


@requires_csrf_token
def server_error(request, template_name=ERROR_500_TEMPLATE_NAME):
    """
    500 error handler which works with django-sekizai

    Templates: :template:`500.html`
    Context: None
    """
    html = '<h1>Server Error (500)</h1>'
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_500_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        template = None
    if template:
        try:
            # Only Django templates guaranteed to work here.
            context = SekizaiContext()
            html = template.template.render(context)
        except Exception:
            try:
                html = template.render()
            except Exception:
                pass
    return http.HttpResponseServerError(html, content_type='text/html')
