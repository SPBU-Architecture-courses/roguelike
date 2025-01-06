from package.engine.gui.gui import GUI

def main():
    try:
        print("Main: Init Starting")
        GUI.create_window()
        print("Main: Init Started")
    except Exception as e:
        print("Main: Произошла ошибка при инициализации GUI")
        print(e)

if __name__ == "__main__":
    main()