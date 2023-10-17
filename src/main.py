from constructor import CommandConstructor, EventConstructor, ProjectConstructor
from prompt import Action, Prompt


if __name__ == "__main__":
  try:
    p = Prompt()
    match p.get_action():
      case Action.GEN_PROJECT: ProjectConstructor(p).gen_project()
      case Action.GEN_COMMAND: CommandConstructor(p).gen_command()
      case Action.GEN_EVENT: EventConstructor(p).gen_event()

  except KeyboardInterrupt: ...
