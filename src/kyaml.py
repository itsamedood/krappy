from os.path import exists
from out import KrappyError
from yaml import FullLoader, load


class KYAML:
  data: dict[str, dict[str, str | bool]]

  def __init__(self, _path: str) -> None:
    path = "%s/krappy.yaml" %_path

    if exists(path):
      with open(path, 'r') as krappyyaml: self.data = load(krappyyaml, FullLoader)
    else: raise KrappyError("'%s' not found" %path, 1)
