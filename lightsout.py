from tkinter import *
import tkinter.ttk as ttk
from numpy import zeros,save,load
from tkinter.messagebox import *
from random import randint
from os import path
from icon import Photo
from pyzip.base import base64
import webbrowser
import sys

def location():
    if getattr(sys, 'frozen', False):
        return path.dirname(sys.executable)
    else:
        return path.dirname(path.abspath(__file__))

VERSION = "2.0"
MAXN = 15
SUPPORTLANGUAGES = ("简体中文","English")

IMAGE = '''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'''

if not path.exists("yjtp1.png"):
    base64.b642file(IMAGE,"yjtp1.png")

if path.exists("MAXN.txt"):
    f = open("MAXN.txt","r",encoding="utf-8")
    MAXN = int(f.read())
    f.close()
    del f
else:
    f = open("MAXN.txt","w",encoding="utf-8")
    f.write(str(MAXN))
    f.close()
    del f

bests = zeros(MAXN)

if path.exists("best.npy"):
    bests = load("best.npy")

rbests = zeros(MAXN)

if path.exists("rbest.npy"):
    rbests = load("rbest.npy")

languages = {
    "简体中文":
    {"开始":"开始",
     "棋盘全部随机（地狱困难版）":
     "棋盘全部随机（地狱困难版）",
     "查看记录榜单":
     "查看记录榜单",
     "您曾创下{}条记录":
     "您曾创下{}条记录",
     "序号":
     "序号",
     "简单版记录":
     "简单版记录",
     "困难版记录":
     "困难版记录",
     "胜利！您的步数为{}步！":
     "胜利！您的步数为{}步！",
     "您创下了简单版新纪录！\n{}->{}":
     "您创下了简单版新纪录！\n{}->{}",
     "您创下了困难版新纪录！\n{}->{}":
     "您创下了困难版新纪录！\n{}->{}",
     "返回":
     "返回",
     "语言":
     "语言：",
     "设置":
     "设置与关于",
     "暂无":
     "暂无",
     "提示":
     "提示",
     "编程":
     "编程",
     "开源自":
     "开源自"},
    "English":
     {"开始":"Start",
     "棋盘全部随机（地狱困难版）":
     "Random Gameboard",
     "查看记录榜单":
     "Records",
     "您曾创下{}条记录":
     "You have set {} records",
     "序号":
     "No.",
     "简单版记录":
     "NormalMode records",
     "困难版记录":
     "HardMode records",
     "胜利！您的步数为{}步！":
     "Victory! You click {} times!",
     "您创下了简单版新纪录！\n{}->{}":
     "You have set a new EasyMode record!\n{}->{}",
     "您创下了困难版新纪录！\n{}->{}":
     "You have set a new HardMode record！\n{}->{}",
     "返回":
     "Back",
     "语言":
     "Language:",
     "设置":
     "Settings & About",
     "暂无":
     "None",
     "提示":
     "Info",
     "编程":
     "Write & Compile",
     "开源自":
     "Open Source From "}}

""

languages_source = str(languages)

before = ''''''

def openx(source,mode,encoding):
    ##print("\n\n\n----open operation----")
    ##print("source :",source)
    ##print("mode :",mode)
    ##print("encoding :",encoding)
    ##print("----open operation end----\n\n\n")
    return open(source,mode,encoding=encoding)

def check(prompt):
    global before
    if before == '''''':
        before = prompt
    else:
        ##print("\n\n\n----detect file result----")
        ##print("Before :",before)
        ##print("Now :",prompt)
        ##print("----detect file result end----")
        before = ''''''

if path.exists("languages.txt"):
    f = openx("languages.txt","r",encoding="utf-8")
    read = f.read()
    check(read)
    languages = eval(read)
    f.close()
    del f
else:
    f = openx("languages.txt","w+",encoding="utf-8")
    check(f.read())
    f.write(languages_source)
    f.close()
    del f
