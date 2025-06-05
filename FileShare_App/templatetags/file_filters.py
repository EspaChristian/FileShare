from django import template

register = template.Library()

@register.filter
def is_viewable(filename):
    viewable_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.txt']
    return any(filename.lower().endswith(ext) for ext in viewable_extensions)
