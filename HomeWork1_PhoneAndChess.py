class Phone:
    number = ''
    _count = 0

    def set_number(self, value):
        self.number = value

    def get_total_count(self):
        return self._count

    def take_call(self):
        self._count += 1

def amount_of_calls(phones: list) -> int:
    total_counts = 0
    for phone in phones:
        total_counts += phone.get_total_count()
    filename = 'calls.csv'
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Total Calls'])
        writer.writerow([total_counts])
    print(f"Total calls: {total_counts}")
    print(f"total_counts saved to {filename}")
    return total_counts
    
    
a = Phone()
a.set_number('+38077777777')
b = Phone()
b.set_number('+38099999999')
c = Phone()
c.set_number('+14752714215')
a.take_call()
a.take_call()
b.take_call()
c.take_call()
c.take_call()
c.take_call()

amount_of_calls([a, b, c]) ->  calls.csv
Total calls: 6
total_counts saved to calls.csv
6



2.

class ChessPiece:
    color = 'white'
    x = 0
    y = 0

    def get_color(self):
        return self.color

    def set_color(self):
        sp_color = ['white', 'black']
        for i in sp_color:
            if self.color != i:
                self.color = i
                break
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
pawn.set_color()  / black
pawn.get_color()   / black
pawn.new_position(4, 5) 
pawn.x / 4
pawn.y / 5

horse = Horse()
king = King()
queen = Queen()
rook = Rook()
elephant = Elephant()

chesses = [pawn, horse, king, queen, rook, elephant]

get_reachable_pieces(chesses, (6,6))   /  queen, elephant