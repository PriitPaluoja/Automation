import pyperclip

new = pyperclip.paste
old = new

# Write clipboard changes to file
with open("clipboard_listener.txt", "a", encoding="UTF-8") as out:
    while True:
        if new == "EXIT_":
            break

        if old == new:
            new = pyperclip.paste()
        else:
            old = new
            print(new)
            out.write(new + "\n")
