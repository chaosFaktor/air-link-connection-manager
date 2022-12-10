import modules.selUI.selUI as selUI
import modules.selUI.uniKey as uniKey
import modules.ANSIcolour as ansi
import shared
import os



class localnetworkcfg:
    port = 9999
    pth = ''
    cypher = 'TWOFISH'
    pswd = ''
    def __init__(self, port, pth, cypher, pswd):
        self.port=port
        self.pth=pth
        self.cypher=cypher
        self.pswd=pswd
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
            ##  !!! Remember you can differenciate files and dirs from the '/'
                cfg.pth=dialog
                return cfg
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
            
    def selectcypher(cfg):
        mymen=selUI.SelectionMenu.create(['TWOFISH', 'AES256', 'none'], 'Please select your prefered Encryption-Cypher (Using no encryption is highly dangerous, since your connection is performed using an unsecure socket-connection!) (AES-256 is most commonly used)')
        while True:
            print(mymen.refresh())
            inp = uniKey.getch()
            os.system('clear')
            if inp in 'Ww8':
                mymen.selDown()
            if inp in 'Ss2':
                mymen.selUp()
            if inp in 'Dd6 \n':
                cfg.cypher=mymen.select()
                return cfg
    
    def selectpswd(cfg):
        
        while True:
            print('Please select your password for symmetric encryption. The password should be at least 6 characters long, and contain numbers, lower- and uppercase letters, and special-characters')
            inp = input('->')
            os.system('clear')
            print('Please re-enter your password')
            inpb = input('->')
            os.system('clear')
            if inp==inpb:
                cfg.pswd=inp
                return cfg






def run(cfg):
    os.system('clear')
    if len(cfg.pswd)<6 | cfg.cypher=='none':
        while True:
            print(ansi.Bold.RED+'Warning!!!  |  You entered an insecure password, or disabled encryption. This is highly inadvised, only continue if you know what you\'re doing!'+ansi.RESET)
            print('Enter YES to continue, or NO to quit')
            inp = input('->')
            if inp == 'YES':
               break 
            elif inp == 'NO':
                shared.escape()

    if cfg.pth[-1] == '/':  #   Directory

