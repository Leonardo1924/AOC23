# ____                ____       ____      _              
#|  _ \  __ _ _   _  |___ \ _   / ___|   _| |__   ___     
#| | | |/ _` | | | |   __) (_) | |  | | | | '_ \ / _ \    
#| |_| | (_| | |_| |  / __/ _  | |__| |_| | |_) |  __/    
#|____/ \__,_|\__, | |_____(_)  \____\__,_|_.__/ \___|    
#             |___/                                       

import re

class day2:
    def __init__(self):
        self.input = open("input_files/day2.in", "r").read().strip()
        print("Part 1: ")
        self.part1()
        self.part2()

    def part1(self, ispart2 = False):
        total = 0
        total2 = 0
        for game, line in enumerate(self.input.split("\n"), 1):
            valid = True
            min_red = min_green = min_blue = 0
            for s in line.split(": ")[-1].split("; "):
                red = sum(int(x) for x in re.findall(r"(\d+)\sred", s))
                green = sum(int(x) for x in re.findall(r"(\d+)\sgreen", s))
                blue = sum(int(x) for x in re.findall(r"(\d+)\sblue", s))
                
                min_red = max(min_red, red)
                min_green = max(min_green, green)
                min_blue = max(min_blue, blue)

                if red > 12 or green > 13 or blue > 14:
                    valid = False
        
            if valid:
                total += game

            total2 += min_red * min_green * min_blue

        if ispart2:
            return total2

        else:
            print(total)

    def part2(self):
        print("Part 2:")
        total = 0
        total = day2.part1(self, True)
        print(total)
