def string_length(s: str = '') -> int:
    return (len(s))


s: str = 'жджыд'

print(string_length(s))

s: str = 'жджsdfsdfыд'

print(string_length(s))

#___________________________________________________________


def list_length(a: list, b: list) -> int:
    return max(len(a), len(b))


a = (1, 2, 4, 5, 6)

b = (1, 2, 4, 5, 6, 7)

print(list_length(a, b))

#___________________________________________________________


def adding_value(list: list) -> int:
    list.append('d')

    return list


a = 4

b = 3

c = 2

print(adding_value([a, b, c]))

#___________________________________________________________


def list_sum(list: list) -> int:
    result = 0

    for elem in list:
        result = result + elem
    return result


print(list_sum([1, 2, 3, 4, 5, 6]))





