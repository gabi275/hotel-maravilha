from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def pagina_com_filtros(context, numero):
    params = context['request'].GET.copy()
    params['page'] = numero
    return '?' + params.urlencode()
