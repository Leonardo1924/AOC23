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

import sys
import time
from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4
from day5 import day5
from day6 import day6

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
            start = time.time()
            day5()          
            end = time.time()
            total = end - start
            total = round(total*1000)
            print("Time taken: " + str(total) + " ms")  
        elif sys.argv[1] == "day6":
            day6()
        else:
            print("Invalid argument")