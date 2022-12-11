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



def run_localnetwork():
    import modules.networkshare as netshare
    config = netshare.localnetworkcfg(100000, os.getcwd(), 'TWOFISH', '')
    entr=[]
    curSelui = selUI.SelectionMenu.create(entr, 'Network connection setup')
    while True:
        entr=[  'Port: '+str(config.port),
            'File/Folder-Path: '+str(config.pth),
            'Encryption-Cypher: '+str(config.cypher),
            'Password: '+'*'*len(config.pswd),
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
            elif sel == entr[2]:
                config.selectcypher()
            elif sel == entr[3]:
                config.selectpswd()
            elif sel == entr[4]:
                netshare.run(config)
                
    



