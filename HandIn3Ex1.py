import random

class Student():
    def __init__(self, name, gender, data_sheet, imagurl):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.imagurl = imagurl
    
    def __str__(self):
        return "Name: " + self.name + ", Gender:" +self.gender + ", datasheet:" + self.data_sheet + ", url:" + self.imagurl
    
    def get_avg_grade(self, lst):
        sum = 0
        for t in lst:
            sum = sum + t
        
        avg = sum / len(lst)
        return avg




class DataSheet():
    def __init__(self, courses = []):
        self.courses = courses

    def get_grades_as_list(self, *classCourz):
        grade = classCourz
        listx = list(grade)
        newlistz = [float(i.optgrade) for i in listx]
        return newlistz
        #A list is returned but cant put in arbitrary number of the class. 
        # It makes them a tuple and the tuple donr understand .optgrade



class Course():
    def __init__(self, name, classroom, teacher, etcs, optgrade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.optgrade = optgrade


coursez = ['Python', 'JavaScipt','Unity']
classdat = DataSheet(coursez)
classCourzz = Course('navn','105','thomas',10,'7')
classCourzz1 = Course('navn','105','thomas',10,'10')
classStud = Student('fred','mand',classdat, 'url.dk')

print(classdat.get_grades_as_list(classCourzz1,classCourzz))

gradez = classdat.get_grades_as_list(classCourzz1,classCourzz)

print(classStud.get_avg_grade(gradez))


def to_str(f1):
    return str(f1)

def new_stud(): #laver en ny Student med 'random' values
    gradezstr = map(to_str, gradez)
    names=['fred','niels']
    genders=['male','female']
    img_url=['url.dk','url1.dk']
    new_Stud1 = Student(random.choice(names),random.choice(genders),random.choice(gradezstr),random.choice(img_url))
    return new_Stud1


def repeat_func(n, f): #koerer funktionen n gange
    for i in range(n): print(f()) #remove print from here

new_stud()

repeat_func(3,new_stud)

