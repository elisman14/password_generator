from crypt.pass_generator import PasswordGenerator, RandomChoicePasswordGenerator
from crypt.saver import PasswordSaver, FilePasswordSaver


def getPasswordGenerator() -> PasswordGenerator:
    saver: PasswordSaver = FilePasswordSaver()
    return RandomChoicePasswordGenerator(saver)