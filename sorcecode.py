#!python3.9
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import colorchooser


import os
import file_array as FA
from tkinter import filedialog
import subprocess
import json
import time
import sys

import keyboard
import webbrowser



global ColorFB,Widget_List
#SYSTEM_PATH = "py -3.9 tk6.py"
SYSTEM_PATH = "config.exe"
Widget_List =[]
#Widget_List.append()

class PIN_SET:
    def __init__(self,tex,xx,yy):
        
        self.BT =tk.Button(root,text=tex,command=self.com)
        self.BT.place(x=xx,y=yy)
        Widget_List.append(self.BT)
    def com(self):
        if not self.sub==None:
            self.sub.destroy()
        self.sub = tk.Toplevel()
        
        
        #listbox 左
        #ボタン(send)
        #ボタン(push)
        #ボタン（release）
        #ボタン(releaseALL)
        #sleep
        
        ## [ > ]            
        ## [ >>]       右リスト append(left_list[])　選択の動作を一番下に設定
        ## [🚮]               pop(num) 選択の動作を破棄
        ##　[↑] / [↓]         chenge(num) 選択の動作を (上／下)と入れ替える
        
        
        
        
        #listbox 右
        
        #選択した動作1
        #選択した動作2
        #選択した動作3
        #   .
        #   .
        #   .
        
        ## 引数(num)  テンキーが表示されるので入力、もしくは同時に表示されるテキストボックスに数字を入れる
        ##　引数(char) key_eventを取得する、もしくはボタンが表示されるので好きなキーのボタンを押す
        ### 無効な操作は無効化する
make_num =0
#class SingletonWindow:
def change(text3,pID,pNum,window_d):
    global prof_but
    print(text3,prof_but)
    key_obj_list[pID][pNum][1]=text3
    
    temp_list =key_obj_list[pID]
    prof_but[pID-1].key_listbox.delete(0, tk.END)
    for item in temp_list:
            prof_but[pID-1].key_listbox.insert(tk.END, str(item))
    
    
    window_d.destroy()
    



        







    
def sub_window(pID,pNum):
    global sub_win,make_num,root,prof_but
    if sub_win == None or not sub_win.winfo_exists():
        print("make")
        #root.grab_set()
        sub_win = tk.Toplevel()
        sub_win.geometry("560x180")
        
        if start["language"] =="jp":
            temp =f'{lang["keysetting"]}{make_num}/{lang["button_num"]}:{pID} {pNum+1}{lang["com"]}'
        else:
            temp=f"Key setting {make_num}/button number:{pID}  command in line {pNum+1}"
        
        sub_win.title(temp)
        text1=""
        for i in lang["text1"]:
        
            text1= text1+"\n"+i


        
        
        print(key_obj_list[pID][pNum])
        set_conf= key_obj_list[pID][pNum]
        label_sub = tk.Label(sub_win, text=text1,anchor=tk.NW,justify=tk.LEFT)
        #["send","push","release","releaseALL","sleep"]
        if set_conf[0]=="send":
            text2 = lang["t2send"]
        elif set_conf[0]=="push":
            text2 = lang["t2push"]
        elif set_conf[0]=="release":
            text2 =  lang["t2release"]
        elif set_conf[0]=="releaseALL":
            text2=  lang["t2releaseALL"]
        elif set_conf[0]=="sleep":
            text2= lang["t2sleep"]
        elif set_conf[0]=="PLAY_PAUSE":
            text2= lang["PLAY_PAUSE"]  #consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
        else:
            text2= lang["t2vol"]
        label_sub01 =tk.Label(sub_win, text=text2,justify=tk.RIGHT,anchor=tk.NE)
        
        label_sub.pack()
        Widget_List.append(label_sub)
        label_sub01.place(x=150,y=140)
        Widget_List.append(label_sub01)
        setting_box =tk.Entry(sub_win,width=16,font=("",15))
        setting_box.place(x=300,y=140)
        #PLAY_PAUSE
        setting_button= tk.Button(sub_win,text=lang["change"],command=lambda:change(setting_box.get(),pID,pNum,sub_win))
        setting_button.place(x=500,y=140)
        
        Widget_List.append(setting_button)
        
        label_sub.pack()
        make_num +=1
        
        sub_win.mainloop()
        #root.grab_release() 
        
        
    else:
        print("destroy")
        sub_win.destroy()
        sub_window(pID,pNum)
        #root.grab_release()
        
class SetKey_handler_Browser:

    def __init__(self,setkey,browser,start ):
        self.hot_key = setkey 
        self.startMes = start
        keyboard.add_hotkey(self.hot_key, self.handler)
        self.browser = browser
        
    def handler(self):
        print(f"Hotkey {self.hot_key} pressed!")
        print(self.startMes)
        webbrowser.open(self.browser)
        
class SetKey_handler_Exefile:

    def __init__(self,setkey,Exe,start ):
        self.hot_key = setkey 
        self.Exefile = Exe
        self.startMes = start
        keyboard.add_hotkey(self.hot_key, self.handler)
    def handler(self):
        print(f"Hotkey {self.hot_key} pressed!")
        print(self.startMes)
        try:
                print("3")
                subprocess.Popen(['start', '', self.Exefile], shell=True)  # Windows
        except subprocess.CalledProcessError:
                print(f"\n\nCould not open the file {self.Exefile}. Please check your system.\n\n")

        
    def remove_key(self):
        # ホットキーを削除
        keyboard.remove_hotkey(self.hot_key)
        print("hot_keyの削除完了")

class plof:
    def __init__(self):
        self.pin =[]
        for i in range(20):
            temp = tk.Button(root,)
            
            self.pin.append(i)
        print(self.pin)
        
befor_obj =None        
sub_win =None        
        
