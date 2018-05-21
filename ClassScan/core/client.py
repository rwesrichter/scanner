import sys
sys.path.append('../')

from twilio.rest import Client
import ClassScan

config = ClassScan.get_config()


class client:
    """
    Wrapper for Twilio.Client
    Usage: sms.message, call.message
    """
    def __init__(self):
        self.number = config.get('PHONE', 'NUMBER')
        self.sid = config.get('PHONE', 'SID')
        self.token = config.get('PHONE', 'TOKEN')
        self.client = Client(self.sid, self.token)

    def message(self, address, message):
        return False


class sms(client):
    def __init__(self):
        super().__init__()

    def message(self, message, address):
        self.client.messages.create(body=message,
                                    to=address,
                                    from_=self.number)
        return True


class call(client):
    def __init__(self):
        super().__init__()

    def message(self, message, address):
        self.client.calls.create(body=message,
                                 to=address,
                                 from_=self.number)
        return True