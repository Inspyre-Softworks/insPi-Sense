from inspi_sense.helpers.constants import PROG_NAME
from inspi_sense.helpers import Locales

from inspi_sense.helpers.os_io import get_paste

from inspi_sense.models.menus.right_click import RightClickMenu

import PySimpleGUI

from logging import getLogger

locations = Locales()
verify_zipcode = Locales.validate_zipcode
get_territories_and_states = Locales.get_territories_and_states


class ConfigWindow:

    def refresh(self):
        self.log.info('')
        self.window.refresh()
        window_refreshes += 1

    def __init__(self):
        gui = PySimpleGUI

        gui.change_look_and_feel('DarkAmber')

        _address_frame = [
            [gui.Text('Address 1:'), gui.InputText('123 Example Dr', key='address_1_input')],
            [gui.Text('Address 2:'), gui.InputText('Apt 2', key='address_2_input')],
            [gui.Text('City:'), gui.InputText('', key='city_input')],
            [gui.Text('State (Territory):'), gui.Combo(get_territories_and_states(), key='state_combo_input')],
            [gui.Text('Postal Code:'), gui.InputText('', enable_events=True, key='postal_code_input',
                                                     tooltip='Please enter your zipcode/postal code',
                                                     right_click_menu=RightClickMenu().menu)
             ]
        ]

        _layout = [
            [gui.Text('Where would you like your config files to go?'), gui.FolderBrowse(key='config_file_browser',
                                                                                         change_submits=True)],
            [gui.Frame('Address Information', layout=_address_frame)],
            [gui.OK(key='ok_button'), gui.Button('Check Zipcode', disabled=True, enable_events=True,
                                                 key='check_zip_button')]
        ]

        self.window = gui.Window('Config', _layout)

        self.active = True
        self.user_was_last = False

        log = getLogger(PROG_NAME)
        self.log = log
        info = log.info
        warn = log.warning

        info(f'Logger started for {__class__.__name__}')

        self.invalid_input = False
        _enabled_buttons = []

        while True:
            self.event, self.values = self.window.read(timeout=100)

            if self.event is None:
                info('Received "None". (Most likely closed by the user)')
                info('Closing window')

                self.window.close()

                info('Window closed, stopping class loop.')

                break

            if self.event == 'check_zip_button':
                res = verify_zipcode(zip_code=self.values['postal_code_input'])
                if res is not None:
                    if self.values['state_combo_input'] == '':
                        self.window['state_combo_input'].update(value=res.state_long)

                    if self.values['city_input'] == '':
                        self.window['city_input'].update(value=res.major_city)

                    if self.values['address_1_input'] == '123 Example Dr' or self.values['address_1_input'] == '':
                        self.window['address_1_input'].update(value='')
                        self.window['address_2_input'].update(value='')

            if self.event == 'Paste':
                self.window['postal_code_input'].update(value=get_paste())

            if self.event == 'postal_code_input':
                try:
                    if self.values['postal_code_input'][-1] not in ('0123456789'):
                        self.window['postal_code_input'].update(self.values['postal_code_input'][:-1])
                        self.window.Element('postal_code_input').set_tooltip('Please enter a number!')
                        if not self.invalid_input:
                            self.window.extend_layout(self.window, [[gui.Text('Please enter only digits!',
                                                                              text_color='red',
                                                                              justification='center',
                                                                              key='zip_err_msg')]])
                            self.invalid_input = True
                            self.window.Element('postal_code_input').Update(background_color='red')
                            self.window.refresh()

                        else:
                            self.window['zip_err_msg'].update(visible=True)
                            self.window.Element('postal_code_input').Update(background_color='red')
                            self.refresh()

                        print('\a', end='', flush=True)

                    else:
                        if self.invalid_input:
                            self.window['zip_err_msg'].update(visible=False)
                            self.window.Element('postal_code_input').Update(background_color='white')
                            self.window.refresh()

                        if 'check_zip_button' in _enabled_buttons and len(self.values['postal_code_input']) <= 4:
                            self.window['check_zip_button'].update(disabled=True)
                            _enabled_buttons.remove('check_zip_button')

                        if len(self.values['postal_code_input']) == 5:
                            info('Zipcode field now has 5 digits, enabling "Check Zipcode" button')
                            info('Checking to see if already enabled...')
                            if 'check_zip_button' not in _enabled_buttons:
                                info('"Check Zipcode" not found among the enabled buttons')
                                _enabled_buttons.append('check_zip_button')
                                info(f'Added! The list of enabled buttons is here: {_enabled_buttons}')
                                self.window['check_zip_button'].update(disabled=False)
                                self.window.refresh()
                        else:
                            if 'check_zip_button' in _enabled_buttons:
                                warn('Zipcode must be 5 numbers in length!')
                                info(f'Currently enabled buttons: {_enabled_buttons}')
                                info(f'Removing "Check Zipcode" button from enabled buttons...')
                                _enabled_buttons.remove('check_zip_button')
                                info('Removed!')
                                info('Disabling button')
                                self.window['check_zip_button'].update(disabled=True)
                                info('Disabled!')
                                info('Refreshing window')
                                self.window.refresh()
                                info('Refreshed!')


                except IndexError as e:
                    warn('Unable to shift up a value, field must be empty')
                    info('Emptying field, resetting to 0 input')
                    self.window['postal_code_input'].update(value='')

            if self.event == 'ok_button':
                info('OK button was pressed!')
                print(self.values)
                self.window.close()
