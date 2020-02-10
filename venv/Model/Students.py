import PreferenceList as P

class Student:
    testId = 1312
    pre = P.PreferenceList()

    def setStudentID(self, id):
        try:
            int_id = int(id)
            self.studentID = int_id
        except(TypeError):
            print("typeError")

        print("the Id is ", self.studentID)
    def testMethod(self):
        self.pre.setPreferenceList("abc")
        self.pre.showname()


student = Student()
student.testMethod()
