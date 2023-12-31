from kyaml import KYAML
from out import KrappyError
from os import getcwd
from os.path import exists
from prompts.eventPrompt import EventPrompt
from prompts.promptTypes import DiscordLibrary
from re import match
from writer import Writer


class EventConstructor:
  """ Holds functions for generating a event. """

  def __init__(self) -> None:
    self.prompt = EventPrompt()

  def gen_event(self) -> None:
    match self.prompt.get_library():
      case DiscordLibrary.DISCORD_JS: self.__gen_djs_event()
      case DiscordLibrary.DISCORD_PY: self.__gen_dpy_event()
      case DiscordLibrary.PYCORD: self.__gen_pycord_event()
      case DiscordLibrary.JDA: self.__gen_jda_event()
      case DiscordLibrary.CONCORD: self.__gen_concord_event()
      case DiscordLibrary.DISCATSHARP: self.__gen_discatsharp_event()
      case DiscordLibrary.DPP: self.__gen_dpp_event()
      case _: raise KrappyError("unknown library", 1)

  def __gen_djs_event(self) -> None:
    kyaml = KYAML(getcwd()).data
    options = kyaml["options"]
    path, language = options["path"], options["language"]
    module_type = options["module_type"] if "module_type" in options else None

    eventoptions = self.prompt.get_event_options()
    en, eventonce = eventoptions["eventname"], eventoptions["eventonce"]
    if not type(en) == str or not type(eventonce) == bool: raise KrappyError("eventname should be of type 'str' and eventonce should be of type 'bool'", 1)
    if not match(r"^[a-zA-Z][a-zA-Z]*$", en): raise KrappyError("invalid event name: '%s'" %en, 1)

    eventname = f"{en[0].upper()}{en[1:]}Event"
    eventfile = f"{en[0].lower()}{en[1:]}"
    eventpath = f"{path}/src/events/{eventfile}.{language}"

    if exists(eventpath): raise KrappyError("%s event already exists" %eventname, 1)
    if language == "ts":  # TypeScript.
      Writer.write_src(f"""import Event from '../types/event';
import Bot from '../bot';

export default class {eventname} extends Event {{
  constructor() {{
    super({{
      name: '{eventfile}',
      once: {str(eventonce).lower()}
    }});
  }}

  public async execute(client: Bot /* Add necessary parameters here. */) {{
    return console.log(`{eventfile} event triggered.`);
  }}
}}
""", eventpath)
    else:  # JavaScript.
      if module_type == "ESM": ...
      else:
        Writer.write_src(f"""module.exports = {{
  name: '{eventfile}',
  once: {str(eventonce).lower()},
  async execute(client) {{ }} // Add parameters for the event before the `client` parameter!
}};
""", eventpath)

  def __gen_dpy_event(self) -> None: print("To be supported...")
  def __gen_pycord_event(self) -> None: print("To be supported...")
  def __gen_jda_event(self) -> None: print("To be supported...")
  def __gen_concord_event(self) -> None: print("To be supported...")
  def __gen_discatsharp_event(self) -> None: print("To be supported...")
  def __gen_dpp_event(self) -> None: print("To be supported...")
