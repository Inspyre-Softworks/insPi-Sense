from inspi_sense.helpers.constants import PROG_NAME
from inspi_sense.helpers.locations import get_territories_and_states

import PySimpleGUI
import sys

from logging import getLogger


class ConfigWindow:

    @staticmethod
    def popup_not_yet_implemented():
        import PySimpleGUI as _gui

        _gui.PopupError('This feature has yet to be implemented')


    def __init__(self):
        _gui = PySimpleGUI

        _address_frame = [
            [_gui.Text('Address 1:'), _gui.InputText('123 Example Dr', key='address_1_input')],
            [_gui.Text('Address 2:'), _gui.InputText('Apt 2', key='address_2_input')],
            [_gui.Text('City:'), _gui.InputText('', key='city_input')],
            [_gui.Text('State (Territory):'), _gui.Combo(get_territories_and_states(), key='state_combo_input')],
            [_gui.Text('Postal Code:'), _gui.InputText('', enable_events=True, key='postal_code_input',
                                                       tooltip='Please enter your zipcode/postal code')]
        ]

        _layout = [
            [_gui.Text('Where would you like your config files to go?'), _gui.FolderBrowse(key='config_file_browser',
                                                                                           change_submits=True)],
            [_gui.Frame('Address Information', layout=_address_frame)],
            [_gui.OK(key='ok_button'), _gui.Button('Check Zipcode', disabled=True, enable_events=True,
                                                   key='check_zip_button')]
        ]

        _window = _gui.Window('Config', _layout)

        self.active = True
        self.user_was_last = False


        log = getLogger(PROG_NAME)
        info = log.info

        info(f'Logger started for {__class__.__name__}')

        self.invalid_input = False
        _enabled_buttons = []


        while True:
            self.event, self.values = _window.read(timeout=100)

            if self.event is None:
                info('Received "None". (Most likely closed by the user)')
                info('Closing window')
                _window.close()
                info('Window closed, stopping class loop.')
                break

            if self.event == 'check_zip_button':
                self.popup_not_yet_implemented()

            if self.event == 'postal_code_input':
                if self.values['postal_code_input'][-1] not in ('0123456789'):
                    _window['postal_code_input'].update(self.values['postal_code_input'][:-1])
                    _window.Element('postal_code_input').set_tooltip('Please enter a number!')
                    if not self.invalid_input:
                        _window.extend_layout(_window, [[_gui.Text('Please enter only digits!', text_color='red',
                                                               justification='center', key='zip_err_msg')]])
                        self.invalid_input = True
                        _window.Element('postal_code_input').Update(background_color='red')
                        _window.refresh()

                    else:
                        _window['zip_err_msg'].update(visible=True)
                        _window.Element('postal_code_input').Update(background_color='red')
                        _window.refresh()

                    print('\a', end='', flush=True)

                else:
                    if self.invalid_input:
                        _window['zip_err_msg'].update(visible=False)
                        _window.Element('postal_code_input').Update(background_color='white')
                        _window.refresh()

                    if 'check_zip_button' in _enabled_buttons and len(self.values['postal_code_input']) <= 4:
                        _window['check_zip_button'].update(disabled=True)
                        _enabled_buttons.remove('check_zip_button')

                    if len(self.values['postal_code_input']) == 5:
                        if 'check_zip_button' not in _enabled_buttons:
                            _window['check_zip_button'].update(disabled=False)
                            _enabled_buttons.append('check_zip_button')
                            _window.refresh()

                print(self.event, self.values)


            #
            # if len(self.values['postal_code_input']):
            #     self.user_was_last = True
            #     if self.values['postal_code_input'][-1] not in ('0123456789'):
            #         # delete last char from input
            #         _window['postal_code_input'].update(self.values['postal_code_input'][:-1])
            #         self.user_was_last = False
            #         _window.Element('postal_code_input').set_tooltip('Please enter a number!')
            #

            #     else:
            #         if self.user_was_last:
            #             if zip_error_trigger:
            #                 _window.Element('postal_code_input').Update(background_color='white')
            #                 _window['zip_err_msg'].update(visible=False)
            #                 _window.refresh()

            if self.event == 'ok_button':
                info('OK button was pressed!')
                print(self.values)
                _window.close()









