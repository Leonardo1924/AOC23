import re

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
