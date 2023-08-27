import socket
import select
from utils.Log import Logger
from utils.consts import getConstValue

SOCKET_BUFFER_SIZE: int = int(getConstValue("SOCKET_BUFFER_SIZE"))

class ZeusSocket:
  def __init__(self, socket_IP: str, port: int) -> None:
    """Initializes a ZeusSocket object.
    """
    self.zeusLogger = Logger(self.__class__.__name__)
    self.socket = socket.socket(0, socket.SOCK_STREAM)
    self.poller = select.poll()
    self.IP = socket_IP
    self.port = port

  def connect(self) -> socket.socket:
    self.zeusLogger.logNewline(f"Connecting socket on IP: {self.IP}")
    self.socket.connect((self.IP, self.port))
    self.socket.send(f"Hello from Innate Domain")
    return self.socket

  def disconnect(self) -> None:
    self.zeusLogger.logNewline("Disconnecting socket")
    self.socket.close()

  def listen(self) -> None:
    read_socks, write_socks, err_socks = select.select([self.socket], [], [])

    for sock in read_socks:
      if sock == self.socket:
        data = sock.recv(SOCKET_BUFFER_SIZE).decode()
        if not data:
          self.zeusLogger.log("Disconnected from server")
        else:
          self.zeusLogger.log(data)
    # self.poller.register(self.socket, select.POLLIN)
    # res = self.poller.poll(1000)
    # if res:
    #   self.zeusLogger.log(res)