from constructor import CommandConstructor, EventConstructor, ProjectConstructor
from prompt import Action, ActionChoice


if __name__ == "__main__":
  try:
    match Action.get_action():
      case ActionChoice.GEN_PROJECT: ProjectConstructor().gen_project()
      case ActionChoice.GEN_COMMAND: CommandConstructor().gen_command()
      case ActionChoice.GEN_EVENT: EventConstructor().gen_event()

  except KeyboardInterrupt: ...
