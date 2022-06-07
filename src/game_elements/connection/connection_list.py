class ConnectionList():
    def __init__(self):
        self.connection_list = []

    def add_connection(self, connection):
        self.connection_list.append(connection)
    
    def remove_connection(self, connection): 
        self.connection_list.remove(connection)
    
    def calculate_constraints(self):
        for connection in self.connection_list: 
            node1 = connection.node_list[0]
            node2 = connection.node_list[1]

            node1.neighbor(node2)
            node2.neighbor(node1)


    def find_unique_connections(self):
        unique_connections = []

        for connection in self.connection_list:
            node1 = connection.node_list[0]
            node2 = connection.node_list[1]
            
            if len(unique_connections) > 0:
                found = False
                for c_connection in unique_connections:
                    c_node1 = c_connection.node_list[0]
                    c_node2 = c_connection.node_list[1]

                    if (node1.index == c_node1.index and node2.index == c_node2.index) or (node1.index == c_node2.index and node2.index == c_node1.index):
                        found = True
                    
                    if node1.index == node2.index:
                        found = True
                
                if found == True: 
                    continue
                else: 
                    unique_connections.append(connection)
            else:
                unique_connections.append(connection)
        
        self.connection_list = unique_connections