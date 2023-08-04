from out import KrappyError
from prompt import *


class Constructor:
    def __init__(self, _lib: DiscordLibrary) -> None:
        self.lib, self.prompt = _lib, Prompt()

    def gen_project(self) -> None:
        match self.lib:
            case DiscordLibrary.DISCORD_JS: self.__gen_djs_project()
            case DiscordLibrary.DISCORD_PY: self.__gen_dpy_project()
            case DiscordLibrary.JDA: self.__gen_jda_project()
            case DiscordLibrary.PYCORD: self.__gen_pycord_project()
            case _: raise KrappyError("unknown library", 1)

    def __gen_djs_project(self) -> None:
        options = self.prompt.get_djs_options()
        options |= self.prompt.get_general_options()
        options |= self.prompt.get_path(str(options["name"]))
        print(options)

    def __gen_dpy_project(self) -> None: ...
    def __gen_jda_project(self) -> None: ...
    def __gen_pycord_project(self) -> None: ...
