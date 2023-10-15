from pkgMng import *
from prompt import *
from writer import *


class Constructor:
    """ Holds functions for generating a project. """

    def __init__(self, _lib: DiscordLibrary) -> None: self.lib, self.prompt = _lib, Prompt()

    def gen_project(self) -> None:
        match self.lib:
            case DiscordLibrary.DISCORD_JS: self.__gen_djs_project()
            case DiscordLibrary.DISCORD_PY: self.__gen_dpy_project()
            case DiscordLibrary.JDA: self.__gen_jda_project()
            case DiscordLibrary.PYCORD: self.__gen_pycord_project()
            case _: raise KrappyError("unknown library", 1)

    def __gen_djs_project(self) -> None:
        pm = self.prompt.get_js_package_manager()
        install_cmd = ''

        match pm:
            case JSPackageManager.NPM: install_cmd = "npm i"
            case JSPackageManager.PNPM: install_cmd = "pnpm i"  # Need to double check.
            case JSPackageManager.YARN: install_cmd = "yarn add"
            case JSPackageManager.BUN: install_cmd = "bun add"

        options = self.prompt.get_djs_options()
        options |= self.prompt.get_general_options()
        options |= self.prompt.get_path(str(options["name"]))
        options |= self.prompt.get_token()
        path = str(options["path"])
        print(options)

        # `krappy.json`.
        krappy_json = SourceCode(f"""{{
  "language": "{options["language"]}",
  "module_type": "{options["module_type"]}",
  "name": "{options["name"]}",
  "globalcmds": {str(options["globalcmds"]).lower()},
  "path": "{options["path"]}",
  "pmi": "{install_cmd}"
}}
""", "%s/krappy.json" %path)
        Writer.write_src(krappy_json)

        # `.env`.
        dotenv_code = SourceCode(f"""TOKEN={options["token"]}
CLIENT_ID={options["clientid"]}
{f"GUILD_ID={options["guildid"]}" if "guildid" in options else ''}
""", "%s/.env" %path)
        Writer.write_src(dotenv_code)

        # `package.json`.
        pkg_json = SourceCode(f"""{{
  "name": "{options["name"]}",
  "version": "1.0.0",
  "description": "Generated with Krappy :)",
  "main": "src/index.{options["language"]}",
  "scripts": {{
    "test": "echo \\"Error: no test specified\\" && exit 1"
  }},
  "keywords": [],
  "author": "",
  "license": "ISC"
}}
""", "%s/package.json" %path)
        Writer.write_src(pkg_json)

        # Install packages.
        PkgMng(install_cmd, "discord.js", "glob", "dotenv" if not pm == JSPackageManager.BUN else None).install()

        # Write README.md and finish!
        readme = SourceCode(f"""# Generation finished!
""", "%s/README.md" %path)

    def __gen_dpy_project(self) -> None: ...
    def __gen_jda_project(self) -> None: ...
    def __gen_pycord_project(self) -> None: ...
