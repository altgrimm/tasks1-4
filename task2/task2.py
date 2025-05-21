import sys

from decimal import Decimal

#считать координаты центра и радиуса окружности из файла
def read_circle_data(file_path):
    with open(file_path, 'r') as f:
        #центр
        x_str, y_str = f.readline().split()
        #окружность
        r_str = f.readline().strip()
        #перевод str в decimal
        return Decimal(x_str), Decimal(y_str), Decimal(r_str)
    
#считать координаты точек из файла
def read_points(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():
                # разбить текст на 2 координаты
                x_str, y_str = line.split()
                #добавить decimal точки в points
                points.append((Decimal(x_str), Decimal(y_str)))
    return points

# xc, yc - координаты центра
# r-радиус, x, y - координаты точки
def point_position(xc, yc, r, x, y):
    # расстояние до точки по оси x
    dx = x - xc
    # расстояние до точки по оси y
    dy = y - yc
    # квадрат расстояния до центра
    dist_squared = dx * dx + dy * dy
    # квадрат радиуса
    r_squared = r * r

    # если квадрат расстояния = квадрат радиуса
    if dist_squared == r_squared:
        return 0  # точка на окружности
    elif dist_squared < r_squared:
        return 1  # точка внутри
    else:
        return 2  # точка снаружи

def main():
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # считать координаты центра и радиуса
    xc, yc, r = read_circle_data(circle_file)
    # считать координаты точек
    points = read_points(points_file)

    for x, y in points:
        print(point_position(xc, yc, r, x, y))


if __name__ == "__main__":
    main()