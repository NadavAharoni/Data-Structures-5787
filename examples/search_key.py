def print_list(a, format_func = lambda s: ""):
    for i in range(len(a)):
        print(f"{i}: {a[i]}, {format_func(a[i])}")


def linear_search(a, search_term, focus_func):
    for i in range(len(a)):
        print(f"{i}: checking if {focus_func(a[i])} == {search_term}")
        if search_term == focus_func(a[i]):
            return i
    return None

def last_name(scientist):
    return scientist[0]

def first_name(scientist):
    return scientist[1]


# ====
scientists = [("Curie", "Marie", 1898),
              ("Darwin", "Charles", 1859),
              ("Lovelace", "Ada", 1843),
              ("Newton", "Isaac", 1687)
             ]


index = linear_search(scientists, ("Curie", "Marie", 1898), lambda s: s)
print(index)

list_of_numbers = [100,
                   200,
                   320,
                   17]

index = linear_search(list_of_numbers, 200, lambda x : x)

# def len_name(s):
#     return len(s[0]) + len(s[1])

# def century(s):
#     return s[2] // 100

# print_list(scientists)
# print("==")
# print_list(scientists, lambda x: x[1]+" "+x[0])
# print("==")
# print_list(scientists, lambda s: s[2])


# print_list(scientists, len_name)
# print_list(scientists, century)


# sc1 = scientists[0]
# print(sc1)
# print(last_name(sc1))
# print(first_name(sc1))

# index = linear_search(scientists, "Curie", last_name)
# if index is not None:
#     print("index=", index, scientists[index])
# else:
#     print("not found")

# index = linear_search(scientists, "Curie", first_name)
# if index is not None:
#     print("index=", index, scientists[index])
# else:
#     print("not found")
