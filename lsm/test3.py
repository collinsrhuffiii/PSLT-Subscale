from lsm6ds33 import LSM6DS33

lsm = LSM6DS33()
lsm.enableLSM()
while True:
	print(lsm.getAllRaw())

