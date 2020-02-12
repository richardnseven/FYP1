import Students as S
import Projects as P
import LabelCounters as coun

studentDict = dict()
projectDict = dict()

def creatStudent(id):
    "在这里创建学生，需要id"
    student = S.Student(id)
    studentDict[id] = student



def creatProject(id):
    "在这里创建项目，需要项目名和label"
    project = P.Project(id)
    projectDict[id] = project

def countLabel():
    "在这里对label计数"
    counter = coun.LabelCounter()
    for project in projectDict.values():
        pass




creatStudent()
countLabel()
print(studentList[0].getID())
creatProject()
print(projectList[0])
