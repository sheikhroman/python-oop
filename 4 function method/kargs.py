""" def full_name(f_name,l_name):
    name=f'{f_name} {l_name}'
    return name

name = full_name(l_name="Khan",f_name="Baccha")
print(name) """

""" def long_name(**kargs):
    print(kargs)

long_name(fist="Dr", last="Khan", middle="Baccha")
 """

from ast import arg
from multiprocessing.sharedctypes import Value


def name_mixed(first,last,**name_parts):
    print(first,last,name_parts)

name = name_mixed(first="Dr", last="Khan", middle="Baccha")
print(name)


def all_types(first, *args, **kargs):
    print(first)
    for word in args:
        print(word)
    print(kargs)
    for key, Value in kargs.items():
        print(key,Value)
all_types("abd","ddd","kjk","lll", "pp",name="Abul",father="Babul")