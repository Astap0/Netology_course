boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]
girls.sort()
boys.sort()

pairs = zip(boys, girls)


print("idial pairs:")
for i in tuple(pairs):
    print(f"{i[0]} and {i[1]}")
