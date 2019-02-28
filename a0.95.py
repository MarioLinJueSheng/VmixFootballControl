# -*- coding: utf-8 -*
#!/usr/bin/env python3

#球队名
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

#比分
score_home = "0"
score_away = "0"
session_period = "上半场"
file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
file.close()


from tkinter import *
from tkinter import ttk
from tkinter import StringVar

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("绝笙Vmix字幕软件足球比赛控制面板 0.95(20190228) by:林嘉瑜")  #窗口名
        #self.init_window_name.geometry('800x580+10+10')     #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.resizable(0,0)    #固定窗口大小
        self.init_window_name["bg"] = "snow"       #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha",1)     #虚化，值越小虚化程度越高
        
        self.frame_root = Frame(self.init_window_name,bg="red",width=1200,height=720)#最外层frame
        self.canvas_root = Canvas(self.frame_root,bg="#f4e7fc",borderwidth=0)#canvas
        self.frame_container = Frame(self.canvas_root,bg="#f7f7f7")#canvas内部frame
        
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

        self.sessionVar = StringVar()#
        self.sessionVar.set("上半场")

        self.scoreHomeVar = IntVar()#
        self.scoreHomeVar.set(0)

        self.scoreAwayVar = IntVar()#
        self.scoreAwayVar.set(0)

        '''各模块frame'''

        #球队名单
        self.frame_player_list = Frame(self.frame_container,bg="#E6E6F0")
        self.frame_player_list.grid(row=0,column=0,padx=10,pady=10,sticky="NW")

        #换人模块
        self.frame_sub = Frame(self.frame_container,bg="#C3D7DF")
        self.frame_sub.grid(row=25,column=0,padx=10,pady=10,sticky="NW")

        #红黄牌模块
        self.frame_red_yellow_card = Frame(self.frame_container,bg="#B1EDE7")
        self.frame_red_yellow_card.grid(row=0,column=100,padx=10,pady=10,sticky="NW")

        #记分板模块
        self.frame_scoreboard = Frame(self.frame_container,bg="#E0D9CE")
        self.frame_scoreboard.grid(row=25,column=100,padx=10,pady=10,sticky="NW")       

        #组件

        '''名单显示'''
        #主队名称
        self.home_list_title = Label(self.frame_player_list, text= "主："+teamname_home,font=('YaHei', 18), bg="#E6E6F0")
        self.home_list_title.grid(row=2,column=0,sticky=W,rowspan=2,pady=8)     

        #客队名称
        self.away_list_title = Label(self.frame_player_list, text= "客："+teamname_away,font=('YaHei', 18), bg="#E6E6F0")
        self.away_list_title.grid(row=2,column=38,sticky=W,rowspan=2,pady=8)  

        #主队名单
        self.list_home = Listbox(self.frame_player_list, selectmode=SINGLE,height=len(home_list),bg ="#E9D2CD", bd=0,font=('YaHei', 14))
        for item in home_list:
            self.list_home.insert(END, item)
        self.list_home.grid(row=4,column=0,rowspan=30, columnspan=8)

        #客队名单
        self.list_away = Listbox(self.frame_player_list, selectmode=SINGLE,height=len(away_list),bg ="#E9D2CD", bd=0,font=('YaHei', 14))
        for item in away_list:
            self.list_away.insert(END, item)
        self.list_away.grid(row=4,column=38,rowspan=30, columnspan=8)


        '''换人模块'''
        #换人标题
        self.sub_module_title = Label(self.frame_sub, text= "换人模块",font=('YaHei', 20), bg="#C3D7DF")
        self.sub_module_title.grid(row=40,column=0,sticky=W,rowspan=2,pady=6)

        self.sub_away_title = Label(self.frame_sub, text= "客队（"+teamname_away+"）换人",font=('YaHei', 14), bg="#C3D7DF")
        self.sub_away_title.grid(row=60,column=0,sticky=W,rowspan=2,pady=1)

        self.sub_away_out_title = Label(self.frame_sub, text= "客队换下",font=('YaHei', 10), bg="#C3D7DF")
        self.sub_away_out_title.grid(row=62,column=0,sticky=W,pady=1, rowspan=2)

        self.sub_away_in_title = Label(self.frame_sub, text= "客队换上",font=('YaHei', 10), bg="#C3D7DF")
        self.sub_away_in_title.grid(row=64,column=0,sticky=W,pady=1, rowspan=2)

        self.sub_home_title = Label(self.frame_sub, text= "主队（"+teamname_home+"）换人",font=('YaHei', 14), bg="#C3D7DF")
        self.sub_home_title.grid(row=80,column=0,sticky=W,rowspan=2,pady=1)

        self.sub_home_out_title = Label(self.frame_sub, text= "主队换下",font=('YaHei', 10), bg="#C3D7DF")
        self.sub_home_out_title.grid(row=82,column=0,sticky=W,pady=1, rowspan=2)

        self.sub_home_in_title = Label(self.frame_sub, text= "主队换上",font=('YaHei', 10), bg="#C3D7DF")
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
        self.sub_away_button = Button(self.frame_sub, text="客队换人", background="MintCream",width=10, height=4, command=self.sub_away, font=('YaHei', 16)) # 换人按钮
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
        self.sub_home_button = Button(self.frame_sub, text="主队换人", background="MintCream",width=10, height=4, command=self.sub_home, font=('YaHei', 16)) # 换人按钮
        self.sub_home_button.grid(row=84, column=15, rowspan=2,columnspan=10,padx=4,pady=4)

        #主队清空按钮
        self.sub_clear_home_button = Button(self.frame_sub, text="清空", foreground = "red", width=5,height=2,command=self.sub_clear_home) # 换人清空按钮
        self.sub_clear_home_button.grid(row=84, column=26, rowspan=2,columnspan=5,padx=4,pady=4)


        '''红黄牌'''
        #红黄牌标题
        self.red_yellow_card_title = Label(self.frame_red_yellow_card, text= "红黄牌",font=('YaHei', 20), bg="#B1EDE7")
        self.red_yellow_card_title.grid(row=0,column=0,sticky=W,rowspan=2,pady=6)

        self.red_home_title = Label(self.frame_red_yellow_card, text= "主队（"+teamname_home+"）红黄牌",font=('YaHei', 14), bg="#B1EDE7")
        self.red_home_title.grid(row=10,column=0,sticky=W,rowspan=2,pady=1)

        self.red_away_title = Label(self.frame_red_yellow_card, text= "客队（"+teamname_away+"）红黄牌",font=('YaHei', 14), bg="#B1EDE7")
        self.red_away_title.grid(row=20,column=0,sticky=W,rowspan=2,pady=1)

        self.red_away_title = Label(self.frame_red_yellow_card, text= "历史记录",font=('YaHei', 14), bg="#B1EDE7")
        self.red_away_title.grid(row=30,column=0,sticky=W,rowspan=2,pady=1)

        #主队球员选择
        self.red_home_choose = ttk.Combobox(self.frame_red_yellow_card)
        self.red_home_choose.grid(row=13,column=0,pady=1, rowspan=2)
        self.red_home_choose['value'] = home_list
        self.red_home_choose["state"] = "readonly"
        self.red_home_choose.current(0)
        self.red_home_choose.bind("<<ComboboxSelected>>", self.red_card_home_read_list)

        #主队红牌按钮
        self.red_home_button = Button(self.frame_red_yellow_card, text="主队红牌", background="MintCream",foreground="red",width=6, height=2, command=self.red_home, font=('YaHei', 12)) 
        self.red_home_button.grid(row=13, column=15, rowspan=2,columnspan=6,padx=4,pady=4)

        #主队黄牌按钮
        self.yellow_home_button = Button(self.frame_red_yellow_card, text="主队黄牌", background="MintCream",foreground="DarkKhaki",width=6, height=2, command=self.yellow_home, font=('YaHei', 12)) 
        self.yellow_home_button.grid(row=13, column=25, rowspan=2,columnspan=6,padx=4,pady=4)

        #客队球员选择
        self.red_away_choose = ttk.Combobox(self.frame_red_yellow_card)
        self.red_away_choose.grid(row=23,column=0,pady=1, rowspan=2)
        self.red_away_choose['value'] = away_list
        self.red_away_choose["state"] = "readonly"
        self.red_away_choose.current(0)
        self.red_away_choose.bind("<<ComboboxSelected>>", self.red_card_away_read_list)

        #客队红牌按钮
        self.red_away_button = Button(self.frame_red_yellow_card, text="客队红牌", background="MintCream",foreground="red",width=6, height=2, command=self.red_away, font=('YaHei', 12)) 
        self.red_away_button.grid(row=23, column=15, rowspan=2,columnspan=6,padx=4,pady=4)

        #客队黄牌按钮
        self.yellow_away_button = Button(self.frame_red_yellow_card, text="客队黄牌", background="MintCream",foreground="DarkKhaki",width=6, height=2, command=self.yellow_away, font=('YaHei', 12)) 
        self.yellow_away_button.grid(row=23, column=25, rowspan=2,columnspan=6,padx=4,pady=4)

        #历史记录显示
        self.red_yellow_info = Text(self.frame_red_yellow_card, width=20, height=5) #记录文本框
        self.red_yellow_info.grid(row=33, column=0, rowspan=5,columnspan=5,pady=4)

        #历史记录清空按钮
        self.red_clear_button = Button(self.frame_red_yellow_card, text="清空", foreground = "red", width=6,height=2,command=self.red_clear_history) # 历史清空按钮
        self.red_clear_button.grid(row=33, column=15, rowspan=2,columnspan=6,padx=4,pady=4)

        '''记分板'''
        #记分板标题
        self.scoreboard_title = Label(self.frame_scoreboard, text= "记分板",font=('YaHei', 20), bg="#E0D9CE")
        self.scoreboard_title.grid(row=0,column=0,sticky=W,rowspan=2,pady=6)
        
        self.scoreboard_home_name_title = Label(self.frame_scoreboard, text= teamname_home,font=('YaHei', 14), bg="#E0D9CE")   #主队名
        self.scoreboard_home_name_title.grid(row=10,column=0,sticky=W,rowspan=2,pady=1)
        
        self.scoreboard_away_name_title = Label(self.frame_scoreboard, text= teamname_away,font=('YaHei', 14), bg="#E0D9CE")   #客队名
        self.scoreboard_away_name_title.grid(row=10,column=20,sticky=W,rowspan=2,pady=1)

        self.scoreboard_vs_title = Label(self.frame_scoreboard, text= ":",font=('YaHei', 72), bg="#E0D9CE")
        self.scoreboard_vs_title.grid(row=10,column=10,rowspan=15,padx=80)

        self.scoreboard_home_score_title = Label(self.frame_scoreboard, textvariable= self.scoreHomeVar,font=('YaHei', 48), bg="#E0D9CE")  #主队比分
        self.scoreboard_home_score_title.grid(row=20,column=0,rowspan=2,pady=1)
        
        self.scoreboard_away_score_title = Label(self.frame_scoreboard, textvariable= self.scoreAwayVar,font=('YaHei', 48), bg="#E0D9CE")  #客队比分
        self.scoreboard_away_score_title.grid(row=20,column=20,rowspan=2,pady=1)

        self.scoreboard_session_title = Label(self.frame_scoreboard, textvariable= self.sessionVar,font=('YaHei', 14), foreground="red",bg="#E0D9CE")  #上下半场
        self.scoreboard_session_title.grid(row=30,column=10,rowspan=2,pady=1)

        #上下半场选择
        self.scoreboard_session_first_radio = Radiobutton(self.frame_scoreboard, text="上半场", value="上半场",bg="#E0D9CE" ,variable=self.sessionVar, command=self.scoreboard_session_switch, font=('YaHei', 12)) 
        self.scoreboard_session_first_radio.grid(row=40, column=10, rowspan=2,columnspan=6,padx=4,pady=4)
       
        self.scoreboard_session_second_radio = Radiobutton(self.frame_scoreboard, text="下半场", value="下半场",bg="#E0D9CE" , variable=self.sessionVar, command=self.scoreboard_session_switch, font=('YaHei', 12)) 
        self.scoreboard_session_second_radio.grid(row=41, column=10, rowspan=2,columnspan=6,padx=4,pady=4)

        #主队比分按钮
        self.scoreboard_home_scoreplus_button = Button(self.frame_scoreboard, text="主+1", background="MintCream",width=6, height=2, command=self.scoreboard_home_scoreplus, font=('YaHei', 12)) 
        self.scoreboard_home_scoreplus_button.grid(row=40, column=0, rowspan=2,columnspan=6,padx=4,pady=4)

        self.scoreboard_away_scoreplus_button = Button(self.frame_scoreboard, text="客+1", background="MintCream",width=6, height=2, command=self.scoreboard_away_scoreplus, font=('YaHei', 12)) 
        self.scoreboard_away_scoreplus_button.grid(row=40, column=20, rowspan=2,columnspan=6,padx=4,pady=4)

        #客队比分按钮
        self.scoreboard_home_scoreminus_button = Button(self.frame_scoreboard, text="主-1", background="MintCream",width=6, height=2, command=self.scoreboard_home_scoreminus, font=('YaHei', 12)) 
        self.scoreboard_home_scoreminus_button.grid(row=42, column=0, rowspan=2,columnspan=6,padx=4,pady=4)

        self.scoreboard_away_scoreminus_button = Button(self.frame_scoreboard, text="客-1", background="MintCream",width=6, height=2, command=self.scoreboard_away_scoreminus, font=('YaHei', 12)) 
        self.scoreboard_away_scoreminus_button.grid(row=42, column=20, rowspan=2,columnspan=6,padx=4,pady=4)

        #清空按钮
        self.scoreboard_score_clear_button = Button(self.frame_scoreboard, text="清空", background="MintCream",width=6, height=2,foreground="red",command=self.scoreboard_score_clear, font=('YaHei', 12)) 
        self.scoreboard_score_clear_button.grid(row=46, column=10, rowspan=2,columnspan=6,padx=4,pady=4)


    '''换人'''
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
        file.close()

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
        file.close()

    '''红黄牌'''
    #主队红黄牌人选
    def red_card_home_read_list(self,*args):
        red_choose = self.red_home_choose.get() # 读取换下
        #print(red_choose)
    
    #主队红牌写入
    def red_home(self,*args):
        red_choose = self.red_home_choose.get() # 读取换下
        file = open('red_card.csv', mode='w+',encoding="utf-8")#写入csv
        file.write(teamname_home + "," + red_choose)
        file.close()
        self.red_yellow_info.insert(1.0,"主队红牌：" + red_choose + '\n')#文本框显示信息

    #主队黄牌写入
    def yellow_home(self,*args):
        red_choose = self.red_home_choose.get() # 读取换下
        file = open('yellow_card.csv', mode='w+',encoding="utf-8")#写入csv
        file.write(teamname_home + "," + red_choose)
        file.close()
        self.red_yellow_info.insert(1.0,"主队黄牌：" + red_choose +'\n')#文本框显示信息

    #客队红黄牌人选
    def red_card_away_read_list(self,*args):
        red_choose = self.red_away_choose.get() # 读取换下
        #print(red_choose)
    
    #客队红牌写入
    def red_away(self,*args):
        red_choose = self.red_away_choose.get() # 读取换下
        file = open('red_card.csv', mode='w+',encoding="utf-8")#写入csv
        file.write(teamname_away + "," + red_choose)
        file.close()
        self.red_yellow_info.insert(1.0,"客队红牌：" + red_choose +'\n')#文本框显示信息

    #客队黄牌写入
    def yellow_away(self,*args):
        red_choose = self.red_away_choose.get() # 读取换下
        file = open('yellow_card.csv', mode='w+',encoding="utf-8")#写入csv
        file.write(teamname_away + "," + red_choose)
        file.close()
        self.red_yellow_info.insert(1.0,"客队黄牌：" + red_choose +'\n')#文本框显示信息

    #清空历史记录
    def red_clear_history(self):
        self.red_yellow_info.delete(1.0,END)#清空显示框
        file = open('red_card.csv', mode='w+',encoding="utf-8")#清空csv文件
        file.write('')
        file.close()
        file = open('yellow_card.csv', mode='w+',encoding="utf-8")#清空csv文件
        file.write('')
        file.close()

    '''记分板'''
    #上下半场选择
    def scoreboard_session_switch(self):
        score_home = self.scoreHomeVar.get()
        score_away = self.scoreAwayVar.get()
        session_period = self.sessionVar.get()
        file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
        file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
        file.close()

    #主队比分增加
    def scoreboard_home_scoreplus(self):
        score_home = self.scoreHomeVar.get()
        score_away = self.scoreAwayVar.get()
        session_period = self.sessionVar.get()
        score_home = score_home + 1
        self.scoreHomeVar.set(score_home)
        file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
        file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
        file.close()

    #客队比分增加
    def scoreboard_away_scoreplus(self):
        score_home = self.scoreHomeVar.get()
        score_away = self.scoreAwayVar.get()
        session_period = self.sessionVar.get()
        score_away = score_away + 1
        self.scoreAwayVar.set(score_away)
        file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
        file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
        file.close()

    #主队比分减少
    def scoreboard_home_scoreminus(self):
        score_home = self.scoreHomeVar.get()
        score_away = self.scoreAwayVar.get()
        session_period = self.sessionVar.get()
        if score_home <= 0:
            score_home == 0
        else:
            score_home = score_home - 1
        self.scoreHomeVar.set(score_home)
        file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
        file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
        file.close()

    #客队比分减少
    def scoreboard_away_scoreminus(self):
        score_home = self.scoreHomeVar.get()
        score_away = self.scoreAwayVar.get()
        session_period = self.sessionVar.get()
        if score_away <= 0:
            score_away == 0
        else:
            score_away = score_away - 1
        self.scoreAwayVar.set(score_away)
        file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
        file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
        file.close()

    #清空比分
    def scoreboard_score_clear(self):
        self.scoreHomeVar.set(0)
        self.scoreAwayVar.set(0)
        score_home = self.scoreHomeVar.get()
        score_away = self.scoreAwayVar.get()
        session_period = self.sessionVar.get()
        file = open('scoreboard.csv', mode='w+',encoding="utf-8")#写入csv文件
        file.write(teamname_home + "," + str(score_home) + '\n' + teamname_away + "," + str(score_away) + '\n' + session_period)
        file.close()


    '''滚动条'''
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