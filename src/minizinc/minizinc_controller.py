import minizinc
from string import ascii_lowercase

class MinizincController():
    def __init__(self):
        self.model = minizinc.Model()
        
    def execute_minizinc(self, nodes):
        for index in range(len(nodes.node_list)):
            letter = ascii_lowercase[index]
            letter_string = """
            var 0..20: {};
            """.format(letter)
            self.model.add_string(letter_string)

        
        for index, node in enumerate(nodes.node_list): 
            amount_of_constraints = len(node.neighbors)
            own_letter = ascii_lowercase[index]
            constraint_string = "constraint {} -{}*{}".format(node.number, amount_of_constraints, own_letter)

            for constraint in node.neighbors:
                letter = ascii_lowercase[constraint.index]
                constraint_string += "+{}".format(letter)
            
            constraint_string += " >= 0;"
            print(constraint_string)
            self.model.add_string(constraint_string)

        final_config_string = """
        solve satisfy;
        """
        
        self.model.add_string(final_config_string)

        gecode = minizinc.Solver.lookup("gecode")
        inst = minizinc.Instance(gecode, self.model)

        result = inst.solve(all_solutions=False)
        
        for node in nodes.node_list:
            letter = ascii_lowercase[node.index]
            try:    
                clicks = result[letter]
                print(node.number, clicks)
                node.amount_of_clicks = clicks
            except:
                error = "An error occured while solving the equation with minizinc at the letter {} for node {}".format(letter, node.number)
                print(error)
                node.amount_of_clicks = 0

            