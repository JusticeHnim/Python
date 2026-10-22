def even_number_generator(max_n):
    ans = 2
    while ans <= max_n:
        yield ans
        ans += 2

for num in even_number_generator(10):
    print(num, end=" ")