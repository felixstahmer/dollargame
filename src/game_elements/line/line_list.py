class LineList():
    def __init__(self):
        self.line_list = []

    def add_line(self, node):
        self.line_list.append(node)
    
    def remove_line(self, node): 
        self.line_list.remove(node)
    