from calendar import c
from socket import timeout
from tkinter import *
from tkinter import ttk
import serial
from PIL import Image,ImageTk
import os
import random

ArduinoUnoSerial = serial.Serial('COM1',9600) #create Serial object *REMEMBER to check the number of COM
ArduinoUnoSerial.timeout=0.5
print(ArduinoUnoSerial.readline()) #read the serial data and print it as line
print("You have new message from Arduino")

class Gui_1 :
    def __init__(self,master1) :
        self.master = master1
        def sh():
            ArduinoUnoSerial.write(str(95).encode())
        def sct():
            ArduinoUnoSerial.write(str(96).encode())
        def checkX():
            var=99
            ArduinoUnoSerial.write(str(var).encode()) #send 1 to the arduino's Data code
            print(var)
        def checkO():
            var=100
            ArduinoUnoSerial.write(str(var).encode())
            print(var)
        def Start():
            ArduinoUnoSerial.write(str(20).encode())
            print(20)

        self.name_1 = Label(self.master, text='CONTROL ROBOT CARO', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=423, y=150)
        self.name_2 = Label(self.master, text='Please Choose X or O?', font=("Times New Roman, Bold", 25),bg='#66CC00').place(x=50, y=270)
        self.name_3 = Label(self.master, text='Position', font=("Times New Roman, Bold", 25),bg='yellow').place(x=50, y=400)
        self.name_4 = Label(self.master, text='WELCOME TO TIC TAC TOE GAME', font=("Times New Roman, Bold", 40)).place(x=260, y=30)
        self.name_5 = Label(self.master, text='Mode Play', font=("Times New Roman, Bold", 25),bg='blue').place(x=50, y=540)
        self.name_7 = Label(self.master, text='Mode Auto', font=("Times New Roman, Bold", 25),bg='#33FF00').place(x=50, y=650)
        self.name_6 = Label(self.master, text='Please Press Start', font=("Times New Roman, Bold", 25),bg='Green').place(x=920, y=310)

        self.BT_1 = Button(self.master, text='X', fg='blue', bg='pink', height=1, width=3, font=("Times New Roman", 30),command=checkX).place(x=430, y=240)
        self.BT_2 = Button(self.master, text='O', fg='Red', bg='pink', height=1, width=3, font=("Times New Roman", 30),command=checkO).place(x=530, y=240)
        self.sethome = Button(self.master, text='SetHome', fg='red', bg='#F5DEB3', height=1, width=7, font=("Times New Roman, Bold", 20),command=sh).place(x=200, y=390)
        self.setcenter = Button(self.master, text='SetCenter', fg='red', bg='#F5DEB3', height=1, width=7, font=("Times New Roman, Bold", 20),command=sct).place(x=350, y=390)
        self.play3x3 = Button(self.master, text='Mode 3x3', fg='black', bg='#EFAAD1', height=1, width=10, font=("Times New Roman, Bold", 20),command=self.play33).place(x=300, y=530)
        self.play5x5 = Button(self.master, text='Mode 5x5', fg='black', bg='#FF8A83', height=1, width=10, font=("Times New Roman, Bold", 20),command=self.play55).place(x=550, y=530)
        self.play7x7 = Button(self.master, text='Mode 7x7', fg='black', bg='#9F8CBE', height=1, width=10, font=("Times New Roman, Bold", 20),command=self.play77).place(x=800, y=530)
        self.play9x9 = Button(self.master, text='Mode 9x9', fg='black', bg='#FF3030', height=1, width=10, font=("Times New Roman, Bold", 20),command=self.play99).place(x=1050, y=530)
        self.Start = Button(self.master, text='Start', fg='white', bg='Green', height=1, width=9, font=("Times New Roman, Bold", 20),command=Start).place(x=980, y=390)
        self.ModeAuto = Button(self.master, text='Mode Auto', fg='black', bg='#00CC99', height=1, width=11, font=("Times New Roman, Bold", 25)).place(x=650, y=650)

    def play33(self):
        ArduinoUnoSerial.write(str(9).encode())
        print(9)
        while True :
            try :
                root1 = Toplevel()   # Đặt Toplevel ở đây để khi 2 Listbox không có giá trị vẫn ấn About nó sẽ báo lỗi và không hiện Toplevel này lên
                root1.state('zoomed')
                root1.title('PLay 3x3')
                BackGround=PhotoImage(file = "D:\Python Workspace\RobotCaro\BackGroundScreen.png")
                L1 = Label(root1, image=BackGround)
                L1.place(x=0,y=0)

                app1 = Gui_2(root1)
                root1.grab_set()
                root1.mainloop()
            except :
                self.Error()
            break

    def play55(self):
        ArduinoUnoSerial.write(str(25).encode())
        print(25)
        while True :
            try :
                root2 = Toplevel()   # Đặt Toplevel ở đây để khi 2 Listbox không có giá trị vẫn ấn About nó sẽ báo lỗi và không hiện Toplevel này lên
                root2.state('zoomed')
                root2.title('PLay 5x5')
                BackGround=PhotoImage(file = "D:\Python Workspace\RobotCaro\BackGroundScreen.png")
                L1 = Label(root2, image=BackGround)
                L1.place(x=0,y=0)

                app1 = Gui_3(root2)
                root2.grab_set()
                root2.mainloop()
            except :
                self.Error()
            break

    def play77(self):
        ArduinoUnoSerial.write(str(49).encode())
        print(49)
        while True :
            try :
                root3 = Toplevel()   # Đặt Toplevel ở đây để khi 2 Listbox không có giá trị vẫn ấn About nó sẽ báo lỗi và không hiện Toplevel này lên
                root3.state('zoomed')
                root3.title('PLay 7x7')
                BackGround=PhotoImage(file = "D:\Python Workspace\RobotCaro\BackGroundScreen.png")
                L1 = Label(root3, image=BackGround)
                L1.place(x=0,y=0)

                app1 = Gui_4(root3)
                root3.grab_set()
                root3.mainloop()
            except :
                self.Error()
            break

    def play99(self):
        ArduinoUnoSerial.write(str(81).encode())
        print(81)
        while True :
            try :
                root4 = Toplevel()   # Đặt Toplevel ở đây để khi 2 Listbox không có giá trị vẫn ấn About nó sẽ báo lỗi và không hiện Toplevel này lên
                root4.state('zoomed')
                root4.title('PLay 9x9')
                BackGround=PhotoImage(file = "D:\Python Workspace\RobotCaro\BackGroundScreen.png")
                L1 = Label(root4, image=BackGround)
                L1.place(x=0,y=0)

                app1 = Gui_5(root4)
                root4.grab_set()
                root4.mainloop()
            except :
                self.Error()
            break
    

