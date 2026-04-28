class Classroom:
    def __init__(self):
        self.sutdent=[]

    def add_student(self,name):
        self.sutdent.append(name)

    def count_students(self):
        return len(self.sutdent)    

c = Classroom()
c.add_student("maher")
c.add_student("Hee heee")
print(c.count_students())