from tkinter import *
import tkinter.ttk as ttk
from numpy import zeros,save,load
from tkinter.messagebox import *
from random import randint
from os.path import exists

MAXN = 15

if exists("MAXN.txt"):
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

if exists("best.npy"):
    bests = load("best.npy")

rbests = zeros(MAXN)

if exists("rbest.npy"):
    rbests = load("rbest.npy")

def countOfOverOne(array):
    cnt = 0
    for i in array:
        if(i>0):
            cnt+=1
    return cnt

class Game:
    def __init__(self):
        self.chess = zeros((100,100))
        self.steps = 0

        self.root = Tk()
        self.root.geometry("500x500")
        self.root.resizable(0,0)

        self.enabledHellMode = IntVar()
        self.CONFIGFRAME = Frame(self.root)
        self.s = Scale(self.CONFIGFRAME,from_=1,to=MAXN-1,orient="horizontal")
        self.s.pack(anchor="center",ipadx=100,pady=10)
        ttk.Button(self.CONFIGFRAME,text="开始",command=self.start).pack(anchor="center",pady=10,ipadx=60)
        Checkbutton(self.CONFIGFRAME,text="棋盘全部随机（地狱困难版）",variable=self.enabledHellMode,onvalue=1,offvalue=0).pack(anchor="center",ipadx=60,pady=10)
        ttk.Button(self.CONFIGFRAME,text="查看记录榜单",command=self.showbest).pack(anchor="center",ipadx=60,pady=10)
        self.root.title("LightsOut")
        self.root.protocol("WM_DELETE_WINDOW",self.savebests)

        self.CONFIGFRAME.pack(anchor="center",pady=120)
        self.root.mainloop()

    def showbest(self):
        def back():
            nonlocal self
            nonlocal BESTFRAME
            BESTFRAME.pack_forget()
            self.CONFIGFRAME.pack(anchor="center",pady=120)
        self.CONFIGFRAME.pack_forget()
        BESTFRAME = Frame(self.root)
        Label(BESTFRAME,text="您曾创下"+str(countOfOverOne(bests)+countOfOverOne(rbests))+"条记录",font=("微软雅黑",20)).grid(row=0,column=0,columnspan=2,pady=20)
        columns = ('序号', '简单版记录')
        tree = ttk.Treeview(BESTFRAME, columns=columns, show='headings')
        tree.column('序号', width=100)
        tree.column('简单版记录', width=100)
        tree.heading('序号', text='序号')
        tree.heading('简单版记录', text='简单版记录')
        cnt = 0
        for i in bests:
            tree.insert('', 'end', values=(cnt+1,int(i) if i!=0 else "暂无"))
            cnt += 1
        tree.grid(row=1,column=0,ipady=40,padx=10)
        columns = ('序号', '困难版记录')
        tree2 = ttk.Treeview(BESTFRAME, columns=columns, show='headings')
        tree2.column('序号', width=100)
        tree2.column('困难版记录', width=100)
        tree2.heading('序号', text='序号')
        tree2.heading('困难版记录', text='困难版记录')
        cnt = 0
        for i in rbests:
            tree2.insert('', 'end', values=(cnt+1,int(i) if i!=0 else "暂无"))
            cnt += 1
        tree2.grid(row=1,column=1,ipady=40,padx=10)
        ttk.Button(BESTFRAME,text="返回",command=back).grid(row=2,column=0,columnspan=2,pady=40,ipadx=80,ipady=10)
        BESTFRAME.pack()


    def savebests(self):
        save("best.npy",bests)
        save("rbest.npy",rbests)
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
            showinfo("提示","胜利！您的步数为"+str(self.steps)+"步！")
            if(self.enabledHellMode.get()):
                if(self.steps<rbests[i] or rbests[i]==0):
                    showinfo("提示","您创下了困难版新纪录！\n"+str(rbests[i])+"->"+str(self.steps))
                    rbests[i] = self.steps
            else:
                if(self.steps<bests[i] or bests[i]==0):
                    showinfo("提示","您创下了简单版新纪录！\n"+str(bests[i])+"->"+str(self.steps))
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
        self.back = ttk.Button(self.root,text="返回",command=back)
        self.back.place(relx=0.03,rely=0.03)
        self.GAMEFRAME.place(relx=0.1,rely=0.1,relheight=1,relwidth=1)
        self.l.place(relx=0.4,rely=0)


Game()