exe_w =None

def fdf(filename):
   if getattr(sys, "frozen", False):
       # The application is frozen
       datadir = os.path.dirname(sys.executable)
   else:
       # The application is not frozen
       # Change this bit to match where you store your data files:
       datadir = os.path.dirname(__file__)
   return os.path.join(datadir, filename)





def f0():
    selectLang("test 呼び出し")
    root.destroy()
    start_option_ch("flag",1)
    os.system(SYSTEM_PATH)
    #os.system("tk5.exe")
    
    exit(2)
    
    
    #END
"""    code = code_text.get("1.0", "end-1c")  # テキストエディタのコードを取得

    # ファイルダイアログを開いてコードを保存
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(code)
"""

def start_option_ch(ch,ch_value):
    start_ch =start
    print(start_ch)
    print(start_ch[ch])
    #フラグがふえたらココ
    #
    #
    start_ch[ch] = ch_value
    
    with open(fdf("option.json"),"w") as f:
            json_str = json.dumps(start_ch)
            print(json_str)
            f.write('{"start":'+json_str+"}")

    
select_glocal_ID =-1

class button_set:
    def __init__(self,text_x,xx,yy):
       global root
       self.ID = int(text_x)
       self.key_button = tk.Button(root,text=text_x,font=("",14),command=self.select_obj,height=1, width=3)
       self.key_button.place(x=xx,y=yy)
       self.selected_item =""
       self.command_listbox =None
       self.command_list2 =[]
       self.key_listbox =tk.Listbox(frame_groove,height=16,width=16)
       self.key_listbox.bind('<<ListboxSelect>>',self.select_print)
       self.keylist_select =-1
       
       Widget_List.append(self.key_button)
    def select_obj(self):
       global befor_obj,frame_groove,select_glocal_ID
       frame_groove.destroy()
       frame_groove = tk.Frame(root, bg='black',width=10,height=10)
       frame_groove.place(x=450,y=20)
       self.key_listbox =tk.Listbox(frame_groove,height=15,width=20)
       self.key_listbox.bind('<<ListboxSelect>>',self.select_print)
       self.keylist_select =-1
       #root.destroyall()
       #setup()
       self.command_list2 =key_obj_list[self.ID]
       self.key_listbox.delete(0, tk.END)
       for item in self.command_list2:
            self.key_listbox.insert(tk.END, str(item))
       
       print("ID:",self.ID)
       select_glocal_ID = self.ID
       
       
       if not befor_obj ==None:
         befor_obj.pack_forget()
       
       self.command_list1 =["send","push","release","releaseALL","sleep","VolumeUP","VolumeDown","PLAY_PAUSE","CC.send"]
       self.command_listbox =tk.Listbox(root,height=10,width=12,font=("",13))
       for item in self.command_list1:
         self.command_listbox.insert(tk.END, item)
       self.command_listbox.bind('<<ListboxSelect>>',self.select_print)
       self.command_listbox.place(x=260,y=30)
       befor_obj = self.command_listbox
       self.insert = tk.Button(root,text=">",width=1,font=("",13),command=lambda:self.obj_event(0,self.ID))
       self.push = tk.Button(root,text=">>",width=1,font=("",13),command=lambda:self.obj_event(1,self.ID))
       
       self.delete= tk.Button(root,text="<",width=1,font=("",13),command=lambda:self.obj_event(2,self.ID))
       self.up = tk.Button(root,text="↑",width=1,font=("",13),command=lambda:self.obj_event(3,self.ID))
       self.down=tk.Button(root,text="↓",width=1,font=("",13),command=lambda:self.obj_event(4,self.ID))
       
       self.insert.place(x=400,y=20)
       self.push.place(x=400,y=55)
       self.delete.place(x=400,y=90)
       self.up.place(x=400,y=125)
       self.down.place(x=400,y=160)

       Widget_List.append(self.insert)
       Widget_List.append(self.push)
       Widget_List.append(self.delete)
       Widget_List.append(self.up)
       Widget_List.append(self.down)

       self.key_listbox.pack()
    
       self.errorLavel = tk.Label(root,text="ERROR")
       #self.errorLavel.place(x=200,y=200)
       Widget_List.append(self.errorLavel)
       self.changeButton=tk.Button(root,text=lang["ch_config"],command=lambda:self.key_option(self.keylist_select))
       self.changeButton.place(x=590,y=30)
       Widget_List.append(self.changeButton)
       self.selectAuto()

    def key_option(self,num):
        if num ==-1:
            print("ERROR:選択されていません")
        else:
            print(key_obj_list[self.ID][num])
            sub_window(self.ID,num)



    def obj_event(self,list_event,event_id):
        
        print("選択",self.keylist_select)
        if len(key_obj_list[event_id]) <2 and list_event>2:
            print("error:0")
        
        
        elif list_event==0:
            if self.keylist_select <0:
                key_obj_list[event_id].insert(0,[self.selected_item,"0"])
            else:
                key_obj_list[event_id].insert(self.keylist_select,[self.selected_item,"0"])
        elif list_event==1:
            key_obj_list[event_id].append([self.selected_item,"0"])
        elif list_event==2:
            if len(key_obj_list[event_id]) ==0:
                print("error:2")
            if not self.keylist_select =="":
                    key_obj_list[event_id].pop(self.keylist_select)
            #temp,keylist_select = {objの現在何番目を選択されているかの数値}
            #self.ID,event_id ={objの現在選択されているボタンＩＤ}
            else:
                print("test 2")
        elif list_event==3:
            if self.keylist_select <1:
                print("error:リストの最上段")
            else:
                print("\n\n",self.keylist_select,"\n\n")
                key_obj_list[event_id][self.keylist_select-1],key_obj_list[event_id][self.keylist_select]=key_obj_list[event_id][self.keylist_select],key_obj_list[event_id][self.keylist_select-1]
            
                self.keylist_select -= 1
                print("test 3")
        elif list_event==4:
            if self.keylist_select >len(key_obj_list[event_id])-2:
                print("error:リストの最下段")
            else:
                key_obj_list[event_id][self.keylist_select+1],key_obj_list[event_id][self.keylist_select]=key_obj_list[event_id][self.keylist_select],key_obj_list[event_id][self.keylist_select+1]
                
                self.keylist_select+=1
                print("test 4")        
        
        self.command_list2 =key_obj_list[event_id]
        self.key_listbox.delete(0, tk.END)
        for item in self.command_list2:
            self.key_listbox.insert(tk.END, str(item))
    #######
    def reflesh(self):
        self.command_list2 =key_obj_list[self.ID]
        self.key_listbox.delete(0, tk.END)
        for item in self.command_list2:
            self.key_listbox.insert(tk.END, str(item))    
        
        for ix in range(20):
            print(ix,end=" : ")
            for jx in key_obj_list[ix]:
                print(jx,end="  ")
            print("")
        
    def selectAuto(self):
        global frame_sub,root
        frame_sub.destroy()
        frame_sub = tk.Frame(root,width=300,height=40)
        frame_sub.place(x=200,y=280)
        
       # key = tk.Label(frame_sub,text=f"{self.ID}で実行したいもの",bg="#DDDDDD")
        #path_b = tk.Button(frame_sub,text=lang["Browse"],command=self.path_select)
        
        self.entry_set_but =  tk.Button(frame_sub,text=lang["auto"],command=self.Autosetting,width=10)
        self.entry_set_but.place(x=180,y=0)
       # key.place(x=0,y=5)
        
        Widget_List.append(self.entry_set_but)
        
        
        #HotkeyCounter(frame_sub)
        
        
        #path_b.place(x=140,y=0)
        
        print(self.ID)
       # root.mainloop()
        
    def path_select(self):
        path =filedialog.askopenfilename()
        print(path)

    def Autosetting(self):
    
        key_obj_list[self.ID].append(["push","CONTROL"])
        key_obj_list[self.ID].append(["push","ALT"])
        key_obj_list[self.ID].append(["push",f"F{self.ID}"])
        key_obj_list[self.ID].append(["sleep","0.1"])
        key_obj_list[self.ID].append(["releaseALL","0"])
        self.reflesh()
    
    

    def select_print(self, event):
     #try:
        if event.widget == self.command_listbox:
            # command_listbox からの選択イベントの処理
            selected_indices = event.widget.curselection()
            if selected_indices:
                self.selected_item = event.widget.get(selected_indices[0])
            # 選択されたアイテムを処理するためのコードをここに追加
                
                #print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                print(f"Selected item: {self.selected_item},id=")
            else:
                print("command_listbox: アイテムが選択されていません")
        elif event.widget == self.key_listbox:
            # self.key_listbox からの選択イベントの処理
            selected_indices = event.widget.curselection()
            if selected_indices:
                
                select_temp = event.widget.get(selected_indices[0])
            # 選択されたアイテムを処理するためのコードをここに追加
                #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print(f"Selected list item :{select_temp},id=")

                selected_keylistnum = self.key_listbox.curselection()
                self.keylist_select = selected_keylistnum[0]
                print(self.keylist_select)
            else:
                print("self.key_listbox: アイテムが選択されていません")
 #    except Exception as e:
      #  error_window()



        #self.obj_event(self.command_list1.index(self.selected_item))
        
  #listbox 左
          #ボタン(send)
          #ボタン(push)
          #ボタン（release）
          #ボタン(releaseALL)
          #sleep
          
          ## [ > ]            
          ## [ >>]       右リスト append(left_list[])　選択の動作を一番下に設定
          ## [🚮]               pop(num) 選択の動作を破棄
          ##　[↑] / [↓]         chenge(num) 選択の動作を (上／下)と入れ替える
 

          #listbox 右
          
          #選択した動作1
          #選択した動作2
          #選択した動作3

