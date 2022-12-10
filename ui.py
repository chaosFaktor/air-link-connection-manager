import modules.selUI.selUI as selUI
import modules.selUI.uniKey as uniKey
import shared
import os






def run_bluetooth():

    entr=[  '',
            'start']
    curSelui = selUI.SelectionMenu.create(entr, 'Bluetooth connection setup')

    try:
        inp = uniKey.getch()
    except InterruptedError:
        shared.escape()
    if inp in 'wW8':
        curSelui.selDown()
    elif inp in 'sS2':
        curSelui.selUp()
    


    import modules.bluetoothshare as blueshare
    blueshare.run()






class localnetworkcfg:
    port = 9999
    pth = ''
    def __init__(self, port, pth):
        self.port=port
        self.pth=pth
    def selectport(cfg):
        print('Please select a port the server should run on  (If unsure select a random high number)')
        while True:
            try:
                print(cfg.port)
                cfg.port = int(input('->'))
                os.system('clear')
                return cfg
            except InterruptedError:
                print()
                shared.escape()
            except KeyboardInterrupt:
                print()
                shared.escape()
            except:
                os.system('clear')
                print('Selection error!  Please enter an integer number')
    def selectpth(cfg):
        os.system('clear')
        mymen=selUI.SelectionMenu.create([], '')
        selection=''
        while True:
            dialog = mymen.fileDialog(selection)
            if dialog != None:
                if dialog[-1]=='/':
                    print('returned folder: '+dialog)
                else:
                    print('returned file: '+dialog)

            selection=''
            print(mymen.refresh())
            print(mymen.vcwd)
            try: inp=uniKey.getch()
            except InterruptedError:
                quit()
            os.system('clear')
            if inp in "sS2":
                mymen.selUp()
            elif inp in "wW8":
                mymen.selDown()
            elif inp in 'dD6 \n':
                selection=mymen.select()
            


def run_localnetwork():

    config = localnetworkcfg(100000, os.getcwd())
    entr=[  'Port: '+str(localnetworkcfg.port),
            'File/Folder-Path: '+localnetworkcfg.pth,
            'start']
    curSelui = selUI.SelectionMenu.create(entr, 'Network connection setup')

    while True:
        entr=[  'Port: '+str(config.port),
            'File/Folder-Path: '+str(config.pth),
            'start']
        opt_no_sel=selUI.SelectionMenu.defaultOptions
        opt_no_sel[3]=curSelui.sel
        curSelui.update(entr, 'Network connection setup', opt_no_sel)

        print(curSelui.refresh())
        try:
            inp = uniKey.getch()
            os.system('clear')
        except InterruptedError:
            shared.escape()
        if inp in 'wW8':
            curSelui.selDown()
        elif inp in 'sS2':
            curSelui.selUp()
        elif inp in 'dD6 \n':
            os.system('clear')
            sel = curSelui.select()
            if sel == entr[0]:
                config.selectport()
            elif sel == entr[1]:
                config.selectpth()
                
    


    import modules.networkshare as localshare
    localshare.run()