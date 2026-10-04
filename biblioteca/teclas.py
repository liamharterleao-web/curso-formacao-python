import os, sys

if os.name == "nt":
    import msvcrt

    def get_key():
        return msvcrt.getch()

else:  # Linux / Mac
    import tty, termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':  # sequência de escape (setas)
                ch += sys.stdin.read(2)
            return ch.encode()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
