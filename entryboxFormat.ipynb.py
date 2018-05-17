import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

class Window(tk.Tk):                      
    #docstring
    """(docstring) Classe Fenetre"""
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = EntryBoxFormated()
        self.entry2 = EntryBoxFormated()
        
        self.entry.entryTkValue.set("0000.1111")
        
        self.entry.pack()
        self.entry2.pack()
        
class EntryBoxFormated (tk.Entry):          #PRENDRE UN INTERVALLE EN PARAM DE CE WIDGET ( min et max autorisés -> 2 attributs d'instance)
                                            # + une variable pour le nombre de chiffres après la virgule
                                            # ameliorer pour tenir compte des nombres négatifs ??
    #docstring
    """(docstring) Classe Fenetre"""
    

    def __init__ (self, min=None, max=None, precision=None, type=None):  #precision = nb digits after comma     
                                                                #type : "float" or "string", if string no need for validation
        if (min == None):
            self.min = 0
        if (max == None):
            self.max = 10
        if (precision == None):
            self.precision = 4
        if (type == None or type != 'string'):
            self.type = "float" 
        
        self.entryTkValue = self.initEntryValue()
        #self.entryTkValue = tk.StringVar(value="0000.0000")
        #self.entryTkTtkValue = tk.StringVar()
        
        print(self.entryTkValue)
        
        super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL)
        #super().register(self.entryFloatValidation)
        cmd = self.register(self.entryFloatValidation)
        self.configure(validatecommand=cmd)
        
        #self.entryTk = tk.Entry(self, textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = {})
        #super().__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = self.register(self.entryFloatValidation) ) #, validatecommand = self.entryFloatValidation
        
        #super(EntryBoxFormated,self).__init__(textvariable = self.entryTkValue, text = self.entryTkValue, validate=tk.ALL, validatecommand = self.entryFloatValidation) 
        
        
        #self.entryTkTtk = tk.Entry(self, textvariable = self.entryTkTtkValue, text = self.entryTkTtkValue)
        
        #print(self.entryTk.get())
        
        
        #POUR UPDATE, FAIRE UN DELETE PUIS UN INSERT ou FAIRE UN SET SUR LA VARIABLE
        
        #self.entryTk.delete(0, tk.END) #deletes the current value
        #self.entryTk.insert(0, "0000.1111")
        
        #self.entryTkValue.set("0000.1111")
        
        
        
        #self.entryTk.configure(textvariable = "0000.1111")
        #print(self.entryTk.get())
        #self.entryTk["textvariable"] = "0000.1111"    ##WORKS
        
        
        #print(self.entryTk["textvariable"])
        
        #self.pack()
        
        
        #print(self.entryTkTtk.get())
        #self.entryTkTtk.configure(textvariable = "0000.0000")
        #print(self.entryTkTtk.get())
        
        #self.entryTkTtk.pack()

    
    def initEntryValue(self):
        initVal = "0"
        if (self.precision > 0):
            initVal += "."
            for i in range(0,self.precision):
                initVal += "0"
        return tk.StringVar(value=initVal)
    
 
    def entryFloatValidation(self):
        
        """
        Cas : - pas de "." dans la chaine, si c'est que des entiers c'est bon
               - caractères non autorisés
               - plus d'un point
               - chaine correcte mais valeur en dehors de l'intervalle de valeur
               - s'il rentre "," instead of '.', change it
        
        """
        
        tempString = self.entryTkValue.get()
        n = len(tempString)
        print(n)
        nbPoints = 0
        res = True
        i=0
        
        """for i in range (0,n):
            if (string[i] < '0' and string[i] > '9'):
                res = False
          """  
            
        while (i<n):
            if (tempString[i] < '0' or tempString[i] > '9'):
                if (tempString[i] == ',' or tempString[i] == ';'):
                    tempString[i] == '.'

                if (tempString[i] == '.'):
                    nbPoints += 1
                    if (nbPoints > 1):
                        res = False
                else:
                    res = False
        
        if (res):
            if (float(tempString) < self.min or float(tempString) > self.max):
                res = False
            else:
                self.delete(0,tk.END)
                self.insert(0,tempString)
            
        
        #update ??
        return res
                
                
                

if (__name__ == '__main__'):
    
    #print(tk.StringVar().configure())
    window = Window()    
    window.mainloop()
    window.quit()
    
    
