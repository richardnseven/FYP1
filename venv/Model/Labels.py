class Label:
    labels = dict.fromkeys(("primary", "second", "type"))

    def setLalel(self, label, position):
        self.labels[position] = label

    def getLabel(self, position):
        return self.labels[position]

    def deleteLabel(self, position):
        self.labels[position] = None