import os
import uuid


ABBREVIATIONS = []


def camelcase(word):
    word = pascalcase(word)
    return word[:1].lower() + word[1:]


def pascalcase(word):
    return ''.join(
        letter.capitalize() if letter not in ABBREVIATIONS else letter.upper() for letter in word.split('_')
    )


def file_directory(instance, filename):
    if hasattr(instance, 'file_directory'):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join(instance.file_directory, filename)

    raise AttributeError(
        "{name} does not have 'file_directory' attribute".format(
            name=instance.__class__.__name__
        )
    )


def image_directory(instance, filename):
    if hasattr(instance, 'image_directory'):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join(instance.image_directory, filename)

    raise AttributeError(
        "{name} does not have 'image_directory' attribute".format(
            name=instance.__class__.__name__
        )
    )
