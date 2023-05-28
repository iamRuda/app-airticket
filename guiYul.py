from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.toast import toast

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem, OneLineAvatarIconListItem, ThreeLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.relativelayout import MDRelativeLayout

from kivy.config import Config

import time

from kivymd.uix.selectioncontrol import MDCheckbox

Builder.load_string("""
<CustomListItem>
    # отступ текста от левого края
    _txt_left_pad: "80dp"

    # какую иконку ставить в элементе, выбор производится в программе
    IconLeftWidgetWithoutTouch:
        icon: root.icon

<CustomOfferListItem>
    # отступ текста от левого края
    _txt_left_pad: "80dp"

    # какую иконку ставить в элементе, выбор производится в программе
    IconLeftWidgetWithoutTouch:
        icon: root.icon

<CustomListItemWithCheckbox>:
    _txt_left_pad: "80dp"

    IconLeftWidgetWithoutTouch:
        icon: root.icon

    RightCheckbox:

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
        icon_left: root.icon

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
                opposite_colors: True
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
            icon: "key"
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
                on_press: root.manager.screens[0].switchRegister()
            MDRaisedButton:
                text: "Войти"
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.screens[0].switchOffer()

<RegisterScreen>:
    name: 'login'

    MDBoxLayout:
        adaptive_height: True
        orientation: "vertical"
        pos: 0,root.height-(root.height*0.65)-45

        ClickableTextFieldRound:
            id: textfield_login
            size_hint_x: None
            icon: "email"
            width: "300dp"
            hint_text: "Электронная почта"
            pos_hint: {"center_x": .5}

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
            icon: "key"
            hint_text: "Пароль"
            pos_hint: {"center_x": .5}

        ClickableTextFieldPasswordRound:
            id: textfield_password
            size_hint_x: None
            icon: "key-change"
            width: "300dp"
            hint_text: "Повторить пароль"
            pos_hint: {"center_x": .5}

        MDBoxLayout:
            padding: ["0dp", "20dp", "0dp", "0dp"]
            spacing: "100dp"
            adaptive_size: True
            pos_hint: {'center_x': .5, 'center_y': .5}  
            MDFlatButton:
                text: "Тестовый экран"
                theme_text_color: "Custom"
                on_press: root.manager.screens[6].switchTest()
            MDRaisedButton:
                text: "Зарегистрироваться"
                md_bg_color: app.theme_cls.primary_color
                on_press: root.manager.screens[6].switchOffer()

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

    MDIconButton:
        icon: "calendar"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_press:
            app.show_date_picker()

<OfferScreen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            id: "topbar"
            title: "Авиалинии РУТ(МИИТ)"
            # use_overflow: True
            elevation: 10
            anchor_title: "left"
            # в switch theme можно увидеть, как обратится к функции в python коде
            right_action_items:
                [
                ["account", lambda x: app.switch_myaccount('offer'), "Мой аккаунт", "My account"],
                ["ticket-confirmation", lambda x: app.switch_myticket('offer'), "Мои билеты", "My tickets"],
                ["cog", lambda x: app.switch_settings('offer'), "Настройки", "Settings"],
                ]

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(20)
            padding: ["20dp", "0dp", "20dp", "0dp"]

            MDTextField:
                id: search_from_field
                hint_text: 'Откуда'
                on_text: root.set_list(text_from=self.text, search=True)

            MDTextField:
                id: search_in_field
                hint_text: 'Куда'
                on_text: root.set_list(text_in=self.text, search=True)

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(20)
            padding: ["20dp", "0dp", "20dp", "0dp"]

            ClickableTextFieldDateRound:
                id: date_field
                height: "30dp"
                hint_text: 'Когда(в формате гггг/мм/дд)'
                on_text: root.set_list(text_date=self.text, search=True)

            MDBoxLayout:              
                MDCheckbox:
                    id: checkbox_econom
                    active: True
                    pos_hint: {'center_x': .4, 'center_y': .5}
                    on_release: root.set_list(search=True)

                MDLabel:
                    text: "Эконом"

                MDCheckbox:
                    id: checkbox_comfort
                    active: True
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_release: root.set_list(search=True)

                MDLabel:
                    text: "Комфорт"

                MDCheckbox:
                    id: checkbox_business
                    active: True
                    pos_hint: {'center_x': .6, 'center_y': .5}
                    on_release: root.set_list(search=True)

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
    MDBoxLayout:
        orientation: "vertical"

        # верхнее меню
        MDBoxLayout:
            id: box
            orientation: "vertical"
            spacing: "12dp"
            pos_hint: {"top": 1}
            adaptive_height: True
            bg_hint_color: app.theme_cls.primary_light

            MDTopAppBar:
                id: toolbar
                anchor_title: "center"
                type_height: "small"
                elevation: 10
                title: "Настройки"
                left_action_items: [["arrow-left", lambda x: app.backScreen(root.manager.screens[3].screen)]]
                right_action_items: 
                    [
                    # ["sync", lambda x: root.manager.screens[3].switchIcon()],
                    ]

        # место для списка элементов
        RecycleView:
            id: rvaccount
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: ['10dp', '0dp', '10dp', '0dp']
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'

<MyAccountScreen>:
    MDBoxLayout:
        orientation: "vertical"

        # верхнее меню
        MDBoxLayout:
            id: box
            orientation: "vertical"
            spacing: "12dp"
            pos_hint: {"top": 1}
            adaptive_height: True
            bg_hint_color: app.theme_cls.primary_light

            MDTopAppBar:
                id: toolbar
                anchor_title: "center"
                type_height: "small"
                elevation: 10
                title: "Мой аккаунт"
                left_action_items: [["arrow-left", lambda x: app.backScreen(root.manager.screens[4].screen)]]
                right_action_items: 
                    [
                    # ["sync", lambda x: root.manager.screens[3].switchIcon()],
                    ]

        # место для списка элементов
        RecycleView:
            id: rvaccount
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: ['10dp', '0dp', '10dp', '0dp']
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'

<MyTicketScreen>:
    name: 'myticket'

    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: toolbar
            anchor_title: "center"
            type_height: "small"
            elevation: 10
            title: "Настройки"
            left_action_items: [["arrow-left", lambda x: app.backScreen(root.manager.screens[5].screen)]]
            right_action_items: 
                [
                # ["sync", lambda x: root.manager.screens[3].switchIcon()],
                ]
        
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

<ContentNewAccount>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "330dp"

    MDBoxLayout:           
        MDLabel:
            text: "Тип аккаунта: "

        Check:
            id: check_user
            active: True
            pos_hint: {'center_x': .4, 'center_y': .5}

        MDLabel:
            text: "Юзер"

        Check:
            id: check_cashier
            pos_hint: {'center_x': .4, 'center_y': .5}

        MDLabel:
            text: "Кассир"

        Check:
            id: check_admin
            pos_hint: {'center_x': .5, 'center_y': .5}

        MDLabel:
            text: "Админ"

    ClickableTextFieldRound:
        id: textfield_login
        size_hint_x: None
        icon: "email"
        width: root.width
        hint_text: "Электронная почта"

    ClickableTextFieldRound:
        id: textfield_login
        size_hint_x: None
        icon: "account"
        width: root.width
        hint_text: "Логин"

    ClickableTextFieldRound:
        id: textfield_login
        size_hint_x: None
        icon: "key"
        width: root.width
        hint_text: "Пароль"

    ClickableTextFieldRound:
        id: textfield_login
        size_hint_x: None
        icon: "key-change"
        width: root.width
        hint_text: "Повторить пароль"

<ContentDelAccount>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "130dp"

    ClickableTextFieldRound:
        id: textfield_login
        size_hint_x: None
        icon: "login"
        width: root.width
        hint_text: "Логин"

    ClickableTextFieldRound:
        id: textfield_login
        size_hint_x: None
        icon: "alert"
        width: root.width
        hint_text: "Причина удаления"

<AdminScreen>
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Панель администрирования"
            # use_overflow: True
            elevation: 10
            anchor_title: "left"
            # в switch theme можно увидеть, как обратится к функции в python коде
            right_action_items:
                [
                ["account", lambda x: app.switch_myaccount('admin'), "Мой аккаунт", "My account"],
                ["ticket-confirmation", lambda x: app.switch_myticket('offer'), "Мои билеты", "My tickets"],
                ["cog", lambda x: app.switch_settings('admin'), "Настройки", "Settings"],
                ]

        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            spacing: dp(20)
            padding: ["20dp", "20dp", "20dp", "0dp"]

            MDRaisedButton:
                text: "Просмотр база данных рейсов"
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .5}
                width: root.width*0.8

            MDRaisedButton:
                text: "Создание нового аккаунта"
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .5}
                width: root.width*0.8
                on_press: root.manager.screens[7].new_account_dialog()

            MDRaisedButton:
                text: "Удаление существующего аккаунта"
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {"center_x": .5}
                width: root.width*0.8
                on_press: root.manager.screens[7].del_account_dialog()

        RecycleView:
            key_size: 'height'

""")

