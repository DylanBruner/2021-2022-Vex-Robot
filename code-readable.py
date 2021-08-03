from vex import *

f = open("modules/screenlib.module",'w')
f.write("""Y2xhc3Mgc2NyZWVubGliX3NjcmVlbl90ZXh0KG9iamVjdCk6CiAgICBkZWYgX19pbml0X18oc2VsZix0cix0Yyx0ZXh0LHRjb2xvcix0ZmlsbCk6CiAgICAgICAgc2VsZi50ciA9IHRyCiAgICAgICAgc2VsZi50YyA9IHRjCiAgICAgICAgc2VsZi50ZXh0ID0gdGV4dAogICAgICAgIHNlbGYudGNvbG9yID0gdGNvbG9yCiAgICAgICAgc2VsZi50ZmlsbCA9IHRmaWxsCgogICAgZGVmIGRyYXcoc2VsZik6CiAgICAgICAgYnJhaW4uc2NyZWVuLnNldF9jdXJzb3Ioc2VsZi50cixzZWxmLnRjKQogICAgICAgIGJyYWluLnNjcmVlbi5zZXRfcGVuX2NvbG9yKHNlbGYudGNvbG9yKQogICAgICAgIGJyYWluLnNjcmVlbi5zZXRfZmlsbF9jb2xvcihzZWxmLnRmaWxsKQogICAgICAgIGJyYWluLnNjcmVlbi5wcmludChzZWxmLnRleHQpCgpjbGFzcyBzY3JlZW5saWJfc2NyZWVuX2J1dHRvbihvYmplY3QpOgogICAgZGVmIF9faW5pdF9fKHNlbGYseCx5LHcsaCxjLHRleHQsdGMsdHIpOgogICAgICAgIHNlbGYueCA9IHgKICAgICAgICBzZWxmLnkgPSB5CiAgICAgICAgc2VsZi53ID0gdwogICAgICAgIHNlbGYuaCA9IGgKICAgICAgICBzZWxmLmMgPSBjCiAgICAgICAgc2VsZi50YyA9IHRjCiAgICAgICAgc2VsZi50ciA9IHRyCiAgICAgICAgc2VsZi50ZXh0ID0gdGV4dAogICAgICAgIHNlbGYuaGlkZSA9IEZhbHNlCgogICAgZGVmIGRyYXcoc2VsZik6CiAgICAgICAgaWYgbm90IHNlbGYuaGlkZToKICAgICAgICAgICAgaWYgc2VsZi53ID09IHNlbGYuaDoKICAgICAgICAgICAgICAgIGwgPSAyCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBsID0gNAoKICAgICAgICAgICAgYnJhaW4uc2NyZWVuLnNldF9maWxsX2NvbG9yKHNlbGYuYykKICAgICAgICAgICAgYnJhaW4uc2NyZWVuLnNldF9wZW5fY29sb3IoQ29sb3IuUFVSUExFKQogICAgICAgICAgICBicmFpbi5zY3JlZW4uZHJhd19yZWN0YW5nbGUoc2VsZi54LHNlbGYueSxzZWxmLncsc2VsZi5oLHNlbGYuYykKCgogICAgICAgICAgICBicmFpbi5zY3JlZW4uc2V0X2ZpbGxfY29sb3Ioc2VsZi5jKQogICAgICAgICAgICBicmFpbi5zY3JlZW4uc2V0X2N1cnNvcihzZWxmLnRjLHNlbGYudHIpCiAgICAgICAgICAgIGJyYWluLnNjcmVlbi5wcmludChzZWxmLnRleHQpCgogICAgZGVmIGlzX3ByZXNzaW5nKHNlbGYpOgogICAgICAgIGlmIGJyYWluLnNjcmVlbi5wcmVzc2luZygpIGFuZCBub3Qgc2VsZi5oaWRlOgogICAgICAgICAgICBpZiBicmFpbi5zY3JlZW4ueF9wb3NpdGlvbigpIDw9IHNlbGYueCArIHNlbGYudyBhbmQgYnJhaW4uc2NyZWVuLnlfcG9zaXRpb24oKSA8PSBzZWxmLnkgKyBzZWxmLmggYW5kIG5vdCBicmFpbi5zY3JlZW4ueV9wb3NpdGlvbigpIDw9IHNlbGYueSBhbmQgbm90IGJyYWluLnNjcmVlbi54X3Bvc2l0aW9uKCkgPD0gc2VsZi54OgogICAgICAgICAgICAgICAgb2MgPSBzZWxmLmMKICAgICAgICAgICAgICAgIHNlbGYuYyA9IENvbG9yLldISVRFCiAgICAgICAgICAgICAgICBicmFpbi5zY3JlZW4uY2xlYXJfc2NyZWVuKCkKICAgICAgICAgICAgICAgIHNlbGYuZHJhdygpCgogICAgICAgICAgICAgICAgd2hpbGUgYnJhaW4uc2NyZWVuLnByZXNzaW5nKCk6CiAgICAgICAgICAgICAgICAgICAgd2FpdCguMDA1LFNFQ09ORFMpCgogICAgICAgICAgICAgICAgc2VsZi5jID0gb2MKICAgICAgICAgICAgICAgIHNlbGYuZHJhdygpCiAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICAgICByZXR1cm4gRmFsc2UKCiAgICBkZWYgaGlkZV9vYmplY3Qoc2VsZik6CiAgICAgICAgc2VsZi5oaWRlID0gVHJ1ZQoKICAgIGRlZiBzaG93X29iamVjdChzZWxmKToKICAgICAgICBzZWxmLmhpZGUgPSBGYWxzZQoKY2xhc3Mgc2NyZWVubGliX3NjcmVlbl9tZW51KG9iamVjdCk6CiAgICBkZWYgX19pbml0X18oc2VsZixuYW1lPSJtZW51Iik6CiAgICAgICAgc2VsZi5uYW1lID0gbmFtZQogICAgICAgIHNlbGYuYnV0dG9ucyA9IFtdCiAgICAgICAgc2VsZi5vYmplY3RzID0gW10KICAgICAgICBzZWxmLnNob3duID0gRmFsc2UKCiAgICBkZWYgbWFpbmxvb3Aoc2VsZik6CiAgICAgICAgc2VsZi5zaG93biA9IFRydWUKICAgICAgICBicmFpbi5zY3JlZW4uY2xlYXJfc2NyZWVuKCkKICAgICAgICB3aGlsZSBzZWxmLnNob3duOgogICAgICAgICAgICB3YWl0KC4wMjUsU0VDT05EUykKCgogICAgICAgICAgICBmb3IgeCBpbiBzZWxmLmJ1dHRvbnM6CiAgICAgICAgICAgICAgICB4LmRyYXcoKQoKICAgICAgICAgICAgICAgIGlmIHguaXNfcHJlc3NpbmcoKToKICAgICAgICAgICAgICAgICAgICBicmFpbi5zY3JlZW4uY2xlYXJfc2NyZWVuKCkKICAgICAgICAgICAgICAgICAgICByZXR1cm4geC50ZXh0CgogICAgICAgICAgICBmb3IgeCBpbiBzZWxmLm9iamVjdHM6CiAgICAgICAgICAgICAgICB4LmRyYXcoKQoKICAgIGRlZiBhbGVydChzZWxmLHRleHQpOgogICAgICAgIGJyYWluLnNjcmVlbi5kcmF3X3JlY3RhbmdsZSgxLDEsNjAwLDYwMCxDb2xvci5CTFVFKQogICAgICAgIGJyYWluLnNjcmVlbi5zZXRfY3Vyc29yKDYsMjIpCiAgICAgICAgYnJhaW4uc2NyZWVuLnNldF9maWxsX2NvbG9yKENvbG9yLkJMVUUpCiAgICAgICAgYnJhaW4uc2NyZWVuLnByaW50KHRleHQpCiAgICAgICAgd2FpdCgyLjUsU0VDT05EUykKCmNsYXNzIHNjcmVlbmxpYl9jb250cm9sbGVyX21lbnUob2JqZWN0KToKICAgIGRlZiBfX2luaXRfXyhzZWxmKToKICAgICAgICBzZWxmLml0ZW1zID0gW10KICAgICAgICBzZWxmLnNlbGVjdGVkSXRlbSA9IDAKCiAgICBkZWYgY3JlYXRlX2l0ZW0oc2VsZiwgdGV4dCk6CiAgICAgICAgc2VsZi5pdGVtcy5hcHBlbmQodGV4dCkKCiAgICBkZWYgY3JlYXRlX2l0ZW1zKHNlbGYsIGl0ZW1zKToKICAgICAgICBmb3IgeCBpbiBpdGVtczoKICAgICAgICAgICAgc2VsZi5pdGVtcy5hcHBlbmQoeCkKCiAgICBkZWYgZHJhdyhzZWxmKToKICAgICAgICBjb250cm9sbGVyXzEuc2NyZWVuLmNsZWFyX3NjcmVlbigpCiAgICAgICAgY29udHJvbGxlcl8xLnNjcmVlbi5zZXRfY3Vyc29yKDAsMCkKICAgICAgICBmb3IgaXRlbSBpbiBzZWxmLml0ZW1zOgogICAgICAgICAgICBpZiBzZWxmLml0ZW1zLmluZGV4KGl0ZW0pID09IHNlbGYuc2VsZWN0ZWRJdGVtOgogICAgICAgICAgICAgICAgY29udHJvbGxlcl8xLnNjcmVlbi5wcmludCgiPiAiK2l0ZW0pCgogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgY29udHJvbGxlcl8xLnNjcmVlbi5wcmludCgiICAiK2l0ZW0pCiAgICAgICAgICAgIGNvbnRyb2xsZXJfMS5zY3JlZW4uc2V0X2N1cnNvcihjb250cm9sbGVyXzEuc2NyZWVuLnJvdygpKzEsIDApCgogICAgZGVmIHJ1bihzZWxmKToKICAgICAgICBzZWxmLmRyYXcoKQoKICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICBpZiBjb250cm9sbGVyXzEuYnV0dG9uRG93bi5wcmVzc2luZygpOgogICAgICAgICAgICAgICAgaWYgbGVuKHNlbGYuaXRlbXMpIC0gMSAhPSBzZWxmLnNlbGVjdGVkSXRlbToKICAgICAgICAgICAgICAgICAgICBzZWxmLnNlbGVjdGVkSXRlbSArPSAxCiAgICAgICAgICAgICAgICAgICAgc2VsZi5kcmF3KCkKCiAgICAgICAgICAgIGVsaWYgY29udHJvbGxlcl8xLmJ1dHRvblVwLnByZXNzaW5nKCk6CiAgICAgICAgICAgICAgICBpZiBzZWxmLnNlbGVjdGVkSXRlbSAhPSAwOgogICAgICAgICAgICAgICAgICAgIHNlbGYuc2VsZWN0ZWRJdGVtIC09IDEKICAgICAgICAgICAgICAgICAgICBzZWxmLmRyYXcoKQogICAgICAgICAgICAgICAgd2FpdCguMSxTRUNPTkRTKQoKICAgICAgICAgICAgZWxpZiBjb250cm9sbGVyXzEuYnV0dG9uUmlnaHQucHJlc3NpbmcoKToKICAgICAgICAgICAgICAgIHJldHVybiBzZWxmLml0ZW1zW3NlbGYuc2VsZWN0ZWRJdGVtXQoKcHJpbnQoIlttb2R1bGUvc2NyZWVubGliXTogTG9hZGVkIikK""")
f.close()
print("DOne")

