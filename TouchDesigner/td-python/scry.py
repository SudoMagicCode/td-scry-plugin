import scryEntities
import json


class scry:
    def __init__(self, ownerOp):
        self.ownerOp = ownerOp
        self.Web_server_DAT = ownerOp.op('webserver_ws')
        self.build: str = app.build
        self.experimental: bool = app.experimental
        print(f"extension init from {self.ownerOp.name}")

    def check_active(self) -> bool:
        active_state: bool = self.ownerOp.par.Wsserveractive.eval()
        return active_state

    def LogError(self, message: str, absFrame: int, severity: int, type, source: callable):
        error: scryEntities.scryError = scryEntities.scryError(
            message=message, severity=severity, opType=type, source=source.path, absFrame=absFrame)

        # NOTE check if ws is currently active before attempting to send
        if self.check_active():
            self._relay_msg(msg=error)

    def SendMessage(self, message: str, sender: str = ""):
        scryMsg: scryEntities.scryMessage = scryEntities.scryMessage(
            message=message, absFrame=absTime.frame, source=sender)

        # NOTE check if ws is currently active before attempting to send
        if self.check_active():
            self._relay_msg(msg=scryMsg)

    def SendImage(self):
        ...

    def _relay_msg(self, msg: scryEntities.scryAbstractMessage) -> None:
        clients = self.Web_server_DAT.webSocketConnections

        for each in clients:
            msg = {
                'source': {
                    'app': 'TouchDesigner',
                    'build': self.build,
                    'experimental': self.experimental
                },
                'payload': {
                    'msgType': msg.messageType.name,
                    'contents': msg.toDict
                }
            }
            self.Web_server_DAT.webSocketSendText(each, json.dumps(msg))
