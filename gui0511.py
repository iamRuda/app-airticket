from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast

from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarIconListItem, ThreeLineAvatarIconListItem
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_string("""
<CustomListItem>
    # отступ текста от левого края
    _txt_left_pad: "80dp"

    # какую иконку ставить в элементе, выбор производится в программе
    IconLeftWidget:
        icon: root.icon

<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        icon_left: root.icon

<ClickableTextFieldPasswordRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True

<LoginScreen>:
    name: 'login'

            
    MDBoxLayout:
        
        
        adaptive_height: True
        orientation: "vertical"
        pos: 0,root.height-(root.height*0.65)-45
 
                 
        MDBoxLayout:
            adaptive_height: True
            md_bg_color: app.theme_cls.primary_color
            MDLabel:
                halign: "center"
                font_style: "H5"
                theme_text_color: "Primary"
                text: "Авиалинии РУТ(МИИТ)"
            
        ClickableTextFieldRound:
            id: textfield_login
            size_hint_x: None
            icon: "account"
            width: "300dp"
            hint_text: "Логин"
            pos_hint: {"center_x": .5}
        
        ClickableTextFieldPasswordRound:
            id: textfield_password
            size_hint_x: None
            width: "300dp"
            hint_text: "Пароль"
            pos_hint: {"center_x": .5}
        
        MDBoxLayout:
            padding: ["0dp", "20dp", "0dp", "0dp"]
            spacing: "100dp"
            adaptive_size: True
            pos_hint: {'center_x': .5, 'center_y': .5}  
            MDFlatButton:
                text: "Регистрация"
                theme_text_color: "Custom"
                on_press: root.manager.screens[0].switchTest()
            MDRaisedButton:
                text: "Войти"
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.screens[0].switchOffer()
                    
<TestScreen>:
    name: 'test'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            id: workspace
            
            MDLabel:
                halign: "center"
                font_style: "H5"
                theme_text_color: "Primary"
                text: "Nothing active"
                
        MDBoxLayout:
            id: textfield
            adaptive_height: True
            padding: 20, 10
            MDTextField:
                adaptive_size: True
                hint_text: "Введите команду"

                
        MDBoxLayout:
            MDGridLayout:
                spacing: 10, 10
                padding: 10, 10
                cols: 3 
                
                Button:
                    text: "Информация обо мне"
                    background_color: app.theme_cls.primary_color
                Button:
                    text: "Мои билеты"
                    background_color: app.theme_cls.primary_color
                Button:
                    text: "Мои настройки"
                    background_color: app.theme_cls.primary_color
                    
                Button:
                    text: "Поиск билета"
                    background_color: app.theme_cls.primary_color
                Button:
                    text: "Посчитать выручку"
                    background_color: app.theme_cls.primary_color
                Button:
                    text: "Выполнить команду"
                    background_color: app.theme_cls.primary_color                

<Check@MDCheckbox>
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)           

<ClickableTextFieldDateRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True

    MDIconButton:
        icon: "calendar"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release: pass

<OfferScreen>
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Авиалинии РУТ(МИИТ)"
            # use_overflow: True
            elevation: 10
            anchor_title: "left"
            # в switch theme можно увидеть, как обратится к функции в python коде
            right_action_items:
                [
                ["theme-light-dark", lambda x: app.switchTheme(x), "Сменить тему", "Switch theme"],
                ["cog", lambda x: x, "Настройки", "Settings"],
                ]
        
        MDBoxLayout:
            adaptive_height: True
            spacing: dp(20)
            padding: ["20dp", "0dp", "20dp", "0dp"]
            
            MDTextField:
                id: search_from_field
                hint_text: 'Откуда'
                on_text: root.set_list_md_icons(self.text, True)
                
            MDTextField:
                id: search_in_field
                hint_text: 'Куда'
                on_text: root.set_list_md_icons(self.text, True)
                
        MDBoxLayout:
            adaptive_height: True
            spacing: dp(20)
            padding: ["20dp", "0dp", "20dp", "0dp"]
            
            ClickableTextFieldDateRound:
                id: date_field
                height: "30dp"
                hint_text: 'Когда(в формате дд.мм.гг)'
                on_text: root.set_list_md_icons(self.text, True)
                
            MDBoxLayout:
                Check:
                    active: True
                    pos_hint: {'center_x': .4, 'center_y': .5}
                
                MDLabel:
                    text: "Эконом"
                
                Check:
                    pos_hint: {'center_x': .6, 'center_y': .5}
                    
                MDLabel:
                    text: "Комфорт"
                
                Check:
                    pos_hint: {'center_x': .6, 'center_y': .5}
                    
                MDLabel:
                    text: "Бизнес"

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(84)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'

<SettingsScreen>:
    name: 'settings'

    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<MyAviabiletScreen>:
    name: 'myAviabilet'

    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

answer = {'status': 'enter'}

class User():
    login, password = '', ''
    id, email, userNane, beneficiary, benefit, benefitDate = '', '', '', '', '', ''


class ClickableTextFieldRound(MDRelativeLayout):
    icon = StringProperty()
    text = StringProperty()
    hint_text = StringProperty()

class ClickableTextFieldPasswordRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class ClickableTextFieldDateRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class CustomListItem(ThreeLineAvatarIconListItem):  # Создание собственного особого элемента
    icon = StringProperty()

# Declare screens
class LoginScreen(Screen):
    global answer
    def checkAccount(self):
        self.login = self.ids.textfield_login.text
        self.password = self.ids.textfield_login.text
        if (answer.get('status') == 'enter'):
            return True
        else:
            toast('Ошибка в логине или пароле. Проверьте корректность.')
            return False

    def switchOffer(self):
        if self.checkAccount() == True:
            self.parent.screens[2].set_list()
            self.parent.current = 'offer'

    def switchTest(self):
        if self.checkAccount() == True:
            self.parent.current = 'test'

class TestScreen(Screen):
    pass

class OfferScreen(Screen):
    bd = {'elem0': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class': "Эконом"},
          'elem1': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class': "Комфорт"},
          'elem2': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class': "Бизнес"}}
    def set_list(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_elem(elem):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomListItem",
                    "icon": 'airplane',
                    "text": self.bd[elem]['from'] + '  -  ' + self.bd[elem]['in'],
                    "secondary_text": self.bd[elem]['time_from'] + '  -  ' + self.bd[elem]['time_in'],
                    "tertiary_text": self.bd[elem]['class'],
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        for elem in self.bd.keys():
            if search:
                if text in elem:
                    add_elem(elem)
            else:
                add_elem(elem)


class SettingsScreen(Screen):
    pass


class MyAviabiletScreen(Screen):
    pass


class TestApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(OfferScreen(name='offer'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(MyAviabiletScreen(name='myAviabilet'))

        return sm


if __name__ == '__main__':
    TestApp().run()