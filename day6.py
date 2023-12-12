#  ____                 __        __        __    _ _     _____            ___ _   
# |  _ \  __ _ _   _   / /_    _  \ \      / /_ _(_) |_  |  ___|__  _ __  |_ _| |_ 
# | | | |/ _` | | | | | '_ \  (_)  \ \ /\ / / _` | | __| | |_ / _ \| '__|  | || __|
# | |_| | (_| | |_| | | (_) |  _    \ V  V / (_| | | |_  |  _| (_) | |     | || |_ 
# |____/ \__,_|\__, |  \___/  (_)    \_/\_/ \__,_|_|\__| |_|  \___/|_|    |___|\__|
#              |___/                                                               

import re
import math

class day6:
    def __init__(self):
        self.puzzle_input = open("input_files/day6.in").read()
        self.part1()
        self.part2()

    def part1(self):
        print("Part 1")
        times, distances = self.puzzle_input.split('\n')
        times = list(map(int, re.findall('\d+', times)))
        distances = list(map(int, re.findall('\d+', distances)))
        total = 1
        for t, d in zip(times, distances):
            wins = 0
            speed = 0
            for acceleration in range(1, t):
                speed += 1
                travelled = (t-acceleration) * speed
                if travelled > d:
                    wins += (travelled > d)
                elif wins:
                    break

            total *= wins

        print(total)

    def part2(self):
        print("Part 2")
        time, distance = self.puzzle_input.split('\n')
        time = int(''.join(re.findall('\d+', time)))
        distance = int(''.join(re.findall('\d+', distance)))
        exact_acceleration = (time - math.sqrt((time**2 - 4*distance))) / 2
        min_acceleration = int(exact_acceleration + 1)
        print(time - 2*min_acceleration + 1)