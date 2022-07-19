from email import generator
from crypt.pass_generator import PasswordGenerator
from crypt import factories


def start() -> None:
    generator: PasswordGenerator = factories.getPasswordGenerator()
    generator.generate()


if __name__ == "__main__":
    start()