f = openx("languages.txt","r",encoding="utf-8")
read = f.read()
check(read)
f.close()
del f

currentlanguage = "简体中文"
if path.exists("current_languages.txt"):
    f = openx("current_languages.txt","r",encoding="utf-8")
    read = f.read()
    if read in SUPPORTLANGUAGES:
        currentlanguage = read
    f.close()
    del f
else:
    #print("false")
    f = openx("current_languages.txt","w",encoding="utf-8")
    f.write(currentlanguage)
    f.close()
    del f

#print("current language",currentlanguage)


def countOfOverOne(array):
    cnt = 0
    for i in array:
        if(i>0):
            cnt+=1
    return cnt

class Game:
    def __init__(self):
        self.Labelorbuttons = {}
        #{"my text",Object}
        self.chess = zeros((100,100))
        self.steps = 0
        

        self.root = Tk()
        self.root.geometry("500x500")
        self.root.resizable(0,0)

        self.enabledHellMode = IntVar()
        self.CONFIGFRAME = Frame(self.root)
        self.s = Scale(self.CONFIGFRAME,from_=1,to=MAXN-1,orient="horizontal")
        self.s.pack(anchor="center",ipadx=100,pady=10)
        self.Labelorbuttons["开始"] = ttk.Button(self.CONFIGFRAME,text="开始",command=self.start)
        self.Labelorbuttons["开始"].pack(anchor="center",pady=10,ipadx=60)
        self.Labelorbuttons["棋盘全部随机（地狱困难版）"] = Checkbutton(self.CONFIGFRAME,text="棋盘全部随机（地狱困难版）",variable=self.enabledHellMode,onvalue=1,offvalue=0)
        self.Labelorbuttons["棋盘全部随机（地狱困难版）"].pack(anchor="center",ipadx=60,pady=10)
        self.Labelorbuttons["查看记录榜单"] = ttk.Button(self.CONFIGFRAME,text="查看记录榜单",command=self.showbest)
        self.Labelorbuttons["查看记录榜单"].pack(anchor="center",ipadx=60,pady=10)
        self.Labelorbuttons["设置"] = ttk.Button(self.CONFIGFRAME,text="设置",command=self.settings)
        self.Labelorbuttons["设置"].pack(anchor="center",ipadx=60,pady=10)
        self.root.title("LightsOut")
        self.root.protocol("WM_DELETE_WINDOW",self.whenclose)

        self.CONFIGFRAME.pack(anchor="center",pady=120)
        self.flash_label_language()
        self.root.mainloop()

    def settings(self):
        def back():
            nonlocal self
            global currentlanguage
            currentlanguage = self.language_combobox.get()
            self.flash_label_language()
            self.SETTINGFRAME.pack_forget()
            self.CONFIGFRAME.pack(anchor="center",pady=120)
        #hide frames
        try:
            self.l.place_forget()
        except:
            pass
        try:
            self.back.place_forget()
        except:
            pass
        try:
            self.GAMEFRAME.place_forget()
        except:
            pass
        try:
            self.CONFIGFRAME.pack_forget()
        except:
            pass
        try:
            self.BESTFRAME.pack_forget()
        except:
            pass
        self.SETTINGFRAME = Frame(self.root)
        self.Labelorbuttons["语言"] = Label(self.SETTINGFRAME,text="语言")
        self.Labelorbuttons["语言"].grid(row=0,column=0,pady=20)
        self.language_combobox = ttk.Combobox(self.SETTINGFRAME,values=tuple(languages.keys()))
        self.language_combobox.grid(row=0,column=1,pady=60)
        Label(self.SETTINGFRAME,text="LightsOut in Python\nVersion "+VERSION+"\nPorchcup "+self.translate("编程"),font=("微软雅黑",20)).grid(row=1,column=0,columnspan=2,rowspan=2)
        link = Label(self.SETTINGFRAME,text=self.translate("开源自")+"https://git\nhub.com/Porchcar/LightsOut",font=("微软雅黑",20),fg="cornflowerblue",cursor="hand2")
        link.grid(row=3,column=0,columnspan=2)
        link.bind("<Button-1>",lambda event:webbrowser.open("https://github.com/Porchcar/LightsOut"))
        Label(self.SETTINGFRAME,image=Photo.new_photo(path.join(location(),"yjtp1.png"))).grid(row=1,column=2,rowspan=3)
        ttk.Button(self.SETTINGFRAME,text="返回",command=back).grid(row=4,column=0,columnspan=2,pady=20,ipadx=60)
        self.language_combobox.insert(END,currentlanguage)
        self.SETTINGFRAME.pack()
        

    def flash_label_language(self):
        #print(self.Labelorbuttons)
        for tu in self.Labelorbuttons.items():
            #("text","object")
            if tu[0] == "您曾创下{}条记录":
                #print("true")
                tu[1]["text"] = self.translate(tu[0],str(countOfOverOne(bests)+countOfOverOne(rbests)))
            tu[1]["text"] = self.translate(tu[0])
            tu[1].update()

    def translate(self,text,arg:tuple|None=None):
        '''
        try:
            if args != None:
                return languages[currentlanguage][text].format(*args)
            else:
                return languages[currentlanguage][text]
        except Exception as e:
            #print(e)
            return "NULL"
        '''
        #print(languages[currentlanguage].keys())
        if arg != None:
            #print("true")
            if isinstance(arg,tuple):
                #print(languages[currentlanguage][text].format(*arg))
                return languages[currentlanguage][text].format(*arg)
            #print(languages[currentlanguage][text].format(arg))
            return languages[currentlanguage][text].format(arg)
        else:
            return languages[currentlanguage][text]

    def showbest(self):
        def back():
            nonlocal self
            self.BESTFRAME.pack_forget()
            self.CONFIGFRAME.pack(anchor="center",pady=120)
        self.CONFIGFRAME.pack_forget()
        self.BESTFRAME = Frame(self.root)
        self.Labelorbuttons["您曾创下{}条记录"] = Label(self.BESTFRAME,text=self.translate("您曾创下{}条记录",str(countOfOverOne(bests)+countOfOverOne(rbests))),font=("微软雅黑",20))
        self.Labelorbuttons["您曾创下{}条记录"].grid(row=0,column=0,columnspan=2,pady=20)
        columns = (self.translate("序号"), self.translate('简单版记录'))
        tree = ttk.Treeview(self.BESTFRAME, columns=columns, show='headings')
        tree.column(self.translate("序号"), width=50)
        tree.column(self.translate("简单版记录"), width=150)
        tree.heading(self.translate("序号"), text=self.translate("序号"))
        tree.heading(self.translate("简单版记录"), text=self.translate("简单版记录"))
        cnt = 0
        for i in bests:
            tree.insert('', 'end', values=(cnt+1,int(i) if i!=0 else self.translate("暂无")))
            cnt += 1
        tree.grid(row=1,column=0,ipady=40,padx=20)
        columns = (self.translate("序号"), self.translate("困难版记录"))
        tree2 = ttk.Treeview(self.BESTFRAME, columns=columns, show='headings')
        tree2.column(self.translate("序号"), width=50)
        tree2.column(self.translate("困难版记录"), width=150)
        tree2.heading(self.translate("序号"), text=self.translate("序号"))
        tree2.heading(self.translate("困难版记录"), text=self.translate("困难版记录"))
        cnt = 0
        for i in rbests:
            tree2.insert('', 'end', values=(cnt+1,int(i) if i!=0 else self.translate("暂无")))
            cnt += 1
        tree2.grid(row=1,column=1,ipady=40,padx=20)
        ttk.Button(self.BESTFRAME,text="返回",command=back).grid(row=2,column=0,columnspan=2,pady=40,ipadx=80,ipady=10)
        self.BESTFRAME.pack()


    def whenclose(self):
        save("best.npy",bests)
        save("rbest.npy",rbests)
        #print("false")
        f = openx("current_languages.txt","w",encoding="utf-8")
        f.write(currentlanguage)
        f.close()
        del f
        self.root.destroy()

    def change(self,x,y):
        self.steps += 1
        self.l["text"] = str(self.steps)
        self.chess[x-1][y] = int(not self.chess[x-1][y])
        self.chess[x+1][y] = int(not self.chess[x+1][y])
        self.chess[x][y-1] = int(not self.chess[x][y-1])
        self.chess[x][y+1] = int(not self.chess[x][y+1])
        self.chess[x][y] = int(not self.chess[x][y])
        for i in range(self.s.get()):
            for j in range(self.s.get()):
                if(self.chess[i][j]):
                    self.buttons[i,j]["bg"] = "grey"
                else:
                    self.buttons[i,j]["bg"] = "lightgrey"
        if self.victory():
            showinfo(self.translate("提示"),self.translate("胜利！您的步数为{}步！",str(self.steps)))
            if(self.enabledHellMode.get()):
                if(self.steps<rbests[i] or rbests[i]==0):
                    showinfo(self.translate("提示"),self.translate("您创下了困难版新纪录！\n{}->{}",(str(rbests[i]),str(self.steps))))
                    rbests[i] = self.steps
            else:
                if(self.steps<bests[i] or bests[i]==0):
                    showinfo(self.translate("提示"),self.translate("您创下了简单版新纪录！\n{}->{}",(str(bests[i]),str(self.steps))))
                    bests[i] = self.steps
            self.chess = zeros((100,100))
            self.steps = 0
            self.GAMEFRAME.place_forget()
            self.CONFIGFRAME.pack(anchor="center",pady=120)
            self.enabledHellMode.set(0)
            self.l.place_forget()
            self.back.place_forget()


    def victory(self):
        vic=True
        for i in range(self.s.get()):
            for j in range(self.s.get()):
                if(not self.chess[i][j]):
                    vic = False
        return vic
    
    

    def start(self):
        def back():
            nonlocal self
            self.chess = zeros((100,100))
            self.steps = 0
            self.GAMEFRAME.place_forget()
            self.CONFIGFRAME.pack(anchor="center",pady=120)
            self.enabledHellMode.set(0)
            self.l.place_forget()
            self.back.place_forget()
        self.CONFIGFRAME.pack_forget()
        self.GAMEFRAME = Frame(self.root)
        self.l = Label(self.root,text="0",font=("微软雅黑",15))
        
        
        self.buttons = {}
        TEMPVALUE = 400//self.s.get()
        #生成棋盘
        if self.enabledHellMode.get():
            for i in range(self.s.get()):
                for j in range(self.s.get()):
                    self.chess[i][j] = randint(0,1)
                    button = Button(self.GAMEFRAME,command=lambda x=i,y=j:self.change(x,y),bg="grey" if self.chess[i][j] else "lightgrey")
                    button.pack()
                    button.place(x=i*TEMPVALUE,y=j*TEMPVALUE,height=TEMPVALUE,width=TEMPVALUE)
                    self.buttons[i,j] = button
        else:
            for i in range(self.s.get()):
                for j in range(self.s.get()):
                    button = Button(self.GAMEFRAME,command=lambda x=i,y=j:self.change(x,y),bg="lightgrey")
                    button.pack()
                    button.place(x=i*TEMPVALUE,y=j*TEMPVALUE,height=TEMPVALUE,width=TEMPVALUE)
                    self.buttons[i,j] = button
        #
        self.back = ttk.Button(self.root,text=self.translate("返回"),command=back)
        self.back.place(relx=0.03,rely=0.03)
        self.GAMEFRAME.place(relx=0.1,rely=0.1,relheight=1,relwidth=1)
        self.l.place(relx=0.4,rely=0)


Game()
