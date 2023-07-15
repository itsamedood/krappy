from enum import Enum
from inquirer import List, prompt
from sys import exit


class DiscordLibrary(Enum):
    DISCORD_JS = "Discord.JS"
    DISCORD_PY = "Discord.py"
    JDA        = "Java Discord API (JDA)"
    PYCORD     = "Pycord"


class Prompt:
    @staticmethod
    def get_library() -> DiscordLibrary:
        lib: dict[str, str] | None = prompt([List("lib", message="", choices=["Discord.JS", "Discord.py", "Java Discord API (JDA)", "Pycord"], carousel=True)])
        if lib is not None: return DiscordLibrary(lib["lib"])
        else: exit(0)
