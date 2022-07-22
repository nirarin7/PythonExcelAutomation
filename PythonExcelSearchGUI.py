from tkinter import *
from PythonExcelSearch import mergeData
from tkinter import filedialog as fd

def ExecuteMergeData():
  mergeData(mainFileEntry.get(),searchFileEntry.get())

def GetMainFile():
  name = fd.askopenfilename()
  mainFileEntry.insert(0,name)

blankWindow = Tk()

Label(blankWindow, text = "Main File").grid(row=0)
Label(blankWindow, text= "Search File").grid(row=1)

mainFileEntry = Entry(blankWindow)
searchFileEntry = Entry(blankWindow)

mainFileEntry.grid(row=0, column =1)
searchFileEntry.grid(row= 1, column =1)

Button(blankWindow,text = "OK", command = ExecuteMergeData, fg ="violet").grid(row=2, column = 1, sticky=W, pady=4)
Button(blankWindow, text = "Get Main File", command = GetMainFile, fg = "green").grid(row = 2, column = 2, sticky=W, pady=4)

blankWindow.mainloop() ## keeps window displayed, loop breaks when closed
