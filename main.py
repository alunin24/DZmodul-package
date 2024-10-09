from application.db.people import People
from application.salary import Salary
import random
from datetime import datetime, timedelta, date
import locale


locale.setlocale(locale.LC_ALL, 'ru_RU')
now = datetime.now()
print(f'Текущее время:\n{now.strftime('%c')}')


if __name__ == "__main__":
    list_ = [('сергей сергеевич'), ('иван иванов'), ('николай николаев')]
    person = People(list_)
    person.get_employees()

    random_element = random.choice([1.1, 1.2, 1.3, 1.4, 1.5])
    full_sallary = Salary(random_element)
    full_sallary.calculate_salary()