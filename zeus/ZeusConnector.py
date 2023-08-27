import network
from time import sleep
from utils.consts import getConstValue
from utils.Log import Logger

IP_INDEX: int = 0
HOST_IP_INDEX: int = 2


class ZeusConnector:
  """This class connects the Innate Domain to the Zeus network.
  """

  def __init__(self, ssid: str, password: str) -> None:
    """Initializes a new ZeusConnector object and attempts to connect
       to the Zeus network.

    Args:
        ssid (str): The SSID of the Zeus network
        password (str): The password to the Zeus network.
    """
    self.zeusLogger = Logger(self.__class__.__name__)
    self.zeus = network.WLAN(network.STA_IF)
    self.ssid = ssid
    self.password = password

  def connect(self, connection_timeout: int) -> network.WLAN:
    """Connects this Innate Domain client to the Zeus network.

    Args:
        connection_timeout (int): How long the Innate Domain should
                                  wait before timing out.

    Returns:
        network.WLAN: The connection to the Zeus network.
    """
    self.zeusLogger.logNewline(f"Connecting to {self.ssid}. Will timeout after {connection_timeout * 2} seconds")
    self.zeus.active(True)
    if not self.zeus.isconnected():
      self.zeus.connect(self.ssid, self.password)
      while not self.zeus.isconnected() and connection_timeout > 0:
        self.zeusLogger.log(f"Waiting for connection... {connection_timeout}")
        sleep(2)
        connection_timeout -= 1
    if self.zeus.isconnected():
      # self.zeusLogger.log(f"Connected! IP is {self.zeus.ifconfig()[IP_INDEX]}")
      self.zeusLogger.log(f"Connected! IP is {self.zeus.ifconfig()[IP_INDEX]}")
    return self.zeus

  def disconnect(self):
    """Disconnects the Innate Domain from the Zeus network.
    """
    self.zeusLogger.logNewline("Disconnecting")
    self.zeus.disconnect()

  def getIPAddress(self) -> str:
    """Retrieves and returns this Innate Domain's IP address.

    Returns:
        str: The IP address
    """
    return self.zeus.ifconfig()[IP_INDEX]

  def getHostIPAddress(self) -> str:
    """Retrieves and returns the IP address of the server this Innate Domain
       is connected to.

    Returns:
        str: The host's IP address.
    """
    return self.zeus.ifconfig()[HOST_IP_INDEX]
