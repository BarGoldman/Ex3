import pygame
from pygame import *


class Menu:
    def __init__(self, welcome):
        self.welcome = welcome
        self.mid_w = self.welcome.DISPLAY_W / 2
        self.mid_h = self.welcome.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.welcome.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def bilt_screen(self):
        self.welcome.window.blit(self.welcome.display, (0, 0))
        pygame.display.update()
        self.welcome.reset_keys()


class MainMenu(Menu):
    def __init__(self, welcome):
        Menu.__init__(self, welcome)
        self.state = "Start"
        self.start_x = self.mid_w
        self.start_y = self.mid_h + 30
        self.options_x = self.mid_w
        self.options_y = self.mid_h + 50
        self.credits_x = self.mid_w
        self.credits_y = self.mid_h + 70
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.welcome.check_events()
            self.check_input()
            self.welcome.display.fill(self.welcome.BLACK)
            self.welcome.draw_text("Main Menu", 20, self.welcome.DISPLAY_W / 2, self.welcome.DISPLAY_H / 2 - 20)
            self.welcome.draw_text("Start Game", 20, self.start_x, self.start_y)
            self.welcome.draw_text("Options", 20, self.options_x, self.options_y)
            self.welcome.draw_text("Credits", 20, self.credits_x, self.credits_y)
            self.draw_cursor()
            self.bilt_screen()

    def move_cursor(self):
        if self.welcome.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"
        elif self.welcome.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.welcome.START_KEY:
            if self.state == "Start":
                self.welcome.playing = True
            elif self.state == "Options":
                self.welcome.curr_menu=self.welcome.options
            elif self.state == "Credits":
                self.welcome.curr_menu=self.welcome.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, welcome):
        Menu.__init__(self, welcome)
        self.state = "Volume"
        self.vol_x = self.mid_w
        self.vol_y = self.mid_h + 30
        self.controls_x = self.mid_w
        self.controls_y = self.mid_h + 50
        self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.welcome.check_events()
            self.check_input()
            self.welcome.display.fill((0, 0, 0))
            self.welcome.draw_text("Options", 20, self.welcome.DISPLAY_W / 2, self.welcome.DISPLAY_H / 2 - 30)
            self.welcome.draw_text("Volume", 15, self.vol_x, self.vol_y)
            self.welcome.draw_text("Controls", 15, self.controls_x, self.controls_y)
            self.draw_cursor()
            self.bilt_screen()

    def check_input(self):
        if self.welcome.BACK_KEY:
            self.welcome.curr_menu = self.welcome.main_menu
            self.run_display = False
        elif self.welcome.UP_KEY or self.welcome.DOWN_KEY:
            print("here")
            if self.state == "Volume":
                print("here1")
                self.cursor_rect.midtop = (self.controls_x+self.offset, self.controls_y)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)
                self.state = "Volume"
        elif self.welcome.START_KEY:
            pass


class CreditsMenu(Menu):
    def __init__(self, welcome):
        Menu.__init__(self, welcome)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.welcome.check_events()
            if self.welcome.START_KEY or self.welcome.BACK_KEY:
                self.welcome.curr_menu = self.welcome.main_menu
                self.run_display = False
            self.welcome.display.fill(self.welcome.BLACK)
            self.welcome.draw_text("Credits", 20, self.welcome.DISPLAY_W / 2, self.welcome.DISPLAY_H / 2 - 20)
            self.welcome.draw_text("Made by me", 15, self.welcome.DISPLAY_W / 2, self.welcome.DISPLAY_H / 2 + 10)
            self.bilt_screen()
