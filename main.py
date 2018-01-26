import time
from DeskLight import DeskLight

desklight1 = DeskLight()

while True:
  desklight1.flash(5,3)
  time.sleep(2)
  desklight1.dim_up_and_down()
