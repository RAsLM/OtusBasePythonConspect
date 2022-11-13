from itertools import chain, combinations, combinations_with_replacement, count, repeat, cycle, zip_longest, groupby

results = [
    ['Engineer'],
    ['Manager'],
    ['Support'],
    ['QA'],
]

# print(list(chain(*results)))

nums = range(10)
print(nums)
# print(list(combinations(nums, 2)))
# print(list(combinations(nums, 3)))
# print(list(combinations_with_replacement(nums, 2)))

odds = count(start=1, step=2)
# print(list(next(odds) for _ in range(10)))

# r_5 = repeat(5)
# print([next(r_5) for _ in range(7)])


c_name = cycle(["John", "Sam", "Nick"])
# print([next(c_name) for _ in range(13)])

a = (1, 2, 3)
b = ("a", "b", "c")
c = ("X", "Y", "Z")

# print(list(zip(a, b, c)))

# result = [(1, 'a', 'X')], (2, 'b', 'X'), [(3, 'c', 'Z')]
# print(list(zip(*result)))

k = (1, 2, 3, 4)
j = ("A", "B")
# print(list(zip(k, j)))
# print(list(zip_longest(k, j, fillvalue='Z')))

my_list = range(17)

print(list(groupby(my_list, 5)))
