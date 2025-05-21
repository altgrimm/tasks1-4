import json
import sys

# открыть и считать json
def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
# сохранить json
def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# из данных values.json создаем словарь вида {id: value}, чтобы потом искать значение по ID 
def build_value_map(values_data):
    return {item["id"]: item["value"] for item in values_data["values"]}

#
def fill_values(tests, value_map):
    # проход по каждому элементу tests
    for test in tests:
        # взять id
        test_id = test.get("id")
        # если такой id есть в value_map, записываем значение поля value этого id в test.json
        if test_id in value_map:
            test["value"] = value_map[test_id]
        # если у tests есть вложенные тесты ("values"), рекурсивно вызываем fill_values() для них.    
        if "values" in test:
            fill_values(test["values"], value_map)

def main():
    #считать пути к 3 файлам из терминала
    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    result_path = sys.argv[3]

    #считать данные из tests
    tests_data = load_json(tests_path)
    # считать данные из values
    values_data = load_json(values_path)
    # вызов функции для создания словаря
    value_map = build_value_map(values_data)
    # заполняем значения в tests по id
    fill_values(tests_data["tests"], value_map)

    save_json(tests_data, result_path)

if __name__ == "__main__":
    main()