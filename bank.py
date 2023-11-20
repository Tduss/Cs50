def greeting():
    text = input("text: ")
    lowerStrip = text.lower().strip()
    if lowerStrip.startswith("hello"):
        print("$0")
    elif lowerStrip.startswith("h"):
        print("$20")
    else:
        print("$100")

greeting()cd figlet
