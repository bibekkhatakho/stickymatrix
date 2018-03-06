

#!/usr/bin/python

import tkinter
import fileinput

from PIL import Image
top = tkinter.Tk()
top.resizable(width=False, height= False)
size1 = ["imp.png","notimp.png",70,50,295,50,70,263,295,263,15,32,140,15,350,15,15,525,550,0,0,0,270,495,515]
size2 = ["imp2.png","notimp2.png",80,50,404,50,80,375,404,375,23,46,200,13,510,13,18,732,775,0,55,0,430,720,740]
size3 = ["imp3.png","notimp3.png",80,55,504,55,80,478,504,478,30,60,250,13,640,13,20,930,975,0,95,0,590,915,935]
myData = [size1,size2,size3]
sizeIndex = 0
windox=200
windowy=200

try:
    readfile = open("/home/bibek/PycharmProjects/untitled/config.txt","r")
    for line in readfile:
        brokenlines = line.split(" ")
        if brokenlines[0] == "size" and len(brokenlines) == 2 :
            if int(format(ord(brokenlines[1][0]), "x")) >30 and int(format(ord(brokenlines[1][0]), "x")) <34:
                sizeIndex = brokenlines[1][0]
        if brokenlines[0] == "x" and len(brokenlines) == 2:
            if int(brokenlines[1]) > 0:
                windox = int(brokenlines[1])
        if brokenlines[0] == "y" and len(brokenlines) == 2:
            if int(brokenlines[1]) > 0:
                windowy = int(brokenlines[1])
    readfile.close()
except:
    print("error")

if int(sizeIndex) < 1 or int(sizeIndex) > 3:
    sizeIndex = 1

sizeIndex = int(sizeIndex)


def thefun(completeData):
    global loclist
    global textList
    global current
    global windowx
    global windowy

    textList = []
    loclist = []
    current = 0

    image1 = "/home/bibek/PycharmProjects/untitled/" + completeData[0]
    image2 = "/home/bibek/PycharmProjects/untitled/" +completeData[1]
    matrix11x = int(completeData[2])
    matrix11y = int(completeData[3])
    matrix12x = int(completeData[4])
    matrix12y = int(completeData[5])
    matrix21x = int(completeData[6])
    matrix21y = int(completeData[7])
    matrix22x = int(completeData[8])
    matrix22y = int(completeData[9])
    textWidgetheight = int(completeData[10])
    textWidgetwidth = int(completeData[11])
    urgentx = int(completeData[12])
    urgenty = int(completeData[13])
    nurgentx = int(completeData[14])
    nurgenty = int(completeData[15])
    fontsize = int(completeData[16])
    rootwidth = int(completeData[17])
    rootheight = int(completeData[18])
    impx = int(completeData[19])
    impy = int(completeData[20])
    nimpx = int(completeData[21])
    nimpy = int(completeData[22])
    notey = int(completeData[23])
    tempy = int(completeData[24])

    try:
        readfile = open("/home/bibek/PycharmProjects/untitled/config.txt", "r")
        for line in readfile:
            brokenlines = line.split(" ")
            if brokenlines[0] == "x" and len(brokenlines) == 2:
                if int(brokenlines[1]) > 0:
                    windowx = int(brokenlines[1])
            if brokenlines[0] == "y" and len(brokenlines) == 2:
                if int(brokenlines[1]) > 0:
                    windowy = int(brokenlines[1])
        readfile.close()
    except:
        print("file read error")
    top.geometry('%dx%d+%d+%d' % (rootwidth, rootheight, windowx, windowy))

    global A11
    global A12
    global A21
    global A22
    global text1
    global text2
    global text3
    global text4
    global text5
    global text6
    global text7
    global label_image1
    global label_image2
    global impImage
    global notimpImage

    text1 = tkinter.Label(top, text="Urgent", font=("Helvetica", fontsize))
    text2 = tkinter.Label(top, text="Not Urgent",font=("Helvetica", fontsize))
    text1.place(x=urgentx,y=urgenty)
    text2.place(x=nurgentx,y=nurgenty)
    text3 = tkinter.Label(top, text="Urgent and important = Do it now", font=("Helvetica", 8))
    text4 = tkinter.Label(top, text="Urgent and not important = Delegate the job", font=("Helvetica", 8))
    text5 = tkinter.Label(top, text="Not urgent and important = Do not forget these", font=("Helvetica", 8))
    text6 = tkinter.Label(top, text="Not urgent and not important = Ignore them", font=("Helvetica", 8))
    text7 = tkinter.Label(top, text="Notes : ", font=("Helvetica", 8))
    text3.place(x = matrix11x,y = notey)
    text5.place(x=matrix12x,y = notey)
    text4.place(x=matrix11x, y=tempy)
    text6.place(x=matrix12x, y=tempy)
    text7.place(x = 20, y = notey)

    impImage = tkinter.PhotoImage(file=image1)
    label_image1 = tkinter.Label(top, image=impImage,height=300,width=80)
    label_image1.place(x=impx,y=impy)
    notimpImage = tkinter.PhotoImage(file=image2)
    label_image2 = tkinter.Label(top, image=notimpImage,height=200,width=80)
    label_image2.place(x=nimpx,y=nimpy)

    A11 = tkinter.Text(top, height=textWidgetheight, width=textWidgetwidth, background = "#02e0a1")
    A12 = tkinter.Text(top, height=textWidgetheight, width=textWidgetwidth, background = "#edac4b")
    A21 = tkinter.Text(top, height=textWidgetheight, width=textWidgetwidth, background = "#37b9e8")
    A22 = tkinter.Text(top, height=textWidgetheight, width=textWidgetwidth, background = "#e58679")

    textList.append(A11)
    textList.append(A12)
    textList.append(A21)
    textList.append(A22)

    loclist.append("11 ")
    loclist.append("12 ")
    loclist.append("21 ")
    loclist.append("22 ")

    A11.place(x=matrix11x, y=matrix11y)
    A12.place(x=matrix12x, y=matrix12y)
    A21.place(x=matrix21x,y=matrix21y)
    A22.place(x=matrix22x,y=matrix22y)
    try:
        readfile = open("/home/bibek/PycharmProjects/untitled/stickymatrix.txt")
        for line in readfile:
            print(line)
            splittedlines = line.split(' ')
            if splittedlines[0] == "11":
                A11.insert(tkinter.END,line[3:])
            elif splittedlines[0] == "12":
                A12.insert(tkinter.END,line[3:])
            elif splittedlines[0] == "21":
                A21.insert(tkinter.END,line[3:])
            elif splittedlines[0] == "22":
                A22.insert(tkinter.END,line[3:])
    except:
        print("no file exist")
