from vex import *

#For updating modules
if False:
    f = open('modules/simplemenulib.module', 'w')
    f.write("""aW1wb3J0IG1hdGgKCmNsYXNzIHNpbXBsZW1lbnVfbWVudShvYmplY3QpOgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIHNlbGYuZGVidWcgPSBGYWxzZQogICAgICAgIHNlbGYubWVudV9jb25maWcgPSB7CiAgICAgICAgICAgICJ5IjogMSwKICAgICAgICAgICAgIngiOiAxLAogICAgICAgICAgICAieF9wYWRkaW5nIjogMTAsCiAgICAgICAgICAgICJ5X3BhZGRpbmciOiAxMCwKICAgICAgICAgICAgImJ0bl93aWR0aCI6IDEyMCwKICAgICAgICAgICAgImJ0bl9oZWlnaHQiOiAxMTAsCiAgICAgICAgICAgICJidXR0b25zX3Blcl9yb3ciOiAwLAogICAgICAgICAgICAiYnV0dG9uc19wZXJfY29sdW1uIjogMCwKICAgICAgICAgICAgImRyYXduX2J1dHRvbnMiOiAwLAogICAgICAgICAgICAibWF4X2J1dHRvbnMiOiAwLAogICAgICAgICAgICAiYnRuX2NvbG9yIjogJ2dyZWVuJywKICAgICAgICAgICAgInRleHRfcGFkZGluZ194IjogMSwKICAgICAgICAgICAgInRleHRfcGFkZGluZ195IjogMSwKICAgICAgICAgICAgInRleHRfb2Zmc2V0X3giOiAxMywKICAgICAgICAgICAgInRleHRfb2Zmc2V0X3kiOiA2CiAgICAgICAgfQoKICAgICAgICB0cnk6CiAgICAgICAgICAgIHNlbGYubWVudV9jb25maWdbJ2J0bl9jb2xvciddID0gQ29sb3IuQkxVRQoKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50KCJbbW9kdWxlL3NpbXBsZW1lbnVdOiBDb2xvci5CTFVFIG5vdCBmb3VuZCwgaWYgdGhpcyBpcyBub3QgYmVpbmcgcmFuIG9uIHRoZSBicmFpbiB0aGVuIGRvIG5vdCB3b3JyeSBhYm91dCB0aGlzIikKCiAgICAgICAgdHJ5OgogICAgICAgICAgICBzZWxmLm1lbnUgPSBzY3JlZW5saWJfc2NyZWVuX21lbnUoKQoKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHNlbGYubWVudSA9IE5vbmUKICAgICAgICAgICAgcHJpbnQoIlttb2R1bGUvc2ltcGxlbWVudV06IHNjcmVlbmxpYiBub3QgZm91bmQhIikKCiAgICAgICAgb2Zmc2V0ID0gc2VsZi5tZW51X2NvbmZpZ1snYnRuX3dpZHRoJ10gKyBzZWxmLm1lbnVfY29uZmlnWyd4X3BhZGRpbmcnXQogICAgICAgIHNlbGYubWVudV9jb25maWdbJ2J1dHRvbnNfcGVyX3JvdyddID0gbWF0aC5mbG9vcig0ODAgLyBvZmZzZXQpCiAgICAgICAgb2Zmc2V0ID0gc2VsZi5tZW51X2NvbmZpZ1snYnRuX2hlaWdodCddICsgc2VsZi5tZW51X2NvbmZpZ1sneF9wYWRkaW5nJ10KICAgICAgICBzZWxmLm1lbnVfY29uZmlnWydidXR0b25zX3Blcl9jb2x1bW4nXSA9IG1hdGguZmxvb3IoMjcyIC8gb2Zmc2V0KQoKICAgICAgICBzZWxmLm1lbnVfY29uZmlnWydtYXhfYnV0dG9ucyddID0gc2VsZi5tZW51X2NvbmZpZ1snYnV0dG9uc19wZXJfcm93J10gKiBzZWxmLm1lbnVfY29uZmlnWydidXR0b25zX3Blcl9jb2x1bW4nXQoKICAgICAgICBwcmludCgnW21vZHVsZS9zaW1wbGVtZW51XTogU2NyZWVuIFNpemUgJytzdHIoc2VsZi5tZW51X2NvbmZpZ1snYnV0dG9uc19wZXJfcm93J10pKyJ4IitzdHIoc2VsZi5tZW51X2NvbmZpZ1snYnV0dG9uc19wZXJfY29sdW1uJ10pKycgYnV0dG9ucyAnK3N0cihzZWxmLm1lbnVfY29uZmlnWydtYXhfYnV0dG9ucyddKSkKCgogICAgZGVmIHJlZ2lzdGVyX2J1dHRvbihzZWxmLCB0eHQpOgogICAgICAgIGlmIHNlbGYubWVudV9jb25maWdbJ2RyYXduX2J1dHRvbnMnXSArIDEgPD0gc2VsZi5tZW51X2NvbmZpZ1snbWF4X2J1dHRvbnMnXToKICAgICAgICAgICAgbmV3QnV0dG9uID0gc2NyZWVubGliX3NjcmVlbl9idXR0b24oCiAgICAgICAgICAgIHggPSBzZWxmLm1lbnVfY29uZmlnWyd4J10sCiAgICAgICAgICAgIHkgPSBzZWxmLm1lbnVfY29uZmlnWyd5J10sCiAgICAgICAgICAgIHcgPSBzZWxmLm1lbnVfY29uZmlnWydidG5fd2lkdGgnXSwKICAgICAgICAgICAgaCA9IHNlbGYubWVudV9jb25maWdbJ2J0bl9oZWlnaHQnXSwKICAgICAgICAgICAgYyA9IHNlbGYubWVudV9jb25maWdbJ2J0bl9jb2xvciddLAogICAgICAgICAgICB0ZXh0ID0gdHh0LAogICAgICAgICAgICB0YyA9IHNlbGYubWVudV9jb25maWdbJ3RleHRfcGFkZGluZ195J10sCiAgICAgICAgICAgIHRyID0gc2VsZi5tZW51X2NvbmZpZ1sndGV4dF9wYWRkaW5nX3gnXSkKICAgICAgICAgICAgc2VsZi5tZW51LmJ1dHRvbnMuYXBwZW5kKG5ld0J1dHRvbikKCiAgICAgICAgICAgIHNlbGYubWVudV9jb25maWdbJ3gnXSArPSBzZWxmLm1lbnVfY29uZmlnWydidG5fd2lkdGgnXSArIHNlbGYubWVudV9jb25maWdbJ3hfcGFkZGluZyddCiAgICAgICAgICAgIHNlbGYubWVudV9jb25maWdbJ3RleHRfcGFkZGluZ194J10gKz0gc2VsZi5tZW51X2NvbmZpZ1sndGV4dF9vZmZzZXRfeCddCgogICAgICAgICAgICBpZiBzZWxmLm1lbnVfY29uZmlnWydidXR0b25zX3Blcl9yb3cnXSA9PSBzZWxmLm1lbnVfY29uZmlnWydkcmF3bl9idXR0b25zJ10gKyAxOgogICAgICAgICAgICAgICAgc2VsZi5tZW51X2NvbmZpZ1sneSddICs9IHNlbGYubWVudV9jb25maWdbJ2J0bl9oZWlnaHQnXSArIHNlbGYubWVudV9jb25maWdbJ3lfcGFkZGluZyddCiAgICAgICAgICAgICAgICBzZWxmLm1lbnVfY29uZmlnWyd4J10gPSAxCiAgICAgICAgICAgICAgICBzZWxmLm1lbnVfY29uZmlnWyd0ZXh0X3BhZGRpbmdfeSddICs9IHNlbGYubWVudV9jb25maWdbJ3RleHRfb2Zmc2V0X3knXQogICAgICAgICAgICAgICAgc2VsZi5tZW51X2NvbmZpZ1sndGV4dF9wYWRkaW5nX3gnXSA9IDEKCiAgICAgICAgICAgIHNlbGYubWVudV9jb25maWdbJ2RyYXduX2J1dHRvbnMnXSArPSAxCgoKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludCgiW21vZHVsZS9zaW1wbGVtZW51XTogTWF4IGFtb3VudCBvZiBidXR0b25zIGhhdmUgYmVlbiBjcmVhdGVkIikKCiAgICBkZWYgcmVnaXN0ZXJfYnV0dG9ucyhzZWxmLCBidXR0b25zKToKICAgICAgICBmb3IgeCBpbiBidXR0b25zOgogICAgICAgICAgICBzZWxmLnJlZ2lzdGVyX2J1dHRvbih4KQoKICAgIGRlZiBydW5fdHJlZShzZWxmLCB0cmVlKToKICAgICAgICB0b3BNZW51QnV0dG9ucyA9IFtdCgogICAgICAgIGZvciBtZW51IGluIHRyZWU6CiAgICAgICAgICAgIHRvcE1lbnVCdXR0b25zLmFwcGVuZChtZW51KQoKICAgICAgICBtZW4xID0gc2ltcGxlbWVudV9tZW51KCkKICAgICAgICBtZW4xLnJlZ2lzdGVyX2J1dHRvbnModG9wTWVudUJ1dHRvbnMpCgogICAgICAgIHNlbGVjdGVkQnV0dG9uID0gbWVuMS5ydW4oKQoKCiAgICAgICAgaWYgJ29wdGlvbnMnIG5vdCBpbiB0cmVlW3NlbGVjdGVkQnV0dG9uXToKICAgICAgICAgICAgcmV0dXJuIHRyZWVbc2VsZWN0ZWRCdXR0b25dWydyZXR1cm4tdmFsdWUnXQoKICAgICAgICBlbHNlOgogICAgICAgICAgICBwcmludCgiUmVydW5uaW5nIikKICAgICAgICAgICAgbnQgPSB7fQogICAgICAgICAgICBmb3IgeCBpbiB0cmVlW3NlbGVjdGVkQnV0dG9uXVsnb3B0aW9ucyddOgogICAgICAgICAgICAgICAgdmFsID0geFsndGV4dCddCiAgICAgICAgICAgICAgICBudFt2YWxdID0geAoKICAgICAgICAgICAgcmV0dXJuIHNlbGYucnVuX3RyZWUobnQpCgogICAgZGVmIGxpc3RfdG9fb3B0aW9ucyhzZWxmLCBkYXRhLCBhY3Rpb249J3JldHVybicsIHJldHVybl92YWx1ZT0nW3RleHRdJyk6CiAgICAgICAgb3B0aW9ucyA9IFtdCiAgICAgICAgZm9yIHggaW4gZGF0YToKICAgICAgICAgICAgbmV3X29wdGlvbiA9IHsKICAgICAgICAgICAgICAgICJ0ZXh0IjogeCwKICAgICAgICAgICAgICAgICJyZXR1cm4tdmFsdWUiOiByZXR1cm5fdmFsdWUucmVwbGFjZSgnW3RleHRdJyx4KQogICAgICAgICAgICB9CgogICAgICAgICAgICBvcHRpb25zLmFwcGVuZChuZXdfb3B0aW9uKQoKICAgICAgICByZXR1cm4gb3B0aW9ucwoKICAgIGRlZiBydW4oc2VsZik6CiAgICAgICAgcmV0dXJuIHNlbGYubWVudS5tYWlubG9vcCgpCgpwcmludCgiW21vZHVsZS9zaW1wbGVtZW51bGliXTogTG9hZGVkIikK""")
    f.close()
    print('Done')

try:
    try:
        load_module = print#stops vex from saying the function doesn't exist
        screenlib_screen_menu = print
        screenlib_screen_button = print
        screenlib_screen_text = print
        simplemenu_menu = print

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




blue_autons = ['test1','test2','test3']#The autons that can be ran, this is mainly for the menu
red_autons = ['test1','test2','test3']#The autons that can be ran, this is mainly for the menu


#The main menu that gets printed to the screen
def MainBrainMenu():
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
        autonToRun = selected_option.split('comp-')[1]
        print("Running comp with auton "+autonToRun)
    
    elif 'auton' in selected_option:#If the button clicked was under the auton portion of the menu
        autonToRun = selected_option.split('auton-')[1]
        print("Running non comp auton "+autonToRun)



def driver():#Driver Loop
    while True:
        StrafePos = controller_1.axis4.position()
        MiddleMotor.set_velocity(StrafePos*2)
        MiddleMotor.spin(FORWARD)


MainBrainMenu()#Runs the brain menu
