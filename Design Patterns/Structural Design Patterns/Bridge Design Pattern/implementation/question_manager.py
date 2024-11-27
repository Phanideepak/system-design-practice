# Question Interface.
class Question:
    def next_question(self):
        pass 
    
    def previous_question(self):
        pass 

    def new_question(self, question):
        pass 

    def delete_question(self, question):
        pass

    def display_question(self):
        pass 

    def display_question_all(self):
        pass



# Concrete Interface Implementation
class  JavaQuestions(Question):
    def __init__(self):
        self.__current = 0
        self.__questions = ['What is class ?', 'What is interface ?']
    
    def next_question(self):
        if self.__current < len(self.__questions):
            self.__current += 1

    def previous_question(self):
        if self.__current > 0:
            self.__current -= 1

    def new_question(self, question):
        self.__questions.append(question)
    
    def delete_question(self, question):
        self.__questions.remove(question)
    
    def display_question(self):
        print(self.__questions[self.__current])
    
    def display_question_all(self):
        print(len(self.__questions))
        for question in self.__questions:
            print(question)


# Bridge Class
class QuestionManager:
    def __init__(self, catalog):
        self.catalog = catalog
        self._q = JavaQuestions() 

    def next(self):
        self._q.next_question()
    
    def previous(self):
        self._q.previous_question()

    def new_one(self, question):
        self._q.new_question(question)
    
    def delete(self, question):
        self._q.delete_question(question)
    
    def display(self):
        self._q.display_question()
    
    def display_all(self):
        self._q.display_question_all()

class QuestionFormat(QuestionManager):
    def __init__(self, catalog):
        super().__init__(catalog)
    
    def display_all(self):
        print('---------------')
        super().display_all()
        print('---------------')

questions  = QuestionFormat('Java Programming Languages')
questions.new_one('What is inheritance')
questions.new_one('How many types of inheritance are there in Java?')
questions.display_all()

        
    

