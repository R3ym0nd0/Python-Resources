#map() Function

#Example 1:

store = [("shirt",1000),
         ("T-shirt",2000),
         ("Jacket",5000)]

to_euros = lambda data: (data[0],data[1]*0.82)

store_euros = map(to_euros, store)

for i in store_euros:
    print(i)

#Example 2:

a: list[str] = ["Reymond", "Gian", "Eiann", "Jerome", "Carlo"]
b = lambda c: c.removeprefix("R")


result: list[str] = list(map(b, a))
print(result)