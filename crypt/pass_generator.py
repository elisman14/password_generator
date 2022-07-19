import random
import string
from typing import Protocol
from crypt.saver import PasswordSaver


class PasswordGenerator(Protocol):
    def generation(self) -> None: ...

class RandomChoicePasswordGenerator:
    def __init__(
        self,
        saver: PasswordSaver  
    ) -> None:
        self.saver = saver

    def generate(self) -> None:
        alphabet: list[str] = self._alphabet_generate()
        password: str = self._password_generate(alphabet)
        self.saver.save(password)

    def _password_generate(self, alph: list[str]) -> str:
        return "".join(random.choices(alph, k=20))

    def _alphabet_generate(self) -> list[str]:
        return list(string.ascii_letters + string.digits + "!@#$%^&*()")
