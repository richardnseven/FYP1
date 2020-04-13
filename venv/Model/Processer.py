import Students as S
import Projects as P
import Labels as L
import csv
import os
import Supervisors
import LabelCounters as coun
import numpy as np

projectDict = dict()

PORJECT_ROOT = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
path = os.path.join(PORJECT_ROOT, "docs\\")


def countLabel(projectDict):
    "在这里对label计数"
    counter = coun.LabelCounter()
    for project in projectDict.values():
        counter.addLabel(project.getLabel())
        # print(counter.dicOfLabels)
    return counter


def initalStudent():  # tested
    path_studnet = os.path.join(path, "test_student.csv")
    studentDict = dict()

    with open(path_studnet, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = S.Student(row["id"])
            studentDict[row["id"]] = student

    return studentDict


def initalProject(suprevisorDict):  # tested
    path_project = os.path.join(path, "test_project.csv")
    projectDict = dict()
    with open(path_project, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            project = P.Project(row['id'])
            project.setLabel(row["primary"], row["second"], row["type"])
            project.setSupervisor(suprevisorDict[row["supervisorID"]])
            suprevisorDict[row["supervisorID"]].addProjectToAvi(project)
            projectDict[row['id']] = project

    return projectDict


def creatprojectDict(projectDict):
    dic = dict()
    for project in projectDict.values():
        label = project.getLabel().getLabel()
        primary = label['primary']
        second = label['second']
        thetype = label['type']
        supervisor = project.getSupervisor()
        if primary in dic:
            if second in dic[primary]:
                if thetype in dic[primary][second]:
                    if supervisor in dicdic[primary][second][thetype]:
                        dicdic[primary][second][thetype][supervisor] += 1
                    else:
                        dicdic[primary][second][thetype][supervisor] = 1
                else:
                    sup = {supervisor: 1}
                    dic[primary][second][thetype] = sup

            else:
                sup = {supervisor: 1}
                ty = {thetype: sup}
                dic[primary][second] = ty
        else:
            sup = {supervisor: 1}
            ty = {thetype: sup}
            se = {second: ty}
            dic[primary] = se

    return dic


def initalSupervisor():  # tested
    path_supervisor = os.path.join(path, "test_supervisor.csv")
    supervisorDict = dict()
    with open(path_supervisor, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            supervisor = Supervisors.Supervisor(row["ID"], row["name"])
            supervisorDict[row["ID"]] = supervisor

            # print("the id is %s the name is %s"%(row["ID"],row["name"]))
    return supervisorDict


def initalpreference(studentDict, counter):  # tested
    path_preference = os.path.join(path, "test_preference.csv")
    with open(path_preference, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for value in row:
                if row[value] == "":
                    row[value] = None
            studentDict[row["id"]].setPreference(row["position"], row["primary"], row["second"], row["type"])
            preAllocation(studentDict[row['id']], counter)


def preAllocation(student, counter):
    thepre = student.getPreference().getPreference()
    position = 0
    for theLabel in thepre.values():
        position += 1
        status = False
        if theLabel is None or status:
            break
        else:
            room = counter.countLabel(theLabel)
            print(room)

            if room > 0:
                if theLabel.isComplete():
                    student.setPreallocation(theLabel)
                    student.setPrePosition(position)
                    counter.minusLabel(theLabel)
                    print("the student" + str(student.getID()) + str(theLabel.getLabel()))
                else:
                    preLabel = counter.findMatch(theLabel)
                    print("the student" + str(student.getID()) + str(preLabel.getLabel()) + str(position))

                    student.setPreallocation(preLabel)
                    student.setPrePosition(position)
                    counter.minusLabel(preLabel)


def reAllocation(studentDict: dict, counter):
    for student in studentDict.values():
        position = student.getPrePosition()
        if (position >= 3):
            preLabel = studnet.getPreAllocation().getLabel()
            counter.addLabel(preLabel)  # add the pre back to avilible list
            resultBackupStudent = None
            resultBackupPosition = None
            resultBackupLabel = None
            resultPosition = None
            resultbackup = None
            for backup in studentDict.values():  # 寻找backupstudent
                # 对所有 preallocation 满足1,2preference的找新坑， 如果找计算结果值， 求得最大结果值
                # 执行更新时 更新所有preallocation position
                if backup == student:
                    continue
                prealo = backup.getPreAllocation()
                backupPostion = backup.getPrePosition()
                backupNewPositon = int()
                result = 0
                if position <= backupPostion:
                    continue
                for i in range(1, position):
                    if isMatch(student.getPreferenceWithPosition(i), prealo):
                        for n in range(1, position):
                            backupLabel = counter.findMatch(backup.getPreferenceWithPosition(n))
                            if backupLabel.getLabel()["type"] is None:  # backup是否找到新位置
                                continue
                            else:
                                backupNewPositon = n
                                res = position - i - (backupNewPositon - backupPostion)
                                # 前进量减退后量
                                if res > result:
                                    result = res
                                    resultBackupStudent = backup
                                    resultBackupPosition = n
                                    resultPosition = i
                                    resultBackupLabel = backupLabel
                                    resultbackup = prealo

            if resultBackupStudent is not None:  # 执行替换
                resultBackupStudent.setPrePosition(resultBackupPosition)

                resultBackupStudent.setPreallocation(resultBackupLabel)

                counter.minusLabel(resultBackupLabel)
                student.setPrePosition(resultPosition)
                student.setPreallocation(resultbackup)


            else:
                counter.minusLabel(preLabel)  # 替换不成功时，取消释放


def finalCheck(studentDict):
    result = True
    for student in studentDict.values():
        if student.getPreAllocation().isComplete():
            print(student.getPreAllocation().getLabel())
            continue
        else:
            result = False
    return result


def projectAllocation(studentDcit: dict, dic: dict):
    'TODO 将项目分配给学生，根据workload'
    for student in studentDcit.values():
        theSupervisor = None
        label = student.getPreAllocation()
        labelDict = label.getLabel()
        theDict = dic[labelDict['primary']][labelDict['second']][labelDict['type']]
        max = float('inf')
        for sup, value in theDict.items():
            if value > 0:
                if sup.getWorkLoad() < max:
                    max = sup.getWorkLoad()
                    theSupervisor = sup

        theProject = theSupervisor.findProject(label)
        student.setProject(theProject)


def finalScore(studentDict, supervisorDict):
    'TODO 计算最终得分'
    studentscorelist = []
    supervisorscorelist = []
    for student in studentDict.values():
        studentscorelist.append(student.getScore())
    for supervisor in supervisorDict.values():
        supervisorscorelist.append(supervisor.getWorkLoad())
    studentsocrearray = np.array(studentscorelist)
    supervisorscorearray = np.array(supervisorscorelist)

    themean = np.mean(studentsocrearray)
    studentVar = np.var(studentsocrearray)
    supervisorVar = np.var(supervisorscorearray)
    print(themean)
    print(studentVar)
    print(supervisorVar)






def isMatch(Label, complabel):
    label = Label.getLabel()
    complabel = complabel.getLabel()
    state_p = False
    state_s = False
    state_t = False
    if label["primary"] is None:
        state_p = True
    else:
        if label["primary"] == complabel['primary']:
            state_p = True

    if label["second"] is None:
        state_s = True
    else:
        if label["second"] is complabel['second']:
            state_s = True

    if label["type"] is None:
        state_t = True
    else:
        if label["type"] == complabel['type']:
            state_t = True
    state = state_t & state_p & state_s
    return state


if __name__ == "__main__":
    supervisor = initalSupervisor()
    student = initalStudent()
    project = initalProject(supervisor)
    counter = countLabel(project)
    testLabel = L.Label()

    testLabel.setLabel(primary="A", second='aa')
    dic = creatprojectDict(project)
    initalpreference(student, counter)  # 需要在countLabel后再载入
    reAllocation(student, counter)
    projectAllocation(student, dic)
    print(finalCheck(student))
    finalScore(student,supervisor)






# testLabel = projectDict["0001"].getLabel()
# print(testLabel.isComplete())
# tested P; T; P,S; P,T; P,S,T
