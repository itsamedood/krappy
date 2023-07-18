from sys import exit


class TextStyle:
    """Changes the font style. Ranges from `0` to `5`."""

    NORMAL      = "\033[0m"
    BOLD        = "\033[1m"
    LIGHT       = "\033[2m"
    ITALICIZED  = "\033[3m"
    UNDERLINED  = "\033[4m"
    BLINK       = "\033[5m"


class TextColor:
    """Changes the font color. Ranges from `30` to `37`."""

    BLACK   = "\033[0;30m"
    RED     = "\033[0;31m"
    GREEN   = "\033[0;32m"
    YELLOW  = "\033[0;33m"
    BLUE    = "\033[0;34m"
    PURPLE  = "\033[0;35m"
    CYAN    = "\033[0;36m"
    WHITE   = "\033[0;37m"


class BGColor:
    """Changes the color of the background. Ranges from `40` to `47`"""

    BLACK   = "\033[0;40m"
    RED     = "\033[0;41m"
    GREEN   = "\033[0;42m"
    YELLOW  = "\033[0;43m"
    BLUE    = "\033[0;44m"
    PURPLE  = "\033[0;45m"
    CYAN    = "\033[0;46m"
    WHITE   = "\033[0;47m"


class Special:
    """Preset color codes for quicker usage."""

    SUCCESS = "\033[1;32m"
    WARNING = "\033[1;33m"
    ERROR   = "\033[1;31m"
    RESET   = "\033[0;0;0m"


class Ansi:
    """Class for using ANSI color codes."""

    style   = TextStyle()
    text    = TextColor()
    bg      = BGColor()
    special = Special()


class KrappyError(BaseException):
    """Represents an error from Krappy."""

    def __init__(self, message: str, code: int) -> None: print(f"lpm: {Ansi.special.ERROR}error{Ansi.special.RESET}: {message}."); return exit(code)


def success(message: str) -> None: return print(f"krappy: {Ansi.special.SUCCESS}success{Ansi.special.RESET}: {message}.")
def warn(message: str) -> None: return print(f"krappy: {Ansi.special.WARNING}warn{Ansi.special.RESET}: {message}.")
def notify(message: str) -> None: return print(f"krappy: {Ansi.style.LIGHT}note{Ansi.special.RESET}: {message}.")
