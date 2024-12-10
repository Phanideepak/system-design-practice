# Interface
class ActionListerCommand:
    def execute(self):
        pass

# Receiver
class Document:
    def open(self):
        print('Document opened')
    
    def save(self):
        print('Document Saved')



# ConcreteCommand : ActionOpen
class ActionOpen(ActionListerCommand):
    def __init__(self, doc):
        self._doc = doc

    def execute(self):
        self._doc.open()


# ConcreteCommand : ActionSave
class ActionSave(ActionListerCommand):
    def __init__(self, doc):
        self._doc : Document = doc 
    
    def execute(self):
        self._doc.save()


# Invoker Class
class MenuOptions:
    def __init__(self, open_command, save_command):
        self.__open_command = open_command
        self.__save_command = save_command
    
    def click_open(self):
        self.__open_command.execute()

    def click_save(self):
        self.__save_command.execute()


# client code 

document = Document()

actionOpen = ActionOpen(document)
actionSave = ActionSave(document)

menu = MenuOptions(actionOpen, actionSave)

menu.click_open()
menu.click_save()