from base_cls.auth import RequestGenerator
from base_cls.utils import get_secret_config


class BaseOperator:
    def __init__(self, name, request: RequestGenerator):
        self.operation_name = name
        self.request = request

    def fetch_response(self):
        return

    def get_operation_name(self):
        return self.operation_name

    def restore_history(self):
        return

    def get_request_gen(self):
        return self.request


class BaseListenerConfig:
    def __init__(self, name: str = 'BaseListener'):
        self.listener_name = name

    def get_listener_name(self):
        return self.listener_name

    def on_open(self, ws):
        return

    def on_message(self, ws, message):
        return

    def on_error(self, ws, error):
        return

    def on_close(self, ws):
        return
