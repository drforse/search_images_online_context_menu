class PayloadTooLarge(Exception):
    def __init__(self, txt: str = None):
        super().__init__(txt)


class SearchEngineNotFound(Exception):
    def __init__(self, txt: str = None):
        super().__init__(txt)


class ConfigError(Exception):
    def __init__(self, txt: str = None):
        super().__init__(txt)


class CaptchaOccurred(Exception):
    def __init__(self, txt: str = "Произошла капча!"):
        super().__init__(txt)
