import board
import digitalio
import time
##a
import key_fun as KF
try:
    
    import socketpool       # TCP/IP接続用のソケット管理用
    import wifi             # WiFi接続を管理用
    import ipaddress
except Exception as e:
    print(e)
    print("無線化はできません")
from secrets import secrets

##




import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import adafruit_requests as requests

from adafruit_hid.mouse import Mouse


GP_data =[board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,  board.GP18,board.GP19,board.GP20]
#LED_PIN

button =[]

for i in GP_data:
    
    temp = digitalio.DigitalInOut(i)
    temp.direction = digitalio.Direction.INPUT
    temp.pull = digitalio.Pull.UP
    button.append(temp)
LED_PIN = digitalio.DigitalInOut(board.GP27)
LED_PIN.direction = digitalio.Direction.OUTPUT
print(LED_PIN,LED_PIN.value)
LED_PIN.value =True





ssid=secrets['ssid']
password=secrets['password']
port_num = 80               # ポート番号（標準は80）
'''
try:
# Wi-Fi接続を実行
    wifi.radio.connect(ssid, password)  # 指定したSSIDとパスワードで接続
    print(ssid,"   ",password)
    
    tt =0
    KF.kbd.press(Keycode.A)
    time.sleep(0.2)
    print("Aを送信")
    KF.kbd.release_all()   #abc 
    print(tt)


    pool = socketpool.SocketPool(wifi.radio)

    print("\033[48;2;100;50;100m##############################",end="")

    ip_to_ping = "8.8.8.8"
    print("my IP addr:", wifi.radio.ipv4_address,end=" | ")
    print("pinging ",ip_to_ping,end=" | ")
    ip1 = ipaddress.ip_address(ip_to_ping)
    print("ping:", wifi.radio.ping(ip1),end="")
    time.sleep(1)


    print("##############################")

# HTTPリクエストを作成し、HTMLファイルを取得
    url = "http://example.com"  # 取得したいHTMLファイルのURLを指定

    http = requests.Session(pool)

    response = http.get(url)

    if response.status_code == 200:
        html_content = response.text
        print(html_content)
    else:
        print("HTTPリクエストエラー：", response.status_code)

# 接続を閉じる
    response.close()
    
    
except Exception as e:
    print(e)
'''
#===========================-

'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("192.168.137.151", "5080")
sock.connect(server_address)

message = "Hello, Host!"
sock.send(message.encode())
'''



def test1():    #音量調節
   KF.cc.send(ConsumerControlCode.VOLUME_INCREMENT)
   KF.cc.send(ConsumerControlCode.VOLUME_DECREMENT )
   KF.cc.send(ConsumerControlCode.PLAY_PAUSE)
   time.sleep(0.1)
    
def test2():
# KF.kbd.send(Keycode.WINDOWS)  #
# KF.kbd.send(Keycode.A)  #press A
# KF.kbd.send(Keycode.ENTER)
 KF.mouse_device.press(Mouse.LEFT_BUTTON)
 KF.mouse_device.release(Mouse.LEFT_BUTTON)
 '''
 time.sleep(0.35)    
 KF.kbd.send(Keycode.R)  #  
 time.sleep(0.05)    
 KF.kbd.send(Keycode.R)
 '''
    
def test30():
    KF.mouse_device.press(Mouse.MIDDLE_BUTTON)

def test31():
    KF.mouse_device.release(Mouse.MIDDLE_BUTTON)

'''
def LED_TF(x):
    LED_PIN.value =True
    time.sleep(x)
    LED_PIN.value =False
    time.sleep(x)
'''

#for i in range(4):
 #   time.sleep(0.5)
  #  print("\r",i,end="")
 

print("##############################")
Flag = False
mol =0
old = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
tt =0
while True:
  #   string =""
 #    string1 =""
     time.sleep(0.001)
     LED_PIN.value = False
    # string+=str(tt)+str(LED_PIN.value)

     tt+=1
        
     if tt >1000:
        tt=0
     for i in range(20):

        if not button[i].value:
            if old[i]==False:
                KF.function_list[str(i)]()
                
                #print("XXXXXXX")
                old[i] =True
          #  string1 +=str(KF.KFprint(i))
        #    string +=" "
         #   string+="\033[48;2;50;50;250m"+str(i)
            old[i] =True
        else:
            if old[i]:
                KF.ResetList[str(i)]()
            old[i]=False
           # string1+="  "
          #  string+="\033[48;2;250;50;50m  "+str(i)
     #print(string,"\033[48;2;200;200;10m  ",string1,end="\033[49m\r")   