prof_but=[]

def setup():
    global prof_but
    if not prof_but ==[]:
        for i in prof_but:
            i.key_button.destroy()

    prof_but =[]
    print("setup")

    for yy in range(0,5):
       for xx in range(1,5):
         #temp = button_set(str(yy*4+xx),-20+(60*xx),5+(40*yy)) #原本
         temp = button_set(str(yy*4+xx),260+(-60*xx),5+(40*yy))
         #temp = button_set(str(yy*4+xx),+20+(60*yy),5+(40*xx)) #90°傾ければ正常
         prof_but.append(temp)

def load_json(path, lang):
    if os.path.isfile(path):
        with open(fdf(path), 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except Exception as e:
                if path == "color.json":
                    json_reflesh()
                print("XX")
      
        return data[lang]
    return 0    


def selectLang(event):
    global lab001,lab002
    print("イベント発生")
    print(event,tk_st_val01.get())
    
    if tk_st_val01.get() =="Japanese":
        print("jp")
        start_option_ch("language","jp")
    elif tk_st_val01.get() =="English":
        print("en")
        start_option_ch("language","en")    

#if option.start["language"] =="en":
 #   lang =load_json("lang.json","en")
    
    
    
#elif option.start["language"] =="jp":
    lang =load_json("lang.json",start["language"])
    lab001["text"] = lang["lab001"]
    lab002["text"] = lang["lab002"]
def openfile():
    global key_obj_list,file_name
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_name =filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    
    print(file_name)
    xxx = "file"
    #eval(f"import {xxx} as savedata")
    key_obj_list =FA.load_array_from_file3(file_name)
    
    setup()

def savefile1():
    global file_name
    if file_name==os.getcwd():
        savefile()
    else:
        FA.save_array_to_file(key_obj_list,file_name)
def savefile():
    global key_obj_list
    
    filename = filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("txt","TXT")], # ファイルフィルタ
        initialdir = "./", # 自分自身のディレクトリ
        defaultextension = "txt"
        )
    print(filename)
    FA.save_array_to_file(key_obj_list,filename)
