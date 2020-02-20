import Students as S
import Projects as P
import Supervisors
import LabelCounters as coun

studentDict = dict()
projectDict = dict()
suprevisorDict = dict()

def creatStudent(id):
    "在这里创建学生，需要id"
    student = S.Student(id)
    studentDict[id] = student



def creatProject(id, primary, second, type, suprevisorID):
    "在这里创建项目，需要项目名和label"
    project = P.Project(id)
    project.setLabel(primary, second, type)
    project.setSupervisor(suprevisorDict[suprevisorID])
    projectDict[id] = project

def creatSupervisor(ID, name):
    "需要在运行creatProject前运行，保证有supervisor"
    suprevisor = Supervisors.Supervisor(ID, name)
    suprevisorDict[ID] = suprevisor


def countLabel():
    "在这里对label计数"
    counter = coun.LabelCounter()
    for project in projectDict.values():
        counter.addLabel(project.getLabel())





creatProject(123,"primary" , "s", "t")
print(projectDict[123].getLabel())
print(projectDict[123])
