from resolvers import URLResolver, RegexPattern
urlconf = 'urls1'
#因为第一次match必须成功，所以RegexPattern是／
r = URLResolver(RegexPattern(r'^/'), urlconf)  # 树根

# print(r.resolve('/foo/'))
# print(r.resolve('/foo/1234/'))
# print(r.resolve('/myapp/bar/'))
pattern = RegexPattern(r'^/')
print (pattern.match('/foo/'))