def langch():
    print("langch")
    global lab001,lab002
    lang_w=tk.Toplevel()
    lang_w.geometry("450x100")
    lab001 =tk.Label(lang_w,text=lang["lab001"],font=("",16))
    lab002 =tk.Label(lang_w,text=lang["lab002"])
    
    combobox = ttk.Combobox(lang_w,height=5,width=10,textvariable=tk_st_val01,values=lang_list,font=("",10))
    combobox.bind("<Button>",func=selectLang)
    
    lab001.pack()
    lab002.pack()
    
    Widget_List.append(lab001)
    Widget_List.append(lab002)
    
    
    combobox.pack()
    setup_button = tk.Button(lang_w, text=lang["setup_button"], command=f0)
    setup_button.pack()
    lang_w.mainloop()
exe_path =""
'''
class HotkeyCounter:
    def __init__(self,window,num):
        
        self.keys_pressed = set()
        self.root= window
        self.bind_temp_key =""
        #root.geometry("400x100") #画面の大きさの決定

        self.countdown_label = tk.Label(self.root, text=f"{num}Hotkey",fg="white",bg="black")
        self.countdown_label.place(x=0,y=3)

        self.countdown_button = tk.Button(self.root, text="Start Countdown", command=self.start_countdown)
        self.countdown_button.place(x=200,y=0)

        #self.root.bind("<KeyPress>", self.on_key_press)
        #exe_w.bind("<KeyPress>", self.on_key_press)
        #self.root.bind("<KeyRelease>", self.on_key_release)
        #exe_w.bind("<KeyRelease>", self.on_key_release)

    def on_key_press(self, event):
        key = event.keysym
        self.keys_pressed.add(key)

    def on_key_release(self, event):
        key = event.keysym
        self.keys_pressed.discard(key)

    def start_countdown(self):
        self.countdown_label.config(text="3")
        self.root.after(1000, lambda: self.update_countdown(2))
        exe_w.bind("<KeyRelease>", self.on_key_release)
        exe_w.bind("<KeyPress>", self.on_key_press)
    def update_countdown(self, count):
        if count > 0:
            self.countdown_label.config(text=str(count))
            self.root.after(1000, lambda: self.update_countdown(count - 1))
        else:
            self.countdown_label.config(text="Countdown complete!")
            hotkey = "+".join(sorted(self.keys_pressed))
            print(hotkey)
            self.root.after(1000, lambda: self.show_hotkey(hotkey))

    def show_hotkey(self, hotkey):
        self.countdown_label.config(text="Hotkey: " + hotkey)
        # ここでホットキーが押されたときの処理を追加できます
        self.bind_temp_key = hotkey
'''

class HotkeyCounter:
    def __init__(self, window, num):
        self.keys_pressed = set()
        self.root = window
        self.bind_temp_key = ""

        self.countdown_label = tk.Label(self.root, text=f"{num}Hotkey", fg="white", bg="black")
        self.countdown_label.place(x=0, y=3)
        self.countdown_button = tk.Button(self.root, text="Start Countdown", command=self.start_countdown)
        Widget_List.append(self.countdown_button)
        self.countdown_button.place(x=200, y=0)
        
        #self.OFF,self.ON
    def on_key_press(self, e):
        key = e.name
        self.keys_pressed.add(key)

    def on_key_release(self, e):
        key = e.name
        self.keys_pressed.discard(key)

    def start_countdown(self):
        self.countdown_label.config(text=lang["3"])
        self.root.after(1000, lambda: self.update_countdown(2))
        self.ON  = keyboard.on_press(self.on_key_press)
        self.OFF = keyboard.on_release(self.on_key_release)
        print("press,release set!!")

    def update_countdown(self, count):
        if count > 0:
            self.countdown_label.config(text=lang[str(count)])
            self.root.after(1000, lambda: self.update_countdown(count - 1))
        else:
            self.countdown_label.config(text=lang["Complete"])
            hotkey = "+".join(sorted(self.keys_pressed))
            print(hotkey)
            self.root.after(1000, lambda: self.show_hotkey(hotkey))

    def show_hotkey(self, hotkey):
        self.keys_pressed.clear()
        keyboard.unhook(self.OFF)
        keyboard.unhook(self.ON)
        self.countdown_label.config(text=lang["hot_key"] + hotkey)
        # ここでホットキーが押されたときの処理を追加できます
        self.bind_temp_key = hotkey
        

    def Destroy_exe(self,num):
        global exe_frame_list
        print(num)
        frame_move(-35)
        exe_frame_list.pop(num)
        self.root.destroy()    # 自身のフレームを削除(root,subwindowのベタ打ち禁止、Frameを生成して渡すべき)
        print("現在：",len(exe_frame_list))
        
        
        
        
        if len(exe_frame_list)>num:
            for i in range(num,len(exe_frame_list)):
                exe_frame_list[i].ch()
    
    def Destroy_brw(self,num):
        global brw_frame_list
        print(num)
        brw_frame_list.pop(num)
        self.root.destroy()    # 自身のフレームを削除(root,subwindowのベタ打ち禁止、Frameを生成して渡すべき)
        print("現在：",len(brw_frame_list))  
        
        if len(brw_frame_list)>num:
            for i in range(num,len(brw_frame_list)):
                brw_frame_list[i].ch()        
    
    def dmp(self):
        return self.bind_temp_key
    def change(self,tx1):
        self.countdown_label.config(text=tx1)



