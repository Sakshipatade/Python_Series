even_sum = 0
odd_sum = 0
for i in range(0,101):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(f"total even sum is {even_sum} and odd sum is {odd_sum}")