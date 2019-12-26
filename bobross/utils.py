import os
import uuid


ABBREVIATIONS = ['url']


def camelcase(word):
    word = pascalcase(word)
    return word[:1].lower() + word[1:]


def pascalcase(word):
    return ''.join(
        letter.capitalize() if letter not in ABBREVIATIONS else letter.upper() for letter in word.split('_')
    )


def upload_to(obj, filename):
    if hasattr(obj, 'file_directory'):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join(obj.file_directory, filename)
    else:
        raise AttributeError("%s does not have 'file_directory' attribute" % obj.__class__.__name__)
