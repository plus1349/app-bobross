import os
import uuid


def upload_to(obj, filename):
    if hasattr(obj, 'file_directory'):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join(obj.file_directory, filename)
    else:
        raise AttributeError("%s does not have 'file_directory' attribute" % obj.__class__.__name__)
