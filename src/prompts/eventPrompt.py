from intents import *
from inquirer import Confirm, List, Text, prompt
from out import KrappyError
from prompts.promptTypes import DiscordLibrary


class EventPrompt:
  def __init__(self) -> None: ...

  def get_library(self) -> DiscordLibrary:
    """ Gets the library user will use. """

    lib: dict[str, str] | None = prompt([List("lib", message="Which library are you using?", choices=[l.value for l in DiscordLibrary], carousel=True)])
    if lib is None: raise KrappyError("need library", 1)
    else: return DiscordLibrary(lib["lib"])

  def get_event_options(self) -> dict[str, str | bool]:
    eventoptions: dict[str, str | bool] = {}

    eventname: dict[str, str] | None = prompt([Text("eventname", message="Event name")])
    if eventname is None: raise KrappyError("need event name", 1)
    else: eventoptions |= eventname
    del eventname

    eventonce: dict[str, bool] | None = prompt([Confirm("eventonce", message="Event once?", default=False)])
    if eventonce is None: raise KrappyError("need event once", 1)
    else: eventoptions |= eventonce
    del eventonce

    return eventoptions
