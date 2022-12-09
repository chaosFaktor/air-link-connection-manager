import sys, termios,tty




def getch():
    try:
        orig_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdout)
        inp = sys.stdin.read(1)[0]
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
        return inp
    except KeyboardInterrupt:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
        raise InterruptedError
    except:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)




##Testing:

