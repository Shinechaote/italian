import pyautogui
import pyperclip
import time
def createNewAnkiFlashCard(question: str, answer: str, tag: str):
    pyautogui.click(1800,228)
    pyperclip.copy(question)
    pyautogui.hotkey("ctrl", "v")
    #time.sleep(1.5)
    if( (255,155,155) == pyautogui.pixel(1800,228)):
        print("FAILED:" + question + ":  " + answer)
        pyautogui.hotkey('ctrlleft','a')
        pyautogui.press('delete')
        return
    pyautogui.press('tab')
    pyperclip.copy(answer)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('tab')
    pyautogui.write(tag)
    pyautogui.press('tab')

    pyautogui.press('enter')

def createNewAnkiFlashCards(number_of_cards = -1):
    with open('C:/Users/Christian/Desktop/Italian/new words.txt',"r", encoding="utf-8") as infile:
        line = infile.readline()
        index = 1
        english_dic = {}
        italian_dic = {}
        while (line and (number_of_cards < 0 or index < number_of_cards)):
            splitLine = line.split("\t")
            print(index)
            splitLine[1] = splitLine[1].replace("\n", "")
            if(splitLine[1] in english_dic):
                    english_dic[splitLine[1]] += "," + splitLine[0]
            else:
                english_dic[splitLine[1]] = splitLine[0]
            if(splitLine[0] in italian_dic):
                        italian_dic[splitLine[0]] += "," + splitLine[1]
            else:
                italian_dic[splitLine[0]] = splitLine[1]
            
            index += 1
            line = infile.readline()
        for key in english_dic:
            createNewAnkiFlashCard(key + " (to Italian)", english_dic[key], "ToItalian")
        for key in italian_dic:
            createNewAnkiFlashCard(key + " (to German)", italian_dic[key], "ToGerman")


createNewAnkiFlashCards()