##
class exe_bind:
    def __init__(self,FRAME,yy):
        self.list_num = yy
        self.y =self.list_num*35+30
        
        self.frame = tk.Frame(FRAME,width=650,height=30,bg="white")
        
        self.hotkey_entry = tk.Entry(self.frame,width=30)
        self.exe_path =""
        
        self.frame.place(x=20,y=self.y)
        self.hotkey_entry.place(x=330,y=3)
        self.hotkey_counter = HotkeyCounter(self.frame,self.list_num)
        
        
        self.sansh_but = tk.Button(self.frame,text=lang["Browse"],command=self.select_exe)
        self.sansh_but.place(x=540,y=0)
        
        
        self.Des_button =tk.Button(self.frame,text=lang["Delete"],command=lambda:self.hotkey_counter.Destroy_exe(self.list_num))
        self.Des_button.place(x=600,y=0)
    def ch(self):
        self.list_num -= 1
        self.y =self.list_num*35+30
        self.frame.place(x=20,y=self.y)
        print(self.list_num+1,"->",self.list_num)
    
    def select_exe(self):
        
        fTyp = [("", "*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        exe_path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        print(exe_path)
        if exe_path==None:
            print("error")
        else:
            #os.system(file_name)
# "Discord"と"Update.exe"が含まれているかどうかを判定
            contains_discord = "Discord" in exe_path
            contains_update_exe = "Update.exe" in exe_path

# 結果の表示
            print(f"Discordが含まれているか: {contains_discord}")
            print(f"Update.exeが含まれているか: {contains_update_exe}")     

            if contains_discord:
                if contains_update_exe:
                    exe_path +=" --processStart DiscordPTB.exe"
            
            self.exe_path = exe_path
            self.hotkey_entry.delete(0, tk.END)
            self.hotkey_entry.insert(tk.END, self.exe_path)
            
    def dmp_data(self):
        
        tx1 =self.hotkey_entry.get()#ホットキーの文字列
        tx2 =self.hotkey_counter.dmp()#実行ファイルのパス
        return (tx1,tx2)
    def change_data(self,tx1,tx2):
        self.hotkey_entry.insert(tk.END,tx1)
        self.hotkey_counter.change(tx2)
    
    
def frame_move(mo):
    global brw_frame_y,brw_frame
    brw_frame_y+=mo
    
    brw_frame_y = len(exe_frame_list)*35+45
    brw_frame.place(x=0,y=brw_frame_y)
    
    
brw_frame_y =40 
exe_frame_list =[]

def exe_bind_list():
    global exe_w,exe_frame_list
    exe_frame_list.append(exe_bind(exe_w,len(exe_frame_list)))
    frame_move(35)
    
def exe_bind_jsonSave(wind):
    global exe_frame_list
    dictionary = {}
    j =0
    print("呼び出しA")
    if exe_frame_list ==[]:
            pass
    else:
        print(exe_frame_list)
        for i in exe_frame_list:
            al,ar =i.dmp_data()
            dictionary[str(j)] = [al,ar]
            j+=1
            print(al,":",ar)
            tek =os.getcwd()+"\\exelist.json"
            print(tek)
        with open(fdf(tek), 'w') as f: # 第二引数：writableオプションを指定
            json.dump(dictionary, f)
            print("書き込み")
        
    brw_bind_jsonSave()
    wind.destroy()

class brw_bind:
    def __init__(self,FRAME,yy):
        self.list_num = yy
        self.y =self.list_num*35+30
        
        self.frame = tk.Frame(FRAME,width=650,height=30,bg="red")
        
        self.hotkey_entry = tk.Entry(self.frame,width=30)
        self.exe_path =""
        
        self.frame.place(x=20,y=self.y)
        self.hotkey_entry.place(x=330,y=3)
        self.hotkey_counter = HotkeyCounter(self.frame,self.list_num)
        
        self.Des_button =tk.Button(self.frame,text=lang["Delete"],command=lambda:self.hotkey_counter.Destroy_brw(self.list_num))
        self.Des_button.place(x=600,y=0)
    def ch(self):
        self.list_num -= 1
        self.y =self.list_num*35+30
        self.frame.place(x=20,y=self.y)
        print(self.list_num+1,"->",self.list_num)
    
            
    def dmp_data(self):
        
        tx1 =self.hotkey_entry.get()#ホットキーの文字列
        tx2 =self.hotkey_counter.dmp()#実行ファイルのパス
        return (tx1,tx2)
    def change_data(self,tx1,tx2):
        self.hotkey_entry.insert(tk.END,tx1)
        self.hotkey_counter.change(tx2)
    
    
    
brw_frame_list =[]

def brw_bind_list():
    global brw_frame,brw_frame_list
    brw_frame_list.append(brw_bind(brw_frame,len(brw_frame_list)))
    
    
def brw_bind_jsonSave():
    global brw_frame_list
    dictionary = {}
    j =0
    if brw_frame_list ==[]:
        return
    print(brw_frame_list)
    for i in brw_frame_list:
        al,ar =i.dmp_data()
        dictionary[str(j)] = [al,ar]
        print(al,"",ar)
        j+=1
    with open(fdf("brwlist.json"), 'w') as f: # 第二引数：writableオプションを指定
        json.dump(dictionary, f)


    

    


def exe_open():
  global prof_but,exe_path,brw_frame_y,brw_frame,exe_w,exe_frame_list,brw_frame_list
  if exe_w == None or not exe_w.winfo_exists():
    exe_w = tk.Toplevel()
    exe_w.geometry("700x400")
    
    brw_frame = tk.Frame(exe_w,width=680,height=220) #ブラウザ
    exe_frame_list =[]      
    brw_frame_list =[]
    pat =fdf("exelist.json")
    if os.path.isfile(pat):
        print("true")
        with open(pat,"r") as f:
           data= json.load(f)
           print("X",data,"X")
           if data =={}:
            print("None")
           else:
            key_list= list(data.keys())
            ix =0
            for i in key_list:
                print(data[str(i)])
                al,ar = data[str(i)]
                print("\n===============",al,":",ar)
                exe_bind_list()
                exe_frame_list[int(ix)].change_data(al,ar)
                ix+=1

           #
    else:
        print(pat)
    pat =fdf("brwlist.json")
    if os.path.isfile(pat):
        print("true")
        with open(pat,"r") as f:
           data= json.load(f)
           print("Y",data,"Y")
           if data =={}:
            print("None")
           else:
            key_list= list(data.keys())
            ix =0
            for i in key_list:
                print(data[str(i)])
                al,ar = data[str(i)]
                print("\n===============",al,":",ar)
                brw_bind_list()
                brw_frame_list[int(ix)].change_data(al,ar)
                ix+=1
               
           
           
           #
    else:
        print(pat)
        #prof_but[select_glocal_ID]
        #select(select_glocal_ID)
    lab003 = tk.Label(exe_w,text=lang["exe"])
    exe_but = tk.Button(exe_w,text=lang["add"],command=exe_bind_list)#frame_move(10))
    
    
    teki = tk.Button(exe_w,text="適用",command=lambda:exe_bind_jsonSave(exe_w))
    teki.pack(side="bottom", anchor="se",padx=10,pady=10  )
    
    
    
    
    
    Widget_List.append(lab003)
    
    
    lab003.place(x=0,y=0)
    exe_but.place(x=80,y=0)
    
    #test1 =exe_web_bind()
    
    
    lab004 = tk.Label(brw_frame,text=lang["Browser"])
    brw_but = tk.Button(brw_frame,text=lang["add"],command=brw_bind_list)
    lab004.place(x=0,y=0)
    brw_but.place(x=80,y=0)

    brw_frame.place(x=0,y=brw_frame_y)
    Widget_List.append(lab004)
        
  else:
        print("destroy")
        exe_w.destroy()
        exe_open()
        #root.grab_release()
        brw_frame_y =40
        time.sleep(0.2)
        
            
  print("end")
        
    

def select_exe():
    exe_path
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    exe_path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    print(exe_path)
    if exe_path==None:
            print("error")
    else:
            #os.system(file_name)
# "Discord"と"Update.exe"が含まれているかどうかを判定
        contains_discord = "Discord" in exe_path
        contains_update_exe = "Update.exe" in exe_path

# 結果の表示
        print(f"Discordが含まれているか: {contains_discord}")
        print(f"Update.exeが含まれているか: {contains_update_exe}")     

        if contains_discord:
            if contains_update_exe:
                exe_path +=" --processStart Discord.exe"
    
            
        
######################################################################################################
def explorer():
    global file_name 
    print("a")
   
    if file_name ==os.getcwd():
        
        print("b",file_name)
        subprocess.Popen(['explorer',file_name], shell=True)
    else:
        y = file_name.replace("/","\\")
        x =y.rsplit("\\",1)
        
        print("c",x[0],"  ",x[1])
        subprocess.Popen(['explorer',x[0]], shell=True)

def export(Spath=None):
    global key_obj_list
    print(fdf("key_fun.py"))
    if Spath==None:
        ps =fdf("key_fun.py")
    else:
        ps = Spath
    with open(ps,"w") as f:
        f.write("""import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time

from adafruit_hid.mouse import Mouse
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
# USB HIDマウスデバイスの初期化
mouse_device = Mouse(usb_hid.devices)
kbd.release_all()
""")
        for i in range(1,21):
            push_release_list =set()
            f.write(f"def function_{i}():\n")
            for j in key_obj_list[i]:
                if j[0]=="releaseALL":
                    f.write(f" kbd.release_all()\n")
                elif j[0]=="send":
                    f.write(f" kbd.send(Keycode.{j[1]})\n")
                    
                elif j[0]=="push":
                    f.write(f" kbd.press(Keycode.{j[1]})\n")
                    push_release_list.add(f" kbd.release(Keycode.{j[1]})\n")
                elif j[0]=="sleep":
                    f.write(f" time.sleep({j[1]})\n")
                elif j[0]=="release":
                    f.write(f" kbd.release(Keycode.{j[1]})\n")
                    push_release_list.discard(f" kbd.release(Keycode.{j[1]})\n")
                elif j[0]=="VolumeUP":
                    for k in range(int(j[1])):
                        f.write(f" cc.send(ConsumerControlCode.VOLUME_INCREMENT)\n")
                elif j[0]=="VolumeDown":
                    for k in range(int(j[1])):
                        f.write(f" cc.send(ConsumerControlCode.VOLUME_DECREMENT)\n")
                elif j[0]=="PLAY_PAUSE":
                    f.write(f" cc.send(ConsumerControlCode.PLAY_PAUSE)\n")
                elif j[0]=="CC.send":
                    f.write(f" cc.send(ConsumerControlCode.{j[1]})\n")
                else:
                    print("error")
                    print(j[0])
            f.write(" pass\n")
            f.write(f"def function_{i}_R():\n")
            if not push_release_list== set():
                for o in push_release_list:
                    f.write(o)
            f.write(" pass\n")
            
        print(key_obj_list[20])


        f.write(""" 
def KFprint(id):
    return id

function_list = {}
ResetList ={}

function_list.setdefault("0",function_1)
function_list.setdefault("1",function_2)
function_list.setdefault("2",function_3)
function_list.setdefault("3",function_4)
function_list.setdefault("4",function_5)
function_list.setdefault("5",function_6)
function_list.setdefault("6",function_7)
function_list.setdefault("7",function_8)
function_list.setdefault("8",function_9)
function_list.setdefault("9",function_10)
function_list.setdefault("10",function_11)
function_list.setdefault("11",function_12)
function_list.setdefault("12",function_13)
function_list.setdefault("13",function_14)
function_list.setdefault("14",function_15)
function_list.setdefault("15",function_16)
function_list.setdefault("16",function_17)
function_list.setdefault("17",function_18)
function_list.setdefault("18",function_19)
function_list.setdefault("19",function_20)

ResetList.setdefault("0",function_1_R)
ResetList.setdefault("1",function_2_R)
ResetList.setdefault("2",function_3_R)
ResetList.setdefault("3",function_4_R)
ResetList.setdefault("4",function_5_R)
ResetList.setdefault("5",function_6_R)
ResetList.setdefault("6",function_7_R)
ResetList.setdefault("7",function_8_R)
ResetList.setdefault("8",function_9_R)
ResetList.setdefault("9",function_10_R)
ResetList.setdefault("10",function_11_R)
ResetList.setdefault("11",function_12_R)
ResetList.setdefault("12",function_13_R)
ResetList.setdefault("13",function_14_R)
ResetList.setdefault("14",function_15_R)
ResetList.setdefault("15",function_16_R)
ResetList.setdefault("16",function_17_R)
ResetList.setdefault("17",function_18_R)
ResetList.setdefault("18",function_19_R)
ResetList.setdefault("19",function_20_R)


print("function::",function_list.keys())

'''
# Test モジュール内の関数名を取得 
function_names = [name for name in dir(Test) if callable(getattr(Test, name))] # "function" という名前の関数名を抽出
function_names_with_function = [name for name in function_names if
"function" in name] print("Test.py モジュール内の function 関数一覧:") for name in
function_names_with_function: print(name)
'''
""")
        
######################################################################################################
######################################################################################################


class ColorSelectButton(tk.Button):
    def __init__(self, master,text,fb,LA):
        global colorFB
        self.fb =fb
        self.Label = LA
        super().__init__(
            master=master,
            text=text,
            width=15,
            command=self.color_change,  #クリック時に実行
            )

    def color_change(self):
        
        c = colorchooser.askcolor() #colorchooser呼び出し
        self.config(bg=c[1])        #背景を選択した色に設定
        
        ColorDump(self.fb,c[1],self.Label)
        #root.configure(foreground=ColorFG,background=ColorBG)

    def jsonload(self):
        if os.path.isfile("color.json"):
            with open(fdf("color.json"),"r") as f:
                temp =json.load(f)
                return temp[self.fb]
######################################################################################################
def style():
    styleW =tk.Toplevel()
    styleW.geometry("230x100")
    
    testLabel = tk.Label(styleW,text="Python Code Customization Tool",font=("",10))
    
    
    FG = ColorSelectButton(styleW,lang["fg"],"fg",LA=testLabel)
    BG = ColorSelectButton(styleW,lang["bg"],"bg",LA=testLabel)
    FG.pack()
    BG.pack(pady=10)
    
    
    testLabel.pack(pady=1)
    
    styleW.mainloop()
    Widget_List.append(testLabel)
    Widget_List.append(styleW)
def main():
    global lab001,lab002
    print(flag)
    if flag==0:
        lab001 =tk.Label(root,text=lang["lab001"],font=("",16))
        lab002 =tk.Label(root,text=lang["lab002"])
        
        combobox = ttk.Combobox(root,height=5,width=10,textvariable=tk_st_val01,values=lang_list,font=("",10))
        combobox.bind("<Button>",func=selectLang)
        
        lab001.pack()
        lab002.pack()
        Widget_List.append(lab001)
        Widget_List.append(lab002)
        combobox.pack()
        setup_button = tk.Button(root, text=lang["setup_button"], command=f0)
        setup_button.pack()
       
    if flag==1:
        menubar = tk.Menu(root)
        root.config(menu=menubar)

# ファイルメニューの作成と設定
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label=lang["FILE"],command=setup)
        file_menu.add_command(label=lang["SETTING"], accelerator="Alt+O",command=openfile)
        file_menu.add_command(label=lang["OPEN"],command=explorer)
        file_menu.add_command(label=lang["Save"],command=savefile1)
        file_menu.add_command(label=lang["NameSave"],command=savefile)
        file_menu.add_separator()  # 仕切り線

        file_menu.add_command(label=lang["export"],command=export)
        file_menu.add_command(label=lang["export"]+'P',command=lambda:export(filedialog.asksaveasfilename(
        title = "名前を付けて保存",
        filetypes = [("py","PY")], # ファイルフィルタ
        initialdir = os.getcwd(), # 自分自身のディレクトリ
        initialfile= "key_fun.py",
        defaultextension = "py"
        )))
        
        
        file_menu.add_separator()  # 仕切り線
        file_menu.add_command(label=lang["Finish"], command=root.destroy)  # 仮の終了コマンド

        menubar.add_cascade(label=lang["menu_file"], menu=file_menu,underline=0)

# 設定メニューの作成と設定
        setting_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=lang["setting"], menu=setting_menu)

        setting_menu.add_command(label=lang["Environmental setting"],command=lambda:print("1"))
        setting_menu.add_command(label=lang["Language settings"],command=langch)
        setting_menu.add_command(label=lang["Font color setting"],command=style)
        
        #
        
        #   json_reflesh
        
        tool_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=lang["tools"], menu=tool_menu)
        #tool_menu.add_command(label="キー操作マクロ自動設計",command=lambda:print("4"))        
        tool_menu.add_command(label=lang["Soft"],command=exe_open)

        
