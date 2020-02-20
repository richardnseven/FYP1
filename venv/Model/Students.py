import PreferenceLists as P
import Labels as L

class Student:

    #TODO add pre ass label, final ass label, final ass project
    def __init__(self, id):
        self.pre = P.PreferenceList()
        self.setStudentID(id)
        
        
    def setPreference(self, position, primary = None, second = None, type = None):
        "set preference by class P's function and the input can be none"
        self.pre.setPreferenceList(position, primary, second, type)




    def setStudentID(self, id):
        try:
            int_id = int(id)
            self.studentID = id
        except(TypeError):
            print("typeError")

    def getPreference(self):
        return self.pre


    def getID(self):
        return self.studentID





   
   
    def testMethod(self):
        self.pre.setPreferenceList("one","primary", "second", "type")
        self.pre.showname()



