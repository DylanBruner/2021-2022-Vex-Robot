class screenlib_screen_text(object):
    def __init__(self,tr,tc,text,tcolor,tfill):
        self.tr = tr
        self.tc = tc
        self.text = text
        self.tcolor = tcolor
        self.tfill = tfill

    def draw(self):
        brain.screen.set_cursor(self.tr,self.tc)
        brain.screen.set_pen_color(self.tcolor)
        brain.screen.set_fill_color(self.tfill)
        brain.screen.print(self.text)

class screenlib_screen_button(object):
    def __init__(self,x,y,w,h,c,text,tc,tr):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.tc = tc
        self.tr = tr
        self.text = text
        self.hide = False

    def draw(self):
        if not self.hide:
            if self.w == self.h:
                l = 2
            else:
                l = 4

            brain.screen.set_fill_color(self.c)
            brain.screen.set_pen_color(Color.PURPLE)
            brain.screen.draw_rectangle(self.x,self.y,self.w,self.h,self.c)
            brain.screen.draw_circle(self.x+self.w,self.y+self.h/2,self.w/l)
            brain.screen.draw_circle(self.x,self.y+self.h/2,self.w/l)

            brain.screen.set_fill_color(self.c)
            brain.screen.set_cursor(self.tc,self.tr)
            brain.screen.print(self.text)

    def is_pressing(self):
        if brain.screen.pressing() and not self.hide:
            if brain.screen.x_position() <= self.x + self.w and brain.screen.y_position() <= self.y + self.h and not brain.screen.y_position() <= self.y and not brain.screen.x_position() <= self.x:
                oc = self.c
                self.c = Color.WHITE
                brain.screen.clear_screen()
                self.draw()

                while brain.screen.pressing():
                    wait(.005,SECONDS)

                self.c = oc
                self.draw()
                return True

        return False

    def hide_object(self):
        self.hide = True

    def show_object(self):
        self.hide = False

class screenlib_screen_menu(object):
    def __init__(self,name="menu"):
        self.name = name
        self.buttons = []
        self.objects = []
        self.shown = False

    def mainloop(self):
        self.shown = True
        brain.screen.clear_screen()
        while self.shown:
            wait(.025,SECONDS)


            for x in self.buttons:
                x.draw()

                if x.is_pressing():
                    brain.screen.clear_screen()
                    return x.text

            for x in self.objects:
                x.draw()

    def alert(self,text):
        brain.screen.draw_rectangle(1,1,600,600,Color.BLUE)
        brain.screen.set_cursor(6,22)
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.print(text)
        wait(2.5,SECONDS)

class screenlib_controller_menu(object):
    def __init__(self):
        self.items = []
        self.selectedItem = 0

    def create_item(self, text):
        self.items.append(text)
    
    def create_items(self, items):
        for x in items:
            self.items.append(x)
    
    def draw(self):
        controller_1.screen.clear_screen()
        controller_1.screen.set_cursor(0,0)
        for item in self.items:
            if self.items.index(item) == self.selectedItem:
                controller_1.screen.print("> "+item)
            
            else:
                controller_1.screen.print("  "+item)
            controller_1.screen.set_cursor(controller_1.screen.row()+1, 0)
    
    def run(self):
        self.draw()

        while True:
            if controller_1.buttonDown.pressing():
                if len(self.items) - 1 != self.selectedItem:
                    self.selectedItem += 1
                    self.draw()
                
            elif controller_1.buttonUp.pressing():
                if self.selectedItem != 0:
                    self.selectedItem -= 1
                    self.draw()
                wait(.1,SECONDS)
            
            elif controller_1.buttonRight.pressing():
                return self.items[self.selectedItem]

print("[module/screenlib]: Loaded")