# menubarを親としてヘルプメニューを作成と表示
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='ヘルプ', menu=help_menu)
        
        help_menu.add_command(label="A",command=lambda:print("A"))   
        
        test_but = tk.Button(root,text="test:セーブデータ確認",command=all_dump)
        test_but.place(x=10,y=280)
        
        global frame_groove
        
        frame_groove.place(x=410,y=10)
        
        
    root.mainloop()
    print(tk_st_val01,tk_st_val01.get())


def error_window(string):
    
# GUIのセットアップ
    errorW = tk.Tk()
    errorW.geometry("200x50")
    errorW.title(f"ERROR")
    tk.Label(errorW,text=f"ERROR:{string}").pack()




      
        
        
    
    
#    code_text = tk.Text(root, wrap="none", width=40, height=10)
 #   code_text.pack()

    #save_button = tk.Button(root, text="Save", command=save_code)
    #save_button.pack()
    




def ColorDump(key,data,LLL):
        
        color_temp = {"fg":load_json("color.json","fg"),"bg":load_json("color.json","bg")}
        
        color_temp[key]=data
        
        print(color_temp["fg"],color_temp["bg"],"\n\n\n\n\n")
        with open(fdf("color.json"),"w") as f:
                json.dump(color_temp, f)
             
        LLL.configure(fg=color_temp["fg"],bg=color_temp["bg"])
        
        '''
        errors=[]
        for item in Widget_List:  # itemsは処理したいリストやイテラブルなものとして想定
            try:
            # ここにエラーが発生する可能性のある処理
                item.configure(fg=color_temp["fg"],bg=color_temp["bg"])
                
            except Exception as e:
                errors.append((item, e))
                print(item,e)
        try:
            root.configure(fg=color_temp["fg"],bg=color_temp["bg"])
        except Exception as e:
            print("ERROR:root")
       '''

