def right_sum(wheel):
    a = wheel.pop()
    return [a] + wheel
def left_sum(wheel):
    a = wheel.pop(0)
    return wheel + [a]

print(left_sum([1, 2, 3]))