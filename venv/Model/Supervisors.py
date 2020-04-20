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

    def getID(self):
        return self.id


    def findProject(self, label):
        for project in self.aviprojectlist:
            thelabel = label.getLabel()
            if project.getLabel().labelIsEqual(thelabel):
                self.aviprojectlist.remove(project)
                self.workload += 1
                return project