class Gui_2 :   #Play 3x3
    def __init__(self, master2):
        self.master = master2
        def BT1():
            ArduinoUnoSerial.write(str(11).encode())
        def BT2():
            ArduinoUnoSerial.write(str(12).encode())
        def BT3():
            ArduinoUnoSerial.write(str(13).encode())
        def BT4():
            ArduinoUnoSerial.write(str(21).encode())
        def BT5():
            ArduinoUnoSerial.write(str(22).encode())
        def BT6():
            ArduinoUnoSerial.write(str(23).encode())
        def BT7():
            ArduinoUnoSerial.write(str(31).encode())
        def BT8():
            ArduinoUnoSerial.write(str(32).encode())
        def BT9():
            ArduinoUnoSerial.write(str(33).encode())

        self.L1 = Label(self.master, text='CONTROL ROBOT CARO', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=423, y=150)
        self.L2 = Label(self.master, text='WELCOME TO TIC TAC TOE GAME', font=("Times New Roman, Bold", 40)).place(x=260, y=30)
        self.L3 = Label(self.master, text='MODE PLAY 3X3', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=530, y=250)

        self.BT_3 = Button(self.master, text='7', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT7).place(x=600, y=380)
        self.BT_4 = Button(self.master, text='8', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT8).place(x=655, y=380)
        self.BT_5 = Button(self.master, text='9', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT9).place(x=710, y=380)

        self.BT_6 = Button(self.master, text='4', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT4).place(x=600, y=435)
        self.BT_7 = Button(self.master, text='5', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT5).place(x=655, y=435)
        self.BT_8 = Button(self.master, text='6', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT6).place(x=710, y=435)

        self.BT_9 = Button(self.master, text='1', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT1).place(x=600, y=490)
        self.BT_10 = Button(self.master, text='2', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT2).place(x=655, y=490)
        self.BT_11 = Button(self.master, text='3', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT3).place(x=710, y=490)

