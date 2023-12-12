
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