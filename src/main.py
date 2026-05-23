from gui.app import GUI
import platform
import os

def main():
    print("🍋‍🟩 Optilime 📸 -- Desktop image resizing for the web and gif maker with Python!")
        # Mac performance tweak: ensures the window comes to the front
    if platform.system() == "Darwin":
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    app = GUI()
    print(app)
    app.mainloop()


if __name__ == "__main__":
    main()