class Gui_3 :   #Play 5x5
    def __init__(self, master3):
        self.master = master3
        def BT1():
            ArduinoUnoSerial.write(str(11).encode())
        def BT2():
            ArduinoUnoSerial.write(str(12).encode())
        def BT3():
            ArduinoUnoSerial.write(str(13).encode())
        def BT4():
            ArduinoUnoSerial.write(str(14).encode())
        def BT5():
            ArduinoUnoSerial.write(str(15).encode())
        def BT6():
            ArduinoUnoSerial.write(str(21).encode())
        def BT7():
            ArduinoUnoSerial.write(str(22).encode())
        def BT8():
            ArduinoUnoSerial.write(str(23).encode())
        def BT9():
            ArduinoUnoSerial.write(str(24).encode())
        def BT10():
            ArduinoUnoSerial.write(str(25).encode())
        def BT11():
            ArduinoUnoSerial.write(str(31).encode())
        def BT12():
            ArduinoUnoSerial.write(str(32).encode())
        def BT13():
            ArduinoUnoSerial.write(str(33).encode())
        def BT14():
            ArduinoUnoSerial.write(str(34).encode())
        def BT15():
            ArduinoUnoSerial.write(str(35).encode())
        def BT16():
            ArduinoUnoSerial.write(str(41).encode())
        def BT17():
            ArduinoUnoSerial.write(str(42).encode())
        def BT18():
            ArduinoUnoSerial.write(str(43).encode())
        def BT19():
            ArduinoUnoSerial.write(str(44).encode())
        def BT20():
            ArduinoUnoSerial.write(str(45).encode())
        def BT21():
            ArduinoUnoSerial.write(str(51).encode())
        def BT22():
            ArduinoUnoSerial.write(str(52).encode())
        def BT23():
            ArduinoUnoSerial.write(str(53).encode())
        def BT24():
            ArduinoUnoSerial.write(str(54).encode())
        def BT25():
            ArduinoUnoSerial.write(str(55).encode())

        self.L1 = Label(self.master, text='CONTROL ROBOT CARO', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=423, y=150)
        self.L2 = Label(self.master, text='WELCOME TO TIC TAC TOE GAME', font=("Times New Roman, Bold", 40)).place(x=260, y=30)
        self.L3 = Label(self.master, text='MODE PLAY 5X5', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=530, y=250)

        self.BT_1 = Button(self.master, text='1', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT1).place(x=545, y=600)
        self.BT_2 = Button(self.master, text='2', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT2).place(x=600, y=600)
        self.BT_3 = Button(self.master, text='3', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT3).place(x=655, y=600)

        self.BT_4 = Button(self.master, text='4', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT4).place(x=710, y=600)
        self.BT_5 = Button(self.master, text='5', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT5).place(x=765, y=600)
        self.BT_6 = Button(self.master, text='6', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT6).place(x=545, y=545)

        self.BT_7 = Button(self.master, text='7', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT7).place(x=600, y=545)
        self.BT_8 = Button(self.master, text='8', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT8).place(x=655, y=545)
        self.BT_9 = Button(self.master, text='9', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT9).place(x=710, y=545)

        self.BT_10 = Button(self.master, text='10', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT10).place(x=765, y=545)
        self.BT_11 = Button(self.master, text='11', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT11).place(x=545, y=490)
        self.BT_12 = Button(self.master, text='12', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT12).place(x=600, y=490)

        self.BT_13 = Button(self.master, text='13', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT13).place(x=655, y=490)
        self.BT_14 = Button(self.master, text='14', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT14).place(x=710, y=490)
        self.BT_15 = Button(self.master, text='15', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT15).place(x=765, y=490)

        self.BT_16 = Button(self.master, text='16', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT16).place(x=545, y=435)
        self.BT_17 = Button(self.master, text='17', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT17).place(x=600, y=435)
        self.BT_18 = Button(self.master, text='18', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT18).place(x=655, y=435)

        self.BT_19 = Button(self.master, text='19', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT19).place(x=710, y=435)

        self.BT_20 = Button(self.master, text='20', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT20).place(x=765, y=435)
        self.BT_21 = Button(self.master, text='21', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT21).place(x=545, y=380)
        self.BT_22 = Button(self.master, text='22', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT22).place(x=600, y=380)

        self.BT_23 = Button(self.master, text='23', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT23).place(x=655, y=380)
        self.BT_24 = Button(self.master, text='24', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT24).place(x=710, y=380)
        self.BT_25 = Button(self.master, text='25', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT25).place(x=765, y=380)

