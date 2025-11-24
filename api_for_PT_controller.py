from time import time
import json
import socket


class PTClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def _send_requests(self, request):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                s.sendall(json.dumps(request).encode())
                response = s.recv(1024).decode()
                return json.loads(response)
        except ConnectionRefusedError:
            return {"error": "B program is not running"}

    def get_temperature(self):
        request = {
            "action": "get_temperature",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", 999.0)

    def get_magnet(self):
        request = {
            "action": "get_magnet",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", 999.0)

    def is_magnet_ready(self):
        request = {
            "action": "is_magnet_ready",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", False)

    def is_probe_ready(self):
        request = {
            "action": "is_probe_ready",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", False)

    def get_temp_magnet(self):
        request = {
            "action": "get_temp_magnet",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", [999.0, 999.0])

    def get_pt_setting(self):
        request = {
            "action": "get_pt_setting",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result")

    def get_magnet_temperature(self):
        request = {
            "action": "get_magnet_temperature",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", 999.0)

    def is_magnet_reached(self):
        request = {
            "action": "is_magnet_reached",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result", False)

    def set_temperature(self, goal):
        request = {
            "action": "set_temperature",
            "params": [goal]
        }
        response = self._send_requests(request)
        return response.get("result")

    def set_magnet(self, goal, rate=None):
        request = {
            "action": "set_magnet",
            "params": [goal, rate]
        }
        response = self._send_requests(request)
        return response.get("result")

    def pause_magnet(self):
        request = {
            "action": "pause_magnet",
            "params": []
        }
        response = self._send_requests(request)
        return response.get("result")


if __name__ == "__main__":
    client = PTClient("localhost", 19020)

