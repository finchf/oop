import csv
import datetime

class EmailAlreadyExistsException(Exception):
    pass


class Employee:

    def __init__(self, name, day_salary, email):
        self.name = name
        self._day_salary = day_salary
        self.email = email
        self.save_email()

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days):
        return int(self._day_salary * (days / 7 * 5))

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self._day_salary == other._day_salary

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self._day_salary < other._day_salary

    def save_email(self):
        with open('emails.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.email])

    def validate(self):
        try:
            with open('emails.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[1] == self.email:
                        raise EmailAlreadyExistsException
        except EmailAlreadyExistsException:
            self.log_error("Email already exists")

    def log_error(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{timestamp} | {message}\n")


class Recruiter(Employee):

    def work(self):
        return 'I come to the office and start hiring.'

    def position(self):
        return self.__str__()


class Developer(Employee):
    def __init__(self, name, day_salary, tech_stack: list, email):
        super().__init__(name, day_salary, email)
        self.tech_stack = tech_stack

    def work(self):
        return 'I come to the office and start coding.'

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
            return Developer(combined_name, combined_salary, combined_tech_stack, self.email)


try:
    emp1 = Employee("John", 100, "john@example.com")
    emp2 = Employee("Alice", 120, "alice@example.com")
    emp3 = Employee("Bob", 110, "john@example.com")
except EmailAlreadyExistsException:
    pass  

try:
    dev1 = Developer("Eve", 150, ["Python", "JavaScript"], "eve@example.com")
    dev2 = Developer("Carol", 140, ["Java"], "carol@example.com")
    dev3 = Developer("Mike", 160, ["Python"], "eve@example.com")  
except EmailAlreadyExistsException:
    pass  