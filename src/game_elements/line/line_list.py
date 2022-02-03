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

                    c = 2

                    if d1 < c or d2 < c or d3 < c:
                        found = True
                if found: 
                    continue
                else: 
                    cleaned_up_lines.append(line)
            else: 
                cleaned_up_lines.append(line)
        
        self.line_list = cleaned_up_lines