import pyautogui as pg
import pyperclip
import functools

question_pos = (2042, 915)
answer_pos = (2012, 1020)
to_english_pos = (1440, 1349)
to_italian_pos = (1440, 1375)
num_to_eng = 1138
num_to_ita = 1209

def get_words_anki():
    with open("all_words.txt", "w") as outfile: 
        pg.click(to_italian_pos)
        for i in range(num_to_ita):
            pg.click(question_pos)
            pg.hotkey("ctrl","a")
            pg.hotkey("ctrl", "c")
            quest = pyperclip.paste().replace("(to Italian)", "").strip()
            pg.click(answer_pos)
            pg.hotkey("ctrl","a")
            pg.hotkey("ctrl", "c")
            ans = pyperclip.paste()
            outfile.write(ans + "\t" + quest+"\n")
            pg.press('tab')
            pg.press('tab')
            pg.press('tab')
            pg.press("down")
        pg.click(to_english_pos)
        for i in range(num_to_eng):
            pg.click(question_pos)
            pg.hotkey("ctrl","a")
            pg.hotkey("ctrl", "c")
            quest = pyperclip.paste().replace("(to English)", "").strip()
            pg.click(answer_pos)
            pg.hotkey("ctrl","a")
            pg.hotkey("ctrl", "c")
            ans = pyperclip.paste()
            outfile.write(quest + "\t" + ans+"\n")
            pg.press('tab')
            pg.press('tab')
            pg.press('tab')
            pg.press("down")

def compress_word_list():
    with open("all_words.txt", "r") as infile:
        with open("compressed_all_words.txt", "w") as outfile:
            line = infile.readline()
            english_dic = {}
            italian_dic = {}
            while line:
                splitLine = line.split("\t")
                if(len(splitLine)<2):
                    print("Splitline smaller 2")
                    break
                splitLine[0] = splitLine[0].replace(", ", ",").replace(",  ", ",").strip()
                splitLine[1] = splitLine[1].replace("\n", "").replace(", ", ",").replace(",  ", ",").strip()

                keywords = functools.reduce(lambda a, b: a +", "+b,set(splitLine[1].split(","))).strip()
                if(keywords in english_dic):
                    if(keywords not in english_dic[keywords]):
                        words = splitLine[0].split(",")
                        for word in words:
                            english_dic[keywords].append(word.strip())
                else:
                    english_dic[keywords] = []
                    words = splitLine[0].split(",")
                    for word in words:
                        english_dic[keywords].append(word.strip())

                keywords = functools.reduce(lambda a, b: a +", "+b,set(splitLine[0].split(","))).strip()
                if(keywords in italian_dic):
                    if(keywords not in italian_dic[keywords]):
                            words = splitLine[1].split(",")
                            for word in words:
                                italian_dic[keywords].append(word.strip())
                else:
                    italian_dic[keywords] = []
                    words = splitLine[1].split(",")
                    for word in words:
                        italian_dic[keywords].append(word.strip())
                line = infile.readline()
            
            word_dic_ita = {}
            for key in italian_dic:
                word_dic_ita[key] = functools.reduce(lambda a, b: a +", "+b, set(italian_dic[key]))
            italian_dic = word_dic_ita

            word_dic_eng = {}
            for key in english_dic:
                word_dic_eng[key] = functools.reduce(lambda a, b: a +", "+b, set(english_dic[key]))
            english_dic = word_dic_eng

            for key in italian_dic:
                outfile.write(key +"\t"+italian_dic[key] + "\n")
                if(italian_dic[key] in english_dic.keys()):
                    if(key != english_dic[italian_dic[key]]):
                        outfile.write(english_dic[italian_dic[key]] +"\t"+italian_dic[key] +"\n")

compress_word_list()