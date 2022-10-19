d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

def create_list():
    new_d = []
    for item in d.items():
        new_d.extend(item)
    print(new_d)

create_list() 