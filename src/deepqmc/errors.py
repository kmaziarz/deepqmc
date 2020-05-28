__all__ = ()


class InfoException(Exception):
    def __init__(self, info=None):
        self.info = info or {}
        super().__init__(self.info)


class DeepQMCError(Exception):
    pass


class NanError(DeepQMCError):
    def __init__(self, rs):
        super().__init__()
        self.rs = rs


class TrainingBlowup(DeepQMCError):
    pass


class TrainingCrash(DeepQMCError):
    def __init__(self, state):
        super().__init__()
        self.state = state


class LUFactError(InfoException, DeepQMCError):
    pass
