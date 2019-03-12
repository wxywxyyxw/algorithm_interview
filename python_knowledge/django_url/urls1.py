from conf import re_path, include


def foo_list_view(request):
    pass


def foo_view(request, user_id):
    pass


urlpatterns = [
    re_path('^foo/$', foo_list_view),
    re_path('^foo/(?P<user_id>\d+)/$', foo_view),
    re_path('^myapp/', include('urls2')),  # 这里用了include
]
