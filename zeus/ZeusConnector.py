import network
from time import sleep
from utils.consts import getConstValue
from utils.Log import Logger

NETWORK_TIMEOUT: int = int(getConstValue("NETWORK_TIMEOUT"))
IP_INDEX: int = 0


class ZeusConnector:
  """This class connects the Innate Domain to the Zeus network.
  """

  def __init__(self, ssid: str, password: str):
    """Initializes a new ZeusConnector object and attempts to connect
       to the Zeus network.

    Args:
        ssid (str): The SSID of the Zeus network
        password (str): The password to the Zeus network.
    """
    self.zeusLogger = Logger(self.__class__.__name__)
    self.zeusLogger.logNewline(f"Initializing a ZeusConnector.")
    self.zeus = network.WLAN(network.STA_IF)
    self.ssid = ssid
    self.password = password
    self.connect(NETWORK_TIMEOUT)

  def connect(self, connection_timeout: int) -> network.WLAN:
    """Connects this Innate Domain client to the Zeus network.

    Args:
        connection_timeout (int): How long the Innate Domain should
                                  wait before timing out.

    Returns:
        network.WLAN: The connection to the Zeus network.
    """
    self.zeusLogger.logNewline(f"Connecting to {self.ssid}.")
    if not self.zeus.isconnected():
      self.zeus.connect(self.ssid, self.password)
      while not self.zeus.isconnected() and connection_timeout > 0:
        self.zeusLogger.log("Waiting for connection...")
        sleep(2)
        connection_timeout -= 1
    self.zeusLogger.log(f"Connected! IP is {self.zeus.ifconfig()[IP_INDEX]}")
    return self.zeus

  def disconnect(self):
    """Disconnects the Innate Domain from the Zeus network.
    """
    self.zeusLogger.logNewline("Disconnecting")
    self.zeus.disconnect()
