import random



avg_error = 0.0
runs = 1000
rolls = 3000
sides_of_die = 6
round_digits = 9

# what's the correct answer?
correct_value = 0.0
for i in range(1, sides_of_die+1):
    correct_value += i
correct_value /= sides_of_die


for _ in range(runs):
    # make an estimate!
    sum = 0.0
    for i in range(rolls):
        sum += random.randint(1,sides_of_die)

    measured = round(sum / rolls, round_digits)
    error = round(measured - correct_value, round_digits)
    avg_error += error
avg_error /= runs

print("It has an error of:", avg_error)