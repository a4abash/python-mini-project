import win32com.client as wincom
say = wincom.Dispatch("SAPI.SpVoice")


if __name__ == '__main__':
    print("Welcome to your first Text to Voice project")
    print("To End Program Enter 0 ")
    while True:
        var = input("Enter what do you want to speak: ")
        if var == "0":
            say.Speak("Thanks for using Text to Voice project")
            break
        command = f"{var}"
        say.Speak(command)

