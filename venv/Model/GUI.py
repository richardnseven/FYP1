from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Processer as p







class GUI:
    def __init__(self, master):
        self.master = master
        self.student_path = "demo_student.csv"
        self.supervisor_path = "demo_supervisor.csv"
        self.project_path = "demo_project.csv"
        self.preference_path = "demo_preference.csv"

        self.frame = Frame(master)
        self.secondFrame = Frame(master)
        self.frame.pack(side="top")
        self.secondFrame.pack(padx=20, pady=20)
        self.thirdFrame = Frame(master)
        self.thirdFrame.pack(side="bottom", padx=20, pady=20)

        Label(self.frame, text="Project Input file: ").grid(row=0, padx=5, pady=5)
        Label(self.frame, text="Preference Input file: ").grid(row=1, padx=5, pady=5)
        self.cmb_project = ttk.Combobox(self.frame)
        self.cmb_project.grid(row=0, column=1, padx=5, pady=5)
        self.cmb_project['value'] = "demo_project.csv"
        self.cmb_project.current(0)
        self.cmb_project.bind("<<ComboboxSelected>>", self.setProject)

        self.cmb_preference = ttk.Combobox(self.frame)
        self.cmb_preference.grid(row=1, column=1, padx=5, pady=5)
        self.cmb_preference['value'] = ("demo_preference.csv", "demo_preference01.csv")
        self.cmb_preference.current(0)
        self.cmb_preference.bind("<<ComboboxSelected>>", self.setPreference)

        self.b = Button(self.frame, text="Run the load process", command=self.load)
        self.b.config(padx=10, pady=10)
        self.b.grid(row=2)

        self.label_studentid = Label(self.secondFrame, text="Student Id")
        self.label_studentid.grid(row=0,column=0)
        self.studentid = Entry(self.secondFrame, relief="raised")
        self.studentid.grid(row=0,column=1)
        self.button_Edit = Button(self.secondFrame, text="Edit this student's preference", command=self.editPreferenct)
        self.button_Edit.grid(row=1)
        Button(self.thirdFrame, text="Run Main Process",height=2, command=self.runMainProcess).pack()

    def runMainProcess(self):
        p.mainProcess()
    def setProject(self, event):
        self.project_path = self.cmb_project.get()


    def setPreference(self, event):
        self.preference_path = self.cmb_preference.get()
        self.cmb_project['value'] = ("demo_project.csv", "123")

    def editPreferenct(self,):
        self.id = str(self.studentid.get())
        self.student = p.getStudent(self.id)
        self.counter = p.getCounter()
        self.counterdic = self.counter.dicOfLabels
        self.preference = self.student.getPreference()
        self.preferencelist = self.preference.getPreference()
        self.selector = Toplevel()
        self.selector.title("selector")
        self.frame_one = Frame(self.selector)
        self.frame_one.pack()
        Label(self.frame_one, text="Position:").grid(row=0, column=0)
        self.cmb_position = ttk.Combobox(self.frame_one)
        self.cmb_position.bind("<<ComboboxSelected>>",self.positionSelected)
        self.cmb_position['value'] = ['one', 'two', 'three', 'four', 'five']
        self.cmb_position.current(0)
        self.cmb_position.grid(row=0, column=2)
        self.stringLabel = StringVar()
        Label(self.frame_one, textvariable=self.stringLabel).grid(row=1)
        Label(self.frame_one, text='Primary').grid(row=2, column=0)
        Label(self.frame_one, text='Second').grid(row=2, column=1)
        Label(self.frame_one, text='Type').grid(row=2, column=2)
        self.cmb_primary_one = ttk.Combobox(self.frame_one)
        self.primaryList = list(self.counterdic.keys())
        self.primaryList.append("None")
        self.cmb_primary_one['value'] = self.primaryList
        self.cmb_primary_one.bind("<<ComboboxSelected>>", self.primarySelected)
        self.cmb_primary_one.grid(row=3, column=0)
        self.secondList = list()

        self.cmb_second_one = ttk.Combobox(self.frame_one)
        self.cmb_second_one['value'] = self.secondList
        self.cmb_second_one.grid(row=3, column=1)
        self.cmb_type_one = ttk.Combobox(self.frame_one)
        self.cmb_type_one['value'] = ['p', 't', "None"]
        self.cmb_type_one.grid(row=3, column=2)
        Button(self.frame_one, text="set preference", command=self.setPretoStudent).grid(row=4)


    def replaceNone(self, string):
        if string == "None":
            string = None
        return string
    def setPretoStudent(self):
        position = self.cmb_position.get()
        primary = self.replaceNone(self.cmb_primary_one.get())
        second = self.replaceNone(self.cmb_second_one.get())
        thetype = self.replaceNone(self.cmb_type_one.get())
        p.setPreferenct(self.student, position, primary, second, thetype)


    def primarySelected(self,event):
        self.secondList = list(self.counterdic[self.cmb_primary_one.get()])
        self.secondList.append('None')
        self.cmb_second_one['value'] = self.secondList
    def positionSelected(self,event):
        position = self.cmb_position.get()
        label = self.preferencelist[position]
        if label != None:
            labeldic = label.getLabel()
            self.stringLabel.set("Primary: %s Second: %s Type: %s" %(labeldic['primary'], labeldic['second'], labeldic['type']))
        else:
            self.stringLabel.set("No preference in this position")





    def load(self):
        message = "The student input is: %s\n The supervisor input is: %s\n" \
                  "The project input is: %s \n The preference is: %s\n" % (self.student_path, self.supervisor_path,
                                                                         self.project_path, self.preference_path)
        if messagebox.askyesno("Final check", message):

            p. loadProcess(self.student_path, self.supervisor_path, self.project_path, self.preference_path)


root = Tk()
root.title("Demo process")
root.geometry("500x300+600+400")
gui = GUI(root)
root.mainloop()


