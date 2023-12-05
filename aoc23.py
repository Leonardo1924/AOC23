#                 .     .  .      +     .      .          .
#            .       .      .     #       .           .
#               .      .         ###            .      .      .
#             .      .   "#:. .:##"##:. .:#"  .      .
#                 .      . "####"###"####"  .
#              .     "#:.    .:#"###"#:.    .:#"  .        .       .
#         .             "#########"#########"        .        .
#               .    "#:.  "####"###"####"  .:#"   .       .
#            .     .  "#######""##"##""#######"                  .
#                       ."##"#####"#####"##"           .      .
#           .   "#:. ...  .:##"###"###"##:.  ... .:#"     .
#             .     "#######"##"#####"##"#######"      .     .
#           .    .     "#####""#######""#####"    .      .
#                   .     "      000      "    .     .
#              .         .   .   000     .        .       .
#       .. .. ..................O000O........................ ...... ...
#     :::     :::::::::  :::     ::: :::::::::: ::::    ::: :::::::::::
#   :+: :+:   :+:    :+: :+:     :+: :+:        :+:+:   :+:     :+: 
#  +:+   +:+  +:+    +:+ +:+     +:+ +:+        :+:+:+  +:+     +:+ 
# +#++:++#++: +#+    +:+ +#+     +:+ +#++:++#   +#+ +:+ +#+     +#+ 
# +#+     +#+ +#+    +#+  +#+   +#+  +#+        +#+  +#+#+#     +#+ 
# #+#     #+# #+#    #+#   #+#+#+#   #+#        #+#   #+#+#     #+# 
# ###     ### #########      ###     ########## ###    ####     ### 


import re
import sys
import collections
import time

#  ____                _     _____         _                _          _  ___ _ 
# |  _ \  __ _ _   _  / |_  |_   _| __ ___| |__  _   _  ___| |__   ___| ||__ \ |
# | | | |/ _` | | | | | (_)   | || '__/ _ \ '_ \| | | |/ __| '_ \ / _ \ __|/ / |
# | |_| | (_| | |_| | | |_    | || | |  __/ |_) | |_| | (__| | | |  __/ |_|_||_|
# |____/ \__,_|\__, | |_(_)   |_||_|  \___|_.__/ \__,_|\___|_| |_|\___|\__(_)(_)
#              |___/                                                            
#


class day1:
    def __init__(self):
        self.input = open("input_files/day1.in", "r").read().splitlines()
        self.part1()
        self.part2()

    def part1(self):
        print("Part 1: ")
        combined_numbers_sum = 0
    
        for line in self.input:
            first_digit = None
            last_digit = None
            for char in line:
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    last_digit = char
            
            if first_digit is not None and last_digit is not None:
                combined_number = int(first_digit + last_digit)
                #sum all the combined_numbers
                combined_numbers_sum += combined_number
        
        print(combined_numbers_sum)


    def convert_to_int(v: str) -> str:
        digitnames = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return v if v.isdigit() else str(digitnames.index(v)+1)
        

    def part2(self):
        print("Part 2: ")
        combined_numbers_sum = 0

        for line in self.input:
            nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
            combined_numbers_sum += int((day1.convert_to_int(nums[0])) + day1.convert_to_int(nums[-1]))
        
        print(combined_numbers_sum)


# ____                ____       ____      _              
#|  _ \  __ _ _   _  |___ \ _   / ___|   _| |__   ___     
#| | | |/ _` | | | |   __) (_) | |  | | | | '_ \ / _ \    
#| |_| | (_| | |_| |  / __/ _  | |__| |_| | |_) |  __/    
#|____/ \__,_|\__, | |_____(_)  \____\__,_|_.__/ \___|    
#             |___/                                       


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


#  ____                _  _      ____                 _       _                       _     
# |  _ \  __ _ _   _  | || | _  / ___|  ___ _ __ __ _| |_ ___| |__   ___ __ _ _ __ __| |___ 
# | | | |/ _` | | | | | || |(_) \___ \ / __| '__/ _` | __/ __| '_ \ / __/ _` | '__/ _` / __|
# | |_| | (_| | |_| | |__   _|   ___) | (__| | | (_| | || (__| | | | (_| (_| | | | (_| \__ \
# |____/ \__,_|\__, |    |_|(_) |____/ \___|_|  \__,_|\__\___|_| |_|\___\__,_|_|  \__,_|___/
#              |___/                                                                        
# 


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


