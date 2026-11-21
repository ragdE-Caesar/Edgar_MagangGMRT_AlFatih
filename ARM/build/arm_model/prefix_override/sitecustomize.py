import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/muhammad-edgar/mwagang_ws/src/arm_model/install/arm_model'
