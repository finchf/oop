import csv
import datetime
import requests

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

    def check_salary(self, workdays):
        workdays_per_week = 5  # Рабочих дней в неделю
        workdays_per_month = workdays_per_week * 4  # Рабочих дней в месяце
        return int(self._day_salary * (workdays / workdays_per_month))


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


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_candidates(cls, path_or_url):
        if path_or_url.startswith("http"):
            response = requests.get(path_or_url)
            content = response.content.decode("utf-8")
            reader = csv.reader(content.splitlines(), delimiter=",")
        else:
            with open(path_or_url, "r") as file:
                reader = csv.reader(file, delimiter=",")

        candidates = []

        next(reader)

        for row in reader:
            full_name, email, tech_stack, main_skill, main_skill_grade = row
            first_name, last_name = full_name.split()
            tech_stack = tech_stack.split("|")
            candidate = Candidate(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
            candidates.append(candidate)

        return candidates



url = "https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv"
candidates = Candidate.generate_candidates(url)

for candidate in candidates:
    print(f"Full Name: {candidate.full_name}")
    print(f"Email: {candidate.email}")
    print(f"Technologies: {', '.join(candidate.tech_stack)}")
    print(f"Main Skill: {candidate.main_skill}")
    print(f"Main Skill Grade: {candidate.main_skill_grade}")
    print()