thefun(myData[sizeIndex-1])
def key(event):
    #print( "pressed", repr(event.char))
    writefile()

def writefile():
    myfile = open("/home/bibek/PycharmProjects/untitled/stickymatrix.txt", "w")
    for counter in range(4):
        input = textList[counter].get("1.0", tkinter.END)
        b = input[:-1]
        comlpetewords = b
        separatelines = comlpetewords.split("\n")
        for i in range(len(separatelines)):
            tempString = separatelines[i]
            if len(separatelines[i]) > 0:
                count = 0
                for j in range(len(tempString)):
                    if tempString[j] != ' ' and tempString[j] != '\n':
                        count = count + 1
                if count > 0:
                    myfile.write(loclist[counter] + separatelines[i] + "\n")
    myfile.close()
def writeConfig():
    writemyfile = open("/home/bibek/PycharmProjects/untitled/config.txt","w")
    writemyfile.write("size " + str(sizeIndex)+"\n")
    writemyfile.write("x " + str(top.winfo_x())+"\n")
    writemyfile.write("y " + str(top.winfo_y())+"\n")

def callback11(event):
    A11.focus_set()
    current = 0
    #print ("clicked at", event.x, event.y)

def callback12(event):
    A12.focus_set()
    current = 1
    #print ("clicked at", event.x, event.y)

def callback21(event):
    A21.focus_set()
    current = 2
    #print ("clicked at", event.x, event.y)

def callback22(event):
    A22.focus_set()
    current = 3
    #print ("clicked at", event.x, event.y)

def increasesize(event):
    global sizeIndex
    if sizeIndex == 1 or sizeIndex == 2:
        sizeIndex = sizeIndex + 1
    delAll()
    thefun(myData[sizeIndex-1])

    writeConfig()


def decreasesize(event):
    global sizeIndex
    if sizeIndex == 2 or sizeIndex == 3:
        sizeIndex = sizeIndex - 1
    delAll()
    thefun(myData[sizeIndex - 1])

    writeConfig()

def delAll():
    A11.destroy()
    A12.destroy()
    A21.destroy()
    A22.destroy()
    label_image1.destroy()
    label_image2.destroy()
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    text7.destroy()

def onFormEvent(event):
    writeConfig()


A11.bind("<KeyRelease>", key)
A11.bind("<Button-1>", callback11)
A12.bind("<KeyRelease>", key)
A12.bind("<Button-1>", callback12)
A21.bind("<KeyRelease>", key)
A21.bind("<Button-1>", callback21)
A22.bind("<KeyRelease>", key)
A22.bind("<Button-1>", callback22)
top.bind("<Alt-Up>", increasesize)
top.bind("<Alt-Down>", decreasesize)
top.bind( '<Configure>', onFormEvent )
top.mainloop()