def json_reflesh():
    temp ={"fg":"black", "bg":"#40E0D0"}
    print(temp)
    print("X")
    with open(fdf("color.json"),"w") as f:
        json.dump(temp,f)
#       
    os.system(SYSTEM_PATH)


def all_dump():
    print(key_obj_list)
    print("XX")
    
    errors=[]
    for item in Widget_List:  # itemsは処理したいリストやイテラブルなものとして想定
        try:
            # ここにエラーが発生する可能性のある処理
            print(item["text"])
        except Exception as e:
            errors.append((item, e))
            print(item)

    if errors:
            print(f"エラーが {len(errors)} 回発生しました:")
            
    else:
            print("エラーは発生しませんでした。")





 

if __name__ == '__main__':
    
    lang =load_json("lang.json","en")
    ColorFG = load_json("color.json","fg")
    ColorBG = load_json("color.json","bg")
    ColorFB = {"fg":ColorFG,"bg":ColorBG}
    print(ColorFG,ColorBG)
    
    if os.path.isfile("option.json"):
        with open(fdf("option.json"),"r") as f:
            temp =json.load(f)
            start =temp["start"]
    else:
        root =tk.Tk()
        root.title("error")
        if lang==0:
            er = tk.Label(root,text="lang.json not found")
        else:
            er = tk.Label(root,text=lang["option_error"])
        er.pack()
        Widget_List.append(er)
        root.mainloop()
    
        with open(fdf("option.json"),"w") as f:
            f.write('{"start" :{"flag": 0, "file": "", "language": "en"}}')
        exit(1)


