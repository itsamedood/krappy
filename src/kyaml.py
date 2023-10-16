from os.path import exists
from yaml import FullLoader, load


class KYAML:
  def __init__(self, _path: str) -> None:
    path = "%s/krappy.yaml" %_path
    if exists(path):
      with open(path, 'r') as krappyyaml: self.data = load(krappyyaml, FullLoader)
    else: self.data = None

    print(self.data)
