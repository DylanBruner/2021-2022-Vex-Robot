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
            brain.screen.set_fill_color(self.c)
            brain.screen.set_pen_color(Color.PURPLE)
            brain.screen.draw_rectangle(self.x,self.y,self.w,self.h,self.c)

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

print("[module/screenlib]: Loaded")
