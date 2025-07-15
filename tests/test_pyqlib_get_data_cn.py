from qlib.tests.data import GetData
import socket
import socks

def proxy():
    socks.setdefaultproxy(socks.SOCKS5, "localhost", 10808)
    socket.socket = socks.socksocket

def test_get_data_cn():
    proxy()
    GetData().qlib_data(target_dir=r"D:\jxch-capital\capitals4py\data\qlib\data\cn", region="cn")

def test_get_data_us():
    proxy()
    GetData().qlib_data(target_dir=r"D:\jxch-capital\capitals4py\data\qlib\data\us", region="us")



