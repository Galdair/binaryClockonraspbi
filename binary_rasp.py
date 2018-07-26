import RPi.GPIO as GPIO #PI GPIO module
import time


 
 
def decimaltobinary(decimal): 
    '''converts to variable length array,of ones and zeros'''
    binary_list = []
    while decimal is not 0:
        binary_list.append(decimal % 2)
        decimal = decimal // 2
    binary_list.reverse()
    return binary_list
 
 
 
# print(decimaltobinary(10))
# print(decimaltobinary(11))
# print(decimaltobinary(59))
# print(decimaltobinary(46))
 
 



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)#BOARD LAYOUT ,its important

pinlist = [26,12,16,18,22,24] #Currently used board pins found here https://pinout.xyz/pinout/pin18_gpio24
for i in pinlist:
    GPIO.setup(i,GPIO.OUT,initial=GPIO.LOW) #setting everything to zero
while True:
    current_time = time.localtime() #getting current time
    #print(decimaltobinary(current_time.tm_sec))
    current_sec = decimaltobinary(current_time.tm_sec) #converting to binary 
    zero_list = [] 
    for k in range(0,6-len(current_sec)): #making a zero filled padding list,to be able to iterate trough all the pins with the 1,0 setting`
        zero_list.append(0)
    end_list = zero_list +current_sec #this is the correct way to append a zero padding and the variable length seconds array
    print(end_list)
    for i in range(0,6): #iterating thruogh pinlist and end list
        if end_list[i] == 0: #this is the off setting
            GPIO.output(pinlist[i],GPIO.LOW)
        if end_list[i] == 1:
            GPIO.output(pinlist[i],GPIO.HIGH) #this is the on setting
    time.sleep(1) #this is a second timer