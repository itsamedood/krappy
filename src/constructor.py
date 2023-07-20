from out import KrappyError
from prompt import *


class Constructor:
    def __init__(self, _lib: DiscordLibrary) -> None: self.lib = _lib


    def gen_project(self) -> None:
        prompt = Prompt()

        match self.lib:
            case DiscordLibrary.DISCORD_JS:
                options = prompt.get_djs_options()
                options |= prompt.get_general_options()
                options |= prompt.get_path(str(options["name"]))
                print(options)

            case DiscordLibrary.DISCORD_PY: ...
            case DiscordLibrary.JDA: ...
            case DiscordLibrary.PYCORD: ...
            case _: raise KrappyError("unknown library", 1)
