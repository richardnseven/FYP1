class Supervisor:
    def __init__(self, ID, name):
        self.id = ID
        self.name = name
        self.workload = 0
        self.aviprojectlist = []
    def addProjectToAvi(self, project):
        self.aviprojectlist.append(project)

    def getWorkLoad(self):
        return self.workload


    def findProject(self, label):
        for project in self.aviprojectlist:
            label = label.getLabel()
            if project.getLabel().labelIsEqual(label):
                self.aviprojectlist.remove(project)
                self.workload += 1
                return project


