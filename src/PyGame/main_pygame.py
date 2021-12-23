
from src.PyGame.Welcome import Welcome

if __name__ == '__main__':
    b = Welcome()
    while b.running:
        b.curr_menu.display_menu()
        b.game_loop()
