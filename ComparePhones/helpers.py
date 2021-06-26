import os, datetime, random

def upload_file_name(instance, filename):
    _, ext = os.path.splitext(filename)

    return "media/{}/{:%Y-%m-%d-%H-%M-%S}-{}-{}".format(
        datetime.datetime.now().strftime("%Y%m"),
        datetime.datetime.now(), random.randint(1000, 9999), ext)