class Gui_4 :   #Play 7x7
    def __init__(self, master4):
        self.master = master4
        def BT1():
            ArduinoUnoSerial.write(str(11).encode())
        def BT2():
            ArduinoUnoSerial.write(str(12).encode())
        def BT3():
            ArduinoUnoSerial.write(str(13).encode())
        def BT4():
            ArduinoUnoSerial.write(str(14).encode())
        def BT5():
            ArduinoUnoSerial.write(str(15).encode())
        def BT6():
            ArduinoUnoSerial.write(str(16).encode())
        def BT7():
            ArduinoUnoSerial.write(str(17).encode())
        def BT8():
            ArduinoUnoSerial.write(str(21).encode())
        def BT9():
            ArduinoUnoSerial.write(str(22).encode())
        def BT10():
            ArduinoUnoSerial.write(str(23).encode())
        def BT11():
            ArduinoUnoSerial.write(str(24).encode())
        def BT12():
            ArduinoUnoSerial.write(str(25).encode())
        def BT13():
            ArduinoUnoSerial.write(str(26).encode())
        def BT14():
            ArduinoUnoSerial.write(str(27).encode())
        def BT15():
            ArduinoUnoSerial.write(str(31).encode())
        def BT16():
            ArduinoUnoSerial.write(str(32).encode())
        def BT17():
            ArduinoUnoSerial.write(str(33).encode())
        def BT18():
            ArduinoUnoSerial.write(str(34).encode())
        def BT19():
            ArduinoUnoSerial.write(str(35).encode())
        def BT20():
            ArduinoUnoSerial.write(str(36).encode())
        def BT21():
            ArduinoUnoSerial.write(str(37).encode())
        def BT22():
            ArduinoUnoSerial.write(str(41).encode())
        def BT23():
            ArduinoUnoSerial.write(str(42).encode())
        def BT24():
            ArduinoUnoSerial.write(str(43).encode())
        def BT25():
            ArduinoUnoSerial.write(str(44).encode())
        def BT26():
            ArduinoUnoSerial.write(str(45).encode())
        def BT27():
            ArduinoUnoSerial.write(str(46).encode())
        def BT28():
            ArduinoUnoSerial.write(str(47).encode())
        def BT29():
            ArduinoUnoSerial.write(str(51).encode())
        def BT30():
            ArduinoUnoSerial.write(str(52).encode())
        def BT31():
            ArduinoUnoSerial.write(str(53).encode())
        def BT32():
            ArduinoUnoSerial.write(str(54).encode())
        def BT33():
            ArduinoUnoSerial.write(str(55).encode())
        def BT34():
            ArduinoUnoSerial.write(str(56).encode())
        def BT35():
            ArduinoUnoSerial.write(str(57).encode())
        def BT36():
            ArduinoUnoSerial.write(str(61).encode())
        def BT37():
            ArduinoUnoSerial.write(str(62).encode())
        def BT38():
            ArduinoUnoSerial.write(str(63).encode())
        def BT39():
            ArduinoUnoSerial.write(str(64).encode())
        def BT40():
            ArduinoUnoSerial.write(str(65).encode())
        def BT41():
            ArduinoUnoSerial.write(str(66).encode())
        def BT42():
            ArduinoUnoSerial.write(str(67).encode())
        def BT43():
            ArduinoUnoSerial.write(str(71).encode())
        def BT44():
            ArduinoUnoSerial.write(str(72).encode())
        def BT45():
            ArduinoUnoSerial.write(str(73).encode())
        def BT46():
            ArduinoUnoSerial.write(str(74).encode())
        def BT47():
            ArduinoUnoSerial.write(str(75).encode())
        def BT48():
            ArduinoUnoSerial.write(str(76).encode())
        def BT49():
            ArduinoUnoSerial.write(str(77).encode())

        self.L1 = Label(self.master, text='CONTROL ROBOT CARO', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=423, y=125)
        self.L2 = Label(self.master, text='WELCOME TO TIC TAC TOE GAME', font=("Times New Roman, Bold", 40)).place(x=260, y=30)
        self.L3 = Label(self.master, text='MODE PLAY 7X7', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=530, y=200)
        self.BT_1 = Button(self.master, text='1', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT1).place(x=490, y=600)
        self.BT_2 = Button(self.master, text='2', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT2).place(x=545, y=600)
        self.BT_3 = Button(self.master, text='3', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT3).place(x=600, y=600)

        self.BT_4 = Button(self.master, text='4', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT4).place(x=655, y=600)
        self.BT_5 = Button(self.master, text='5', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT5).place(x=710, y=600)
        self.BT_6 = Button(self.master, text='6', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT6).place(x=765, y=600)

        self.BT_7 = Button(self.master, text='7', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT7).place(x=820, y=600)
        self.BT_8 = Button(self.master, text='8', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT8).place(x=490, y=545)
        self.BT_9 = Button(self.master, text='9', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT9).place(x=545, y=545)

        self.BT_10 = Button(self.master, text='10', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT10).place(x=600, y=545)
        self.BT_11 = Button(self.master, text='11', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT11).place(x=655, y=545)
        self.BT_12 = Button(self.master, text='12', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT12).place(x=710, y=545)

        self.BT_13 = Button(self.master, text='13', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT13).place(x=765, y=545)
        self.BT_14 = Button(self.master, text='14', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT14).place(x=820, y=545)
        self.BT_15 = Button(self.master, text='15', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT15).place(x=490, y=490)

        self.BT_16 = Button(self.master, text='16', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT16).place(x=545, y=490)
        self.BT_17 = Button(self.master, text='17', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT17).place(x=600, y=490)
        self.BT_18 = Button(self.master, text='18', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT18).place(x=655, y=490)

        self.BT_19 = Button(self.master, text='19', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT19).place(x=710, y=490)

        self.BT_20 = Button(self.master, text='20', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT20).place(x=765, y=490)
        self.BT_21 = Button(self.master, text='21', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT21).place(x=820, y=490)
        self.BT_22 = Button(self.master, text='22', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT22).place(x=490, y=435)

        self.BT_23 = Button(self.master, text='23', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT23).place(x=545, y=435)
        self.BT_24 = Button(self.master, text='24', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT24).place(x=600, y=435)
        self.BT_25 = Button(self.master, text='25', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT25).place(x=655, y=435)

        self.BT_26 = Button(self.master, text='26', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT26).place(x=710, y=435)
        self.BT_27 = Button(self.master, text='27', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT27).place(x=765, y=435)
        self.BT_28 = Button(self.master, text='28', fg='blue', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT28).place(x=820, y=435)

        self.BT_29 = Button(self.master, text='29', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT29).place(x=490, y=380)
        self.BT_30 = Button(self.master, text='30', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT30).place(x=545, y=380)
        self.BT_31 = Button(self.master, text='31', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT31).place(x=600, y=380)

        self.BT_32 = Button(self.master, text='32', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT32).place(x=655, y=380)
        self.BT_33 = Button(self.master, text='33', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT33).place(x=710, y=380)
        self.BT_34 = Button(self.master, text='34', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT34).place(x=765, y=380)

        self.BT_35 = Button(self.master, text='35', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT35).place(x=820, y=380)
        self.BT_36 = Button(self.master, text='36', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT36).place(x=490, y=325)
        self.BT_37 = Button(self.master, text='37', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT37).place(x=545, y=325)

        self.BT_38 = Button(self.master, text='38', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT38).place(x=600, y=325)
        self.BT_39 = Button(self.master, text='39', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT39).place(x=655, y=325)
        self.BT_40 = Button(self.master, text='40', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT40).place(x=710, y=325)

        self.BT_41 = Button(self.master, text='41', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT41).place(x=765, y=325)
        self.BT_42 = Button(self.master, text='42', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT42).place(x=820, y=325)
        self.BT_43 = Button(self.master, text='43', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT43).place(x=490, y=270)

        self.BT_44 = Button(self.master, text='44', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT44).place(x=545, y=270)
        self.BT_45 = Button(self.master, text='45', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT45).place(x=600, y=270)
        self.BT_46 = Button(self.master, text='46', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT46).place(x=655, y=270)
        
        self.BT_47 = Button(self.master, text='47', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT47).place(x=710, y=270)
        self.BT_48 = Button(self.master, text='48', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT48).place(x=765, y=270)
        self.BT_49 = Button(self.master, text='49', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT49).place(x=820, y=270)

