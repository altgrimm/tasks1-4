import sys

def min_moves_to_equal_elements(nums):
    # сортировка массива
    nums.sort()
    # находим серединный элемент массива
    median = nums[len(nums) // 2]
    # находим расстояние каждого элемента массива от середины и складываем
    return sum(abs(num - median) for num in nums)

def main():  
    filename = sys.argv[1]

    try:
        # открываем файл
        with open(filename, 'r') as f:
            #удаляем пробелы и переводы строк, преобразуем str в int
            nums = [int(line.strip()) for line in f if line.strip()]
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    #вызываем функцию нахождения медианы массива
    result = min_moves_to_equal_elements(nums)
    print(result)

if __name__ == "__main__":
    main()
