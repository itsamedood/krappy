from enum import Enum
from inquirer import Confirm, List, Path, Text, prompt
from os import getcwd, scandir
from os.path import exists
from out import KrappyError
from sys import exit


class DiscordLibrary(Enum):
    DISCORD_JS = "Discord.JS"
    DISCORD_PY = "Discord.py"
    JDA        = "Java Discord API (JDA)"
    PYCORD     = "Pycord"


class Prompt:
    def __init__(self) -> None: ...

    def get_library(self) -> DiscordLibrary:
        lib: dict[str, str] | None = prompt([List("lib", message="Which library are you using?", choices=[l.value for l in DiscordLibrary], carousel=True)])
        if lib is not None: return DiscordLibrary(lib["lib"])
        else: exit(0)

    def get_path(self, bot_name: str) -> dict[str, str]:
        path: dict[str, str] | None = prompt([Text("path", message="Path to generate project", default=f"{getcwd()}/{bot_name}")])
        if path is None: raise KrappyError("need path", 1)

        try:
            if not exists(path["path"]): raise KrappyError("bad path", 1)
            elif len([f for f in scandir(path["path"])]) > 0: raise KrappyError("directory is not empty", 1)
        except NotADirectoryError: raise KrappyError("path does not lead to a directory", 1)

        return path

    def get_general_options(self) -> dict[str, str | bool]:
        gen_options: dict[str, str | bool] = {}

        name: dict[str, str] | None = prompt([Text("name", message="Name of your bot")])
        if name is None: raise KrappyError("need name", 1)
        else: gen_options |= name

        cmdscope = prompt([Confirm("cmdscope", message="Global commands", default=True)])
        if cmdscope is None: raise KrappyError("need cmdscope", 1)
        else: gen_options |= cmdscope

        clientid = prompt([Text("clientid", message="Client ID")])
        if clientid is None: raise KrappyError("need client id", 1)
        else: gen_options |= clientid

        return gen_options

    def get_djs_options(self) -> dict[str, str]:
        options: dict[str, str] = {}

        language: dict[str, str] | None = prompt([List("language", message="JS or TS", choices=["JavaScript", "TypeScript"], carousel=True)])
        if language is None: raise KrappyError("need language", 1)
        else: options |= language

        if language["language"] == "JavaScript":
            module_type: dict[str, str] | None = prompt([List("module_type", message="Module", choices=["CommonJS", "ES"], carousel=True)])
            if module_type is None: raise KrappyError("need module type", 1)
            else: options |= module_type
        else: options["module_type"] = "ES"

        return options
