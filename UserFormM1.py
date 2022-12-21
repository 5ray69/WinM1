# -*- coding: utf-8 -*-

import clr
# clr.AddReference('System.IO')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
# import System.IO
import System.Drawing
import System.Windows.Forms
import json
from ColumnStoyak import Create_combobox
from Draw import DrawBorder

# comment1


'''
DESERIALIZATION
'''
# читаем файл
with open('drop_list.json', 'r') as file:
    Dict_from_json = json.load(file)

# # FOR DYNAMO читаем файл из текущей дирректории
# with open(IN[0].DirectoryName + r'\drop_list.json', 'r') as file:
#     dict_from_json = json.load(file)

'''
VARIABLE FOR DIMENSIONS POINT LOCATIONS AND SIZES
'''
Left_Point_ComboBox = 100
Height_Point_ComboBox = 10

Width_Size_ComboBox = 70
Height_Size_ComboBox = 100

Label_Offset = 47

Width_Size_Label = 50
Height_Size_Label = 25

Number_of_levels = 26

# для основного стояка - значение 0, для других - смещение 
# (заготовка на будущую работу, сейчас создаем только один стояк)
Offset_stoyak1 = 0
Offset_stoyak2 = 250


class User_input_form(System.Windows.Forms.Form):
    def __init__(self):
        self.Text = "Выберите какая магистраль квартир на каком этаже"  # текст
        self.BackColor = System.Drawing.Color.FromArgb(238, 238, 238)  # цвет фона формы
        self.ClientSize = System.Drawing.Size(600, 900)  # размер формы в точках
        caption_height = System.Windows.Forms.SystemInformation.CaptionHeight  # создаем переменную высота заголовка
        self.MinimumSize = System.Drawing.Size(580, (870 + caption_height))  # минимальный размер формы
        self._combobox = []
        self._initialize_components()
        self._draw = DrawBorder(self, Offset_stoyak1, Number_of_levels,
                                Left_Point_ComboBox, Height_Point_ComboBox, Height_Size_ComboBox,
                                Label_Offset, Height_Size_Label)
        self.Paint += System.Windows.Forms.PaintEventHandler(self._draw.drawBorders)  # рисование прямоугольника вокруг комбобоксов

        '''
        DEFINE THE LOAD BUTTON
        '''
        self._defin_button = System.Windows.Forms.Button()
        self._defin_button.Location = System.Drawing.Point(30, 800)
        self._defin_button.Size = System.Drawing.Size(230, 54)
        # define the Style of our button (FlatStyle - плоский стиль)
        self._defin_button.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        # размер границы кнопки сделали 0, то есть нет границы у кнопки
        self._defin_button.FlatAppearance.BorderSize = 0
        self._defin_button.Text = "Назначить выбранное"
        # шрифта текста на кнопке, Arial, жинрый и прочее
        define_button_font = System.Drawing.Font(
            'Arial',
            System.Single(12),
            System.Drawing.FontStyle.Bold,
            System.Drawing.GraphicsUnit.Point
            )
        self._defin_button.Font = define_button_font
        # цвет шрифта текста на кнопке - белый
        self._defin_button.ForeColor = System.Drawing.Color.FromName('White')
        # цвет самой кнопки, ее заливка. Если не указывать прозрачность,
        # то он будет полностью непрозрачен
        self._defin_button.BackColor = System.Drawing.Color.FromArgb(255, 60, 90, 100)
        # создали отдельную переменную/свойство = объект шрифта, которое будем использовать потом
        # это демонстрация альтернативного способа задания шрифтов в разных местах кода
        self.button_fonts = System.Drawing.Font('Arial', System.Single(10.5))
        self._defin_button.Anchor = (
            System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
        self.Controls.Add(self._defin_button)
# self.label.Anchor = ((WinForms.AnchorStyles)(
#     ((WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom)
#      | WinForms.AnchorStyles.Left)))
        '''
        DEFINE THE CANCEL BUTTON
        '''
        self._cancel_button = System.Windows.Forms.Button()
        self._cancel_button.Location = System.Drawing.Point(340, 800)
        self._cancel_button.Size = System.Drawing.Size(230, 54)
        # define the Style of our button (FlatStyle - плоский стиль)
        self._cancel_button.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        # размер границы кнопки сделали 0, то есть нет границы у кнопки
        self._cancel_button.FlatAppearance.BorderSize = 0
        self._cancel_button.Text = "Отмена"
        # шрифта текста на кнопке, Arial, жинрый и прочее
        cancel_button_font = System.Drawing.Font(
            'Arial',
            System.Single(12),
            System.Drawing.FontStyle.Bold,
            System.Drawing.GraphicsUnit.Point
            )
        self._cancel_button.Font = cancel_button_font

        # цвет шрифта текста на кнопке - белый
        self._cancel_button.ForeColor = System.Drawing.Color.FromName('White')
        # цвет самой кнопки, ее заливка. Если не указывать прозрачность,
        # то он будет полностью непрозрачен
        self._cancel_button.BackColor = System.Drawing.Color.FromArgb(255, 60, 90, 100)
        self._cancel_button.Anchor = (
            System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)
        self.Controls.Add(self._cancel_button)

        '''
        BIND EVENTS TO CONTROL
        '''
        # Control.MouseEnter Событие, когда указатель мыши заходит в пределы элемента управления.
        self._defin_button.MouseEnter += self.LoadFileButton_mouse_enter
        # MouseLeave происходит, когда указатель мыши покидает элемент управления.
        self._defin_button.MouseLeave += self.LoadFileButton_mouse_leave

        # Control.MouseEnter Событие, когда указатель мыши заходит в пределы элемента управления.
        self._cancel_button.MouseEnter += self.CloseFileButton_mouse_enter
        # MouseLeave происходит, когда указатель мыши покидает элемент управления.
        self._cancel_button.MouseLeave += self.CloseFileButton_mouse_leave

        self._defin_button.Click += self._click_on_define_button
        self._cancel_button.Click += self._click_on_cancel_button

    def _initialize_components(self):
        self._create_combobox()

    '''
    DEFINE THE COMBO BOXS
    '''
    def _create_combobox(self):
        create_combobox = Create_combobox(self, Offset_stoyak1, Number_of_levels,
                            Left_Point_ComboBox, Height_Point_ComboBox, Width_Size_ComboBox, Height_Size_ComboBox,
                            Label_Offset, Width_Size_Label, Height_Size_Label, Dict_from_json)
        self._combobox = create_combobox.all_combobox
        return create_combobox

    '''
    DEFINE MOUSE CLICK
    '''
    def _click_on_define_button(self, sender, args):
        dict_user_select = {}
        for comb_box in self._combobox:
            print(comb_box.Name)
            print(comb_box.SelectedItem)
            dict_user_select[comb_box.Name] = comb_box.SelectedItem

        # '''
        # SERIALIZATION
        # '''
        # # создаем файл json, существующий с тем же именем перезапишется
        # with open('drop_list.json', 'w') as file:
        #     json.dump(dict_user_select, file, indent=4)

        # # FOR DYNAMO создаем файл json в текущей дирректории, существующий с тем же именем перезапишется
        # with open(IN[0].DirectoryName + r'\drop_list.json', 'w') as file:
        #     json.dump(dict_user_select, file, indent=4)
        
        self.Close()

    '''
    CANCEL MOUSE CLICK
    '''
    def _click_on_cancel_button(self, sender, args):
        # Ошибка возникает, когда мы пытаемся закрыть форму в конструкторе или в событии Load
        self.Close()

    '''
    DEFINE MOUSE ENTER EVENT
    '''
    # при наведении курсором мыши кнопка меняет цвет(событие - наведение курсором)
    def LoadFileButton_mouse_enter(self, sender, args):
        self._defin_button.ForeColor = System.Drawing.Color.FromName('White')
        self._defin_button.BackColor = System.Drawing.Color.FromArgb((int(255 * .02)), 60, 90, 100)

        # возвращаем цвет кнопки, когда указатель мыши покидает пределы кнонки/элемента управления
    def LoadFileButton_mouse_leave(self, sender, args):
        self._defin_button.ForeColor = System.Drawing.Color.FromName('White')
        self._defin_button.BackColor = System.Drawing.Color.FromArgb(255, 60, 90, 100)

        # меняем цвет кнопки, когда указатель мыши входит в пределы кнонки/элемента управления
    def CloseFileButton_mouse_enter(self, sender, args):
        self._cancel_button.ForeColor = System.Drawing.Color.FromName('White')
        self._cancel_button.BackColor = System.Drawing.Color.FromArgb((int(255 * .02)), 60, 90, 100)

        # возвращаем цвет кнопки, когда указатель мыши покидает пределы кнонки/элемента управления
    def CloseFileButton_mouse_leave(self, sender, args):
        self._cancel_button.ForeColor = System.Drawing.Color.FromName('White')
        self._cancel_button.BackColor = System.Drawing.Color.FromArgb(255, 60, 90, 100)

def main_user_from():
    user_form = User_input_form()
    win_form_app = System.Windows.Forms.Application
    win_form_app.Run(user_form)  # запуск формы

if __name__ == '__main__':
    main_user_from()

# if __name__ == "__main__":
#     inst = User_input_form()
#     inst.ShowDialog()

# условие if __name__ == "__main__": в ноде dynamo не выполняется,
# нужно в dynamo без этого условия запускать
