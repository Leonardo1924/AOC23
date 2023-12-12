#  ____                _  _      ____                 _       _                       _     
# |  _ \  __ _ _   _  | || | _  / ___|  ___ _ __ __ _| |_ ___| |__   ___ __ _ _ __ __| |___ 
# | | | |/ _` | | | | | || |(_) \___ \ / __| '__/ _` | __/ __| '_ \ / __/ _` | '__/ _` / __|
# | |_| | (_| | |_| | |__   _|   ___) | (__| | | (_| | || (__| | | | (_| (_| | | | (_| \__ \
# |____/ \__,_|\__, |    |_|(_) |____/ \___|_|  \__,_|\__\___|_| |_|\___\__,_|_|  \__,_|___/
#              |___/                                                                        
# 
import collections

class day4:
    def __init__(self):
        self.input = open("input_files/day4.in", "r").read().splitlines()
        self.part1()
        self.part2()
    
    def part1(self):
        print("Part 1:")
        total = 0
        for line in self.input:
            win_nums , my_nums = line.split(":")[1].split("|")
            win_nums = [int(num) for num in win_nums.split()]
            my_nums = [int(num) for num in my_nums.split()]
            value = 0
            for num in win_nums:
                if num in my_nums:
                    value = 2*value if value != 0 else 1
            total += value
        print(total)
    
    def part2(self):
        print("Part 2:")
        card_to_count = collections.defaultdict(lambda: 1)
        for idx, line in enumerate(self.input):
            card_idx = idx + 1
            card_to_count[card_idx]
            win_nums , my_nums = line.split(":")[1].split("|")
            win_nums = [int(num) for num in win_nums.split()]
            my_nums = [int(num) for num in my_nums.split()]
            value = 0
            for num in win_nums:
                if num in my_nums:
                    value += 1
            for i in range(value):
                card_to_count[card_idx+i+1] += card_to_count[card_idx]
        print(sum(card_to_count.values()))
