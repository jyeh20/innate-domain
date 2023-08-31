CONSTS = dict(
    NETWORK_TIMEOUT=15,
    SOCKET_BUFFER_SIZE=1024
)


def getConstValue(key: str) -> str:
  return str(CONSTS.get(key))
