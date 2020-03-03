from PySide2.QtCore import Signal, QObject, QEventLoop, Slot


class PcMoveSignal(QObject):
    sig = Signal(list, list, list, bool)


class PlayerMoveSignal(QObject):
    def __init__(self):
        super(PlayerMoveSignal, self).__init__()
        self.sig = Signal(str)
        self.eventLoop = QEventLoop(self)
        self.data = None

    @Slot(str)
    def stop_waiting(self, data):
        self.data = data
        self.eventLoop.exit()

    def wait_for_move(self):
        self.eventLoop.exec_()
        return self.data