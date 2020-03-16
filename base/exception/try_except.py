try:
    answer = 5 / 0
except ZeroDivisionError:
    print('can not divide by zero!')
else:
    print(answer)