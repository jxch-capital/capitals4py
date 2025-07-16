from capitals4py.config.app_setting import Settings
import socket
import socks


def proxy():
    from capitals4py import container
    settings: Settings = container.app_settings()
    if settings.proxy_enable:
        socks.setdefaultproxy(socks.SOCKS5, settings.proxy_addr, settings.proxy_port)
        socket.socket = socks.socksocket
