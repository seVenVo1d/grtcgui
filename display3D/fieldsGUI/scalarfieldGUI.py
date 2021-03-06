import PySimpleGUI as sg
from display3D.image_resizer_fields import resize_cd_image3d, resize_ld_image3d
from equations.FieldsEP.scalarfieldEP import *
from sympy import preview, sympify


def scalarfield_gui3d(coord_sys):
    """
    The main process of the GUI that produces the image of a scalar field
    for a given coordinate system in 3D

    Args:
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
    """
    scalar_field_layout = [
                                [sg.Image(r'display3D\input images\scalarfield.png'),
                                 sg.Input('0')],

                                [sg.Frame(layout=[
                                    [sg.Button('Calculate', button_color='purple'),
                                     sg.Image(r'display3D\input images\cov_scalarfield.png'),
                                     sg.Text('for', font=('Verdana', 11)),
                                     sg.Image(r'display3D\input images\e.png'),
                                     sg.InputCombo(coord_sys, default_value=coord_sys[0])
                                     ]], title='Covariant Derivative', font=('Verdana', 12))],

                                [sg.Frame(layout=[
                                    [sg.Image(r'display3D\input images\LX0.png'),
                                    sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(r'display3D\input images\LX1.png'),
                                     sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Image(r'display3D\input images\LX2.png'),
                                     sg.InputText(default_text='0', font=('Tahoma', 11))],
                                    [sg.Button('Calculate', button_color='purple'),
                                     sg.Image(r'display3D\input images\LX_scalarfield.png')]], title='Lie Derivative', font=('Verdana', 12))]
                                ]
    windows_scalar_field = sg.Window('Scalar Field', scalar_field_layout)
    while True:
        event, values = windows_scalar_field.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        else:
            scalar_field = values[1]   # Obtaining the scalar field

            # Calculation of the covariant derivative
            if event == 'Calculate':
                index_symbol = values[4]
                cd_scalar_field_eqn = cd_scalarfield_ep(coord_sys, scalar_field, index_symbol)
                preview(cd_scalar_field_eqn, viewer='file', filename=r'display3D\output images\cd_scalar_field.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_cd_image3d ('Scalar Field')
                layout_cd_scalar_field_result = [
                                                    [sg.Image(r'display3D\output images\cd_scalar_field.png')],
                                                ]
                window_cd_scalar_field_result = sg.Window('Scalar Field', layout_cd_scalar_field_result)
                while True:
                    event, values = window_cd_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break

            # Calculation of the lie derivative
            if event == 'Calculate0':
                X = [sympify(values[i]) for i in range(6, 12, 2)]
                ld_scalar_field_eqn = ld_scalarfield_ep(coord_sys, scalar_field, X)
                preview(ld_scalar_field_eqn, viewer='file', filename=r'display3D\output images\ld_scalar_field.png', euler=True,
                        dvioptions=['-T', 'tight', '-z', '0', '--truecolor', '-D 1200', '-bg', 'Transparent'])
                resize_ld_image3d('Scalar Field')
                layout_ld_scalar_field_result = [
                                                    [sg.Image(r'display3D\output images\ld_scalar_field.png')],
                                                ]
                window_ld_scalar_field_result = sg.Window('Scalar Field', layout_ld_scalar_field_result)
                while True:
                    event, values = window_ld_scalar_field_result.read()
                    if event == sg.WIN_CLOSED:
                        break
