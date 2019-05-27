import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.config import Config
space = ""

def func():
    print(space)
    while True:
        try:
            a = int(input("### Screen Size? : "))
            break
        except:
            print(space)
            print(">>> INVALID INPUT!")
    x = [(a * 9), (a*16)]
    Config.set('graphics', 'width', x[0])
    Config.set('graphics', 'height', x[1])

    def show_popup(x):
        show = P()
        popupWindow = Popup(title="Popup Window", content=show,
                            size_hint=(.7, .7))
        if x == "open":
            popupWindow.open()
        elif x == "close":
            popupWindow.dismiss()

    class P(FloatLayout):
        pass

    class MainScreen(Screen):
        pass

    class SecondScreen(Screen):
        pass

    class ThirdScreen(Screen):
        pass

    kv = Builder.load_file("main.kv")
    class ComplimentUI(App):
        def build(self):
            return kv
        def change_screen(self, x):
            scrnmanager = self.root.ids['sm']
            scrnmanager.current = x
        def popup(self,x,y): ##x is text, y is open or close
            if x == "":
                print(f"this is x:{x}")
                if y == "open":
                    print(f"this is y:{y}")
                    show_popup(y)
            elif y == "close":
                print(f"this is y:{y}")
                show_popup(y)
    if __name__ == "__main__":
        ComplimentUI().run()

func()
