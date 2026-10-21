scientists = [("Curie", "Marie", 1898),
              ("Darwin", "Charles", 1859),
              ("Lovelace", "Ada", 1843),
              ("Newton", "Isaac", 1687)
             ]

def linear_search(a, target, key):
    for i in range(len(a)):
        if target == key(a[i]):
            return i
    return None

def last_name(scientist):
    return scientist[0]

def first_name(scientist):
    return scientist[1]

sc1 = scientists[0]
print(sc1)
print(last_name(sc1))
print(first_name(sc1))

index = linear_search(scientists, "Curie", last_name)
if index is not None:
    print("index=", index, scientists[index])
else:
    print("not found")

index = linear_search(scientists, "Curie", first_name)
if index is not None:
    print("index=", index, scientists[index])
else:
    print("not found")
