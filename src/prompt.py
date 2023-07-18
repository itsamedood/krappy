from enum import Enum
from inquirer import Text, List, prompt
from os import getcwd
from out import KrappyError
from sys import exit


class DiscordLibrary(Enum):
    DISCORD_JS = "Discord.JS"
    DISCORD_PY = "Discord.py"
    JDA        = "Java Discord API (JDA)"
    PYCORD     = "Pycord"


class Prompt:
    @staticmethod
    def get_library() -> DiscordLibrary:
        lib: dict[str, str] | None = prompt([List("lib", message="Which library are you using?", choices=["Discord.JS", "Discord.py", "Java Discord API (JDA)", "Pycord"], carousel=True)])
        if lib is not None: return DiscordLibrary(lib["lib"])
        else: exit(0)

    @staticmethod
    def get_djs_options() -> dict[str, str]:
        options: dict[str, str] = {}

        name: dict[str, str] | None = prompt([Text("name", message="Name of your bot")])
        if name is None: raise KrappyError("need name", 1)
        else: options |= name

        path: dict[str, str] | None = prompt([Text("path", message="Path to generate project", default=f"{getcwd()}/{options['name']}")])
        if path is None: raise KrappyError("need path", 1)
        else: options |= path

        return options
