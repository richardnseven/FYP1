import Students as S
import Projects as P
import Labels as L
import csv
import os
import Supervisors
import LabelCounters as coun


projectDict = dict()

PORJECT_ROOT = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
path = os.path.join(PORJECT_ROOT, "docs\\")







def creatProject(id, primary, second, type, supervisorID, suprevisorDict):
    "在这里创建项目，需要项目名和label"





def countLabel(projectDict):
    "在这里对label计数"
    counter = coun.LabelCounter()
    for project in projectDict.values():
        counter.addLabel(project.getLabel())
        # print(counter.dicOfLabels)
    return counter

def initalStudent():#tested
    path_studnet = os.path.join(path,"test_student.csv")
    studentDict = dict()

    with open(path_studnet, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = S.Student(row["id"])
            studentDict[row["id"]] = student

    return studentDict


def initalProject(suprevisorDict):#tested
    path_project = os.path.join(path,"test_project.csv")
    projectDict = dict()
    with open(path_project, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            project = P.Project(row['id'])
            project.setLabel(row["primary"], row["second"], row["type"])
            project.setSupervisor(suprevisorDict[row["supervisorID"]])
            projectDict[row['id']] = project

    return projectDict



def initalSupervisor():#tested
    path_supervisor = os.path.join(path, "test_supervisor.csv")
    supervisorDict = dict()
    with open(path_supervisor, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            supervisor = Supervisors.Supervisor(row["ID"], row["name"])
            supervisorDict[row["ID"]] = supervisor

            #print("the id is %s the name is %s"%(row["ID"],row["name"]))
    return supervisorDict

def initalpreference(studentDict):#tested
    path_preference = os.path.join(path, "test_preference.csv")
    with open(path_preference,encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for value in row:
               if row[value] == "":
                   row[value] = None
            studentDict[row["id"]].setPreference(row["position"],row["primary"], row["second"], row["type"])



def preAllocation():
    for student in studentDict.values():
        thepre = student.getPreference().getPreference()
        for theLabel in thepre.values():
            if theLabel is None:
                print("the end of this student")
                break
            else:
                room = counter.countLabel(theLabel)

                if room > 0:
                    if theLabel.isComplete():
                        student.setPreallocation(theLabel)
                        print("the student" + str(student.getID()) + str(theLabel.getLabel()))
                    else:
                        preLabel = counter.findMatch(theLabel)

                        student.setPreallocation(preLabel)




if __name__ == "__main__":
    supervisor = initalSupervisor()
    student = initalStudent()
    project = initalProject(supervisor)
    counter = countLabel(project)
    testLabel = L.Label()
    testLabel.setLabel(primary="A", second = 'aa')

    initalpreference(student)#需要在countLabel后再载入
    #
    #
    #
    #
    # preAllocation()
    
    
   # testLabel = projectDict["0001"].getLabel()
    # print(testLabel.isComplete())
    #tested P; T; P,S; P,T; P,S,T