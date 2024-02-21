from constructors.commandConstructor import CommandConstructor
from constructors.eventConstructor import EventConstructor
from constructors.projectConstructor import ProjectConstructor
from prompts.promptTypes import Action, ActionChoice
from sys import exit


if __name__ == "__main__":
  try:
    match Action.get_action():
      case ActionChoice.GEN_PROJECT: ProjectConstructor().gen_project()
      case ActionChoice.GEN_COMMAND: CommandConstructor().gen_command()
      case ActionChoice.GEN_EVENT: EventConstructor().gen_event()
      case ActionChoice.EXIT: exit(0)

  except KeyboardInterrupt: ...
