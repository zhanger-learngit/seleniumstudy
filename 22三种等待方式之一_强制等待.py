import time

time.sleep(10)  # 强制等待10秒
# 当页面发生切换时、切换窗口句柄时甚至于切换iframe时，
# 强烈建议强制等待1~2秒，使得脚本更加稳定（即使使用了智能等待，也建议这样）【面试说这句话】
# 其实time.sleep()不能算是selenium的，人家这个是Python自带的
