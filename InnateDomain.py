from private.private import getPrivateValue
from utils.Log import Logger
from zeus.ZeusConnector import ZeusConnector

ZEUS = getPrivateValue("ZEUS_SSID")
ZEUS_PW = getPrivateValue("ZEUS_PASSWORD")


class InnateDomain:
  """This Innate Domain class is a controller of the Innate Domain
     controlling LED lights around a poster collection.
  """

  def __init__(self):
    """Initializes an Innate Domain.
    """
    self.logger = Logger("InnateDomain")
    self.logger.logNewline("Initializing an Innate Domain")
    self.zeus = ZeusConnector(ZEUS, ZEUS_PW)

  def reset(self):
    """Resets the Innate Domain, destroying all connections.
    """
    self.logger.logNewline("Resetting the Innate Domain")
    self.zeus.disconnect()
