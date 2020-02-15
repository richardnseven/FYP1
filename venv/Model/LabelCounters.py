class LabelCounter:
    def __init__(self):
        self.dicOfLabels = dict()

    def creatPrimary(self, primary: str):
        self.dicOfLabels[primary] = dict()

    def creatSecond(self, primary, second):
        self.dicOfLabels[primary][second] = {"p":0, "t":0}


    def addLabel(self, Label):
        primary = Label["primary"]
        second = Label["second"]
        thetype = Label["type"]#tyep is origanil variable thus use thetpye to avoid confuse
        if primary in self.dicOfLabels:
            if second in self.dicOfLabels[primary]:
                self.dicOfLabels[primary][second][thetype] += 1
            else:
                self.creatSecond(primary, second)
                self.dicOfLabels[primary][second][thetype] += 1
        else:
            self.creatPrimary(primary)
            self.creatSecond(primary, second)
            self.dicOfLabels[primary][second][thetype] += 1

    def counter(self, primary=None, second=None, type=None):
        "通过这个方法返回 某个特定标签的数量。 当second有值的时候 primary不能为空"

        #all of p,s,t has value
        if primary is not None & second is not None & type is not None:
            self.count = self.dicOfLabels[primary][second][type]
            return self.count


        #both p and s has value, t == None
        elif primary is not None & second is not None:
            self.count = 0
            for value in self.dicOfLabels[primary][second].values():
                self.count = self.count + value
            return self.count

        #both p and t has value, s == None
        elif primary is not None & type is not None:
            self.count = 0
            for label in self.dicOfLabels[primary]:
                self.count = self.count + label[type]
            return self.count

        #only p has value, s == None and t == None
        elif primary is not None:
            self.count = 0
            for label in self.dicOfLabels[primary]:
                for value in label.values():
                    self.count = self.count + value
            return  self.count

        #only t has value, p == None and s == None
        elif type is not None:
            self.count = 0
            for label in self.dicOfLabels:
                for secLabel in lebel:
                    self.count = self.count + secLabel[type]
            return self.count
        else:
            print("counter function has an input error")