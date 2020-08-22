import os
import pyttsx3

print("Dear User ,I can provid the following services to you \n 1.Notepad \n 2.Chrome\n 3.WPS Office\n 4.wmplayer\n 5.VLC player")
pyttsx3.speak("Dear User ,I can provid the following services to you \n Notepad \n Chrome\n WPS Office\n wmplayer\n and VLC player")

while True:
        print("How can i help you:", end='')
        pyttsx3.speak("how can i help you")
        k=input()
        p=k.lower()
#I have written the code in such a way that if user ask to open two applications

        if("notepad" in p or "editer" in p ):
                if("do not " in p or "does not" in p or "donot" in p or "doesnt" in p or (r"doesn't" in p) or (r"don't" in p)):
                        print("Okay ,I will not open")
                        pyttsx3.speak("okay i will not open")
                elif("open" in p or "run" in p or "launch" in p):
                        if(("notepad" in p or "editer" in p) and ("chrome" in p or "browser" in p or "google chrome" in p)):
                                os.system("notepad")
                                os.system("chrome")
                        elif(("notepad" in p  or "editer" in p)and ("wps office" in p or "office" in p or "wpsoffice" in p)):
                                os.system("notepad")
                                os.system("ksolaunch")
                        elif(("notepad" in p or "editer" in p)and ("wmplayer" in p or "player" in p)):
                                os.system("notepad")
                                os.system("wmplayer")
                        elif(("notepad" in p or "editer" in p)and ("vlc player" in p or "vlc" in p or "player" in p)):
                                os.system("notepad")
                                os.system("vlc")
                        else:
                                os.system("notepad")
                else:
                        print("Try again")
                        pyttsx3.speak("try again")
        elif("chrome" in p or "browser" in p or "google chrome" in p):
                if("do not" in p or "does not" in p or "doesnt" in p or "dont" in p or (r"doesn't" in p) or (r"don't" in p)):
                        print("okay i will not open")
                        pyttsx3.speak("okay i will not open")
                elif("open" in p or "run" in p or "launch" in p):
                     if(("chrome" in p or "browser" in p or "google chrome" in p) and ("notepad" in p or "editer" in p)):
                             os.system("chrome")
                             os.system("notepad")
                     elif(("chrome" in p  or "browser" in p or "google chrome" in p)and ("wps office" in p or "wps" in p or "office" in p)):
                             os.system("chrome")
                             os.system("notepad")
                     elif(("chrome" in p or "browser" in p or "google chrome" in p)and ("wmplayer" in p or "player" in p)):
                             os.sytem("chrome")
                             os.sytem("wmplayer")
                     elif(("chrome" in p or "browser" in p or "google chrome" in p) and ("vlc player" in p or "vlc" in p or "player" in p)):
                             os.system("chrome")
                             os.system("vlc")
                     else:
                        os.system("chrome")
                else:
                        print("Try again")
                        pyttsx3.speak("try again")
        elif("wps" in p or "office" in p or "wps office" in p):
                if("donot" in p or "doesnot" in p or "do not" in p or "does not" in p or (r"doesn't" in p) or (r"don't" in p)):
                        print("okay i will not open")
                        pyttsx3.speak("okay i will not open")
                elif("open" in p or "run" in p or "launch" in p):
                        if(("wps office" in p or "office" in p or "wps" in p) and ("editer" in p or "notepad" in p)):
                                os.system("ksolaunch")
                                os.system("notepad")
                        elif(("wps office" in p or "office" in p or "wps" in p) and ("google chrome" in p or "browser" in p or "chrome" in p)):
                                os.system("ksolaunch")
                                os.system("chrome")
                        elif(("wps office" in p or "office" in p or "wps" in p) and ("player" in p or "wmplayer" in p)):
                                os.system("ksolaunch")
                                os.system("wmplayer")
                        elif(("wps office" in p or "office" in p or "wps" in p) and ("vlc player" in p or "vlc" in p or "player" in p)):
                                os.system("ksolaunch")
                                os.system("vlc")
                        else:
                                os.system("ksolaunch")
                else:
                        print("Try again")
        elif("wmplayer" in p or "window" in p or "media player" in p):
                if("donot" in p or "doesnot" in p or "do not" in p or "does not" in p):
                        print("okay i will not open")
                        pyttsx3.speak("okay i will not open")
                elif("open" in p or "run" in p or "launch" in p):
                        if(("wmplayer" in p or "media player" in p or "window" in p)  and ("editer" in p or "notepad" in p)):
                                os.system("wmplayer")
                                os.system("notepad")
                        elif(("wmplayer" in p or "media player" in p or "window" in p)and ("wps office" in p or "wps" in p or "office" in p)):
                                os.system("wmplayer")
                                os.system("ksolaunch")
                        elif(("wmplayer" in p or "media player" in p or "window" in p) and ("vlc player" in p or "player" in p)):
                                os.system("wmplayer")
                                os.system("vlc")
                        elif(("wmplayer" in p or "media player" in p or "window" in p)and ("chrome" in p or "google chrome" in p)):
                                os.system("wmplayer")
                                os.system("chrome")
                        else:
                                os.system("wmplayer")
                else:
                        print("Try again")
                        pyttsx3.speak("try again")
        elif("vlc" in p or "player" in p or "vlc player" in p):
                if("donot" in p or "doesnot" in p or "do not" in p or "does not" in p or (r"doesn't" in p) or (r"don't" in p)):
                        print("okay, i wil not open")
                        pyttsx3.speak("okay i will not open")
                elif("open" in p or "run" in p or "launch" in p):
                        if(("vlc" in p or "player" in p or "vlc player" in p)and ("notepad" in p or "editer" in p)):
                                os.system("vlc")
                                os.system("notepad")
                        elif(("vlc" in p or "player" in p or "vlc player" in p)and ("chrome" in p or "google chrome" in p)):
                                os.system("vlc")
                                os.system("chrome")
                        elif(("vlc" in p or "player" in p or "vlc player" in p) and ("wmplayer" in p or "media player" in p or "window" in p)):
                                os.system("vlc")
                                os.system("wmplayer")
                        elif(("vlc" in p or "player" in p or "vlc player" in p) and ("wps office" in p or "office" in p or "wps" in p)):
                                os.system("vlc")
                                os.system("ksolaunch")
                        else:
                                os.system("vlc")
                else:
                        print("try again")
                        pyttsx3.speak("try again")
        elif("close" in p or "exit" in p or "break" in p):
                break
        else:
                print("doesnot support")
                        
