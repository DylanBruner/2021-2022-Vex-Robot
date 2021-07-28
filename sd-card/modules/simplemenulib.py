import math

class simplemenu_menu(object):
    def __init__(self):
        self.debug = False
        self.menu_config = {
            "y": 1,
            "x": 1,
            "x_padding": 10,
            "y_padding": 10,
            "btn_width": 120,
            "btn_height": 110,
            "buttons_per_row": 0,
            "buttons_per_column": 0,
            "drawn_buttons": 0,
            "max_buttons": 0,
            "btn_color": 'green',
            "text_padding_x": 1,
            "text_padding_y": 1,
            "text_offset_x": 13,
            "text_offset_y": 6
        }

        try:
            self.menu_config['btn_color'] = Color.BLUE

        except:
            print("[module/simplemenu]: Color.BLUE not found, if this is not being ran on the brain then do not worry about this")

        try:
            self.menu = screenlib_screen_menu()

        except:
            self.menu = None
            print("[module/simplemenu]: screenlib not found!")

        offset = self.menu_config['btn_width'] + self.menu_config['x_padding']
        self.menu_config['buttons_per_row'] = math.floor(480 / offset)
        offset = self.menu_config['btn_height'] + self.menu_config['x_padding']
        self.menu_config['buttons_per_column'] = math.floor(272 / offset)

        self.menu_config['max_buttons'] = self.menu_config['buttons_per_row'] * self.menu_config['buttons_per_column']

        print('[module/simplemenu]: Screen Size '+str(self.menu_config['buttons_per_row'])+"x"+str(self.menu_config['buttons_per_column'])+' buttons '+str(self.menu_config['max_buttons']))


    def register_button(self, txt):
        if self.menu_config['drawn_buttons'] + 1 <= self.menu_config['max_buttons']:
            newButton = screenlib_screen_button(
            x = self.menu_config['x'],
            y = self.menu_config['y'],
            w = self.menu_config['btn_width'],
            h = self.menu_config['btn_height'],
            c = self.menu_config['btn_color'],
            text = txt,
            tc = self.menu_config['text_padding_y'],
            tr = self.menu_config['text_padding_x'])
            self.menu.buttons.append(newButton)

            self.menu_config['x'] += self.menu_config['btn_width'] + self.menu_config['x_padding']
            self.menu_config['text_padding_x'] += self.menu_config['text_offset_x']

            if self.menu_config['buttons_per_row'] == self.menu_config['drawn_buttons'] + 1:
                self.menu_config['y'] += self.menu_config['btn_height'] + self.menu_config['y_padding']
                self.menu_config['x'] = 1
                self.menu_config['text_padding_y'] += self.menu_config['text_offset_y']
                self.menu_config['text_padding_x'] = 1

            self.menu_config['drawn_buttons'] += 1


        else:
            print("[module/simplemenu]: Max amount of buttons have been created")

    def register_buttons(self, buttons):
        for x in buttons:
            self.register_button(x)

    def run_tree(self, tree):
        topMenuButtons = []

        for menu in tree:
            topMenuButtons.append(menu)

        men1 = simplemenu_menu()
        men1.register_buttons(topMenuButtons)

        selectedButton = men1.run()


        if 'options' not in tree[selectedButton]:
            return tree[selectedButton]['return-value']

        else:
            print("Rerunning")
            nt = {}
            for x in tree[selectedButton]['options']:
                val = x['text']
                nt[val] = x

            return self.run_tree(nt)

    def list_to_options(self, data, action='return', return_value='[text]'):
        options = []
        for x in data:
            new_option = {
                "text": x,
                "return-value": return_value.replace('[text]',x)
            }

            options.append(new_option)

        return options

    def run(self):
        return self.menu.mainloop()

class simplemenu_controller_menu(object):
    def __init__(self, pages):
        self.itemsPerPage = 2
        self.pages = pages
        self.selectedItem = 0
        self.selectedPage = 0
    
    def draw(self):
        self.menu = screenlib_controller_menu()
        for x in self.pages[self.selectedPage]:
            self.menu.create_item(x)
        
        if self.selectedPage != len(self.pages) - 1:
            self.menu.create_item("Next Page")
    
    def run(self):
        op = self.menu.run()
        if op.lower() == 'next page':
            print("Next Page")
            self.selectedPage += 1
            self.draw()
            return self.run()
        
        else:
            return self.menu.run()

print("[module/simplemenulib]: Loaded")
