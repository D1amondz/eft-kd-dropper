import pyautogui as pag
import time

#Globals
global doHumanizedMouse
global photoArray
global raidCount
global currentRaid

doHumanizedMouse = int(input('Humanize mouse movements? [1] - Yes, [2] - No'))
raidCount = int(input("How many raids to do? : "))
currentRaid = 0

    

def checkIfRaidsDone(count):
    if count == raidCount:
        print("Raids done!")
        print("Program will close in 5 seconds")
        time.sleep(5)
        exit()
    else:
        return

def humanMouse(xy):
        if doHumanizedMouse == 1:
            pag.moveTo(xy[0],xy[1],1)
            pag.click()
        else:
            pag.click(xy)
            time.sleep(1)
def checkIfOnScreen(png,confidence):
    try:
        pag.locateOnScreen(png, confidence=confidence)
    except:
        return False
    else:
        return True
def main():
    global currentRaid
    checkIfRaidsDone(currentRaid)
    global photoArray
    photoArray = ['eft.png', 'pmc.png','next.png','factory.png','ready.png','factory2.png','deploy.png','raidend.png', 'raidmenu.png','yes.png']
    count = 0
    while True:
        if checkIfOnScreen('menu.png',0.7) == True:
            while count !=10:
                if checkIfOnScreen(photoArray[count],0.7) == True:
                    if count == 5 or count == 7:
                        if count == 7 & checkIfOnScreen('raidend.png',0.7) == True:
                            print(f"Found {photoArray[count]}")
                            count = count+1
                        elif count == 5:
                            print(f"Found {photoArray[count]}")
                            count = count+1
                    elif count == 6:
                        print("Trying to find deploy.png...")
                        while True:
                            time.sleep(1)
                            try:
                                pag.locateOnScreen('deploy.png', confidence=0.7)
                            except:
                                print("Cant find deploy...")
                                continue
                            else:
                                print("Found deploy...")
                                time.sleep(9)
                                while True:
                                    if checkIfOnScreen('raidmenu.png', confidence=0.7) == True:
                                        count = count+1
                                        break
                                    pag.press('space')
                                    time.sleep(2)
                            break
                        print("Raid ended")
                        count = count+1                                    
                    else:
                        humanMouse(pag.locateCenterOnScreen(photoArray[count], confidence=0.7))
                        print(f"Found {photoArray[count]}")
                        print(count)
                        if count == 9:
                            currentRaid = currentRaid+1
                            time.sleep(3)
                            main()
                        count = count+1
                        time.sleep(0.8) 
                else:
                    if count == 1:
                        if checkIfOnScreen('pmc.png',0.7) == False:
                            print("PMC Already Selected")
                            print(count)
                            count = count+1
                        elif checkIfOnScreen('pmc.png',0.7) == True:
                            humanMouse(pag.locateCenterOnScreen('pmc.png', confidence=0.7))
                            print("PMC Not Selected, Selecting it now...")
                            print(count)
                            count = count+1
                    elif count == 3:
                        if checkIfOnScreen('factory.png',0.7) == False:
                            print("Factory Already Selected")
                            print(count)
                            count = count+1
                            
                    elif count == 5 or count == 6 or count == 7:
                        pass   
        else:
            print('Waiting for menu to be on screen...')
        time.sleep(1)
main()

