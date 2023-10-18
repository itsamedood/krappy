from intents import *  # Also imports `Enum`.
from inquirer import Checkbox, Confirm, List, Text, prompt
from os import getcwd, scandir
from os.path import exists
from out import KrappyError
from sys import exit


class Action(Enum):
  GEN_PROJECT = "Generate Project"
  GEN_COMMAND = "Generate Command"
  GEN_EVENT   = "Generate Event"


class DiscordLibrary(Enum):
  """ Represents all supported libraries by Krappy. """

  DISCORD_JS  = "Discord.JS"  # JavaScript / TypeScript.
  DISCORD_PY  = "Discord.py"  # Python.
  PYCORD      = "Pycord"  # Also Python.
  JDA         = "Java Discord API (JDA)"  # Java.
  CONCORD     = "Concord"  # C.
  DISCATSHARP = "DisCatSharp (DCS)"  # C#.
  DPP         = "DPP"  # C++.


class Prompt:
  """ Holds functions for prompting user for information to use for generation. """

  def __init__(self) -> None: ...

  def get_action(self) -> Action:
    action: dict[str, str] | None = prompt([List("action", message="What do you want to do?", choices=[a.value for a in Action], carousel=True)])
    if action is not None: return Action(action["action"])
    else: exit(0)

  def get_library(self) -> DiscordLibrary:
    """ Gets the library user will use. """

    lib: dict[str, str] | None = prompt([List("lib", message="Which library are you using?", choices=[l.value for l in DiscordLibrary], carousel=True)])
    if lib is not None: return DiscordLibrary(lib["lib"])
    else: raise KrappyError("need library", 1)

  def get_path(self, bot_name: str) -> dict[str, str]:
    """ Gets path for the project. """

    pathd: dict[str, str] | None = prompt([Text("path", message="Path to generate project", default=f"{getcwd()}/{bot_name}")])
    if pathd is None: raise KrappyError("need path", 1)
    path = pathd["path"]

    try:
      if not exists(path): raise KrappyError("bad path", 1)
      elif len([f for f in scandir(path)]) > 0: raise KrappyError("directory is not empty", 1)
    except NotADirectoryError: raise KrappyError("path does not lead to a directory", 1)

    return pathd

  def get_general_options(self) -> dict[str, str | bool]:
    """ Gets options that are needed regardless of language or library. """

    gen_options: dict[str, str | bool] = {}

    # Bot name.
    name: dict[str, str] | None = prompt([Text("name", message="Name of your bot")])
    if name is None: raise KrappyError("need name", 1)
    else: gen_options |= name

    # Global or local commands (guild exclusive).
    globalcmds = prompt([Confirm("globalcmds", message="Global commands", default=True)])
    if globalcmds is None: raise KrappyError("need globalcmds", 1)
    else: gen_options |= globalcmds

    # Client ID.
    clientid = prompt([Text("clientid", message="Client ID")])
    if clientid is None: raise KrappyError("need client id", 1)
    else: gen_options |= clientid

    # Guild ID (only if globalcmds is False).
    if gen_options["globalcmds"] is not True:
      guildid = prompt([Text("guildid", message="Guild ID")])
      if guildid is None: raise KrappyError("need guild id", 1)
      else: gen_options |= guildid

    return gen_options

  def get_intents_and_partials(self) -> dict[str, list[str]]:
    """ Gets the intents and partials for the bot. """

    is_and_ps: dict[str, list[str]] = {}

    intents: dict[str, list[str]] | None = prompt([Checkbox("intents", message="Intents", choices=[i.value for i in Intent], default=[Intent.GUILDS.value], carousel=True)])
    if intents is None: raise KrappyError("need intents", 1)
    else: is_and_ps |= intents

    partials: dict[str, list[str]] | None = prompt([Checkbox("partials", message="Partials", choices=[p.value for p in Partial], carousel=True)])
    if partials is None: raise KrappyError("need partials", 1)
    else: is_and_ps |= partials

    return is_and_ps

  def get_token(self) -> dict[str, str]:
    """ Gets the token for the bot. """

    token: dict[str, str] | None = prompt([Text("token", message="Token")])
    if token is None: raise KrappyError("need token", 1)
    else: return token

  def get_djs_options(self) -> dict[str, str]:
    """ Gets options for Discord.JS, JS or TS. """

    options: dict[str, str] = {}

    # JS or TS (TS>>>JS).
    language: dict[str, str] | None = prompt([List("language", message="JS or TS", choices=["JavaScript", "TypeScript"], carousel=True)])
    if language is None: raise KrappyError("need language", 1)
    else:
      lang_name = language["language"]
      lang: dict[str, str] = {}
      lang["language"] = "js" if lang_name[0] == 'J' else "ts"
      options |= lang

    # CommonJS or ES modules (only if lang is JS).
    if language["language"] == "JavaScript":
      module_type: dict[str, str] | None = prompt([List("module_type", message="Module", choices=["CommonJS", "ES"], carousel=True)])
      if module_type is None: raise KrappyError("need module type", 1)
      else: options |= module_type
    else: options["module_type"] = "ES"

    return options

  def get_dpy_options(self) -> dict[str, str]:
    """ Gets options for Discord.py. """

    options: dict[str, str] = {}

    ...

    return options

  def get_pycord_options(self) -> dict[str, str]:
    """ Gets options for Pycord. """

    options: dict[str, str] = {}

    ...

    return options

  def get_jda_options(self) -> dict[str, str]:
    """ Gets options for Java Discord API. """

    options: dict[str, str] = {}

    ...

    return options

  def get_concord_options(self) -> dict[str, str]:
    """ Gets options for Concord. """

    options: dict[str, str] = {}

    ...

    return options

  def get_discatsharp_options(self) -> dict[str, str]:
    """ Gets options for DisCatSharp. """

    options: dict[str, str] = {}

    ...

    return options

  def get_dpp_options(self) -> dict[str, str]:
    """ Gets options for DPP. """

    options: dict[str, str] = {}

    ...

    return options
