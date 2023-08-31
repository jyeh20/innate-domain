from time import sleep
from utils.Log import Logger
from private.private import getPrivateValue
from utils.consts import getConstValue
from zeus.ZeusConnector import ZeusConnector
from zeus.ZeusSocket import ZeusSocket
from utils.onboardLED import turnLEDOff, turnLEDOn

ZEUS = getPrivateValue("ZEUS_SSID")
ZEUS_PW = getPrivateValue("ZEUS_PASSWORD")
SOCKET_PORT = int(getPrivateValue("INNATE_DOMAIN_SOCKET_PORT"))
NETWORK_TIMEOUT: int = int(getConstValue("NETWORK_TIMEOUT"))


class InnateDomain:
  """This Innate Domain class is a controller of the Innate Domain
     controlling LED lights around a poster collection.
  """

  def __init__(self) -> None:
    """Initializes an Innate Domain.
    """
    self.active = False
    self.logger: Logger = Logger("InnateDomain")
    turnLEDOn()
    self.zeus = ZeusConnector(ZEUS, ZEUS_PW)
    self.zeus_socket = ZeusSocket(
      self.zeus.getIPAddress(),
      self.zeus.getHostIPAddress(),
      SOCKET_PORT
    )
    self.connectNetwork()

  def connectNetwork(self) -> None:
    try:
      try:
        self.zeus.connect(NETWORK_TIMEOUT)
      except Exception as e:
        self.logger.log(f"{e}")
        raise Exception("Failed to connect to zeus")
      self.zeus_socket.connect()
    except Exception as error:
      self.logger.log(f"{error}")
      self.reset()
    else:
      self.logger.log("Successfully connected to network!")
      self.active = True

  def run(self) -> None:
    self.logger.log("Running the Innate Domain")
    try:
      self.logger.log("Entering listening loop")
      while True:
        self.zeus_socket.listen()
    except KeyboardInterrupt:
      self.logger.log("User interrupt!")
    except RuntimeError as error:
      self.logger.log(f"{error}")
    except Exception as error:
      self.logger.log(f"{error}")
    finally:
      self.reset()

  def reset(self) -> None:
    """Resets the Innate Domain, destroying all connections.
    """
    self.logger.logNewline("Resetting the Innate Domain")
    self.zeus_socket.disconnect()
    self.zeus.disconnect()
    turnLEDOff()

  def isActive(self) -> bool:
    return self.active