answer = {'status': 'enter'}


class User():
    login, password = 'firstclient', '12345678'
    info = {'ID': ['53526262', 'identifier'], 'Логин': ['firstclient', 'login'],
            'Электронная почта': ['rudfireman@gmail.com', 'email'],
            'ФИО': ['Рудченко Андрей Сергеевич', 'account'], 'Дата регистрации': ['2022/06/11', 'calendar-account'],
            'Количество милей': ['1200', 'airplane']}


class ClickableTextFieldRound(MDRelativeLayout):
    icon = StringProperty()
    text = StringProperty()
    hint_text = StringProperty()


class ClickableTextFieldPasswordRound(MDRelativeLayout):
    icon = StringProperty()
    text = StringProperty()
    hint_text = StringProperty()


class ClickableTextFieldDateRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class CustomListItem(OneLineIconListItem):
    icon = StringProperty()


class CustomOfferListItem(ThreeLineAvatarIconListItem):
    icon = StringProperty()


class CustomListItemWithCheckbox(OneLineAvatarIconListItem):
    icon = StringProperty()


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class ContentNewAccount(MDBoxLayout):
    pass


class ContentDelAccount(MDBoxLayout):
    pass

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

    def switchRegister(self):
        if self.checkAccount() == True:
            self.parent.transition.direction = 'up'
            self.parent.current = 'register'

