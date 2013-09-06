#!/usr/bin/env python

#Generates all possible pattern bricks with elements in ascii hex values, stores in new xml file

def generator(rbx="", rm="", card="", qie=""):
    out = []
    for letter in rbx:
        out.append(format(ord(letter),"x"))
    for i in str(rm):
        out.append(format(ord(str(i)),"x"))
    rm_fib = 2*(card-1) + 2 + qie/4
    for i in str(rm_fib):
        out.append(format(ord(str(i)),"x"))
    return " ".join(out)

output = open("PATTERNS_2.xml", "w")

for subdet in ["HO1M","HO1P","HO2M","HO2P"]: 
#for subdet in ["HBP", "HBM", "HEP", "HEM", "HFB", "HFM", "HO0", "HO1M", "HO2M", "HO1P", "HO2P"]:   #Select Sub-Detector Range
    for box in [2,4,6,8,10,12]:    #Select rbx Range
        box = "%02d" % box   #adds a leading 0 to single digits
        rbx = subdet+str(box)
        
        brick_begin = '<CFGBrick>\n'
        param1 = '<Parameter name="RBX" type="string">%s</Parameter>\n' % rbx
        param2 = '<Parameter name="INFOTYPE" type="string">PATTERNS</Parameter>\n'
        param3 = '<Parameter name="CREATIONTAG" type="string">pattern_test</Parameter>\n'
        param4 = '<Parameter name="CREATIONSTAMP" type="string">13-08-13</Parameter>\n'
        output.writelines(brick_begin + param1 + param2 + param3 + param4)
        
        for rm in range(1, 5):
            for card in range(1,4):
                for qie in (0,4):
                    if subdet in ["HO1M", "HO2M", "HO1P", "HO2P"]:
                        brick = '<Data elements="10" encoding="hex" rm="%s" card="%s" qie="%s">%s 0</Data>\n' %(rm, card, qie, generator(rbx, rm, card, qie))
                        output.writelines(brick)
                    else:
                        brick = '<Data elements="10" encoding="hex" rm="%s" card="%s" qie="%s">%s 0 0</Data>\n' %(rm, card, qie, generator(rbx, rm, card, qie))
                        output.writelines(brick)

        brick_end = '</CFGBrick>\n\n'
        output.writelines(brick_end)
                
output.close()