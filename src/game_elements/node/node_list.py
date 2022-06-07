class NodeList():
    def __init__(self):
        self.node_list = []

    def add_node(self, node):
        self.node_list.append(node)
    
    def remove_node(self, node): 
        self.node_list.remove(node)

    def white_out_all_circles(self, img):
        for node in self.node_list: 
            img = node.white_out(img)
        return img
    
    def detect_numbers(self):
        for node in self.node_list:
            node.detect_numbers()
    
    def save_nodes_to_img(self, img_url):
        for node in self.node_list:
            node.save_img(img_url)

             