class Gui_5 :   #Play 9x9
    def __init__(self, master5):
        self.master = master5
        def BT1():
            ArduinoUnoSerial.write(str(11).encode())
        def BT2():
            ArduinoUnoSerial.write(str(12).encode())
        def BT3():
            ArduinoUnoSerial.write(str(13).encode())
        def BT4():
            ArduinoUnoSerial.write(str(14).encode())
        def BT5():
            ArduinoUnoSerial.write(str(15).encode())
        def BT6():
            ArduinoUnoSerial.write(str(16).encode())
        def BT7():
            ArduinoUnoSerial.write(str(17).encode())
        def BT8():
            ArduinoUnoSerial.write(str(18).encode())
        def BT9():
            ArduinoUnoSerial.write(str(19).encode())
        def BT10():
            ArduinoUnoSerial.write(str(21).encode())
        def BT11():
            ArduinoUnoSerial.write(str(22).encode())
        def BT12():
            ArduinoUnoSerial.write(str(23).encode())
        def BT13():
            ArduinoUnoSerial.write(str(24).encode())
        def BT14():
            ArduinoUnoSerial.write(str(25).encode())
        def BT15():
            ArduinoUnoSerial.write(str(26).encode())
        def BT16():
            ArduinoUnoSerial.write(str(27).encode())
        def BT17():
            ArduinoUnoSerial.write(str(28).encode())
        def BT18():
            ArduinoUnoSerial.write(str(29).encode())
        def BT19():
            ArduinoUnoSerial.write(str(31).encode())
        def BT20():
            ArduinoUnoSerial.write(str(32).encode())
        def BT21():
            ArduinoUnoSerial.write(str(33).encode())
        def BT22():
            ArduinoUnoSerial.write(str(34).encode())
        def BT23():
            ArduinoUnoSerial.write(str(35).encode())
        def BT24():
            ArduinoUnoSerial.write(str(36).encode())
        def BT25():
            ArduinoUnoSerial.write(str(37).encode())
        def BT26():
            ArduinoUnoSerial.write(str(38).encode())
        def BT27():
            ArduinoUnoSerial.write(str(39).encode())
        def BT28():
            ArduinoUnoSerial.write(str(41).encode())
        def BT29():
            ArduinoUnoSerial.write(str(42).encode())
        def BT30():
            ArduinoUnoSerial.write(str(43).encode())
        def BT31():
            ArduinoUnoSerial.write(str(44).encode())
        def BT32():
            ArduinoUnoSerial.write(str(45).encode())
        def BT33():
            ArduinoUnoSerial.write(str(46).encode())
        def BT34():
            ArduinoUnoSerial.write(str(47).encode())
        def BT35():
            ArduinoUnoSerial.write(str(48).encode())
        def BT36():
            ArduinoUnoSerial.write(str(49).encode())
        def BT37():
            ArduinoUnoSerial.write(str(51).encode())
        def BT38():
            ArduinoUnoSerial.write(str(52).encode())
        def BT39():
            ArduinoUnoSerial.write(str(53).encode())
        def BT40():
            ArduinoUnoSerial.write(str(54).encode())
        def BT41():
            ArduinoUnoSerial.write(str(55).encode())
        def BT42():
            ArduinoUnoSerial.write(str(56).encode())
        def BT43():
            ArduinoUnoSerial.write(str(57).encode())
        def BT44():
            ArduinoUnoSerial.write(str(58).encode())
        def BT45():
            ArduinoUnoSerial.write(str(59).encode())
        def BT46():
            ArduinoUnoSerial.write(str(61).encode())
        def BT47():
            ArduinoUnoSerial.write(str(62).encode())
        def BT48():
            ArduinoUnoSerial.write(str(63).encode())
        def BT49():
            ArduinoUnoSerial.write(str(64).encode())
        def BT50():
            ArduinoUnoSerial.write(str(65).encode())
        def BT51():
            ArduinoUnoSerial.write(str(66).encode())
        def BT52():
            ArduinoUnoSerial.write(str(67).encode())
        def BT53():
            ArduinoUnoSerial.write(str(68).encode())
        def BT54():
            ArduinoUnoSerial.write(str(69).encode())
        def BT55():
            ArduinoUnoSerial.write(str(71).encode())
        def BT56():
            ArduinoUnoSerial.write(str(72).encode())
        def BT57():
            ArduinoUnoSerial.write(str(73).encode())
        def BT58():
            ArduinoUnoSerial.write(str(74).encode())
        def BT59():
            ArduinoUnoSerial.write(str(75).encode())
        def BT60():
            ArduinoUnoSerial.write(str(76).encode())
        def BT61():
            ArduinoUnoSerial.write(str(77).encode())
        def BT62():
            ArduinoUnoSerial.write(str(78).encode())
        def BT63():
            ArduinoUnoSerial.write(str(79).encode())
        def BT64():
            ArduinoUnoSerial.write(str(81).encode())
        def BT65():
            ArduinoUnoSerial.write(str(82).encode())
        def BT66():
            ArduinoUnoSerial.write(str(83).encode())
        def BT67():
            ArduinoUnoSerial.write(str(84).encode())
        def BT68():
            ArduinoUnoSerial.write(str(85).encode())
        def BT69():
            ArduinoUnoSerial.write(str(86).encode())
        def BT70():
            ArduinoUnoSerial.write(str(87).encode())
        def BT71():
            ArduinoUnoSerial.write(str(88).encode())
        def BT72():
            ArduinoUnoSerial.write(str(89).encode())
        def BT73():
            ArduinoUnoSerial.write(str(91).encode())
        def BT74():
            ArduinoUnoSerial.write(str(92).encode())
        def BT75():
            ArduinoUnoSerial.write(str(93).encode())
        def BT76():
            ArduinoUnoSerial.write(str(94).encode())
        def BT77():
            ArduinoUnoSerial.write(str(95).encode())
        def BT78():
            ArduinoUnoSerial.write(str(96).encode())
        def BT79():
            ArduinoUnoSerial.write(str(97).encode())
        def BT80():
            ArduinoUnoSerial.write(str(98).encode())
        def BT81():
            ArduinoUnoSerial.write(str(99).encode())

        self.L1 = Label(self.master, text='CONTROL ROBOT CARO', font=("Times New Roman, Bold", 35),bg='#FF8A83').place(x=423, y=115)
        self.L2 = Label(self.master, text='WELCOME TO TIC TAC TOE GAME', font=("Times New Roman, Bold", 40)).place(x=260, y=30)
        self.L3 = Label(self.master, text='MODE PLAY 9X9', font=("Times New Roman, Bold", 27),bg='#FF8A83').place(x=550, y=180)
        
        self.BT_1 = Button(self.master, text='1', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT1).place(x=435, y=680)
        self.BT_2 = Button(self.master, text='2', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT2).place(x=490, y=680)
        self.BT_3 = Button(self.master, text='3', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT3).place(x=545, y=680)

        self.BT_4 = Button(self.master, text='4', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT4).place(x=600, y=680)
        self.BT_5 = Button(self.master, text='5', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT5).place(x=655, y=680)
        self.BT_6 = Button(self.master, text='6', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT6).place(x=710, y=680)

        self.BT_7 = Button(self.master, text='7', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT7).place(x=765, y=680)
        self.BT_8 = Button(self.master, text='8', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT8).place(x=820, y=680)
        self.BT_9 = Button(self.master, text='9', fg='Green', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT9).place(x=875, y=680)

        self.BT_10 = Button(self.master, text='10', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT10).place(x=435, y=625)
        self.BT_11 = Button(self.master, text='11', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT11).place(x=490, y=625)
        self.BT_12 = Button(self.master, text='12', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT12).place(x=545, y=625)

        self.BT_13 = Button(self.master, text='13', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT13).place(x=600, y=625)
        self.BT_14 = Button(self.master, text='14', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT14).place(x=655, y=625)
        self.BT_15 = Button(self.master, text='15', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT15).place(x=710, y=625)

        self.BT_16 = Button(self.master, text='16', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT16).place(x=765, y=625)
        self.BT_17 = Button(self.master, text='17', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT17).place(x=820, y=625)
        self.BT_18 = Button(self.master, text='18', fg='Orange', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT18).place(x=875, y=625)

        self.BT_19 = Button(self.master, text='19', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT19).place(x=435, y=570)

        self.BT_20 = Button(self.master, text='20', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT20).place(x=490, y=570)
        self.BT_21 = Button(self.master, text='21', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT21).place(x=545, y=570)
        self.BT_22 = Button(self.master, text='22', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT22).place(x=600, y=570)

        self.BT_23 = Button(self.master, text='23', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT23).place(x=655, y=570)
        self.BT_24 = Button(self.master, text='24', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT24).place(x=710, y=570)
        self.BT_25 = Button(self.master, text='25', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT25).place(x=765, y=570)

        self.BT_26 = Button(self.master, text='26', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT26).place(x=820, y=570)
        self.BT_27 = Button(self.master, text='27', fg='Red', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT27).place(x=875, y=570)
        self.BT_28 = Button(self.master, text='28', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT28).place(x=435, y=515)

        self.BT_29 = Button(self.master, text='29', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT29).place(x=490, y=515)
        self.BT_30 = Button(self.master, text='30', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT30).place(x=545, y=515)
        self.BT_31 = Button(self.master, text='31', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT31).place(x=600, y=515)

        self.BT_32 = Button(self.master, text='32', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT32).place(x=655, y=515)
        self.BT_33 = Button(self.master, text='33', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT33).place(x=710, y=515)
        self.BT_34 = Button(self.master, text='34', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT34).place(x=765, y=515)

        self.BT_35 = Button(self.master, text='35', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT35).place(x=820, y=515)
        self.BT_36 = Button(self.master, text='36', fg='yellow', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT36).place(x=875, y=515)
        self.BT_37 = Button(self.master, text='37', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT37).place(x=435, y=460)

        self.BT_38 = Button(self.master, text='38', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT38).place(x=490, y=460)
        self.BT_39 = Button(self.master, text='39', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT39).place(x=545, y=460)
        self.BT_40 = Button(self.master, text='40', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT40).place(x=600, y=460)

        self.BT_41 = Button(self.master, text='41', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT41).place(x=655, y=460)
        self.BT_42 = Button(self.master, text='42', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT42).place(x=710, y=460)
        self.BT_43 = Button(self.master, text='43', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT43).place(x=765, y=460)

        self.BT_44 = Button(self.master, text='44', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT44).place(x=820, y=460)
        self.BT_45 = Button(self.master, text='45', fg='purple', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT45).place(x=875, y=460)
        self.BT_46 = Button(self.master, text='46', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT46).place(x=435, y=405)
        
        self.BT_47 = Button(self.master, text='47', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT47).place(x=490, y=405)
        self.BT_48 = Button(self.master, text='48', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT48).place(x=545, y=405)
        self.BT_49 = Button(self.master, text='49', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT49).place(x=600, y=405)
        
        self.BT_50 = Button(self.master, text='50', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT50).place(x=655, y=405)
        self.BT_51 = Button(self.master, text='51', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT51).place(x=710, y=405)
        self.BT_52 = Button(self.master, text='52', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT52).place(x=765, y=405)

        self.BT_53 = Button(self.master, text='53', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT53).place(x=820, y=405)
        self.BT_54 = Button(self.master, text='54', fg='#00FFFF', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT54).place(x=875, y=405)
        self.BT_55 = Button(self.master, text='55', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT55).place(x=435, y=350)

        self.BT_56 = Button(self.master, text='56', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT56).place(x=490, y=350)
        self.BT_57 = Button(self.master, text='57', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT57).place(x=545, y=350)
        self.BT_58 = Button(self.master, text='58', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT58).place(x=600, y=350)

        self.BT_59 = Button(self.master, text='59', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT59).place(x=655, y=350)
        self.BT_60 = Button(self.master, text='60', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT60).place(x=710, y=350)
        self.BT_61 = Button(self.master, text='61', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT61).place(x=765, y=350)

        self.BT_62 = Button(self.master, text='62', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT62).place(x=820, y=350)
        self.BT_63 = Button(self.master, text='63', fg='#FF3399', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT63).place(x=875, y=350)
        self.BT_64 = Button(self.master, text='64', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT64).place(x=435, y=295)

        self.BT_65 = Button(self.master, text='65', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT65).place(x=490, y=295)
        self.BT_66 = Button(self.master, text='66', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT66).place(x=545, y=295)
        self.BT_67 = Button(self.master, text='67', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT67).place(x=600, y=295)

        self.BT_68 = Button(self.master, text='68', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT68).place(x=655, y=295)

        self.BT_69 = Button(self.master, text='69', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT69).place(x=710, y=295)
        self.BT_70 = Button(self.master, text='70', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT70).place(x=765, y=295)
        self.BT_71 = Button(self.master, text='71', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT71).place(x=820, y=295)

        self.BT_72 = Button(self.master, text='72', fg='#FF4500', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT72).place(x=875, y=295)
        self.BT_73 = Button(self.master, text='73', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT73).place(x=435, y=240)
        self.BT_74 = Button(self.master, text='74', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT74).place(x=490, y=240)

        self.BT_75 = Button(self.master, text='75', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT75).place(x=545, y=240)
        self.BT_76 = Button(self.master, text='76', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT76).place(x=600, y=240)
        self.BT_77 = Button(self.master, text='77', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT77).place(x=655, y=240)

        self.BT_78 = Button(self.master, text='78', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT78).place(x=710, y=240)
        self.BT_79 = Button(self.master, text='79', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT79).place(x=765, y=240)
        self.BT_80 = Button(self.master, text='80', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT80).place(x=820, y=240)

        self.BT_81 = Button(self.master, text='81', fg='#8B4513', bg='white', height=1, width=3, font=("Times New Roman, Bold", 20),command=BT81).place(x=875, y=240)

def main() :
    root = Tk()
    root.title('SCARA ROBOT')
    root.state('zoomed')
    root.iconbitmap(r"D:\Python Workspace\RobotCaro\Apple.ico")
    root.resizable(False, False)

    BackGround=PhotoImage(file = "D:\Python Workspace\RobotCaro\BackGroundScreen.png")
    L1 = Label(root, image=BackGround)
    L1.place(x=0,y=0)

    app = Gui_1(root)

    root.mainloop()

if __name__ == '__main__' :
    main()