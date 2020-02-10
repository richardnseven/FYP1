class Label:
    def __init__(self):
        self.labels = dict.fromkeys(("primary", "second", "type"))

    def setLabel(self, primary, second, type):
        self.labels["primary"] = primary
        self.labels["second"] = second
        self.labels["type"] = type


    def getLabel(self, position):
        return self.labels[position]

    def deleteLabel(self, position):
        self.labels[position] = None