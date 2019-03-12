from importlib import import_module
from types import ModuleType
from resolvers import RegexPattern, URLResolver, URLPattern


def re_path(route, view):
    if isinstance(view, ModuleType):
        # For include(...) processing.
        pattern = RegexPattern(route)
        urlconf_module = view
        return URLResolver(
            pattern,
            urlconf_module,
        )

    elif callable(view):
        pattern = RegexPattern(route)
        return URLPattern(pattern, view)
    else:
        raise TypeError('blah blah blah')


def include(urlconf_module):
    return import_module(urlconf_module)
