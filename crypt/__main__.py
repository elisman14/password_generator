from crypt.pass_generator import PasswordGenerator, PasswordGeneratorV1


def start() -> None:
    pg:PasswordGenerator = PasswordGeneratorV1()
    pg.generation()