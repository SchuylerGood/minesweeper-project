from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

n = 5
class MyAnchorPane(AnchorLayout):
    def __init__(self, **kwargs):
        super(MyAnchorPane, self).__init__(**kwargs)
        # self.add_widget(Label(text="Hello World!"))


class MainApp(App):
    def build(self):

        layout = MyAnchorPane(anchor_x='left', anchor_y='top')
        nChanger = BoxLayout(orientation='horizontal')
        button1 = Button(text='+',
                        size_hint=(.05, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        background_color=(1, 0, 0, 1))
                        # onPress = self.changeNum(1)
        button2 = Button(text='-',
                        size_hint=(.05, .05),
                        pos_hint={'center_x': .5, 'center_y': .5},
                        background_color=(1, 0, 0, 1))
        nLabel = Label(text='n',
                        size_hint=(.05, .05),
                        pos_hint={'center_x': .5, 'center_y': .5})


        nChanger.add_widget(button1)
        nChanger.add_widget(nLabel)
        nChanger.add_widget(button2)

        layout.add_widget(nChanger)

        # Chess Board
        chess_board = GridLayout(cols=n, rows=n, size_hint=(0.4, 0.4))
        chess_board.bind(minimum_height=chess_board.setter('height'))
        chess_board.bind(minimum_width=chess_board.setter('width'))

        # Chess Board Buttons
        for i in range(n):
            for j in range(n):
                chess_board.add_widget(Button(text="(" + str(i) + "," + str(j) + ")", size_hint=(1, 1)))

        # Chess Board Anchor
        chess_board_anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        chess_board_anchor.add_widget(chess_board)
        
        chess_board_title_anchor = AnchorLayout(anchor_x='center', anchor_y='top')
        chess_board_title_anchor.add_widget(Label(text="Chess Board", size_hint=(1, 1)))

        # Chess Board Box
        chess_board_box = BoxLayout(orientation='vertical')
        chess_board_box.add_widget(chess_board_anchor)
        chess_board_box.add_widget(chess_board_title_anchor)
        chess_board_box.add_widget(layout)

        
        return chess_board_box

if __name__ == '__main__':
    MainApp().run()

