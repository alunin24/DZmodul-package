class People:
    def __init__(self, fullname):
        self.fullname = fullname

    def get_employees(self):
        print('Список сотрудников:')
        for f_name in self.fullname:
            print(f'{f_name.title()}')

if __name__ == "__main__":
    list_ = [('андрей сергеевич'), ('герман волков'), ('николай николаев')]
    person = People(list_)
    person.get_employees()