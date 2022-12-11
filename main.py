import modules.banner as banner
import modules.selUI.selUI as selUI
import modules.selUI.uniKey as uniKey
import modules.ANSIcolour as ansi
import ui
import shared
import os



cui = [   ansi.RESET+'Willkommen zum Link Filesharing-Script!' + 14*' '+ banner.lgbtq[0],
          'Bitte wähle eine der Optionen, um fortzufahren:' +6*' '+banner.lgbtq[1],
          ' '*53+banner.lgbtq[2],
          ]
    
entr = ['Share over Bluetooth'+' '*31+banner.lgbtq[5],
        'Connect to Bluetooth',
        'Share over localnetwork']
        
        
curSelui=selUI.SelectionMenu.create(entr, '<t>')

def mainloop():
    for i in cui:
        print(i)
    print(curSelui.refresh().replace('<t>', ' '*53+banner.lgbtq[3]).replace('▄'*100, '▄'*30+' '*23+banner.lgbtq[4]))
    
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
        # Elif since switch statements suck in python
        sel=curSelui.select()
        if sel == entr[0]:
            ui.run_bluetooth()
        elif sel == entr[2]:
            ui.run_localnetwork()

    os.system('clear')





os.system('clear')
while True:
    try:
        mainloop()
    except KeyboardInterrupt:
        shared.escape()
    except InterruptedError:
        shared.escape()