#  ____                ____     ___  __  __   __             ____ _                _      ____                _      _      _____         _   _ _ _              
# |  _ \  __ _ _   _  | ___|_  |_ _|/ _| \ \ / /__  _   _   / ___(_)_   _____     / \    / ___|  ___  ___  __| |    / \    |  ___|__ _ __| |_(_) (_)_______ _ __ 
# | | | |/ _` | | | | |___ (_)  | || |_   \ V / _ \| | | | | |  _| \ \ / / _ \   / _ \   \___ \ / _ \/ _ \/ _` |   / _ \   | |_ / _ \ '__| __| | | |_  / _ \ '__|
# | |_| | (_| | |_| |  ___) |   | ||  _|   | | (_) | |_| | | |_| | |\ V /  __/  / ___ \   ___) |  __/  __/ (_| |  / ___ \  |  _|  __/ |  | |_| | | |/ /  __/ |   
# |____/ \__,_|\__, | |____(_) |___|_|     |_|\___/ \__,_|  \____|_| \_/ \___| /_/   \_\ |____/ \___|\___|\__,_| /_/   \_\ |_|  \___|_|   \__|_|_|_/___\___|_|   
#              |___/                                                                                                                                             


class day5:


    def __init__(self):
        self.seed_to_soil = []
        self.soil_to_fertilizer = []
        self.fertilizer_to_water = []
        self.water_to_light = []
        self.light_to_temperature = []
        self.temperature_to_humidity = []
        self.humidity_to_location = []
        self.map_lists = [
            self.seed_to_soil, self.soil_to_fertilizer, self.fertilizer_to_water, self.water_to_light, self.light_to_temperature, self.temperature_to_humidity, 
            self.humidity_to_location
        ]
        self.seeds = []
        self.part1()
        self.part2()
    
    def load_mapping_from_file(self):
        with open('input_files/day5.in', 'r') as f:
            for line in f.readlines():
                if not line.strip():
                    continue
                if line.startswith('seeds:'):
                    self.seeds = [int(x) for x in line.split()[1:]]
                    continue
                elif line.startswith('seed-to-soil'):
                    map_list = self.seed_to_soil
                    continue
                elif line.startswith('soil-to-fertilizer'):
                    map_list = self.soil_to_fertilizer
                    continue
                elif line.startswith('fertilizer-to-water'):
                    map_list = self.fertilizer_to_water
                    continue
                elif line.startswith('water-to-light'):
                    map_list = self.water_to_light
                    continue
                elif line.startswith('light-to-temperature'):
                    map_list = self.light_to_temperature
                    continue
                elif line.startswith('temperature-to-humidity'):
                    map_list = self.temperature_to_humidity
                    continue
                elif line.startswith('humidity-to-location'):
                    map_list = self.humidity_to_location
                    continue
                temp = [int(x) for x in line.split()]
                map_list.append((temp[1], temp[2], temp[0]))

    def get_dest(self,src, map_list):
        for s, r, d in map_list:
            if s <= src < s + r:
                return src - s + d
        return src

    def get_location(self, seed):
        temp = seed
        for map_list in self.map_lists:
            temp = self.get_dest(temp, map_list)
        return temp

    def part1(self):
        print("Part 1:")
        self.load_mapping_from_file()
        print(min(self.get_location(seed) for seed in self.seeds))

    def part2(self):
        print("Part 2:")
        seed_ranges = []
        for i in range(0,len(self.seeds),2):
            seed_ranges.append((self.seeds[i], self.seeds[i] + self.seeds[i+1] - 1)) 

        def get_ranges(src_ranges, map_list):
            result = []
            for a,b in src_ranges:
                covered_ranges = []
                for s,r,d in map_list:
                    x,y = s, s+r-1
                    if b < x or a > y:
                        continue
                    inter1 = max(a,x)
                    inter2 = min(b,y)
                    covered_ranges.append((inter1, inter2))
                    result.append((inter1 - s + d , inter2 -s + d))
                
                if not covered_ranges:
                    result.append((a,b))
                    continue
                covered_ranges.sort()

                if covered_ranges[0][0] > a:
                    result.append((a, covered_ranges[0][0] - 1))
                
                if covered_ranges[-1][1] < b:
                    result.append((covered_ranges[-1][1] + 1, b))
                for i in range(len(covered_ranges)-1):
                    x1,y1 = covered_ranges[i]
                    x2,y2 = covered_ranges[i+1]
                    if x2 > y1 + 1:
                        result.append((y1+1, x2-1))
            return result
        
        def get_location_ranges(seed_ranges):
            temp = seed_ranges
            for map_list in self.map_lists:
                temp = get_ranges(temp, map_list)
            return temp

        location = get_location_ranges(seed_ranges)
        print(min(location)[0])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "day1":
            day1()
        elif sys.argv[1] == "day2":
            day2()
        elif sys.argv[1] == "day3":
            day3()
        elif sys.argv[1] == "day4":
            day4()
        elif sys.argv[1] == "day5":
            day5()            
        else:
            print("Invalid argument")