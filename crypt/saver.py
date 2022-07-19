from typing import Protocol
from crypt.config import DEFAULT_PASSWORD_PATH

class PasswordSaver(Protocol):
    def save(self, path, password) -> None: ...


class FilePasswordSaver:
    def __init__(
        self,
        path=DEFAULT_PASSWORD_PATH
    ) -> None:
        self.path = path

    def save(self, password) -> None:
        with open(self.path, "w") as f:
            f.write(password)