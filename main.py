from private.init import init
from InnateDomain import InnateDomain

init()

domain = InnateDomain()

if domain.isActive():
  domain.run()