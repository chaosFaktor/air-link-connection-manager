from collections import namedtuple
import os



"""
class 2axes
(object):


    clock_ison = True
    lenLeft = 14
    lenRight =14
    seperator = " | "


    def __init__(self, clock_ison, ):

        if clock_ison:
            self.heading = (("_"*(lenLeft+lenRight+len(seperator)))
            + "\n")






def build2axesSelectionMenutoString(config):
"""


class SelectionMenu:

##     How to create a SelectionMenu-Object
    #  It takes the options to choose from, a heading, and an array containing cosmetic specifications
    #  The object should be initialized as following:
    #
    #  seperator, selection-flag, null-flag, startpoint, subHeading, maxLen
#Index:    0    | |     1       | |    2   | |    3    | |    4   |  |  5 |
    #
    # The seperator represents the string between the selection flag, and the option, (in 'O|this is an option' the '|' is the seperator)
    # The seperator can contain more than one character ('O<>this is an option')
    #
    # The selection flag (refered to as selFlag in the code) indicates the users current selection ('O|this is an option', the 'O' is the
    # selection flag)
    #
    # The null flag will be used on options not currently selected by the user (' |this is an option', the ' ' is the null flag)
    #
    # The startpoint specifies the index of the entry, the user selection should start at
    #
    # The subHeading describes the char, that should be used to build the seperator under the heading
    # ('This is the title
    #   -------------------
    #   |this is an option', the '-' char)
    #
    # The maxLen describes the length to cut any line of the menu
    #
    #
    defaultOptions=['│', 'O', ' ', 0, '▄', 100]
    seperator = "|"
    selFlag = "O"
    nulFlag = " "
    sel = 0
    subHeading = " "
    maxLen = 60


    def __init__(self, entrys, title, seperator, selFlag, nullFlag, sel, subHeading, maxLen):
        self.entrys = entrys
        self.title = title
        self.seperator = seperator
        self.selFlag = selFlag
        self.nullFlag = nullFlag
        self.sel = sel
        self. subHeading = subHeading
        self.maxLen = maxLen
        try:
            self.vcwd = os.getcwd()
        except:
            pass



    def create(entr, title, options=defaultOptions):
        #menu = namedtuple('menu', ['entrys', 'title', 'seperator', 'selFlag', 'nullFlag', 'sel', 'subHeading', 'maxLen'])


        return SelectionMenu(entr, title, options[0], options[1], options[2], options[3], options[4], options[5])

    def getOpt(menu):
        return [menu.seperator, menu.selFlag, menu.nulFlag, menu.sel, menu.subHeading, menu.maxLen]

    def selUp(menu):
        if menu.sel+1<len(menu.entrys):
            menu.sel+=1
        return menu


    def selDown(menu):
        if menu.sel-1>=0:
            menu.sel-=1
        return menu
    
    def update(menu, entr, title, options=defaultOptions):
        menu.entrys=entr
        menu.title=title
        menu.seperator=options[0]
        menu.selFlag=options[1]
        menu.nullFlag=options[2]
        menu.sel=options[3]
        menu.subHeading=options[4]
        menu.maxLen=options[5]
        return menu



    def refresh(menu):
        output = menu.title+"\n" + (menu.subHeading*menu.maxLen) + "\n"
        for i in range(0, len(menu.entrys)):
            if menu.sel == i:
                output += (menu.selFlag+menu.seperator+menu.entrys[i])[:menu.maxLen]
            else:
                output += (menu.nullFlag+menu.seperator+menu.entrys[i])[:menu.maxLen]
            output+="\n"
        return output

    def select(menu):
        return menu.entrys[menu.sel]


    def scanvcwd(menu):
    #   files as variable name instead of folders and files, since 'Directory' is a file type
        files=[[], []]
        for i in os.listdir(menu.vcwd):        
            if os.path.isfile(menu.vcwd+i):
                if len(i)<15:
                    i+=' '*(15-len(i))
                i=i[:15]
                files[1].append(i+'<file>')
            else:
                if len(i)<15:
                    i+=' '*(15-len(i))
                i=i[:15]
                files[0].append(i+ '<folder>')
        return files

    
    def fileDialog(menu, selection=''):
        if menu.vcwd[-1] != '/':
            menu.vcwd+='/'
        options=menu.getOpt()
        

        filesAndDirs=menu.scanvcwd()
        files=filesAndDirs[1]
        dirs=filesAndDirs[0]
        if len(files)+len(dirs)+1<menu.sel:
            menu.sel=len(files)+len(dirs)
        options[3]=menu.sel
        


        
        if selection != '':
            if selection in dirs:
                menu.vcwd+=(selection.replace('<folder>', '')).rstrip() +'/'
            elif selection in files:
                return menu.vcwd+(selection.replace('<file>', '')).rstrip()
            elif selection == '..':
            #   shorten to the last entry of '/'
                menu.vcwd=menu.vcwd.rsplit('/', 2)[0] +'/'
                if menu.vcwd=='':
                    menu.vcwd='/'
            elif selection == 'Choose this folder':
            #   Directorys may be recognised by the '/'-char at the end of the returned string.
                return menu.vcwd+menu.vcwd+(selection.replace('<folder>', '')).rstrip() +'/'
            

            filesAndDirs=menu.scanvcwd()
            files=filesAndDirs[1]
            dirs=filesAndDirs[0]
        
        entr=dirs+files
        entr.insert(0, '..')
        entr.insert(1, 'Choose this folder')

        menu.update(entr, menu.vcwd, options)
        
        





######        Testing:



##   Code Preset of using the SelectionMenu fileDialog
'''
import uniKey
os.system('clear')
mymen=SelectionMenu.create([], '')
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
'''
    










"""
mymen = SelectionMenu(["Option1", "Option2", "Option3"], "Nice Heading", "|", "O", " ", 0, "_", 24)

while True:
    print(SelectionMenu.refresh(mymen))
    inp = input()
    if inp == "w":
        SelectionMenu.selDown(mymen)
    if inp == "s":
        mymen.selUp()
        #SelectionMenu.selUp(mymen)
    if inp == "d":
        print(SelectionMenu.select(mymen))
"""




