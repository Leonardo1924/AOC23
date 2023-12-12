#  ____                _____     ____                   ____       _   _           
# |  _ \  __ _ _   _  |___ /_   / ___| ___  __ _ _ __  |  _ \ __ _| |_(_) ___  ___ 
# | | | |/ _` | | | |   |_ (_) | |  _ / _ \/ _` | '__| | |_) / _` | __| |/ _ \/ __|
# | |_| | (_| | |_| |  ___) |  | |_| |  __/ (_| | |    |  _ < (_| | |_| | (_) \__ \
# |____/ \__,_|\__, | |____(_)  \____|\___|\__,_|_|    |_| \_\__,_|\__|_|\___/|___/
#              |___/                                                               


class day3:
    def __init__(self):
        with open("input_files/day3.in", 'r') as f:
            self.engine = ['.{}.'.format(row) for row in f.read().split('\n')]
        self.part1()
        self.part2()

    def get_adjacent(self, r, c):
        part_numbers = set()
        offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), 
                   (0, 1), (1, -1), (1, 0), (1, 1))            
        for x, y in offsets:
            if self.engine[r + x][c + y].isdigit():
                left_pos = right_pos = c + y
                while self.engine[r + x][left_pos - 1].isdigit():
                    left_pos -= 1
                while self.engine[r + x][right_pos + 1].isdigit():
                    right_pos += 1
                part_numbers.add(int(self.engine[r + x][left_pos: right_pos + 1]))
        return part_numbers

    def parts_list(self):
        all_parts = []
        for r, row in enumerate(self.engine):
            for c, symbol in enumerate(row):
                if not symbol.isdigit() and symbol != '.':
                    all_parts.append((symbol, self.get_adjacent(r, c)))
        return all_parts

    def part1(self):
        print("Part 1:")
        print(sum(sum(nums) for _, nums in self.parts_list()))

    def part2(self):
        print("Part 2:")
        total = 0
        for symbol, nums in self.parts_list():
            if symbol == '*' and len(nums) == 2:
                total += nums.pop() * nums.pop()
        print(total)