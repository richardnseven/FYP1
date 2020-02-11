class LabelCounter:
    def __init__(self):
        self.dicOfLabels = dict()

    def creatPrimary(self, primary: str):
        self.dicOfLabels[primary] = dict()

    def creatSecond(self, primary, second):
        self.dicOfLabels[primary][second] = {"p":0, "t":0}


    def addLabel(self, primary, second, type):
        if primary in self.dicOfLabels:
            if second in self.dicOfLabels[primary]:
                self.dicOfLabels[primary][second][type] += 1
            else:
                self.creatSecond(primary, second)
                self.dicOfLabels[primary][second][type] += 1
        else:
            self.creatPrimary(primary)
            self.creatSecond(primary, second)
            self.dicOfLabels[primary][second][type] += 1

