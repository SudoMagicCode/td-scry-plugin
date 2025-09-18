from enum import Enum
import json


class scryErrorLevel(Enum):
    info = 0
    warning = 1
    error = 2
    fatal = 3


class scryErrorOpType(Enum):
    comp = 'COMP'
    top = 'TOP'
    chop = 'CHOP'
    sop = 'SOP'
    pop = 'POP'
    mat = 'MAT'
    dat = 'DAT'
    custom = 'CUSTOM'
    misc = 'MISC'


class scryMsgType(Enum):
    message = 'message',
    error = 'error'


class scryAbstractMessage:
    def __init__(self,
                 message: str,
                 source: str,
                 absFrame: int,
                 severity: scryErrorLevel,
                 msgType: scryMsgType):
        self.message = message
        self.source = source
        self.severity = severity
        self.absFrame = absFrame
        self.messageType = msgType

    @property
    def _toDict(self) -> dict:
        dataAsDict: dict = {
            'message': self.message,
            'source': self.source,
            'severity': self.severity.value,
            'absFrame': self.absFrame,
            'msgType': self.messageType.value
        }
        return dataAsDict


class scryMessage(scryAbstractMessage):
    def __init__(self, message: str, source: str, absFrame: int):
        super().__init__(
            message=message,
            source=source,
            absFrame=absFrame,
            severity=scryErrorLevel.info,
            msgType=scryMsgType.message)

    @property
    def toDict(self) -> dict:
        return self._toDict

    @property
    def toJsonString(self) -> str:
        return json.dumps(self.toDict)


class scryError(scryAbstractMessage):
    def __init__(
            self,
            message: str,
            source: str,
            absFrame: int,
            severity: int,
            opType: scryErrorOpType):

        super().__init__(
            message=message,
            source=source,
            absFrame=absFrame,
            severity=scryErrorLevel(severity),
            msgType=scryMsgType.error)

        self.opType = scryErrorOpType(opType)

    def __repr__(self) -> str:
        return self.message

    @property
    def toDict(self) -> dict:
        dataAsDict: dict = self._toDict
        dataAsDict["opType"] = self.opType.name

        return dataAsDict

    @property
    def toJsonString(self) -> str:
        return json.dumps(self.toDict)
