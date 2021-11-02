from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

now_date = date.today().strftime('%d.%m.%Y')

if __name__ == '__main__':
    print(f'Текущая дата: {now_date}')
    calculate_salary()
    get_employees()
    print("Программа завершена. Модули 'salary' и 'people' импортированыю")
