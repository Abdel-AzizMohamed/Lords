import pygame
from MainSetting import *


draw_dict = {}
inc_dict = {}
excluded_dict = {"start_state": 1, "start_list": {},
                "game_state": -1, "game_list": {}}

class UiDesgin():
    ######################## Other Functions ##############################
    def refreshText(self):
        self.rect_text = self.ren_text.get_rect(center=(0, 0))

        text_wid = self.rect_text.width
        text_hei = self.rect_text.height

        if self.text_align == "center":
            rect_pos = self.rect.width // 2 + self.rect.x, self.rect.height // 2 + self.rect.y
        if self.text_align == "left":
            rect_pos = text_wid // 2 + self.rect.x, self.rect.height // 2 + self.rect.y
        if self.text_align == "right":
            rect_pos = (text_wid // 2 + self.rect.x) + abs(text_wid - self.rect.width), self.rect.height // 2 + self.rect.y
        if self.text_align == "top":
            rect_pos = self.rect.width // 2 + self.rect.x, text_hei // 2 + self.rect.y
        if self.text_align == "bottom":
            rect_pos = self.rect.width // 2 + self.rect.x, self.rect.y + self.rect.height

        self.rect_text.center = rect_pos

    def refreshBorder(self):
        rect_pos_x = self.rect.x - self.border_width
        rect_pos_y = self.rect.y - self.border_width
        self.border_rect.x = rect_pos_x
        self.border_rect.y = rect_pos_y

    ######################## Set Functions ##############################
    def setVector(self, size, pos, grab=""):
        rect = pygame.Rect((0, 0), size)

        if grab == "":
            rect.topleft = pos
        elif grab == "bottomleft":
            rect.bottomleft = pos
        elif grab == "center":
            rect.center = pos
        elif grab == "midright":
            rect.midright = pos
        elif grab == "midleft":
            rect.midleft = pos
        elif grab == "midtop":
            rect.midtop = pos
        elif grab == "midbottom":
            rect.midbottom = pos
        elif grab == "bottomright":
            rect.bottomright = pos
        elif grab == "bottomleft":
            rect.bottomleft = pos

        return rect

    def setGeo(self, size, pos, grab="", create=True):
        if self.frame == None:
            base_x = screen_width / y_ceil
            base_y = screen_height / x_ceil
        else:
            base_x = self.frame.rect.width / x_ceil
            base_y = self.frame.rect.height / y_ceil

        if size[0] > y_ceil or size[1] > x_ceil:
            print(f"You have inerted a size bigger than {x_ceil}")
        if pos[0] > y_ceil or pos[1] > x_ceil:
            print(f"You have inerted a position bigger than {x_ceil}")

        size_x = round(size[0] * base_x)
        size_y = round(size[1] * base_y)

        if self.frame == None:
            pos_x = round(pos[0] * base_x)
            pos_y = round(pos[1] * base_y)
        else:
            pos_x = round(pos[0] * base_x) + self.frame.rect.x
            pos_y = round(pos[1] * base_y) + self.frame.rect.y

        if not create:
            return ((pos_x, pos_y), (size_x, size_y))

        rect = pygame.Rect((0, 0), (size_x, size_y))

        if grab == "":
            rect.topleft = (pos_x, pos_y)
        elif grab == "bottomleft":
            rect.bottomleft = (pos_x, pos_y)
        elif grab == "center":
            rect.center = (pos_x, pos_y)
        elif grab == "midright":
            rect.midright = (pos_x, pos_y)
        elif grab == "midleft":
            rect.midleft = (pos_x, pos_y)
        elif grab == "midtop":
            rect.midtop = (pos_x, pos_y)
        elif grab == "midbottom":
            rect.midbottom = (pos_x, pos_y)

        return rect

    def setText(self, rect):
        ren_font = sm_font.render("", False, "#000000")
        rec_font = ren_font.get_rect(center=(rect.width // 2 + rect.x, rect.height // 2 + rect.y))

        return ([ren_font, rec_font])

    ######################## Update Functions ##############################
    def updateText(self, font, text, color, align):
        self.ren_text = font.render(text, False, color)
        self.rect_text = self.ren_text.get_rect(center=(0, 0))

        text_wid = self.rect_text.width
        text_hei = self.rect_text.height

        if align == "center":
            rect_pos = self.rect.width // 2 + self.rect.x, self.rect.height // 2 + self.rect.y
        if align == "left":
            rect_pos = text_wid // 2 + self.rect.x, self.rect.height // 2 + self.rect.y
        if align == "right":
            rect_pos = (text_wid // 2 + self.rect.x) + abs(text_wid - self.rect.width), self.rect.height // 2 + self.rect.y
        if align == "top":
            rect_pos = self.rect.width // 2 + self.rect.x, text_hei // 2 + self.rect.y
        if align == "bottom":
            rect_pos = self.rect.width // 2 + self.rect.x, self.rect.y + self.rect.height

        self.rect_text.center = rect_pos

    def addMargin(self, margin_x=0, margin_y=0, obj=""):
        if obj == "text":
            self.text_margin_x += margin_x
            self.rect_text.x += margin_x
            self.text_margin_y += margin_y
            self.rect_text.y += margin_y
        else:
            if self.type == "SL":
                self.rect.x += margin_x
                self.rect.y += margin_y

                self.bar_fill_rect.x += margin_x
                self.bar_fill_rect.y += margin_y

                self.start_pos = self.bar_rect.centerx - self.bar_rect.width / 2
                self.end_pos = self.bar_rect.centerx + self.bar_rect.width / 2
            else:
                self.rect.x += margin_x
                self.rect.y += margin_y

            self.refreshText()
            if self.name[:2] == "BT":
                self.refreshBorder()

    def addPadding(self, padding_x=0, padding_y=0):
        self.rect.width += padding_x
        self.rect.height += padding_y
        self.refreshText()
        self.refreshBorder()

    def setBorder(self, border_width, border_color):
        self.border_rect.width += border_width * 2
        self.border_rect.height += border_width * 2
        self.border_rect.x -= border_width
        self.border_rect.y -= border_width
        self.border_color = border_color
