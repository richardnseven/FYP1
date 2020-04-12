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


    def setSupervisor(self, supervisor):
        self.supervisor = supervisor

    def getSupervisor(self):
        return self.supervisor