class RegisterScreen(Screen):
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
            self.parent.transition.direction = 'left'
            self.parent.current = 'admin'

    def switchTest(self):
        if self.checkAccount() == True:
            self.parent.transition.direction = 'left'
            self.parent.current = 'test'

class TestScreen(Screen):
    pass

class OfferScreen(Screen):

    bd = {'elem0': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class_ticket': "Эконом"},
          'elem1': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class_ticket': "Комфорт"},
          'elem2': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class_ticket': "Бизнес"},
          'elem3': {'from': 'Москва', 'in': 'Сочи', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class_ticket': "Комфорт"},
          'elem4': {'from': 'Москва', 'in': 'Сочи', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30', 'class_ticket': "Бизнес"}}

    def set_list(self, text_from="", text_in="", text_date="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_elem(elem):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOfferListItem",
                    "icon": 'airplane',
                    "text": self.bd[elem]['from'] + '  -  ' + self.bd[elem]['in'],
                    "secondary_text": self.bd[elem]['time_from'] + '  -  ' + self.bd[elem]['time_in'],
                    "tertiary_text": self.bd[elem]['class_ticket'],
                    "on_press": lambda *args: self.new_dialog(elem),
                }
            )

        self.ids.rv.data = []
        for elem in self.bd.keys():
            if search:
                if text_from in self.bd[elem]['from']:
                    if text_in in self.bd[elem]['in']:
                        if (self.ids.checkbox_econom.active == True) and (self.bd[elem]['class_ticket'] == "Эконом"):
                            add_elem(elem)
                        elif (self.ids.checkbox_comfort.active == True) and (self.bd[elem]['class_ticket'] == "Комфорт"):
                            add_elem(elem)
                        elif (self.ids.checkbox_business.active == True) and (self.bd[elem]['class_ticket'] == "Бизнес"):
                            add_elem(elem)
            else:
                add_elem(elem)



    dialog = None
    def new_dialog(self, elem):
        if not self.dialog:
            self.dialog = MDDialog(

            title="Билет на рейс",
            text = "Город вылета: "+ self.bd[elem]['from'] + " — "+"Город прибытия: "  +self.bd[elem]['in']+
                    "\nВылет в " + self.bd[elem]['time_from'] +" — "+ "Посадка в " + self.bd[elem]['time_in'] +
                   "\nАэрофлот (aeroflot)" +
                    "\nУровень: " + self.bd[elem]['class_ticket'] + "     Цена:  16990р",

            pos_hint={"center_x": .5, "center_y": .5},

            buttons=[
                MDFlatButton(
                    text="Отмена",
                    theme_text_color="Custom",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="Купить билет",
                    theme_text_color="Custom",
                    md_bg_color=(0.12941176470588237, 0.5882352941176471, 0.9529411764705882, 1.0),
                    text_color=(1,1,1,1),
                    on_release=self.on_buy
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        self.dialog = None

    def on_buy(self, *args):
        self.close_dialog()

class SettingsScreen(Screen):
    data_settings = {'switch_theme': {'viewclass': 'CustomListItemWithCheckbox', 'text': 'Включить темную тему', 'text_color': 'black', 'icon': 'theme-light-dark', 'command': 'print(end="")'},
                     'quit_account': {'viewclass': 'CustomListItem', 'text': 'Выйти из аккаунта', 'text_color': 'black', 'icon': 'account-arrow-left', 'command': 'print(end="")'},
                     'del_account': {'viewclass': 'CustomListItem', 'text': 'Удалить аккаунт', 'text_color': 'red', 'icon': 'account-remove', 'command': 'print(end="")'},
                     'change_account': {'viewclass': 'CustomListItem', 'text': 'Смеминть логин или пароль', 'text_color': 'black', 'icon': 'account-key', 'command': 'print(end="")'},
                     'connection': {'viewclass': 'CustomListItem', 'text': 'Связаться с нами', 'text_color': 'black', 'icon': 'human-greeting-proximity', 'command': 'self.new_dialog(elem)'}}

    screen=''
    def set_back_screen(self, screen):
        self.screen = screen

    def set_list(self):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_elem(elem):
            self.ids.rvaccount.data.append(
                {
                    "viewclass": self.data_settings[elem]['viewclass'],
                    "icon": self.data_settings[elem]['icon'],
                    "text": self.data_settings[elem]['text'],
                    "text_color": self.data_settings[elem]['text_color'],
                    "on_press": lambda *args: eval(self.data_settings[elem]['command']),
                }
            )

        self.ids.rvaccount.data = []
        for elem in self.data_settings.keys():
            add_elem(elem)

    dialog = None
    def new_dialog(self, elem, *args):
        if not self.dialog:
            self.dialog = MDDialog(

            title=self.data_settings[elem]['text'],
            text = "",
            pos_hint={"center_x": .5, "center_y": .5},
            buttons=[
                MDFlatButton(
                    text="Понятно",
                    theme_text_color="Custom",
                    on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        self.dialog = None

class MyAccountScreen(Screen):
    screen=''
    def set_back_screen(self, screen):
        self.screen = screen

    def set_list(self):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_elem(elem):
            self.ids.rvaccount.data.append(
                {
                    "viewclass": "CustomListItem",
                    "icon": User.info[elem][1],
                    "text": elem + ': ' + User.info[elem][0],
                    "callback": lambda x: x,
                }
            )

        self.ids.rvaccount.data = []
        for elem in User.info.keys():
            add_elem(elem)

class MyTicketScreen(Screen):
    bd = {
        'elem0': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30',
                  'class_ticket': "Эконом"},
        'elem1': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30',
                  'class_ticket': "Комфорт"},
        'elem2': {'from': 'Москва', 'in': 'Владивосток', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30',
                  'class_ticket': "Бизнес"},
        'elem3': {'from': 'Москва', 'in': 'Сочи', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30',
                  'class_ticket': "Комфорт"},
        'elem4': {'from': 'Москва', 'in': 'Сочи', 'time_from': '20.11.2022 19:50', 'time_in': '21.11.2022 2:30',
                  'class_ticket': "Бизнес"}}

    screen = ''

    def set_back_screen(self, screen):
        self.screen = screen

    def set_list(self):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_elem(elem):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOfferListItem",
                    "icon": 'airplane',
                    "text": self.bd[elem]['from'] + '  -  ' + self.bd[elem]['in'],
                    "secondary_text": self.bd[elem]['time_from'] + '  -  ' + self.bd[elem]['time_in'],
                    "tertiary_text": self.bd[elem]['class_ticket'],
                    "on_press": lambda *args: self.new_dialog(elem),
                }
            )

        self.ids.rv.data = []
        for elem in self.bd.keys():
            add_elem(elem)

    dialog = None
    def new_dialog(self, elem):
        if not self.dialog:
            self.dialog = MDDialog(

                title="Ваш билет на самолёт",
                text="Город вылета: " + self.bd[elem]['from'] + " — " + "Город прибытия: " + self.bd[elem]['in'] +
                     "\nВылет в " + self.bd[elem]['time_from'] + " — " + "Посадка в " + self.bd[elem]['time_in'] +  "\nАэрофлот (aeroflot)" +
                     "\nУровень: " + self.bd[elem]['class_ticket'] ,

                pos_hint={"center_x": .5, "center_y": .5},

                buttons=[

                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="Вернуть",
                        theme_text_color='Custom',
                        md_bg_color=(0.7, 0.1, 0.7, 1),
                        text_color=(1, 1, 1, 1),
                        on_release=self.on_return
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        self.dialog = None

    def on_return(self, *args):
        self.close_dialog()


class AdminScreen(Screen):
    dialog = None

    def new_account_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Создание нового аккаунта",
                type="custom",
                content_cls=ContentNewAccount(),
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=self.close_dialog,
                    ),
                    MDRaisedButton(
                        text="Создать",
                        theme_text_color="Custom",
                        on_release=self.on_create,
                    ),
                ],
            )
        self.dialog.open()

    def del_account_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Удаление существующего аккаунта",
                type="custom",
                content_cls=ContentDelAccount(),
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        theme_text_color="Custom",
                        on_release=self.close_dialog,
                    ),
                    MDRaisedButton(
                        text="Удалить",
                        theme_text_color="Custom",
                        md_bg_color=(1, 0.1, 0.1, 1),
                        on_release=self.on_delete,
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        self.dialog = None

    def on_create(self, *args):
        self.close_dialog()

    def on_delete(self, *args):
        self.close_dialog()


class TestApp(MDApp):
    def backScreen(self, screen):
        self.root.transition.direction = 'right'
        self.root.current = screen

    def switch_myaccount(self, screen):
        self.root.transition.direction = 'left'
        self.root.screens[4].set_back_screen(screen)
        self.root.screens[4].set_list()
        self.root.current = 'myaccount'

    def switch_myticket(self, screen):
        self.root.transition.direction = 'left'
        self.root.screens[5].set_back_screen(screen)
        self.root.screens[5].set_list()
        self.root.current = 'myticket'

    def switch_settings(self, screen):
        self.root.transition.direction = 'left'
        self.root.screens[3].set_back_screen(screen)
        self.root.screens[3].set_list()
        self.root.current = 'settings'

    def build(self):
        Config.set('graphics', 'width', '900')
        Config.set('graphics', 'height', '700')
        Config.write()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(TestScreen(name='test'))
        sm.add_widget(OfferScreen(name='offer'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(MyAccountScreen(name='myaccount'))
        sm.add_widget(MyTicketScreen(name='myticket'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(AdminScreen(name='admin'))

        return sm

    def on_save(self, instance, value, date_range):
        self.root.screens[2].ids.date_field.text = str(value).replace('-', '/')

    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

if __name__ == '__main__':
    TestApp().run()