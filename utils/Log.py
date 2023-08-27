class Logger:
  def __init__(self, name: str) -> None:
    self.name = name
    self.indent = 0
    self.logNewline(f"Initializing an instance of {self.name}")

  def log(self, message: str, newline: bool = False) -> None:
    if newline:
      print()
    print(f"{self.name}: {message}")

  def logNewline(self, message: str) -> None:
    self.log(message, True)
