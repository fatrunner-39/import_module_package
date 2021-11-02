from package import *
from datetime import date

now_date = date.today().strftime('%d.%m.%Y')


if __name__ == '__main__':
    print(f'Текущая дата: {now_date}')
    salary.calculate_salary()
    people.get_employees()
    print("Программа завершена. Модули 'salary' и 'people' импортированыю")