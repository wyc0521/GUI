import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Ellipse, Rectangle, RoundedRectangle, Line

from kivy.config import Config
# Config.set('graphics', 'width', '100')
# Config.set('graphics', 'height', '100')
# Config.write()

Window.clearcolor = (51 / 255, 51 / 255, 51 / 255, 1)
#Window.size = (800,600)


'''
class Login(BoxLayout, Widget):
    IPAddress = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

        self.IPLabel =  Label(text='IP Address:')
        self.IPAddress = TextInput(multiline=False)
        self.add_widget(self.IPLabel)
        self.add_widget(self.IPAddress)

        self.connectButton = Button(text='Connect',
                             font_size = 20,
                             background_color=(98/255,91/255,87/255,1),
                             size_hint=(None, None),
                             width=100,
                             height=50,
                             pos_hint={'x': .4, 'y': .4}
                             )

        self.connectButton.bind(on_press = self.connect)
        self.add_widget(self.connectButton)


    def connect(self):
        print('IP Address:', self.IPAddress.text)
        self.IPAddress.text = ''
'''

class MuteButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MuteButton, self).__init__(**kwargs)
        self.source = 'MuteBtnOffStatusBlack.png'
    def on_press(self):
        self.source = 'MuteBtnOnStatusBlack.png'
    def on_release(self):
        self.source = 'MuteBtnOffStatusBlack.png'
    pass


class nextPageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(nextPageButton, self).__init__(**kwargs)
        self.source = 'nextPushPageBtnOff.png'
    #def on_press(self):
        #self.source = 'MuteBtnOnStatusBlack.png'
    #def on_release(self):
        #self.source = 'MuteBtnOffStatusBlack.png'
    pass



class previousPageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(previousPageButton, self).__init__(**kwargs)
        self.source = 'previousPushPageBtnOff.png'
    #def on_press(self):
        #self.source = 'MuteBtnOnStatusBlack.png'
    #def on_release(self):
        #self.source = 'MuteBtnOffStatusBlack.png'
    pass

#class Infozeige()


class StopButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(StopButton, self).__init__(**kwargs)
        self.source = 'stopBtnOff.png'

        # with self.canvas.before:
        #     Color(30/255,30/255,30/255,1)
        #     self.rect = RoundedRectangle(pos=(60, 369), size=(85, 85), radius=[50])
        # with self.canvas.after:
        #     Color(70 / 255, 70 / 255, 70 / 255, 1)
        #     Line(circle=[103, 411, min(88, 88) / 2],width=0.5)
        #     Line(circle=[103, 411.5, min(70, 70) / 2], width=1.4)


    def on_press(self):
        self.source = 'stopBtnOn.png'
        # with self.canvas.before:
        #     Color(27 / 255, 190 / 255, 54 / 255, 1)
        #     self.rect = RoundedRectangle(pos=(90.5, 370), size=(85, 85), radius=[50])

    def on_release(self):
        self.source = 'stopBtnOff.png'
        # with self.canvas.before:
        #     Color(115/255,115/255,115/255,1)
        #     self.rect = RoundedRectangle(pos=(90.5, 370), size=(85, 85), radius=[50])

    # def zustand(self, n):
    #     if n == 0:
    #         with self.canvas.before:
    #             Color(27 / 255, 190 / 255, 54 / 255, 1)
    #             self.rect = RoundedRectangle(pos=(90.5, 479.5), size=(85,85),radius=[50])
    #
    #     if n == 1:
    #         with self.canvas.before:
    #             Color(27 / 255, 190 / 255, 54 / 255, 1)
    #             self.rect = RoundedRectangle(pos=(90.5, 479.5), size=(85,85),radius=[50])
    #
    #     if n == 2:
    #         with self.canvas.before:
    #             Color(27 / 255, 190 / 255, 54 / 255, 1)
    #             self.rect = RoundedRectangle(pos=(90.5, 479.5), size=(85,85),radius=[50])
    pass


i = 9

class PresetButton(GridLayout, object):
    #global PresetNumber
    def __init__(self, **kwargs):
        super(PresetButton, self).__init__(**kwargs)
        #with self.canvas.before:
            # Color(115 / 255, 115 / 255, 115 / 255, 1)
            # self.rect = RoundedRectangle(pos=(90.5, 479.5), size=(85,85),radius=[50])
        #zustand = StopButton()
        #zustand.zustand(n=1)

        for n in range(1,i+1):
            self.btn_preset = Button(
                                text='Preset '+ str(n),
                                background_normal='generalButtonPicOff.png',
                                background_down='generalButtonPicOn.png',
                                #on_press = self.pressed,
                                #on_prese = self.zustand,
                                size_hint=(None, None),
                                size=(160, 48),
                                )
            # with self.canvas.before:
            #      Color(115/255,115/255,115/255,1)
            #      self.rect = RoundedRectangle(pos=self.pos, size=self.size) #radius=[50]
            self.add_widget(self.btn_preset)
            #self.btn_preset.bind(on_press=self.zustand)

        #self.show_current_preset = Label(text = 'Preset 10')
        #self.add_widget(self.show_current_preset)



    # def pressed(self, instance):
    #     self.PresetNumber = instance.text
    #     self.show_current_preset.text = self.PresetNumber
    #     #print(self.PresetNumber)


    def zustand(self,n):
        n = 2
        if n == 0:
            with self.canvas.before:
                Color(27 / 255, 190 / 255, 54 / 255, 1)
                self.rect = RoundedRectangle(pos=(90.8, 479.9), size=(85,85),radius=[50])

        if n == 1:
            with self.canvas.before:
                Color(27 / 255, 190 / 255, 54 / 255, 1)
                self.rect = RoundedRectangle(pos=(90.5, 479.5), size=(85,85),radius=[50])

        if n == 2:
            with self.canvas.before:
                Color(90 / 255, 19 / 255, 54 / 255, 1)
                self.rect = RoundedRectangle(pos=(90.5, 479.5), size=(85,85),radius=[50])

    pass

# class Display(BoxLayout):
#     def __init__(self, **kwargs):
#         super(Display, self).__init__(**kwargs)
#         self.show_IP_Address = Label(text = '192.168.1.1')
#
#         #self.add_widget(self.show_current_preset)
#         self.add_widget(self.show_IP_Address)


# class VolumeSlider(BoxLayout):
#     def __init__(self, **kwargs):
#         super(VolumeSlider, self).__init__(**kwargs)
#         self.show_volume_label = Label(text ='0')
#         self.slider = Slider(min=0,
#                              max=100,
#                              #value=25,
#                              orientation='vertical'
#                              )
#         self.add_widget(self.slider)
#         self.add_widget(self.show_volume_label)
#         self.slider.bind(value=self.show_volume)
#
#
#
#
#     def show_volume(self, *args):
#         self.show_volume_label.text = str(int(args[1]))


class VolumeButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(VolumeButton, self).__init__(**kwargs)
        self.source = 'volumeBtn.png'
    def on_press(self):
        self.source = 'volumeBtnDown.png'
    def on_release(self):
        self.source = 'volumeBtn.png'
    pass



class MainWindow(Screen):
    pass

class SecondWindow(Screen):

    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Layout.kv')

class MyMainApp(App):
    IPAddress = ObjectProperty(None)

    def build(self):
        return kv

    def get_IP(self):
        print('IP Address:', self.root.ids.first_screen.ids.IPAddress.text)


    # def process(self):
    #     text = self.root.ids.first_screen.ids.IPAddress.text
    #     print(text)


if __name__ == "__main__":
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '480')
    #Config.write()
    MyMainApp().run()
