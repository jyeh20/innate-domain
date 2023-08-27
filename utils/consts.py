CONSTS = dict(
    NETWORK_TIMEOUT=15
)


def getConstValue(key: str) -> str:
  return str(CONSTS.get(key))
