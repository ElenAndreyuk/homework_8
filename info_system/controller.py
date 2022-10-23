import model 
import view

def button_click():
    act = view.show_menu()
    employees = model.read_csv()
    while act != 9:
        if act == 1:
            number = view.refine_search()
            if number == 1:
                id = view.search_id()
                print(model.search_employee(employees, id, 'id'))
                break
            elif number == 2:
                last_name = view.search_ln()
                print(model.search_employee(employees, last_name, 'last_name'))
                break
            elif number == 3:
                name = view.search_name()
                print(model.search_employee(employees, name, 'first_name'))
                break
            elif number == 4:
                phone_num = view.search_phone()
                print(model.search_employee(employees, phone_num, 'phone_number'))
                break
            else:
                print('ошибка ввода')    
                break
        elif act == 2:
            position = view.search_position()
            print(model.search_employee(employees, position, 'position'))
            break
        elif act == 3:
            lo, hi = view.get_salary_range()
            print(model.find_employees_by_salary_range(employees, lo, hi))
            break
        elif act == 4:
            employees.append(view.add_employee())
            model.write_csv(employees)
        elif act == 5:
            id = view.search_id()
            employees = model.delete_employee(employees, id)
            model.write_csv(employees, id)
        elif act == 6:
            id, key, new = view.update_employee(employees)
            employee = model.search_employee(employees, id, 'id')
            print(employee)
            employees.append(model.update_employee(employee, key, new))
            model.write_csv(employees)
            break
        elif act == 7:
            print(model.read_json())
            break
        elif act == 8:
            print(model.read_csv())
            break
        else:
            print('ошибка ввода')    
            break
        act = view.show_menu()
    if act == 9:
        print('всего доброго')

        
    
