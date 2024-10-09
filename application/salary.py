import random

class Salary:
    def __init__(self, service_ratio):
        self.rates = 100_000
        self.service_ratio = service_ratio


    def calculate_salary(self):
        amount = self.rates * self.service_ratio
        print(f"Ваша зарплата: {amount} рублей")

if __name__ == "__main__":

    random_element = random.choice([2, 3, 4, 4, 6])
    full_sallary = Salary(random_element)
    full_sallary.calculate_salary()