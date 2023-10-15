from os.path import exists


class SourceCode:
  """ Represents source code to be written to a specific file. """

  def __init__(self, _code: str, _file: str) -> None:
    self.code = _code.strip()
    """ Actual code as a string (use 3 double quotes.) """

    self.file = _file
    """ File this code is for. """


class Writer:
  """ Used for writing source code during generation. """

  @staticmethod
  def write_src(_src: SourceCode):
    file = _src.file
    mode = 'a'

    if not exists(file): mode = 'x'
    with open(file, mode) as src_file: src_file.write(_src.code)

  @staticmethod
  def touch(_file: str) -> None:
    with open(_file, 'x') as file: file.write('')