# GUIのセットアップ

    
    root = tk.Tk()
    
    #ColorFG = "blue"
    #ColorBG = "white"
    try:
        root.tk_setPalette(foreground=ColorFG,background=ColorBG)
    except Exception as e:
        json_reflesh()
        exit(-1)
  #  Widget_List.append(root)
    
    root.geometry("670x330")
    root.title("Python Code Customization Tool")
    print(start)
    flag = start["flag"]
    print(flag)
    print(start)
    lang_list = ["English","Japanese"]
    frame_groove = tk.Frame(root,width=10,height=10)
    tk_st_val01 = tk.StringVar()
    file_name=os.getcwd()
    key_obj_list =[]
    for ax in range(21):
        key_obj_list.append([])

    frame_sub = tk.Frame(root, bg='black',width=10,height=10)





    if len(sys.argv)>1:
        print(sys.argv)
        
        if sys.argv[1] =="-startBind":
            HotBind_exe_list =[]
            pat =fdf("exelist.json")
            if os.path.isfile(pat):
        
                    with open(pat,"r") as f:
                        data= json.load(f)

                    if data =={}:
                        print("None")
                    else:
                        
                    
                        print("\nXX\n",data)
                        
                        for i in list(data.keys()):
                            print(data[i])
                            al,ar = data[i]
             
                            HotBind_exe_list.append(SetKey_handler_Exefile(ar,al,f"start{i}\n"))
            else:
                print("ERROR10")
                sys.exit(10)
            pat =fdf("brwlist.json")
            if os.path.isfile(pat):
        
                    with open(pat,"r") as f:
                        data= json.load(f)

                    if data =={}:
                        print("None")
                    else:
                        for i in list(data.keys()):
                            print(data[i])
                            al,ar = data[i]
             
                            HotBind_exe_list.append(SetKey_handler_Browser(ar,al,f"start{i}\n"))
            else:
                print("ERROR11")
                sys.exit(11)                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            print("start!")
            while True:
                event = keyboard.read_event()
                if event.event_type == "down":
                    if event.name == "f1":
                        break



                print("\r",event.name,end="   ")
            print("\n=======================\nend\n=======================\n")
            
            
            
            
            
            
            
            
        
    else:
        lang =load_json("lang.json",start["language"])
        main()
#x =plof()
