from constructor import Constructor
from prompt import Prompt


if __name__ == "__main__":
    try: Constructor(Prompt().get_library()).gen_project()
    except KeyboardInterrupt: ...
