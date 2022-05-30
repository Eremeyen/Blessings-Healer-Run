from PIL import Image
import os
from os import listdir
from random import random

#attribute folders:
backgrounds = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Backgrounds"
back_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Back_Wings"
tail = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Tail"
bodies = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Bodies"
eyes = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Eye"
front_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Front_Wings"
hair = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Hair"
halo_crown = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\halo_crown"
accessories = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\accessories" #var/yok
horn = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Horn"

#final images destination
finalImages = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run\Blessings"

#defining an empty images array which we'll use to come up with each final image
images = []

background_names = {}
backW_names = {}
tail_names = {}
body_names = {}
eye_names = {}
fWing_names = {}
hair_names = {}
halo_crown_names = {}
accessory_names = {}
horn_names = {}


for i in range(len(os.listdir(r"C:\Users\meren\OneDrive\Masaüstü\Blessings Healer Run"))-2):
    images.append("")
print(len(images))



bCounter = 1

def whichBackground():
    n = random()
    if(n < 0.01):
        return "HEALER RARE BACKGROUND 1.png"
    elif(n < 0.02):
        return "HEALER RARE BACKGROUND 2.png"
    elif(n < 0.03):
        return "HEALER RARE BACKGROUND 3.png"
    elif(n < 0.04):
        return "HEALER RARE BACKGROUND 4.png"
    elif(n < 0.05):
        return "HEALER RARE BACKGROUND 5.png"
    elif(n < 0.069):
        return "HEALER GRADIENT BACKGROUND 1.png"
    elif(n < 0.088):
        return "HEALER GRADIENT BACKGROUND 2.png"
    elif(n < 0.107):
        return "HEALER GRADIENT BACKGROUND 3.png"
    elif(n < 0.126):
        return "HEALER GRADIENT BACKGROUND 4.png"
    elif(n < 0.145):
        return "HEALER GRADIENT BACKGROUND 5.png"
    elif(n < 0.164):
        return "HEALER GRADIENT BACKGROUND 6.png"
    elif(n < 0.183):
        return "HEALER GRADIENT BACKGROUND 7.png"
    elif(n < 0.202):
        return "HEALER GRADIENT BACKGROUND 8.png"
    elif(n < 0.221):
        return "HEALER GRADIENT BACKGROUND 9.png"
    elif(n < 0.24):
        return "HEALER GRADIENT BACKGROUND 10.png"
    elif(n < 0.3):
        return "HEALER 3GRADIENT BACKGROUND 4.png"
    elif(n < 0.37):
        return "HEALER COLOUR BACKGROUND 1.png"
    elif(n < 0.44):
        return "HEALER COLOUR BACKGROUND 2.png"
    elif(n < 0.51):
        return "HEALER COLOUR BACKGROUND 3.png"
    elif(n < 0.58):
        return "HEALER COLOUR BACKGROUND 4.png"
    elif(n < 0.65):
        return "HEALER COLOUR BACKGROUND 5.png"
    elif(n < 0.72):
        return "HEALER COLOUR BACKGROUND 6.png"
    elif(n < 0.79):
        return "HEALER COLOUR BACKGROUND 7.png"
    elif(n < 0.86):
        return "HEALER COLOUR BACKGROUND 8.png"
    elif(n < 0.93):
        return "HEALER COLOUR BACKGROUND 9.png"
    else:
        return "HEALER COLOUR BACKGROUND 10.png"
    
def whichBackWing():
    n = random()
    if(n < 0.2):
        return "HEALER BACK WING 1.png"
    elif(n < 0.4):
        return "HEALER BACK WING 3.png"
    elif(n < 0.6):
        return "HEALER BACK WING 6.png"
    elif(n < 0.71666666666):
        return "HEALER BACK WING 2.png"
    elif(n < 0.83333333333):
        return "HEALER BACK WING 4.png"
    elif(n < 0.95):
        return "HEALER BACK WING 7.png"
    else:
        return "HEALER BACK WING 5.png"
def whichTail():
    n = random()
    if(n < 0.266666666):
        return "HEALER TAIL 1.png"
    elif(n < 0.5333333):
        return "HEALER TAIL 2.png"
    elif(n < 0.8):
        return "HEALER TAIL 5.png"
    elif(n < 0.9):
        return "HEALER TAIL 3.png"
    else:
        return "HEALER TAIL 4.png"

