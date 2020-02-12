import PreferenceLists as P

class Student:

    #TODO add pre ass label, final ass label, final ass project
    def __init__(self, id):
        self.pre = P.PreferenceList()
        self.setStudentID(id)
        
        
    

    def setStudentID(self, id):
        try:
            int_id = int(id)
            self.studentID = int_id
        except(TypeError):
            print("typeError")

        print("the Id is ", self.studentID)


    def getID(self):
        return self.studentID





   
   
    def testMethod(self):
        self.pre.setPreferenceList("one","primary", "second", "type")
        self.pre.showname()



