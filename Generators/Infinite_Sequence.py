def power_of_two(limit=None):
    ans = 1
    count = 0
    while limit is None or count <= limit:
        yield ans
        ans*=2
        count+=1

my_ans = power_of_two()
print(next(my_ans))
print(next(my_ans)) 