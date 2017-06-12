import csv
from tkinter import *
# # # # # # # # # # # # # # #
# Converts comma delimited  #
# csv files to a txt file.  #
# Author: Julien Legault    #
# Version: 1.0.0            #
# Free and open source      #
# # # # # # # # # # # # # # #
top = Tk()
def run_script():
    inputFileName = e1.get() + '.csv'
    outputFileName = e2.get() + '.txt'
    with open(inputFileName) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        outputFile = open(outputFileName, 'w')
        try:
            header = next(reader)
            for row in reader:
                i = 0
                while(i<len(header)-2):
                    outputFile.write('%s - %s\n' % (header[i], row[i]))
                    i+=1
                outputFile.write('\n\n')
        except csv.Error as e:
            messagebox.showerror("Error", 'file %s, line %d: %s' % (inputFileName, reader.line_num, e))
    e1.delete(0, END)
    e2.delete(0, END)

Label (top, text="Input File").grid(row=0)
Label (top, text="Output File").grid(row=1)
e1 = Entry (top)
e2 = Entry (top)
e1.grid(row=0, column = 1)
e2.grid(row=1, column = 1)
Button(top, text="Go", command=run_script).grid(row=3, column=1, sticky=W, pady=4)
top.mainloop()
