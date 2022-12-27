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
from ColumnStoyak import ColumnOneStoyak
# from Draw import DrawBorder


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
Offset_stoyak = 0
Offset_stoyak2 = 170


class User_input_form(System.Windows.Forms.Form):
    def __init__(self):
        self.Text = "Выберите какая магистраль квартир на каком этаже"  # текст заголовка
        self.BackColor = System.Drawing.Color.FromArgb(238, 238, 238)  # цвет фона формы
        self.ClientSize = System.Drawing.Size(600, 900)  # размер формы в точках
        caption_height = System.Windows.Forms.SystemInformation.CaptionHeight  # создаем переменную высота заголовка
        self.MinimumSize = System.Drawing.Size(600, (900 + caption_height))  # минимальный размер формы
        self.dict_user_select = {}
        self.number_panels = ''

        self.stoyak1 = ColumnOneStoyak(self, 'основной стояк', "1", Offset_stoyak, Number_of_levels,
                Left_Point_ComboBox, Height_Point_ComboBox, Width_Size_ComboBox, Height_Size_ComboBox,
                Label_Offset, Width_Size_Label, Height_Size_Label, Dict_from_json)
        self.Paint += System.Windows.Forms.PaintEventHandler(self.stoyak1.drawBorders)
        self._combobox_stoyak1 = self.stoyak1.all_combobox

        self.stoyak2 = ColumnOneStoyak(self, 'второй стояк', "2", Offset_stoyak2, Number_of_levels,
                Left_Point_ComboBox, Height_Point_ComboBox, Width_Size_ComboBox, Height_Size_ComboBox,
                Label_Offset, Width_Size_Label, Height_Size_Label, Dict_from_json)
        self.Paint += System.Windows.Forms.PaintEventHandler(self.stoyak2.drawBorders)
        self._combobox_stoyak2 = self.stoyak2.all_combobox

        self.label_number_panels = System.Windows.Forms.Label()
        self.label_number_panels.Text = 'все номера коробок ЩК, которые <= N относятся К ПЕРВОЙ ЧАСТИ\
            \nЗДАНИЯ, основному стояку, остальные к второму.\
            \nЕсли в здании один стояк, назначьте N > количества ЩК на одном этаже'
        self.label_number_panels.Font = System.Drawing.Font(
            'Arial',
            System.Single(10.5),
            System.Drawing.FontStyle.Italic,
            System.Drawing.GraphicsUnit.Point
            )
        self.label_number_panels.Location = System.Drawing.Point(30, 750)
        self.label_number_panels.Size = System.Drawing.Size(
            self.label_number_panels.PreferredWidth, self.label_number_panels.PreferredHeight)
        self.Controls.Add(self.label_number_panels)
        self.label_number_panels = self.label_number_panels

        self.combbox_number = System.Windows.Forms.ComboBox()
        self.combbox_number.Parent = self
        self.combbox_number.Location = System.Drawing.Point(300, 730)
        self.combbox_number.Size = System.Drawing.Size(Width_Size_ComboBox - 35, Height_Size_ComboBox)
        self.combbox_number.DropDownHeight = 250  # высота выпадающего списка из Combobox
        self.combbox_number.ForeColor = System.Drawing.Color.FromName('Black')
        self.combbox_number.FlatStyle = System.Windows.Forms.FlatStyle.Flat  # плоский стиль, не объемный
        self.combbox_number.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList  # DropDownList - пользователь не может ввести новое значение
        self.combbox_number.Font = System.Drawing.Font('Arial', System.Single(10.5))
        self.combbox_number.Name = 'Number panels'
        # добавляем строку в выпадающий список, указывая индекс,
        # под которым она должна находиться в списке
        self.combbox_number.Items.Insert(0, Dict_from_json['0'])
        # указываем индекс, который будет выбран и помещен в combo box
        self.combbox_number.SelectedIndex = 0
        self.Controls.Add(self.combbox_number)

        # LOAD DROP DOWN LIST IN combbox_number
        for int_number in range(1, 30):
                self.combbox_number.Items.Add(str(int_number))

        self.label_to_combobox_number = System.Windows.Forms.Label()
        self.label_to_combobox_number.Text = 'назначьте N:'
        self.label_to_combobox_number.Font = System.Drawing.Font(
            'Arial', System.Single(11), System.Drawing.FontStyle.Bold)
        self.label_to_combobox_number.Location = System.Drawing.Point(
            self.combbox_number.Location.X - 100, self.combbox_number.Location.Y + 2)
        self.label_to_combobox_number.Size = System.Drawing.Size(
            self.label_to_combobox_number.PreferredWidth, self.label_to_combobox_number.PreferredHeight)
        self.Controls.Add(self.label_to_combobox_number)


        self._defin_button = System.Windows.Forms.Button()
        self._defin_button.Location = System.Drawing.Point(30, 830)
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

        self._cancel_button = System.Windows.Forms.Button()
        self._cancel_button.Location = System.Drawing.Point(340, 830)
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
                            System.Drawing.GraphicsUnit.Point)
        self._cancel_button.Font = cancel_button_font
        # цвет шрифта текста на кнопке - белый
        self._cancel_button.ForeColor = System.Drawing.Color.FromName('White')
        # цвет самой кнопки, ее заливка. Если не указывать прозрачность,
        # то он будет полностью непрозрачен
        self._cancel_button.BackColor = System.Drawing.Color.FromArgb(255, 60, 90, 100)
        self._cancel_button.Anchor = (
            System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)
        self.Controls.Add(self._cancel_button)

        # BIND EVENTS TO CONTROL
        # Control.MouseEnter Событие, когда указатель мыши заходит в пределы элемента управления.
        self._defin_button.MouseEnter += self.define_button_mouse_enter
        # MouseLeave происходит, когда указатель мыши покидает элемент управления.
        self._defin_button.MouseLeave += self.define_button_mouse_leave

        # Control.MouseEnter Событие, когда указатель мыши заходит в пределы элемента управления.
        self._cancel_button.MouseEnter += self.cancel_button_mouse_enter
        # MouseLeave происходит, когда указатель мыши покидает элемент управления.
        self._cancel_button.MouseLeave += self.cancel_button_mouse_leave

        self._defin_button.Click += self._click_on_define_button
        self._cancel_button.Click += self._click_on_cancel_button

    def _click_on_define_button(self, sender, args):
        dict_general_user_select = {}
        dict1_user_select = {}
        for comb_box in self._combobox_stoyak1:
            print(comb_box.Name)
            print(comb_box.SelectedItem)
            dict1_user_select[comb_box.Name] = comb_box.SelectedItem
        dict_general_user_select["1"] = dict1_user_select
        dict2_user_select = {}
        for comb_box in self._combobox_stoyak2:
            print(comb_box.Name)
            print(comb_box.SelectedItem)
            dict2_user_select[comb_box.Name] = comb_box.SelectedItem
        dict_general_user_select["2"] = dict2_user_select
        print(self.combbox_number.Name)
        print(self.combbox_number.SelectedItem)
        dict_general_user_select["0"] = self.combbox_number.SelectedItem
        self.number_panels = self.combbox_number.SelectedItem
        self.dict_user_select = dict_general_user_select

        # создаем файл json, существующий с тем же именем перезапишется
        with open('drop_list.json', 'w') as file:
            json.dump(dict_general_user_select, file, indent=4)

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
    def define_button_mouse_enter(self, sender, args):
        self._defin_button.ForeColor = System.Drawing.Color.FromName('White')
        self._defin_button.BackColor = System.Drawing.Color.FromArgb((int(255 * .02)), 60, 90, 100)

        # возвращаем цвет кнопки, когда указатель мыши покидает пределы кнонки/элемента управления
    def define_button_mouse_leave(self, sender, args):
        self._defin_button.ForeColor = System.Drawing.Color.FromName('White')
        self._defin_button.BackColor = System.Drawing.Color.FromArgb(255, 60, 90, 100)

        # меняем цвет кнопки, когда указатель мыши входит в пределы кнонки/элемента управления
    def cancel_button_mouse_enter(self, sender, args):
        self._cancel_button.ForeColor = System.Drawing.Color.FromName('White')
        self._cancel_button.BackColor = System.Drawing.Color.FromArgb((int(255 * .02)), 60, 90, 100)

        # возвращаем цвет кнопки, когда указатель мыши покидает пределы кнонки/элемента управления
    def cancel_button_mouse_leave(self, sender, args):
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
