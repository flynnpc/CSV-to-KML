#!/usr/bin/env python

import Tkinter as tk
import ttk
import tkFileDialog as tfd
import csv

class Application(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, borderwidth=10, bg="#FFFFFF")
        self.parent = parent
        self.grid()
        self.parent.title("CSV-2-KML Point Converter")
        self.parent.columnconfigure(0,weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.createWidgets()
    
    def createWidgets(self):
        self.grid(sticky=tk.NSEW)

#-------Begin Attributes--------        
        self.dropHead = tk.StringVar()
        self.complete = tk.StringVar()
#-------Begin Methods-----------        
        self.quitButton()
        self.convertButton()
        self.openButton()
        
#-------Begin Widgets-----------
        self.pointLabel = tk.Label(self, text="Point Name", background='#FFFFFF')
        self.pointLabel.grid(column=0, row=0)
        
        self.latLabel = tk.Label(self, text="Latitude", background='#FFFFFF')
        self.latLabel.grid(column=2, row=0)
        
        self.lonLabel = tk.Label(self, text="Longitude", background='#FFFFFF')
        self.lonLabel.grid(column=4, row=0)
                
        #Name listbox with scrollbar
        self.nameScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.nameScroll.grid(column=1, row=1, sticky=tk.W)
        self.nameList = tk.Listbox(self, exportselection=0, height=3, listvariable=self.dropHead, yscrollcommand=self.nameScroll.set)
        self.nameList.grid(column=0, row=1, padx=(10,0))
        self.nameScroll.config(command=self.nameList.yview)
        
        #Latitude Listbox with scrollbar
        self.latScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.latScroll.grid(column=3, row=1, sticky=tk.W)
        self.latList = tk.Listbox(self, exportselection=0, height=3, listvariable=self.dropHead, yscrollcommand=self.latScroll.set)
        self.latList.grid(column=2, row=1, padx=(10,0))
        self.latScroll.config(command=self.latList.yview)
        
        #Longitude Listbox with scrollbar
        self.lonScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lonScroll.grid(column=5, row=1, sticky=tk.W)           
        self.lonList = tk.Listbox(self, exportselection=0, height=3, listvariable=self.dropHead, yscrollcommand=self.lonScroll.set)
        self.lonList.grid(column=4, row=1, padx=(10,0))
        self.lonScroll.config(command=self.lonList.yview)
        
        #Conversion complete label
        self.convertLabel = tk.Label(self, textvariable=self.complete, background="#FFFFFF")
        self.convertLabel.grid(column=2, row=2, pady=(10,0))
        
#-------Begin Method Definitions    
    def quitButton(self):   
        self.quit = tk.Button(self, text='Quit', width=7, background="#363FD3", fg="#FFFFFF", relief=tk.FLAT, command=self.quit)
        self.quit.grid(column=0, row=2, pady=(10,0), padx=(10,0), sticky=tk.W)  
    
    def openCsv(self):
        self.inputCSV = open(tfd.askopenfilename(filetypes=[('csv Files','*.csv')]),'rb')
        self.csvFile = csv.reader(self.inputCSV)
        self.csvOne = next(self.csvFile,None)
        self.dropHead.set(tuple(self.csvOne))
    
    def openButton(self):                
        self.csvFile = tk.Button(self, text='Load', width=7, background="#363FD3", fg="#FFFFFF", relief=tk.FLAT, command=self.openCsv)
        self.csvFile.grid(column=3, row=2, columnspan=3, pady=(10,0), padx=(0,22))
    
    def convertButton(self):    
        self.convert = tk.Button(self, text='Convert', background="#363FD3", fg="#FFFFFF", relief=tk.FLAT, command=self.kmlWriter, width=7)
        self.convert.grid(column=4, row=2, columnspan=2, pady=(10,0), padx=(10,0), sticky=tk.E)
           
    def kmlWriter(self):
        
        self.namePosit = int(self.nameList.curselection()[0])
        self.latPosit = int(self.latList.curselection()[0])
        self.lonPosit = int(self.lonList.curselection()[0])
        
        self.kmlFile = tfd.asksaveasfile(mode='w', defaultextension='*.kml', filetypes=[('kml File', '*.kml')])
        self.kmlFile.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n\t<Document>\n\t')
        for row in self.csvFile:       
            self.kmlFile.write('<Placemark>\n\t')
            self.kmlFile.write('<name>' + row[self.namePosit] + '</name>\n')
            self.kmlFile.write('\t<description>\n\t\t')
            self.head = 0
            while self.head < len(self.csvOne):
                self.kmlFile.write(self.csvOne[self.head] + ': ' + row[self.head]+ '\n\t')
                self.head += 1
            self.kmlFile.write('</description>\n\t')
            self.kmlFile.write('<Point>\n\t\t<coordinates>'+row[self.lonPosit]+ ','+ row[self.latPosit]+ ',0</coordinates>\n\t</Point>')
            self.kmlFile.write('\n\t</Placemark>\n\t')
        self.kmlFile.write('</Document></kml>')
        self.kmlFile.close()
        #Updates the label to indicate conversion is complete. 
        self.complete.set("Conversion Complete!")
def main():
        root = tk.Tk()
        app = Application(root)
        root.mainloop()
        
if __name__ == '__main__':
    main()