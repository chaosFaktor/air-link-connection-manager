import modules.ANSIcolour as ansi 



"""def fillUpStr(a, b, filler=' '):
    if len(a)>len(b):
        b+=filler*(len(a)-len(b))
    else:
        a+=filler*(len(b)-len(a))
    return (a, b)


def combine(a, b, spacing=1, spacer=' '):
    out = ''
    # Splitting a and b into single lines to 
    a=a.split('\n')
    b=b.split('\n')

    for i in range(0, len(a)):
        fill=fillUpStr(a[i], b[i], spacer)
        out+=fill[0]+(spacing*spacer)+fill[1]+'\n'

    
    return out
"""        

lgbtq=[ 
        ansi.RED+'█'*27+ansi.RESET,
        '\x1b[38;5;208m'+('█'*27)+ansi.RESET,
        '\x1b[38;5;226m'+'█' *27+ansi.RESET,
        ansi.GREEN+'█'  *27+ansi.RESET,
        ansi.BLUE+'█'   *27+ansi.RESET,
        ansi.PURPLE+'█' *27+ansi.RESET
        ]


     






## Testing
if __name__ == '__main__':
    
    #print(fillUp('hallo', 'w', '_'))
    tsta='''----
            |  |
            ----'''
    tstb='''FFFFFF
            OOOOOO
            FFFFFF'''

    for i in lgbtq:
        print(i)
    

    pass