def show_menu() -> int:
    print("\n" + "=" * 30)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def refine_search():
    print("\n" + "=" * 30)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника по ID")
    print("2. Найти сотрудника по фамилии")
    print("3. Найти сотрудника по имени")
    print("4. Найти сотрудника по номеру телефона")
    return int(input("Введите номер необходимого действия: "))


def search_id()  -> int:
    id =  int(input('введите ID сотрудника: '))
    return id 

def search_ln():
    last_name = input('введите фамилию: ')    
    return last_name
    
def search_name():
    name =  input('введите имя: ') 
    return name   
    
def search_phone():
    phone_num =  input('введите номер телефона: ') 
    return phone_num   
    
def search_position():
    position =  input('введите должность: ') 
    return position

def get_salary_range():
    lo = float(input('введите меньшее значение: '))
    hi = float(input('введите большее значение: '))
    return lo, hi

def update_employee(employees):
    id = input("Введите ID сотрудника для изменения: ")
    print("Выберите необходимое действие")
    print("1. Изменить должность сотрудника ")
    print("2. Изменить фамилию сотрудника ")
    print("3. Изменить имя сотрудника")
    print("4. Изменить номер телефона сотрудника")
    print("5. Изменить зарплату сотрудника")   
    number = int(input("Введите номер необходимого действия: "))
    if number == 1:
        key  = "position"
    if number == 2:
        key = "last_name"
    if number == 3:
        key = "first_name"
    if number == 4:
        key = "phone_number"
    if number == 5:
        key = "salary"  
    new = input("Введите новое значение: ")    
    return id, key, new

def add_employee():
    employee = []
    keys = ["id", "last_name", "first_name", "position", "phone_number","salary"]
    for key in keys:
        z = {}
        z[key] = input(f'Введите {key}  сотрудника: ')
        employee.append(z)
    return employee



