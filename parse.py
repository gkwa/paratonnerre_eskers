from itertools import takewhile
from sys import exit



log = "who.log"


with open(log) as f:
    array = []
    for line in f:
        if line.startswith(" "):
            print("start")
            # beginning of section use first lin
            for line in f:
                # check for end of section breaking if we find the stop lone
                if line.startswith(" "):
                    print("stop")
                    break
                # else process lines from section
        print(line)

exit(1)

with open(log) as f:
    array = []
    count = 0
    for line in f:
        if line.startswith(" "):
            header = line
            count += 1
            data = takewhile(lambda x: not x.startswith(" "), f)
            print(count, list(data))
