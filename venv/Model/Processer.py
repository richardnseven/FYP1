import Students as S
import Projects as P
import csv
import os
import Supervisors
import LabelCounters as coun

studentDict = dict()
projectDict = dict()
suprevisorDict = dict()
PORJECT_ROOT = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
path = os.path.join(PORJECT_ROOT, "docs\\")

def creatStudent(id):
    "在这里创建学生，需要id"
    student = S.Student(id)
    studentDict[id] = student



def creatProject(id, primary, second, type, supervisorID):
    "在这里创建项目，需要项目名和label"
    project = P.Project(id)
    project.setLabel(primary, second, type)
    project.setSupervisor(suprevisorDict[supervisorID])
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


def initalStudent():#tested
    path_studnet = os.path.join(path,"test_student.csv")

    with open(path_studnet, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            creatStudent(row["id"])



def initalProject():
    path_project = os.path.join(path,"test_project.csv")
    with open(path_project, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            creatProject(row["id"],row["primary"],row["second"],row["type"], row["supervisorID"])



def initalSupervisor():#tested
    path_supervisor = os.path.join(path, "test_supervisor.csv")
    with open(path_supervisor, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            creatSupervisor(row["ID"], row["name"])
            print("the id is %s the name is %s"%(row["ID"],row["name"]))




