class ComputerPart:
    def accept(self, computer_part_visitor):
        pass

# Concrete classes.
class Keyboard(ComputerPart):
    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)

class Monitor(ComputerPart):
    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)

class Mouse(ComputerPart):
    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)

class Computer(ComputerPart):
    def __init__(self):
        self.parts = [Mouse(), Monitor(), Keyboard()]
    
    def accept(self, computer_part_visitor):
        for part in self.parts:
            part.accept(computer_part_visitor)
        computer_part_visitor.visit(self)



class ComputerPartVisitor:
    def visit(self, computer):
        pass 

    def visit(self, mouse):
        pass 

    def visit(self, keyboard):
        pass 

    def visit(self, monitor):
        pass   


class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit(self, monitor):
        print('Displaying monitor ...')
    
    def visit(self, computer):
        print('Displaying computer ...')
    
    def visit(self, keyboard):
        print('Displaying Keyboard ...')
    
    def visit(self, mouse):
        print('Displaying Mouse ...')

# Client Code

computer = Computer()
computer.accept(ComputerPartDisplayVisitor())