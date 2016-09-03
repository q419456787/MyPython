import re

#  元字符 *={0,}  +={1,}

# 转移字符  \b 就是


#() 分组的作用

print(re.search(r'(a)b','bbb'))

#\1 反向引用时非常强大的，首先得引用() 然后分组了  \1 代表的是反向引用第一个分组
p = re.compile(r'(\b\w+)\s+\1')
print( p.search('Paris in the the spring').groups())

m = re.match("([abc])+", "abc")
print(m.groups())

m = re.match("(?:[abc])+", "abc")
print(m)





