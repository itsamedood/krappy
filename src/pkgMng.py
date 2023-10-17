from enum import Enum
from inquirer import List, prompt
from out import KrappyError
from os import system


class JSPackageManager(Enum):
  """ Represents all supported JS/TS package managers by Krappy. """

  NPM  = "npm"
  PNPM = "pnpm"
  YARN = "yarn"
  BUN  = "bun"


class PkgMng:
  def __init__(self, _path: str,  _install_cmd: str, *_packages: str | None) -> None: self.path, self.install_cmd, self.packages = _path, _install_cmd, _packages

  def install(self): system(f"cd {self.path} && {self.install_cmd} {' '.join([p for p in self.packages if p is not None])}")

  @staticmethod
  def get_js_package_manager() -> JSPackageManager:
    """ Gets desired package manager from the user. """

    pm: dict[str, str] | None = prompt([List("pm", message="Package Manager", choices=[p.value for p in JSPackageManager], carousel=True)])
    if pm is None: raise KrappyError("need js package manager", 1)
    else: return JSPackageManager(pm["pm"])
