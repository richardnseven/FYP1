import Labels as L
import Supervisors


class Project:
    def __init__(self, projectID):
        self.ID = projectID
        self.label = L.Label()

    def setLabel(self, primary, second, type):
        self.label.setLabel(primary, second, type)

    def getLabel(self):
        return self.label

    def getID(self):
        return self.ID


    def setSupervisor(self, supervisor):
        self.supervisor = supervisor

    def getSupervisor(self):
        return self.supervisor