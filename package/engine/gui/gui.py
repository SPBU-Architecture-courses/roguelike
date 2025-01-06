import sys
from package.engine.gui.gameWindow import GameWindow

class GUI:
    @staticmethod
    def create_window():
        try:
            game_window = GameWindow()
            game_window.run()
            print("GUI: Окно закрыто")
        except Exception as e:
            print(f"GUI: Ошибка при создании окна: {e}")
            sys.exit()