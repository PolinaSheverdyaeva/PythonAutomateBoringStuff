def sum_mul(n, m):

    if m < 0 or n < 0:
        return "INVALID"
    else:

        sum = 0
        num = 0

        while sum < m:
            sum = sum + n
            if sum >= m: break
            num = sum + num
        return num

print(sum_mul(2,9)) #20
print(sum_mul(3,13)) #30
print(sum_mul(4,123)) #1860
print(sum_mul(4,-7)) #INVALID

