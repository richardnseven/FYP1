import Students as S
import Projects as P

studentList = []
projectList = []

def creatStudent():
    "在这里创建学生，需要id"
    student = S.Student(123)

    studentList.append(student)

def creatProject():
    "在这里创建项目，需要项目名和label"
    project = P.Project("project", "primary", "second", "type")
    projectList.append(project)

def countLabel():
    "在这里对label计数"
    primaryLabel = {"A": dict(), "B": 0}#对一级标签的计数
    secondA = dict()

    for p in projectList:
        label = p.getLabel()
        primary = label["primary"]
        second = label["second"]
        type = label["type"]


        if primary == "A":
            primaryLabel["A"] += 1



creatStudent()
countLabel()
print(studentList[0].getID())
creatProject()
print(projectList[0])
