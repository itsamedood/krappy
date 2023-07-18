from out import KrappyError
from prompt import DiscordLibrary, Prompt


if __name__ == "__main__":
    try:
        lib = Prompt.get_library()

        match lib:
            case DiscordLibrary.DISCORD_JS:
                options = Prompt.get_djs_options()
                print(options)

            case DiscordLibrary.DISCORD_PY: ...
            case DiscordLibrary.JDA: ...
            case DiscordLibrary.PYCORD: ...
            case _: raise KrappyError("unknown library", 1)

    except KeyboardInterrupt: ...
