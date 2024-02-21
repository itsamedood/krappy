from enum import Enum
from inquirer import List, prompt


class ActionChoice(Enum):
  GEN_PROJECT = "Generate Project"
  GEN_COMMAND = "Generate Command"
  GEN_EVENT   = "Generate Event"
  EXIT        = "Nothing"


class Action:
  @staticmethod
  def get_action() -> ActionChoice:
    action: dict[str, str] | None = prompt([List("action", message="What do you want to do?", choices=[a.value for a in ActionChoice], carousel=True)])
    if action is not None: return ActionChoice(action["action"])
    else: exit(0)


class DiscordLibrary(Enum):
  """ Represents all supported libraries by Krappy. """

  DISCORD_JS  = "Discord.JS"  # JavaScript / TypeScript.
  DISCORD_PY  = "Discord.py"  # Python.
  PYCORD      = "Pycord"  # Also Python.
  JDA         = "Java Discord API (JDA)"  # Java.
  CONCORD     = "Concord"  # C.
  DISCATSHARP = "DisCatSharp (DCS)"  # C#.
  DPP         = "DPP"  # C++.
