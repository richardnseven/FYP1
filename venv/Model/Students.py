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

    def getPreferenceWithPosition(self, position):
        '返回值为label'
        preDict = self.pre.getPreference()
        menu = {1:"one", 2:"two", 3:'three', 4:'four', 5:'five'}
        position = menu[position]
        return  preDict[position]
    def setPreallocation(self,label):
        self.preallocation = label

    def getPreAllocation(self):
        return self.preallocation

    def setLabel(self, label):
        self.Label = label

    def setProject(self, project):
        self.project = project

    def getID(self):
        return self.studentID

    def setPrePosition(self, position):
        self.prePosition = position
    def getPrePosition(self):
        return self.prePosition






   




