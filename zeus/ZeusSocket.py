import socket
import select
import json
from time import sleep
from utils.Log import Logger
from utils.consts import getConstValue

SOCKET_BUFFER_SIZE: int = int(getConstValue("SOCKET_BUFFER_SIZE"))

class ZeusSocket:
  def __init__(self, client_IP: str, server_socket_IP: str, port: int) -> None:
    """Initializes a ZeusSocket object.
    """
    self.zeusLogger = Logger(self.__class__.__name__)
    self.socket = socket.socket(0, socket.SOCK_STREAM)
    self.poller = select.poll()
    self.client_IP = client_IP
    self.server_socket_IP = server_socket_IP
    self.port = port

  def connect(self) -> socket.socket:
    self.zeusLogger.logNewline(f"Connecting socket on IP: {self.server_socket_IP}:{self.port}")
    self.socket.bind(("0.0.0.0", 80))
    sleep(2)
    address = socket.getaddrinfo(self.server_socket_IP, self.port)[0][-1]
    self.socket.connect(address)
    self.sendJson(
      dict(
        ZeusCommand="initSocket",
        type="InnateDomain",
        clientIP=self.client_IP,
      )
    )
    return self.socket

  def disconnect(self) -> None:
    self.sendMsg("Disconnecting socket")
    sleep(2)
    self.socket.close()

  def listen(self) -> None:
    read_socks, write_socks, err_socks = select.select([self.socket], [], [])

    for sock in read_socks:
      if sock == self.socket:
        data = sock.recv(SOCKET_BUFFER_SIZE).decode()
        if not data:
          self.zeusLogger.log("Disconnected from server")
          raise RuntimeError("Disconnected from server")
        else:
          self.zeusLogger.log(data)

  def sendMsg(self, msg) -> None:
    self.zeusLogger.log(f"Sending socket msg: {msg}")
    self.socket.send(msg)

  def sendJson(self, json_msg: dict) -> None:
    separator = (",", ":")
    self.zeusLogger.log(f"Converting {json_msg} into json")
    data = json.dumps(json_msg, separators=separator)
    self.zeusLogger.log(f"Data after conversion: {data}")
    self.sendMsg(data)