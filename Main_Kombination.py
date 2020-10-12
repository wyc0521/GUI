from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.clock import Clock
from time import sleep
import iosono_inside_remote_commands
import socket
import time
import re


Window.clearcolor = (51 / 255, 51 / 255, 51 / 255, 1)




class MuteButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MuteButton, self).__init__(**kwargs)
        self.source = 'MuteBtnOffStatusBlack.png'
    def on_press(self):
        self.source = 'MuteBtnOnStatusBlack.png'
    def on_release(self):
        self.source = 'MuteBtnOffStatusBlack.png'
    pass


# class nextPageButton(ButtonBehavior, Image):
#     def __init__(self, **kwargs):
#         super(nextPageButton, self).__init__(**kwargs)
#         self.source = 'nextPushPageBtnOff.png'
#     #def on_press(self):
#         #self.source = 'MuteBtnOnStatusBlack.png'
#     #def on_release(self):
#         #self.source = 'MuteBtnOffStatusBlack.png'
#     pass
#
#
#
# class previousPageButton(ButtonBehavior, Image):
#     def __init__(self, **kwargs):
#         super(previousPageButton, self).__init__(**kwargs)
#         self.source = 'previousPushPageBtnOff.png'
#     #def on_press(self):
#         #self.source = 'MuteBtnOnStatusBlack.png'
#     #def on_release(self):
#         #self.source = 'MuteBtnOffStatusBlack.png'
#     pass

class StopButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(StopButton, self).__init__(**kwargs)
        self.source = 'stopBtnOff.png'
    def on_press(self):
        self.source = 'stopBtnOn.png'
    def on_release(self):
        self.source = 'stopBtnOff.png'
    pass

class VolumeButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(VolumeButton, self).__init__(**kwargs)
        self.source = 'volumeBtn.png'
    def on_press(self):
        self.source = 'volumeBtnDown.png'
    def on_release(self):
        self.source = 'volumeBtn.png'
    pass


class PresetButton(GridLayout, object):

    def __init__(self, **kwargs):
        super(PresetButton, self).__init__(**kwargs)
        i = 9
        for n in range(1, i + 1):
            self.btn_preset = Button(
                text='Preset ' + str(n),
                background_normal='generalButtonPicOff.png',
                background_down='generalButtonPicOn.png',
                # on_press = self.pressed,
                # on_prese = self.zustand,
                size_hint=(None, None),
                size=(160, 48),
            )
            # with self.canvas.before:
            #      Color(115/255,115/255,115/255,1)
            #      self.rect = RoundedRectangle(pos=self.pos, size=self.size) #radius=[50]
            self.add_widget(self.btn_preset)

    def updatePresetButton(self, List):

        n = len(List)
        Anzahl = n
        #n = re.sub("\D", "", n)
        print(Anzahl)
        Anzahl = int(Anzahl)+1

        '''
        self.preset = GridLayout()
        self.preset.cols = 3
        self.preset.rows = 3
        self.preset.padding = 40
        self.preset.spacing = 35
        '''
        for i in range(int(Anzahl)):
            self.btn_preset = Button(
                text='Preset' + str(i),
                background_normal='generalButtonPicOff.png',
                background_down='generalButtonPicOn.png',
                # on_press = self.pressed,
                # on_prese = self.zustand,
                size_hint=(None, None),
                size=(160, 48),
            )
            self.add_widget(self.btn_preset)
            

    # def pressed(self, instance):
    #     self.PresetNumber = instance.text
    #     self.show_current_preset.text = self.PresetNumber
    #     #print(self.PresetNumber)


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class IOSONOApp(App):
    ResultFromIP = ObjectProperty(None)
    HOST = ObjectProperty(None)
    #Zustand_Color = ListProperty([None, None, None, None])

    def set_IP(self):
        global HOST, PORT, ResultFromIP
        HOST = '192.168.178.34'
        #self.root.ids.first_screen.ids.IPAddress.text
        PORT = 4444
        iosono_inside_remote_commands.setHost(HOST)
        iosono_inside_remote_commands.setPort(PORT)

        self.ResultFromIP = iosono_inside_remote_commands.ping()


        Clock.schedule_interval(self.get_all, 2)

    def get_all(self, dt=0):

        self.Result = iosono_inside_remote_commands.ping()
        print(self.Result)
        
        if self.Result is True:

            #self.List = iosono_inside_remote_commands.getPresetList()
            self.currentPreset = iosono_inside_remote_commands.getCurrentPreset()
            print(self.currentPreset)
            self.root.ids.second_screen.ids.show_current_preset.text = str(self.currentPreset)
            
            self.currentVolume = iosono_inside_remote_commands.getVolume()
            print(self.currentVolume)
            self.root.ids.second_screen.ids.show_current_volume.text = str(self.currentVolume)


            self.state = iosono_inside_remote_commands.getState(self.currentPreset)
            print(self.state)


            '''
            if self.state is 'green':
                self.Zustand_Color = (0/255,255/255,0/255,1)
                self.root.ids.second_screen.ids.SB.canvas.get_group('a').rgba = self.Zustand_Color

            elif self.state is 'red':
                self.self.Zustand_Color = (255/255,0/255,0/255,1)
                self.root.ids.second_screen.ids.first.ids.second.ids.SB.canvas.get_group('a').rgba = self.Zustand_Color
                print(Zustand_Color)

            elif self.state is 'yellow':
                self.Zustand_Color = (255/255,255/255,0/255,1)
                self.root.ids.second_screen.ids.first.ids.second.ids.SB.canvas.get_group('a').rgba = self.Zustand_Color
                print(Zustand_Color)

            elif self.state is 'black':
                self.Zustand_Color = (30/255,30/255,30/255,1)
                self.root.ids.second_screen.ids.first.ids.second.ids.SB.canvas.get_group('a').rgba = self.Zustand_Color
                print(Zustand_Color)
                '''
                

            # print(List)
            # print(currentPreset)
            
            #clock = PresetButton()
            #Clock.schedule_interval(clock.PresetButton.updatePresetButton, 2)

    def PopupWindow(self):
        popupWindow = Popup(title='Error',
                            content=Label(text='can not connect to the given IP Address'),
                            size_hint=(None, None),
                            size=(400, 400))
        popupWindow.open()


    def timeout(self):
        Clock.schedule_once(IOSONOApp.PopupWindow, 1)


    def build(self):
        kv = Builder.load_file('Main_Kombination.kv')
        return kv

if __name__ == "__main__":
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '480')
    #Config.write()
    IOSONOApp().run()
