# -*- coding: utf-8 -*
#!/usr/bin/env python3

file = open('away.txt', mode='r', encoding="utf-8")
t = file.readlines() # 读取整个文件内容
file.close() # 关闭文件
away_list = [x.strip() for x in t]

file = open('home.txt', mode='r', encoding="utf-8")
a = file.readlines() # 读取整个文件内容
file.close() # 关闭文件
home_list = [x.strip() for x in a]

#读队名
file = open('team_name.txt', mode='r', encoding="utf-8")
teamname_home = file.readlines()[0].replace("\n", "")  # 读取整个文件内容
file.close()
file = open('team_name.txt', mode='r', encoding="utf-8")
teamname_away = file.readlines()[1]  # 读取整个文件内容
file.close() # 关闭文件


from tkinter import *
from tkinter import ttk

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("绝笙Vmix字幕软件足球比赛控制面板 alpha0.2(20190115)")  #窗口名
        #self.init_window_name.geometry('800x580+10+10')     #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name["bg"] = "snow"       #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha",1)     #虚化，值越小虚化程度越高
        
        self.frame_root = Frame(self.init_window_name,bg="red",width=800,height=580)#最外层frame
        self.canvas_root = Canvas(self.frame_root,bg="yellow",borderwidth=0)#canvas
        self.frame_container = Frame(self.canvas_root,bg="red")#canvas内部frame
        
        self.frame_root.grid(row=0,column=0)
        self.frame_container.grid(row=0,column=0)
        self.canvas_root.pack(side="left", fill="both", expand=True)
        
        self.canvas_root.create_window((4,4), window=self.frame_container, anchor="nw")#canvas创建窗口

        self.frame_root.pack_propagate(0)#固定大小

        self.scrollbar_y = Scrollbar(self.frame_root)#创建scrollbar
        self.canvas_root.config(yscrollcommand=self.scrollbar_y.set)#关联canvas
        self.scrollbar_y.config(command=self.canvas_root.yview)#反相关联
        self.scrollbar_y.pack(side="right", fill="y")

        self.frame_container.bind("<Configure>", self.onFrameConfigure)#触发条件

        #各模块frame

        #球队名单
        self.frame_player_list = Frame(self.frame_container,bg="blue")
        self.frame_player_list.grid(row=0,column=0,padx=10,pady=10,rowspan=30,sticky="W")

        #换人模块
        self.frame_sub = Frame(self.frame_container,bg="green")
        self.frame_sub.grid(row=30,column=0,padx=10,pady=10,sticky="W")

        #组件

        #主队名称
        self.home_list_title = Label(self.frame_player_list, text= "主："+teamname_home,font=('YaHei', 18), bg="snow")
        self.home_list_title.grid(row=2,column=0,sticky=W,rowspan=2,pady=8)     

        #客队名称
        self.away_list_title = Label(self.frame_player_list, text= "客："+teamname_away,font=('YaHei', 18), bg="snow")
        self.away_list_title.grid(row=2,column=38,sticky=W,rowspan=2,pady=8)  

        #主队名单
        self.list_home = Listbox(self.frame_player_list, selectmode=SINGLE,height=len(home_list),bg ="WhiteSmoke", bd=0,font=('YaHei', 14))
        for item in home_list:
            self.list_home.insert(END, item)
        self.list_home.grid(row=4,column=0,rowspan=30, columnspan=8)

        #客队名单
        self.list_away = Listbox(self.frame_player_list, selectmode=SINGLE,height=len(away_list),bg ="WhiteSmoke", bd=0,font=('YaHei', 14))
        for item in away_list:
            self.list_away.insert(END, item)
        self.list_away.grid(row=4,column=38,rowspan=30, columnspan=8)

        #换人标题
        self.sub_module_title = Label(self.frame_sub, text= "换人模块",font=('YaHei', 20), bg="snow")
        self.sub_module_title.grid(row=40,column=0,sticky=W,rowspan=2,pady=6)

        self.sub_away_title = Label(self.frame_sub, text= "客队换人",font=('YaHei', 14), bg="snow")
        self.sub_away_title.grid(row=60,column=0,sticky=W,rowspan=2,pady=1)

        self.sub_away_out_title = Label(self.frame_sub, text= "客队换下",font=('YaHei', 10), bg="snow")
        self.sub_away_out_title.grid(row=62,column=0,sticky=W,pady=1, rowspan=2)

        self.sub_away_in_title = Label(self.frame_sub, text= "客队换上",font=('YaHei', 10), bg="snow")
        self.sub_away_in_title.grid(row=64,column=0,sticky=W,pady=1, rowspan=2)

        self.sub_home_title = Label(self.frame_sub, text= "主队换人",font=('YaHei', 14), bg="snow")
        self.sub_home_title.grid(row=80,column=0,sticky=W,rowspan=2,pady=1)

        self.sub_home_out_title = Label(self.frame_sub, text= "主队换下",font=('YaHei', 10), bg="snow")
        self.sub_home_out_title.grid(row=82,column=0,sticky=W,pady=1, rowspan=2)

        self.sub_home_in_title = Label(self.frame_sub, text= "主队换上",font=('YaHei', 10), bg="snow")
        self.sub_home_in_title.grid(row=84,column=0,sticky=W,pady=1, rowspan=2)

        #客队换上球员选择
        self.sub_away_choose_in = ttk.Combobox(self.frame_sub)
        self.sub_away_choose_in.grid(row=63,column=0,pady=1, rowspan=2)
        self.sub_away_choose_in['value'] = away_list
        self.sub_away_choose_in["state"] = "readonly"
        self.sub_away_choose_in.current(0)
        self.sub_away_choose_in.bind("<<ComboboxSelected>>", self.sub_away_choose)

        #客队换下球员选择
        self.sub_away_choose_out = ttk.Combobox(self.frame_sub)
        self.sub_away_choose_out.grid(row=65,column=0,pady=1, rowspan=2)
        self.sub_away_choose_out['value'] = away_list
        self.sub_away_choose_out["state"] = "readonly"
        self.sub_away_choose_out.current(0)
        self.sub_away_choose_out.bind("<<ComboboxSelected>>", self.sub_away_choose)

        #客队换人结果显示
        self.sub_away_info = Text(self.frame_sub, width=20, height=2) #处理结果展示
        self.sub_away_info.grid(row=60, column=15, rowspan=2,columnspan=20,padx=4,pady=4)

        #客队换人按钮
        self.sub_away_button = Button(self.frame_sub, text="换人", background="MintCream",width=10, height=4, command=self.sub_away, font=('YaHei', 16)) # 换人按钮
        self.sub_away_button.grid(row=64, column=15, rowspan=2,columnspan=10,padx=4,pady=4)

        #客队清空按钮
        self.sub_clear_away_button = Button(self.frame_sub, text="清空", foreground = "red", width=5,height=2,command=self.sub_clear_away) # 换人清空按钮
        self.sub_clear_away_button.grid(row=64, column=26, rowspan=2,columnspan=5,padx=4,pady=4)

        #主队换上球员选择
        self.sub_home_choose_in = ttk.Combobox(self.frame_sub)
        self.sub_home_choose_in.grid(row=83,column=0,pady=1, rowspan=2)
        self.sub_home_choose_in['value'] = home_list
        self.sub_home_choose_in["state"] = "readonly"
        self.sub_home_choose_in.current(0)
        self.sub_home_choose_in.bind("<<ComboboxSelected>>", self.sub_home_choose)

        #主队换下球员选择
        self.sub_home_choose_out = ttk.Combobox(self.frame_sub)
        self.sub_home_choose_out.grid(row=85,column=0,pady=1, rowspan=2)
        self.sub_home_choose_out['value'] = home_list
        self.sub_home_choose_out["state"] = "readonly"
        self.sub_home_choose_out.current(0)
        self.sub_home_choose_out.bind("<<ComboboxSelected>>", self.sub_home_choose)

        #主队换人结果显示
        self.sub_home_info = Text(self.frame_sub, width=20, height=2) #处理结果展示
        self.sub_home_info.grid(row=80, column=15, rowspan=2,columnspan=20,padx=4,pady=4)

        #主队换人按钮
        self.sub_home_button = Button(self.frame_sub, text="换人", background="MintCream",width=10, height=4, command=self.sub_home, font=('YaHei', 16)) # 换人按钮
        self.sub_home_button.grid(row=84, column=15, rowspan=2,columnspan=10,padx=4,pady=4)

        #主队清空按钮
        self.sub_clear_home_button = Button(self.frame_sub, text="清空", foreground = "red", width=5,height=2,command=self.sub_clear_home) # 换人清空按钮
        self.sub_clear_home_button.grid(row=84, column=26, rowspan=2,columnspan=5,padx=4,pady=4)


    #客队换人选
    def sub_away_choose(self,*args):
        trans_a = self.sub_away_choose_out.get() # 读取换下
        trans_b = self.sub_away_choose_in.get()  # 读取换上
        print("客队换人"+'\n'+"换下："+trans_a+'\n'+"换上："+trans_b)
    
    #客队换人写入
    def sub_away(self,*args):
        trans_a = self.sub_away_choose_out.get() # 读取换下
        trans_b = self.sub_away_choose_in.get()  # 读取换上
        file = open('sub_away.csv', mode='w+',encoding="utf-8")#写入csv
        file.write(trans_a)
        file.write('\n' + trans_b)
        file.close()
        self.sub_away_info.delete(1.0,END)
        self.sub_away_info.insert(1.0,"换下：" + trans_a + '\n' + "换上："  + trans_b)#文本框显示换人信息

    #客队清空文本框
    def sub_clear_away(self):
        self.sub_away_info.delete(1.0,END)#清空显示框
        file = open('sub_away.csv', mode='w+',encoding="utf-8")#清空csv文件
        file.write('')

    #主队换人选
    def sub_home_choose(self,*args):
        trans_a = self.sub_home_choose_out.get() # 读取换下
        trans_b = self.sub_home_choose_in.get()  # 读取换上
        print("主队换人"+'\n'+"换下："+trans_a+'\n'+"换上："+trans_b)
    
    #主队换人写入
    def sub_home(self,*args):
        trans_a = self.sub_home_choose_out.get() # 读取换下
        trans_b = self.sub_home_choose_in.get()  # 读取换上
        file = open('sub_home.csv', mode='w+',encoding="utf-8")#写入csv
        file.write(trans_a)
        file.write('\n' + trans_b)
        file.close()
        self.sub_home_info.delete(1.0,END)
        self.sub_home_info.insert(1.0,"换下：" + trans_a + '\n' + "换上："  + trans_b)#文本框显示换人信息

    #主队清空文本框
    def sub_clear_home(self):
        self.sub_home_info.delete(1.0,END)#清空显示框
        file = open('sub_home.csv', mode='w+',encoding="utf-8")#清空csv文件
        file.write('')

    #触发scrollbar
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas_root.configure(scrollregion=self.canvas_root.bbox("all"))


def gui_start():
        init_window = Tk()    #实例化出一个父窗口
        AAA_PORTAL = MY_GUI(init_window)
        # 设置根窗口默认属性
        AAA_PORTAL.set_init_window()
        init_window.mainloop()   #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
gui_start()