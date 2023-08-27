class Logger:
  def __init__(self, name: str):
    self.name = name
    self.indent = 0

  def log(self, message: str, newline: bool = False):
    if newline:
      print()
    print(f"{self.name}: {message}")

  def logNewline(self, message: str):
    self.log(message, True)
