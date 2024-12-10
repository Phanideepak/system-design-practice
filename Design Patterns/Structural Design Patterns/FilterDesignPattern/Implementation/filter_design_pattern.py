class Person:
    def __init__(self, name, gender, maritial_status):
        self.__name = name 
        self.__gender = gender
        self.__maritial_status = maritial_status
    
    def get_name(self):
        return self.__name
    
    def get_gender(self):
        return self.__gender
    
    def get_maritial_status(self):
        return self.__maritial_status
    
    def __str__(self):
        return f'{self.__name} - {self.__gender} - {self.__maritial_status}'

class Criteria:
    def meet_criteria(self, persons):
        pass 

class CriteriaMale(Criteria):
    def meet_criteria(self, persons):
        return [person for person in persons if person.get_gender().lower() == 'male']

class CriteriaFemale(Criteria):
    def meet_criteria(self, persons):
        return [person for person in persons if person.get_gender().lower() == 'female']


class CriteriaSingle(Criteria):    
    def meet_criteria(self, persons):
        return [person for person in persons if person.get_maritial_status().lower() == 'single']

class AndCriteria(Criteria):
    def __init__(self, criteria, other_criteria):
        self.__criteria = criteria
        self.__other_criteria = other_criteria
    
    def meet_criteria(self, persons):
        return list(set(self.__criteria.meet_criteria(persons)) & set(self.__other_criteria.meet_criteria(persons)))

class OrCriteria(Criteria):
    def __init__(self, criteria, other_criteria):
        self.__criteria = criteria
        self.__other_criteria = other_criteria
    
    def meet_criteria(self, persons):
        return list(set(self.__criteria.meet_criteria(persons)) | set(self.__other_criteria.meet_criteria(persons)))

def print_list(entity_name, persons):
    print(entity_name)
    for person in persons:
        print(person) 
    print()
    print()

persons = []

persons.append(Person("Abhinav","MALE", "SINGLE"))
persons.append(Person("Ammu","FEMALE", "SINGLE"))
persons.append(Person("Alekya","FEMALE", "SINGLE"))
persons.append(Person("Alekya Chowdary","FEMALE", "SINGLE"))
persons.append(Person("Ammulu","FEMALE", "MARRIED"))
persons.append(Person("Donic","MALE", "MARRIED"))
persons.append(Person("Abhi","MALE", "MARRIED"))
persons.append(Person("Binod","MALE", "SINGLE"))

is_male = CriteriaMale()
is_female = CriteriaFemale()
is_single = CriteriaSingle()
is_single_female = AndCriteria(is_single, is_female)
is_single_or_male = OrCriteria(is_single, is_male)

print_list('Males', is_male.meet_criteria(persons))
print_list('Females', is_female.meet_criteria(persons))
print_list('Female Singles',is_single_female.meet_criteria(persons))
print_list('Singles or Males', is_single_or_male.meet_criteria(persons))

