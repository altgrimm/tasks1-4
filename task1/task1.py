

def func(n, m):
    current = 0
    result = []

    while True:
        result.append((current % n) + 1)  # добавить элемент в путь
        print(result)
        # index = (index + step) % len
        current = (current + m - 1) % n  # перейти к следующему интервалу
        print(current)
        if current == 0:
            break

n = 5
m = 4

if __name__ == "__main__":
    func(n, m)
