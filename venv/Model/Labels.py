class Label:
    def __init__(self):
        self.labels = dict.fromkeys(("primary", "second", "type"))

    def setLabel(self, primary, second, type):
        self.labels["primary"] = primary
        self.labels["second"] = second
        self.labels["type"] = type


    def getLabel(self, ):
        return self.labels


    def getAllLabel(self):
        return self.labels

    def deleteLabel(self, position):
        self.labels[position] = None

    def labelIsEqual(self, label):
        if self.labels["primary"] == label["primary"] & self.labels["second"] == label["second"] & self.labels["type"] == label["type"]:
            return True
        else:
            return False