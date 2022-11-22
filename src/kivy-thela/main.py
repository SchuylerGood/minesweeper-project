from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
# from kivy.properties import StringProperty
n = 8

class NChanger(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(NChanger, self).__init__(**kwargs)
        button1 = Button(text='+',
                        size_hint=(.05, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        background_color=(1, 0, 0, 1))

        button2 = Button(text='-',
                        size_hint=(.05, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        background_color=(1, 0, 0, 1))

        nLabel = Label(text='n = ' + str(n) + " (max 10 for GUI)",
                        size_hint=(.05, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},)

        button1.bind(on_press=self.increaseN)
        button2.bind(on_press=self.decreaseN)

        self.add_widget(button1)
        self.add_widget(nLabel)
        self.add_widget(button2)

    def increaseN(self, *args):
        # text = self.ids.nLabel.text
        # print(text)
        global n
        if n < 10:
            n+=1
        
    def decreaseN(self, *args):
        global n
        if n > 1:
            n -= 1
        

class MainApp(App):
    def build(self):

        # nChanger
        nChanger1 = NChanger()
        
        # Chess Board Container
        chess_board_container = BoxLayout(orientation='horizontal')

        # Chess Board container piece info
        chess_board_container_piece_info = BoxLayout(orientation='vertical')
        chess_board_container_piece_info.add_widget(Label(text="K = King"))
        chess_board_container_piece_info.add_widget(Label(text="Q = Queen"))
        chess_board_container_piece_info.add_widget(Label(text="R = Rook"))
        chess_board_container_piece_info.add_widget(Label(text="B = Bishop"))
        chess_board_container_piece_info.add_widget(Label(text="H = Horse/Knight"))

        # Chess Board
        chess_board = GridLayout(
            cols=n, 
            rows=n, 
            size_hint=(1, 1),
            padding=(0, 2)
        )
        chess_board.bind(minimum_height=chess_board.setter('height'))
        chess_board.bind(minimum_width=chess_board.setter('width'))

        # Chess Board Buttons
        for i in range(n):
            for j in range(n):
                if i == (n /2) + n % 2 and j == (n /2) + n % 2:
                    chess_board.add_widget(
                        Button(
                            text="K",
                            background_color=(0.4627450980392157, 0.5882352941176471, 0.3372549019607843, 1) if (i + j) % 2 else (0.9333333333333333, 0.9333333333333333, 0.8235294117647059, 1)
                        )
                    )
                else:
                    chess_board.add_widget(
                    Button(
                        # text="(" + str(i) + "," + str(j) + ")",
                        background_color=(0.4627450980392157, 0.5882352941176471, 0.3372549019607843, 1) if (i + j) % 2 else (0.9333333333333333, 0.9333333333333333, 0.8235294117647059, 1)
                    )
                )

        chess_board_container.add_widget(chess_board_container_piece_info)
        chess_board_container.add_widget(chess_board)
        chess_board_container.add_widget(BoxLayout())

        # Chess Board Title
        chess_board_title_anchor = AnchorLayout(anchor_x='center', anchor_y='top')
        chess_board_title_anchor.add_widget(Label(text="Chess Board", font_size=32, size_hint=(1, 1)))

        # Chess Board Anchor
        chess_board_anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        chess_board_anchor.add_widget(chess_board_container)
        
        # Chess Board nchanger
        chess_board_nChanger = AnchorLayout(anchor_x='left', anchor_y='top')

        #container
        gui_container = BoxLayout(orientation='vertical')
        gui_container.add_widget(nChanger1)
        set_button = Button(
                text="Set Board Size", 
                size_hint=(1, 1), 
                pos_hint={'center_x': .5, 'center_y': .5}, 
                background_color=(1, 0, 0, 1),
            )
        # set_button.bind(on_press=func1)
        gui_container.add_widget(set_button)

        chess_board_nChanger.add_widget(gui_container)

        

        # Chess Board Box
        chess_board_box = BoxLayout(orientation='vertical')
        chess_board_box.add_widget(chess_board_title_anchor)
        chess_board_box.add_widget(chess_board_anchor)
        chess_board_box.add_widget(chess_board_nChanger)

        
        return chess_board_box

if __name__ == '__main__':
    MainApp().run()