def whichBody():
    n = random()
    if(n < 0.25):
        return "HEALER BODY 1.png"
    elif(n < 0.5):
        return "HEALER BODY 3.png"
    elif(n < 0.75):
        return "HEALER BODY 5.png"
    elif(n < 0.92):
        return "HEALER BODY 7.png"
    elif(n < 0.96):
        return "HEALER BODY 2.png"
    else:
        return "HEALER BODY 4.png"

def whichEye():
    n = random()
    if(n < 0.075):
        return "ASTRONAUT EYE F1.png"
    elif(n < 0.15):
        return "ASTRONAUT EYE F2.png"
    elif(n < 0.225):
        return "ASTRONAUT EYE F3.png"
    elif(n < 0.3):
        return "ASTRONAUT EYE F4.png"
    elif(n < 0.475):
        return "ASTRONAUT EYE M1.png"
    elif(n < 0.65):
        return "ASTRONAUT EYE M2.png"
    elif(n < 0.825):
        return "ASTRONAUT EYE M3.png"
    else:
        return "ASTRONAUT EYE M4.png"

def whichHaloCrown():
    n = random()
    if(n < 0.23333333):
        return "HEALER HALO 1.png"
    elif(n < 0.46666666):
        return "HEALER HALO 2.png"
    elif(n < 0.7):
        return "HEALER HALO 3.png"
    elif(n < 0.775):
        return "HEALER CROWN 1.png"
    elif(n < 0.85):
        return "HEALER CROWN 2.png"
    elif(n < 0.925):
        return "HEALER CROWN 3.png"
    else:
        return "HEALER CROWN 4.png"
    

#contains empty layer
def whichAccessory():
    n = random()
    if(n < 0.075):
        return "HEALER ACCESSORY 1.png"
    elif(n < 0.15):
        return "HEALER ACCESSORY 2.png"
    elif(n < 0.225):
        return "HEALER ACCESSORY 3.png"
    elif(n < 0.3):
        return "HEALER ACCESSORY 4.png"
    else:
        return "220329-0959-BOS LAYER.png"

def whichHorn():
    n = random()
    if(n < 0.25):
        return "HEALER HORN 1.png"
    elif(n < 0.5):
        return "HEALER HORN 2.png"
    elif(n < 0.75):
        return "HEALER HORN 3.png"
    else:
        return "HEALER HORN 4.png"




Metadata = {}

while(bCounter < 2531):
    blessing = {}
    
    wBackground = whichBackground()
    images[0] = Image.open(backgrounds + "/" + wBackground).convert("RGBA")
    blessing["Background"] = background_names[wBackground]

    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    blessing["Back Wing"] = backW_names[backW]

    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    blessing["Tail"] = tail_names[wTail]
    
    wBody = whichBody()
    images[3] = Image.open(bodies + "/" + wBody).convert("RGBA")
    blessing["Body"] = body_names[wBody]
    
    wEye = whichEye()
    images[4] = Image.open(eyes + "/" + wEye).convert("RGBA")
    blessing["Eye"] = eye_names[wEye]

    #determining which front wing to use
    fWing = "HEALER FRONT WING " + backW[-5] + ".png"
    images[5] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    blessing["Front Wing"] = fWing_names[fWing]

    #determining which hair to use
    wHair = "HEALER HAIR " + wTail[-5] + ".png"
    images[6] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    blessing["Hair"] = hair_names[wHair]

    wHaloCrown = whichHaloCrown()
    images[7] = Image.open(halo_crown + "/" + wHaloCrown).convert("RGBA")
    blessing["Halo/Crown"] = halo_crown_names[wHaloCrown]

    wAccessory = whichAccessory()
    images[8] = Image.open(accessories + "/" + wAccessory).convert("RGBA")
    blessing["Accessory"] = accessory_names[wAccessory]

    wHorn = whichHorn()
    images[9] = Image.open(horn + "/" + wHorn).convert("RGBA")
    blessing["Horn"] = horn_names[wHorn]

    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Healer " +str(bCounter)+".png")
    if(bCounter < 10):
        id = "000" + str(bCounter)
    elif(bCounter < 100):
        id = "00" + str(bCounter)
    elif(bCounter < 1000):
        id = "0" + str(bCounter)
    else:
        id = str(bCounter)
    
    Metadata[id] = blessing

    bCounter += 1

    






