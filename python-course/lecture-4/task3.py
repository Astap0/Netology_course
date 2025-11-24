from re import split


queries = [
    "смотреть сериалы онлайн",
    "новости спорта",
    "афиша кино",
    "курс доллара",
    "сериалы этим летом",
    "курс по питону",
    "сериалы про спорт",
]

len_qu = []
for i in queries:
    len_qu.append(len(i.split()))
print(len_qu)
for i in set(len_qu):
    count = 0
    for j in len_qu:
        if i == j:
            count += 1
    print(f"{i} слова - {(count / len(queries) * 100):.2f}%")
