from enum import Enum
from os import system


class JSPackageManager(Enum):
    """ Represents all supported JS/TS package managers by Krappy. """

    NPM  = "npm"
    PNPM = "pnpm"
    YARN = "yarn"
    BUN  = "bun"


class PkgMng:
    def __init__(self, _install_cmd: str, *_packages: str | None) -> None: self.install_cmd, self.packages = _install_cmd, _packages

    def install(self): print(f"{self.install_cmd} {' '.join([p for p in self.packages if p is not None])}")
