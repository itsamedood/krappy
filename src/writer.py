from os.path import exists


class Writer:
  """ Used for writing source code during generation. """

  @staticmethod
  def write_src(_src: str, _file: str):
    """
    Writes `_src` (stripped) to `_file`.

    If the file doesn't exist, `mode` is set to `x`, else `a`.
    """

    with open(_file, 'x' if not exists(_file) else 'a') as src_file: src_file.write(_src.strip())

  @staticmethod
  def touch(_file: str) -> None:
    with open(_file, 'x') as file: file.write('')
