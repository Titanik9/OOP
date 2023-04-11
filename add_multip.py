class iter:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

number_a = iter(4)

number_b = iter(12)

print(number_a * number_b)