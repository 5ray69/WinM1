# -*- coding: utf-8 -*-

import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
import System.Drawing
import System.Windows.Forms


'''
DEFINE THE COMBO BOXS
'''
class Create_combobox(System.Windows.Forms.Form):
    def __init__(self, owner, Offset_stoyak, Number_of_levels,
                Left_Point_ComboBox, Height_Point_ComboBox, Width_Size_ComboBox, Height_Size_ComboBox,
                Label_Offset, Width_Size_Label, Height_Size_Label, Dict_from_json):
        self.all_combobox = []

        for namber_int in range(1, Number_of_levels):
            owner.combbox = System.Windows.Forms.ComboBox()
            owner.combbox.Parent = self
            owner.combbox.Location = System.Drawing.Point(
                Left_Point_ComboBox + Offset_stoyak, Height_Point_ComboBox + namber_int * 27)
            owner.combbox.Size = System.Drawing.Size(Width_Size_ComboBox, Height_Size_ComboBox)
            owner.combbox.DropDownHeight = 250  # высота выпадающего списка из Combobox
            owner.combbox.ForeColor = System.Drawing.Color.FromName('Black')
            owner.combbox.FlatStyle = System.Windows.Forms.FlatStyle.Flat  # плоский стиль, не объемный
            owner.combbox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList  # DropDownList - пользователь не может ввести новое значение
            owner.combbox.Font = System.Drawing.Font('Arial', System.Single(10.5))
            owner.combbox.Name = 'L' + str(namber_int).rjust(2, "0") + '00'
            # добавляем строку в выпадающий список, указывая индекс,
            # под которым она должна находиться в списке
            owner.combbox.Items.Insert(0, Dict_from_json['L' + str(namber_int).rjust(2, "0") + '00'])
            # указываем индекс, который будет выбран и помещен в combo box
            owner.combbox.SelectedIndex = 0
            owner.Controls.Add(owner.combbox)
            self.all_combobox.append(owner.combbox)

            '''
            LOAD DROP DOWN LIST IN COMBO BOX
            '''
            for int_namber in range(1, Number_of_levels):
                owner.combbox.Items.Add('M' + str(int_namber))

            '''
            DEFIND LABEL TO COMBO BOX
            '''
            owner.label_to_combobox = System.Windows.Forms.Label()
            owner.label_to_combobox.Text = 'L' + str(namber_int).rjust(2, "0") + '00'
            owner.label_to_combobox.Font = System.Drawing.Font('Arial', System.Single(11))
            owner.label_to_combobox.Location = System.Drawing.Point(
                Left_Point_ComboBox + Offset_stoyak - Label_Offset, Height_Point_ComboBox + 3 + namber_int * 27)
            # PreferredWidth и PreferredHeight предпочтительная ширина и высота
            owner.label_to_combobox.Size = System.Drawing.Size(Width_Size_Label, Height_Size_Label)
            owner.Controls.Add(owner.label_to_combobox)
