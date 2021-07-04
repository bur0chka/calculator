from tkinter import *


calculator = Tk()
calculator.title('Калькулятор')
calculator.geometry('265x281')
textWindow = Label(calculator, text='0', width=24, height=2, font=("Times", 26))
textWindow.grid(column=0, row=0)
otvet = '0'
number = '0'
number2 = '0'

def onePrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '1'
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '1'
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '1'
        textWindow['text'] = number + '+' + number2
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '1'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '1'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '1'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '1'
        textWindow['text'] = number + '+' + number2
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '1'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '1'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 += '1'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '1'
        number2 = '0'
        textWindow['text'] = number

def twoPrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '2'
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '2'
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '2'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '2'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '2'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '2'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '2'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '2'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '2'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 = '2'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '2'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '2'
        number2 = '0'
        textWindow['text'] = number

def threePrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '3'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '3'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '3'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '3'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '3'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '3'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '3'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '3'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '3'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '3'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '3'
        number2 = '0'
        textWindow['text'] = number

def fourPrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '4'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '4'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '4'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '4'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '4'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '4'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '4'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '4'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '4'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '4'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '4'
        number2 = '0'
        textWindow['text'] = number

def fivePrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '5'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '5'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '5'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '5'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '5'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '5'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '5'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '5'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 = '5'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '5'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '5'
        number2 = '0'
        textWindow['text'] = number

def sixPrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '6'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '6'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '6'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '6'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '6'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '6'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '6'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '6'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 = '6'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '6'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '6'
        number2 = '0'
        textWindow['text'] = number

def sevenPrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '7'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] ==number:
        number += '7'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '7'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '7'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '7'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '7'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '7'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '7'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 = '7'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '7'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '7'
        number2 = '0'
        textWindow['text'] = number

def eightPrint():
    """Функция, которая печатает восемь"""
    global number
    global number2
    if textWindow['text'] == '0':
        number = '8'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '8'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '8'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '8'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '8'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '8'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '8'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '8'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '8'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 != '':
        number2 += '8'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '8'
        number2 = '0'
        textWindow['text'] = number

def ninePrint():
    global number
    global number2
    if textWindow['text'] == '0':
        number = '9'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number:
        number += '9'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 == '':
        number2 = '9'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 == '':
        number2 = '9'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 == '':
        number2 = '9'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 = '9'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '9'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '9'
        textWindow['text'] = number + '-' + number2
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '9'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 += '9'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '9'
        number2 = '0'
        textWindow['text'] = number

def zeroPrint():
    global number
    global number2
    if textWindow['text'] == '0':
        pass
    elif textWindow['text'] == number:
        number += '0'
        otvet = int(number)
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2 and number2 != '':
        number2 += '0'
        textWindow['text'] = number + '+' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '-' + number2 and number2 != '':
        number2 += '0'
        textWindow['text'] = number + '-' + number2
        otvet = int(number) - int(number2)
    elif textWindow['text'] == number + '*' + number2 and number2 != '':
        number2 += '0'
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == number + '/' + number2 and number2 == '':
        number2 += '0'
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) + int(number2) or textWindow['text'] == int(number) - int(number2) or int(number) * int(number2) or textWindow['text'] == int(number) / int(number2):
        number = '0'
        number2 = '0'
        textWindow['text'] = number

def deleteText():
    global number
    global number2
    textWindow['text'] = '0'
    number = '0'
    number2 = '0'

def plusnumber2():
    global number
    global number2
    if textWindow['text'] == number:
        number2 = ''
        textWindow['text'] = number + '+' + number2
    elif textWindow['text'] == number:
        number2 = ''
        textWindow['text'] = number + '+' + number2
        number2 = ''
    elif textWindow['text'] == int(number) + int(number2):
        textWindow['text'] = '0'

def minusNumber2():
    global number
    global number2
    if number2 == '':
        number2 = ''
    elif textWindow['text'] == number:
        number2 = ''
        textWindow['text'] = number + '-' + number2
        number2 = ''
    elif textWindow['text'] == number:
        number2 = ''
        textWindow['text'] = number + '-' + number2
        number2 = ''
    elif textWindow['text'] == int(number) - int(number2):
        textWindow['text'] = '0'

def numberMultiplication():
    global number
    global number2
    if number2 == '':
        number2 = ''
    elif textWindow['text'] == number:
        number2 = ''
        textWindow['text'] = number + '*' + number2
    elif textWindow['text'] == int(number) * int(number2):
        textWindow['text'] = '0'

def numberShare():
    global number
    global number2
    if number2 == '':
        number2 = ''
    elif textWindow['text'] == number:
        number2 = ''
        textWindow['text'] = number + '/' + number2
    elif textWindow['text'] == int(number) / int(number2):
        textWindow['text'] = '0'

def printOtvet():
    global number
    global number2
    if textWindow['text'] == number:
        textWindow['text'] = number
    elif textWindow['text'] == number2 == '':
        number2 = '0'
        textWindow['text'] = number
    elif textWindow['text'] == number + '+' + number2:
        textWindow['text'] = int(number) + int(number2)
    elif textWindow['text'] == number + '-' + number2:
        textWindow['text'] = int(number) - int(number2)
    elif textWindow['text'] == number + '*' + number2:
        textWindow['text'] = int(number) * int(number2)
    elif textWindow['text'] == number + '/' + number2:
        textWindow['text'] = int(number) / int(number2)

one = Button(calculator, text='1', width=8, height=4, command=onePrint)
one.place(x=1, y=68)
two = Button(calculator, text='2', width=8, height=4, command=twoPrint)
two.place(x=67,y=68)
three = Button(calculator, text='3', width=8, height=4, command=threePrint)
three.place(x=133,y=68)
four = Button(calculator, text='4', width=8, height=4, command=fourPrint)
four.place(x=1,y=139)
five = Button(calculator, text='5', width=8, height=4, command=fivePrint)
five.place(x=67,y=139)
six = Button(calculator, text='6', width=8, height=4, command=sixPrint)
six.place(x=133,y=139)
seven = Button(calculator, text='7', width=8, height=4, command=sevenPrint)
seven.place(x=1,y=210)
eight = Button(calculator, text='8', width=8, height=4, command=eightPrint)
eight.place(x=67,y=210)
nine = Button(calculator, text='9', width=8, height=4, command=ninePrint)
nine.place(x=133,y=210)
zero = Button(calculator, text='0', width=8, height=2, command=zeroPrint)
zero.place(x=199,y=68)
discharge = Button(calculator, text='C', width=66, command=deleteText)
discharge.place(x=199,y=109, width=66)
plus = Button(calculator, text='+', width=66, command=plusnumber2)
plus.place(x=199,y=135, width=66)
minus = Button(calculator, text='-', command=minusNumber2)
minus.place(x=199,y=161, width=66)
multiplication = Button(calculator, text='*', command=numberMultiplication)
multiplication.place(x=199,y=187, width=66)
share = Button(calculator, text='/', command=numberShare)
share.place(x=199,y=213, width=66)
equally = Button(calculator, text='=',command=printOtvet)
equally.place(x=199,y=239, width=66, height=42)


calculator.mainloop()