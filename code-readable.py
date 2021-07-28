from vex import *


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

    if selected_option == 'Driver':#If the button clicked was called 'Driver'
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
        MiddleMotor.set_velocity(StrafePos*2)
        MiddleMotor.spin(FORWARD)

def run_auton():
    if selected_auton == "blahblahblah":
        pass




#MainBrainMenu()#Runs the brain menu

#brain.screen.draw_image_from_file("download.png",50,50)
