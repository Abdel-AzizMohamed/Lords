import pygame
from MainSetting import *

npc_dict = {}

class Dialogue():
    def __init__(self, text):
        self.text = text
        self.current_chat = 1
        self.chat_replay = 0
        self.max_chat = len(self.text) // 2

        self.current_text = 0

    def displayChat(self, chat_ui):
        text_len = len(self.text[f"chat{self.current_chat}"])
        replay_len = len(self.text[f"chat{self.current_chat}_replay"])
        if (self.current_text >=  text_len or (self.current_text >= replay_len and self.chat_replay == 1)):
            self.current_text = 0
            self.chat_replay = 1
            return -1

        if self.chat_replay == 1:
            chat_sp = self.text[f"chat{self.current_chat}_replay"][self.current_text].split(" ")
        else:
            chat_sp = self.text[f"chat{self.current_chat}"][self.current_text].split(" ")

        for i in range(1, 4):
            chat_ui["chatDailog"][f"text{i}"].updateText(sm_mid_font, "", "#FFFFFF", "left")

        current_length = 0
        chat_str = ""
        ui_index = 1
        ui = chat_ui["chatDailog"]["text1"]

        for word in chat_sp:
            current_length += len(word + " ")

            if (current_length > 55):
                ui.updateText(sm_mid_font, chat_str, "#FFFFFF", "left")
                ui.addMargin(10, 10, "text")
                ui_index += 1
                ui = chat_ui["chatDailog"][f"text{ui_index}"]
                chat_str = ""
                current_length = 0

            chat_str += word + " "

        ui.updateText(sm_mid_font, chat_str, "#FFFFFF", "left")
        ui.addMargin(10, 10, "text")

        return 1

def readChatData(data):
    for key, item in data.items():
        dia_item = Dialogue(item["text"])
        npc_dict.update({key: dia_item})

def checkNpc(npc, chat_ui):
    if npc:
        return npc_dict[npc].displayChat(chat_ui)
    return 0
