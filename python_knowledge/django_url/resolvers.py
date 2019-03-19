import re
from importlib import import_module


class Resolver404(Exception):
    pass


class URLResolver:
    def __init__(self, pattern, urlconf_name):
        self.pattern = pattern
        self.urlconf_name = urlconf_name

    def resolve(self, path):
        print ('resolve')
        match = self.pattern.match(path)
        if match:
            new_path, args, kwargs = match
            for pattern in self.urlconf_module.urlpatterns:
                try:
                    sub_match = pattern.resolve(new_path)
                except Resolver404 as e:
                    pass
                else:
                    if sub_match:
                        return ResolverMatch(
                            sub_match.func,
                            sub_match.args,
                            sub_match.kwargs,
                        )
            raise Resolver404({'path': new_path})
        raise Resolver404({'path': path})

    @property
    def urlconf_module(self):
        if isinstance(self.urlconf_name, str):
            return import_module(self.urlconf_name)
        else:
            return self.urlconf_name


class URLPattern:
    """
    path匹配成功后，返回ResolverMatch
    """
    def __init__(self, pattern, callback):
        self.pattern = pattern
        self.callback = callback  # the view

    def resolve(self, path):
        match = self.pattern.match(path)
        if match:
            _, args, kwargs = match
            return ResolverMatch(self.callback, args, kwargs)

class ResolverMatch:
    """
    路径与函数的结合
    """
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __getitem__(self, index):
        return (self.func, self.args, self.kwargs)[index]

    def __repr__(self):
        return "ResolverMatch(func=%s, args=%s, kwargs=%s)" % (self.func, self.args, self.kwargs)


class RegexPattern:
    """
    返回正则匹配的余下部分
    """
    def __init__(self, regex):
        self.regex = re.compile(regex)

    def match(self, path):
        match = self.regex.search(path)
        if match:
            print ('match')
            kwargs = match.groupdict()
            args = () if kwargs else match.groups()
            return path[match.end():], args, kwargs  # 这里path[match.end():]返回后面未匹配的部分。比如'^myapp/'匹配'myapp/bar/', 就变成了'bar/'
        return None

