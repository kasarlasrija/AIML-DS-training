def count_even(num):
    count = 0
    for num in num:
        if num % 2 == 0:
            count += 1
    return count
list = [1, 2, 3, 4, 5, 6]
print(count_even(list))
