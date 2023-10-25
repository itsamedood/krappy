from intents import *
from inquirer import List, Text, prompt
from out import KrappyError
from prompts.promptTypes import DiscordLibrary


class CommandPrompt:
  def __init__(self) -> None: ...

  def get_library(self) -> DiscordLibrary:
    """ Gets the library user will use. """

    lib: dict[str, str] | None = prompt([List("lib", message="Which library are you using?", choices=[l.value for l in DiscordLibrary], carousel=True)])
    if lib is None: raise KrappyError("need library", 1)
    else: return DiscordLibrary(lib["lib"])

  def get_command_options(self) -> dict[str, str]:
    cmdoptions: dict[str, str] = {}

    cmdname: dict[str, str] | None = prompt([Text("cmdname", message="Command name")])
    if cmdname is None: raise KrappyError("need command name", 1)
    else: cmdoptions |= cmdname
    del cmdname

    cmdcategory: dict[str, str] | None = prompt([Text("cmdcategory", message="Command category")])
    if cmdcategory is None: raise KrappyError("need command category", 1)
    else: cmdoptions |= cmdcategory
    del cmdcategory

    return cmdoptions
