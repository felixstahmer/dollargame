import math

class LineList():
    def __init__(self):
        self.line_list = []

    def add_line(self, line):
        self.line_list.append(line)
    
    def remove_line(self, line): 
        self.line_list.remove(line)
    
    def check_for_duplicates(self):
        cleaned_up_lines = []

        for line in self.line_list: 
            found = False
            if len(cleaned_up_lines) > 0:
                for c_line in cleaned_up_lines: 
                    if c_line == line: 
                        continue
                
                    d1 = int(math.sqrt(math.pow(line.x1 - c_line.x1,2) + math.pow(line.y1 - c_line.y1, 2)))
                    d2 = int(math.sqrt(math.pow(line.x2 - c_line.x2,2) + math.pow(line.y2 - c_line.y2, 2)))
                    d3 = int(math.sqrt(math.pow(line.x1 - c_line.x2,2) + math.pow(line.y1 - c_line.y2, 2)))
                    d4 = int(math.sqrt(math.pow(line.x2 - c_line.x1,2) + math.pow(line.y2 - c_line.y1, 2)))

                    c = 10

                    # calculate increase of the two lines
                    # if they have close start/endpoint and have similar increase 
                    # then remove the shorter line and leave the longer one
                    d = line.m - c_line.m
                    cd = 1

                    if (d1 < c or d2 < c or d3 < c or d4 < c) and (d < cd and d > -cd):
                        found = True
                        if line.length > c_line.length:
                            cleaned_up_lines.remove(c_line)
                            cleaned_up_lines.append(line)
                        
                if found: 
                    continue
                else: 
                    cleaned_up_lines.append(line)
            else: 
                cleaned_up_lines.append(line)
        
        self.line_list = cleaned_up_lines
