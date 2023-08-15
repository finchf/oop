class Employee:

    def __init__(self, name, day_salary):
        self.name = name
        self._day_salary = day_salary

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days):
        return int(self._day_salary * (days/7*5))

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self._day_salary == other._day_salary

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self._day_salary < other._day_salary






class Recruiter(Employee):

    def work(self):
        return 'I come to the office and start to hiring.'

    def position(self):
        return self.__str__()


class Developer(Employee):
    def __init__(self, name, day_salary, tech_stack: list):
        super().__init__(name, day_salary)
        self.tech_stack = tech_stack

    def work(self):
        return 'I come to the office and start to coding.'

    def position(self):
        return self.__str__()

    def __lt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) < len(other.tech_stack)


    def __add__(self, other):
        if isinstance(other, Developer):
            combined_name = f"{self.name} {other.name}"
            combined_tech_stack = list(set(self.tech_stack + other.tech_stack))
            combined_salary = max(self._day_salary, other._day_salary)
            return Developer(combined_name, combined_salary, combined_tech_stack)


# Создание объектов
recruiter = Recruiter('Misha', 100)
developer1 = Developer('Gosha', 150, ['Python', 'JavaScript'])
developer2 = Developer('Anna', 120, ['Python', 'Java'])

# Проверка метода work()
print(recruiter.work())  # Output: I come to the office and start to hiring.
print(developer1.work())  # Output: I come to the office and start to coding.

# Проверка метода position()
print(recruiter.position())  # Output: Recruiter: Misha
print(developer1.position())  # Output: Developer: Gosha

# Проверка метода __lt__()
print(developer1 < developer2)  # Output: False
print(developer2 < developer1)  # Output: True

# Проверка метода __add__()
combined_developer = developer1 + developer2
print(combined_developer.name)  # Output: Gosha Anna
print(combined_developer.tech_stack)  # Output: ['Python', 'JavaScript', 'Java']
print(combined_developer._day_salary)  # Output: 150  # Зарплата developer1, так как она больше

# Проверка на равенство (метод __eq__)
print(developer1 == developer2)  # Output: False