def maxemerald(num, weights):
    sums_list = []
    current_sum= 0

    for i in range(num):
        if weights[i] % 2 == 0:
            current_sum += weights[i]
        else:
            if current_sum > 0:
                sums_list.append(current_sum)
            current_sum = 0

    if current_sum > 0:
        sums_list.append(current_sum)

    return max(sums_list) if sums_list else 0
num = int(input("enter the number of emeralds"))
weights = list(map(int, input("enter weights of each emerald(seperated by a space):").split()))

print("Maximum even weight sum:", maxemerald(num, weights))
