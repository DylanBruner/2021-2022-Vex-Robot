f = open('base64.py', 'r'); base64code = f.read(); f.close()
exec(base64code)

print("[moduler-loader]: Loaded")

def load_module(name):
    print('[module-loader]: Loading '+name)
    f = open('modules/'+name+'.module', 'r')
    moduleData = f.read()
    f.close()

    moduleData = b64decode(bytes(moduleData, 'utf-8')).decode('utf-8')
    exec(moduleData, globals())

print("[moduler-loader]: Loaded")
