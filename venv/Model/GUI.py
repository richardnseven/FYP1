from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Processer as p


class GUI:
    def __init__(self, master):
        self.student_path = "demo_student.csv"
        self.supervisor_path = "demo_supervisor.csv"
        self.project_path = "demo_project.csv"
        self.preference_path = "demo_preference.csv"

        self.frame = Frame(master)
        self.secondFrame = Frame(master)
        self.frame.pack(side="top")
        self.secondFrame.pack(side="bottom", padx=10, pady=10)

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

        self.b = Button(self.secondFrame, text="Run the allocation process", command=self.run)
        self.b.config(padx=10, pady=10)
        self.b.pack()

    def setProject(self, event):
        self.project_path = self.cmb_project.get()

    def setPreference(self, event):
        self.preference_path = self.cmb_preference.get()


    def run(self):
        message = "The student input is: %s\n The supervisor input is: %s\n" \
                  "The project input is: %s \n The preference is: %s\n" % (self.student_path, self.supervisor_path,
                                                                         self.project_path, self.preference_path)
        if messagebox.askyesno("Final check", message):

            p. mainProcess(self.student_path, self.supervisor_path, self.project_path, self.preference_path)


root = Tk()
root.title("Demo process")
root.geometry("500x300+600+400")
gui = GUI(root)
root.mainloop()

# def show(event):
#     print(cmb.get())
#
# def runmain():
#     print("run the process")
#     # p.mainProcess("demo_student.csv", "demo_supervisor.csv", "demo_project.csv", "demo_preference01.csv")
#
#
# root = Tk()
# root.title("Demo process")
#
#
# cmb_student = ttk.Combobox(root)
#
# cmb = ttk.Combobox(root)
# cmb.pack(side = "top")
# cmb['value'] = (1,2,3,4,5)
# cmb.current(2)
# cmb.bind("<<ComboboxSelected>>", show)
#
#
# b = Button(root, text="run", command=runmain)
# b.pack()
# root.mainloop()
