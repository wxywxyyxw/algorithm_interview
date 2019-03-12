from conf import re_path


def bar_view(request):
    pass


urlpatterns = [
    re_path('^bar/$', bar_view),
]