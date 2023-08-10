#Практика:

class LoggingMixin:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Creating an instance of {cls.__name__}')
        return instance


class Human(LoggingMixin):

    def __init__(self, name, date_of_birth: int):
        self.name = name
        self.date_of_birth = date_of_birth

    def to_str(self):
        return f'This is a human. His name is {self.name},\
    his date of birth: {self.date_of_birth}'

    def get_age(self):
        if isinstance(self.date_of_birth, int):
            return 2023 - self.date_of_birth
        else:
            raise ValueError('date_of_birth must be a number')

    def __str__(self):
        return self.to_str()

    def __eq__(self, other):
        if isinstance(other, Human):
            return self.get_age() == other

    def __lt__(self, other):
        if isinstance(other, Human):
            return self.date_of_birth < other.date_of_birth



class Planet:

    def __init__(self, name):
        self.name = name
        self.humans = []

    def to_str(self):
        return f'This is a Planet {self.name}'

    def __str__(self):
        return self.to_str()

    def add_human(self, population):
        self.humans.extend(population)

    def get_count(self):
        return len(self.humans)


    def __eq__(self, other):
        if isinstance(other, Planet):
            return self.get_count == other


planet1 = Planet('Mars')
planet2 = Planet('Earth')
human1 = Human('John', 1991)
human2 = Human('Bob', 1994)
human3 = Human('Smith', 1999)
human2.get_age()
planet1.add_human([human1, human2])
planet2.add_human([human3])
planet1.get_count()
planet2.get_count()


#homework:
import csv
class Phone:
    def __init__(self, number, count):
        self.number = number
        self._count = count
        
    def __str__(self):
        return f'Додано новий номер {self.number} до вашої телефонноъ книги'

    def set_number(self, value):
        self.number = value

    def get_total_count(self):
        return self._count

    def take_call(self):
        self._count += 1

class CallLogger:
    def __init__(self, phones: list, filename='calls.csv'):
        self.phones = phones
        self.filename = filename

    def log_calls(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Phone Number', 'Total Calls'])
            total_counts = 0
            for phone in self.phones:
                total_counts += phone.get_total_count()
                writer.writerow([phone.number, phone.get_total_count()])
        print(f"Total calls: {total_counts}")
        print(f"Log saved to {self.filename}")
        return total_counts

phone1 = Phone('380955701216', 10)
phone2 = Phone('380677777777', 15)

logger = CallLogger([phone1, phone2])

logger.log_calls()



#Chess:


CHESS_COLORS = ['white', 'black']

class ChessPiece:
    def __init__(self, color='white', x=0, y=0):
        if color not in CHESS_COLORS:
            raise ValueError(f"Invalid color. Use one of {CHESS_COLORS}")
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f'На дошку додано нову фігуру за координатами {self.x, self.y}'

    def get_color(self):
        return self.color

    def change_color(self):
        if self.color == CHESS_COLORS[0]:
            self.color = CHESS_COLORS[1]
        elif self.color == CHESS_COLORS[1]:
            self.color = CHESS_COLORS[0]
        return self.color

    def new_position(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            self.x = new_x
            self.y = new_y

class Pawn(ChessPiece):
    def move_possible(self, x, y):
        if self.color == 'white':
            return x == self.x and y == self.y + 1
        else:
            return x == self.x and y == self.y - 1


class Horse(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Elephant(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        return dx == dy


class Rook(ChessPiece):
    def move_possible(self, x, y):
        return x == self.x or y == self.y


class Queen(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        return (dx == dy) or (x == self.x or y == self.y)


class King(ChessPiece):
    def move_possible(self, x, y):
        dx = abs(x - self.x)
        dy = abs(y - self.y)
        return dx <= 1 and dy <= 1


def get_reachable_pieces(pieces, new_position):
    reachable_pieces = []
    for piece in pieces:
        if piece.move_possible(*new_position):
            reachable_pieces.append(piece)
    return reachable_pieces
    
    
pawn = Pawn()
pawn.change_color()
pawn.get_color()
pawn.new_position(4, 5) 
pawn.x
pawn.y

horse = Horse()
king = King()
queen = Queen()
rook = Rook()
elephant = Elephant()

chesses = [pawn, horse, king, queen, rook, elephant]

print(get_reachable_pieces(chesses, (6,6)))   #queen, elephant


#Employee:

class Employee:

    def __init__(self, name, day_salary):
        self.name = name
        self._day_salary = day_salary

    def work(self):
        return 'I come to the office.'

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

    def work(self):
        return 'I come to the office and start to coding.'

    def position(self):
        return self.__str__()


recruiter = Recruiter('Misha', 100)
developer = Developer('Gosha', 150)
print(recruiter)
print(recruiter.position())
print(recruiter.position())
print(developer.work())
print(recruiter == developer)
print(recruiter < developer)