try:
    try:
        load_module = print#stops vex from saying the function doesn't exist
        screenlib_screen_menu = print
        screenlib_screen_button = print
        screenlib_screen_text = print
        simplemenu_menu = print
        screenlib_controller_menu = print
        simplemenu_controller_menu = print  

    except:
        print("Failed to create load_module, screenlib_screen_(menu,button,text)")#not sure why this would happen, but just in case

    try:
        f = open('module_loader.py', 'r'); module_loader = f.read(); f.close()#Get's the code off of the sd card
        exec(module_loader)#Runs the code
        try:
            load_module('screenlib')#Loads the code in modules/screenlib.module from the sd card
        except:
            print("Failed to load screenlib, but module_loader.py loaded fine")#The module might not be on the sd card or there it has a error
        try:
            load_module('simplemenulib')#Loads the code in modules/simplemenulib.module from the sd card
        except:
            print("Failed to load simplemenulib, but module_loader.py loaded file")#The module might not be on the sd card or there it has a error
    except:
        print("module_loader.py failed to load, is it on the sd card?")#Explains itself
except:
    print("Somthing really really went wrong with the module loader")#This should never happen but just in case



selected_auton = None

blue_autons = ['test1','test2','test3']#The autons that can be ran, this is mainly for the menu
red_autons = ['test1','test2','test3']#The autons that can be ran, this is mainly for the menu


