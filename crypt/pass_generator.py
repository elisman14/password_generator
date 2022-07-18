import random
import string
from typing import Protocol


class PasswordGenerator(Protocol):
    def generation(self) -> None: ...

class PasswordGeneratorV1:
    def __init__(self) -> None:
        pass

    def generation(self) -> None:
        alphabet: list[str] = self.alph_generation()
        password: str = self.pass_generation(alphabet)
        with open("./tests/password.txt", "w") as f:
            f.write(password)

    def pass_generation(self, alph: list[str]) -> str:
        return "".join(random.choices(alph, k=20))

    def alph_generation(self) -> list[str]:
        return list(string.ascii_letters + string.digits + "!@#$%^&*()")
