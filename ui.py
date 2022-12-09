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
    def selectport(self):
        print('Please select a port the server should run on  (If unsure select a random high number)')
        port = int(input('->'))
        return port


def run_localnetwork():

    config = localnetworkcfg

    entr=[  'Port: '+str(localnetworkcfg.port),
            'File/Folder-Path: '+localnetworkcfg.pth,
            'start']
    curSelui = selUI.SelectionMenu.create(entr, 'Network connection setup')

    while True:
        print(curSelui.refresh())
        try:
            inp = uniKey.getch()
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
        os.system('clear')
    


    import modules.networkshare as localshare
    localshare.run()