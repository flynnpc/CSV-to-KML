#!/usr/bin/env python

import Tkinter as tk
import tkFileDialog as tfd
import csv

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, borderwidth=10, bg="#FFFFFF")
        self.dropHead = tk.StringVar()
        #self.img = tk.PhotoImage(file='csv.gif')
        
        self.nameScrollBar()
        self.lonScrollBar()
        self.latScrollBar()
        self.grid()
        self.quitButton()
        self.convertButton()
        self.openButton()
        self.promptName()
        self.promptLat()
        self.promptLon()
        self.nameSelect()
        self.latSelect()
        self.lonSelect()
        
    def promptName(self):
        self.pointNameCol = tk.Label(self, text="Point Name", bg="#FFFFFF", fg="#363FD3")
        self.pointNameCol.grid(column=0, row=0)
        
    def nameSelect(self):
        self.nameList = tk.Listbox(self, exportselection=0, height=3, listvariable=self.dropHead, yscrollcommand=self.nameScroll.set)
        self.nameList.grid(column=0, row=1)
        self.nameScroll.config(command=self.nameList.yview)
        
    def nameScrollBar(self):
        self.nameScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.nameScroll.grid(column=1, row=1)
    
    def promptLat(self):
        self.latCol = tk.Label(self, text="Latitude", bg="#FFFFFF")
        self.latCol.grid(column=2, row=0)
        
    def latSelect(self):
        self.latList = tk.Listbox(self, exportselection=0, height=3, listvariable=self.dropHead, yscrollcommand=self.latScroll.set)
        self.latList.grid(column=2, row=1, padx=(10,0))
        self.latScroll.config(command=self.latList.yview)

    def latScrollBar(self):
        self.latScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.latScroll.grid(column=3, row=1, sticky=tk.W)
        
    def promptLon(self):
        self.lonCol = tk.Label(self, text="Longitude", bg="#FFFFFF")
        self.lonCol.grid(column=4, row=0)

    def lonSelect(self):
        self.lonList = tk.Listbox(self, exportselection=0, height=3, listvariable=self.dropHead, yscrollcommand=self.lonScroll.set)
        self.lonList.grid(column=4, row=1, padx=(10,0))
        self.lonScroll.config(command=self.lonList.yview)
   
    def lonScrollBar(self):
        self.lonScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lonScroll.grid(column=5, row=1, sticky=tk.W)      
    
    def quitButton(self):
        self.quit = tk.Button(self, text='Quit', width=7, bg="#363FD3", fg="#FFFFFF", relief=tk.FLAT, command=self.quit)
        self.quit.grid(column=0, row=2, pady=(10,0), sticky=tk.W)  
                       
    def openButton(self):
        self.csvFile = tk.Button(self, text='Load', width=7, bg="#363FD3", fg="#FFFFFF", relief=tk.FLAT, command=self.openCsv)
        self.csvFile.grid(column=3, row=2, columnspan=3, pady=(10,0), padx=(0,22))
        
    def convertButton(self):
        self.convert = tk.Button(self, text='Convert', bg="#363FD3", fg="#FFFFFF", relief=tk.FLAT, command=self.kmlWriter, width=7)
        self.convert.grid(column=4, row=2, columnspan=2, pady=(10,0), padx=(10,0), sticky=tk.E)
                
    def openCsv(self):
        self.inputCSV = open(tfd.askopenfilename(filetypes=[('csv Files','*.csv')]),'rb')
        self.csvFile = csv.reader(self.inputCSV)
        self.csvOne = next(self.csvFile,None)
        self.dropHead.set(tuple(self.csvOne))
        
    def kmlWriter(self):
        
        self.namePosit = int(self.nameList.curselection()[0])
        self.latPosit = int(self.latList.curselection()[0])
        self.lonPosit = int(self.lonList.curselection()[0])
        
        self.kmlFile = tfd.asksaveasfile(mode='w', defaultextension='*.kml', filetypes=[('kml File', '*.kml')])
        self.kmlFile.write('<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n\t<Document>\n\t')
        for row in self.csvFile:       
            self.kmlFile.write('<Placemark>\n\t')
            self.kmlFile.write('<name>' + row[self.namePosit] + '</name>\n')
            self.kmlFile.write('\t<description>\n\t\ttest')
            self.head = 0
            while self.head < len(self.csvOne):
                self.kmlFile.write(self.csvOne[self.head] + ': ' + row[self.head]+ '\n\t')
                self.head += 1
            self.kmlFile.write('</description>\n\t')
            self.kmlFile.write('<Point>\n\t\t<coordinates>'+row[self.lonPosit]+ ','+ row[self.latPosit]+ ',0</coordinates>\n\t</Point>')
            self.kmlFile.write('\n\t</Placemark>\n\t')
        self.kmlFile.write('</Document></kml>')
        self.kmlFile.close()
        

app = Application()
app.master.title('CSV 2 KML Point Converter')
app.mainloop()