#The main menu that gets printed to the screen
def MainBrainMenu():
    global selected_auton
    #Creates a new menu
    menu1 = simplemenu_menu()
    
    #This is a menu tree, a menu tree is somthing i made to make menus super fast
    menu_tree = {
        "Competition": {
            "text": "Competition",
            "options": [
                {
                    "text": "Red",
                    "options": menu1.list_to_options(red_autons,return_value="comp-[text]")#Converts red_autons into a list that's can be read by simplemenulib
                    #return_value="comp-[text]" means, when the button is clicked return the value comp-<the text of the button>
                },
                {
                    "text": "Blue",
                    "options": menu1.list_to_options(blue_autons,return_value="comp-[text]")#Converts blue_autons into a list that's can be read by simplemenulib
                    #return_value="comp-[text]" means, when the button is clicked return the value comp-<the text of the button>
                }
            ]
        },
        "Drive": {
            "text": "Drive",
            "return-value": "Drive"
        },

        "Auton": {
            "text": "Auton",
            "options": [
                {
                    "text": "Red",
                    "options": menu1.list_to_options(red_autons,return_value="auton-[text]")#Converts red_autons into a list that's can be read by simplemenulib
                    #return_value="comp-[text]" means, when the button is clicked return the value comp-<the text of the button>
                },
                {
                    "text": "Blue",
                    "options": menu1.list_to_options(blue_autons,return_value="auton-[text]")#Converts blue_autons into a list that's can be read by simplemenulib
                    #return_value="comp-[text]" means, when the button is clicked return the value comp-<the text of the button>
                }
            ]
        }
    }

    selected_option = menu1.run_tree(menu_tree)#menu1.run_tree returns whatever gets selected from the menu tree
    print(selected_option)#Just prints it for debugging

    if selected_option == 'Drive':#If the button clicked was called 'Driver'
        driver()
    
    elif 'comp' in selected_option:#If the button clicked was under the comp portion of the menu
        selected_auton = selected_option.split('comp-')[1]
        print("Running comp with auton "+selected_auton)
        Competition(driver, run_auton)
    
    elif 'auton' in selected_option:#If the button clicked was under the auton portion of the menu
        selected_auton = selected_option.split('auton-')[1]
        print("Running non comp auton "+selected_auton)
        run_auton()


def driver():#Driver Loop
    while True:
        StrafePos = controller_1.axis4.position()
        HDriveMotor.set_velocity(StrafePos*2)
        HDriveMotor.spin(FORWARD)

def run_auton():
    if selected_auton == "blahblahblah":
        pass




MainBrainMenu()#Runs the brain menu

#brain.screen.draw_image_from_file("download.png",50,50)
