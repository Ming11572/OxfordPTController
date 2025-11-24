import socket
from threading import Lock

from PySide6.QtCore import Qt, Signal, QThread


class SocketThread(QThread):
    signal_log = Signal(int, str)
    signal_client_called = Signal(object, object)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.running = False
        self.quit_lock = Lock()
        # self.target_fun = target_fun
        self.server_socket = None

    def log(self, text):
        self.signal_log.emit(8, text)

    def quit_thread(self):
        with self.quit_lock:
            if self.running:
                self.running = False
            if self.server_socket:
                try:
                    self.server_socket.close()
                except:
                    pass
                finally:
                    self.server_socket = None

    def run(self, /):
        self.running = True
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            self.server_socket.settimeout(1.0)  # 设置超时以便检查退出条件

            # self.log(f"服务器启动成功，监听端口 {self.port}, 等待连接")
            while self.running:
                try:
                    # 接受客户端连接
                    conn, addr = self.server_socket.accept()
                    self.signal_client_called.emit(conn, addr)
                    # self.target_fun(conn, addr)
                except socket.timeout:
                    # 超时，继续检查运行状态
                    continue
                except OSError as e:
                    if self.running:
                        self.log(f"接受连接错误: {e}")
                    break
        except Exception as e:
            self.log(f"服务器错误: {e}")
        finally:
            self.log("服务器线程退出")