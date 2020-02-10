import Labels as L
class Project:
    def __init__(self, projectName, primary, second=None, type=None):
        self.name = projectName
        self.label = L.Label()
        self.label.setLabel(primary, second, type)
    def getLabel(self):
        return self.label.getAllLabel()
