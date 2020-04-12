class Label:
    def __init__(self):
        self.labels = {"primary": None, "second": None, "type": None}

    def setLabel(self, primary = None, second = None, type = None):
        self.labels["primary"] = primary
        self.labels["second"] = second
        self.labels["type"] = type


    def getLabel(self ):
        return self.labels




   

    def isComplete(self):
        if (self.labels["primary"] is not None) & (self.labels["second"] is not None) & (self.labels["type"] is not None):
            return True
        else:
            return False


    def deleteLabel(self, position):
        self.labels[position] = None

    def labelIsEqual(self, label):
        if self.labels["primary"] == label["primary"] & self.labels["second"] == label["second"] & self.labels["type"] == label["type"]:
            return True
        else:
            return False