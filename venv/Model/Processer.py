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

creatStudent()
print(studentList[0].getID())
creatProject()
print(projectList[0])
