import oci
import os
import hashlib

CONFIG = oci.config.from_file()
OBJECT_STORAGE = oci.object_storage.ObjectStorageClient(CONFIG)
NAME_SPACE = OBJECT_STORAGE.get_namespace().data
BUCKET_NAME = "ociextention"


def calculate_md5(path):
  with open(path, "rb") as content:
    hash_md5 = hashlib.md5()
    for chunk in iter(lambda: content.read(4096), b""):
      hash_md5.update(chunk)
    return hash_md5.digest().encode('base64').strip()


def get_objects_to_dict():
  d = {}
  for obj in OBJECT_STORAGE.list_objects(OBJECT_STORAGE.get_namespace().data, BUCKET_NAME, fields="md5").data.objects:
    d[obj.name] = obj.md5
  return d


def put_object(directory):
  existing_objects = get_objects_to_dict()
  for dir_name, _, file_list in os.walk(directory):
    for file_name in file_list:
      if do_not_upload(dir_name, file_name):
        continue
      path = dir_name + "/" + file_name
      if os.path.isfile(path):
        name = path[2:]
        file_name, file_extension = os.path.splitext(name)
      else:
        continue
      md5 = calculate_md5(path)
      with open(path, "rb") as content:
        if md5 == existing_objects.get(name):
          print(u"skip:\t{} (file exists)".format(name))
          continue
        if file_extension == '.json':
          OBJECT_STORAGE.put_object(NAME_SPACE, BUCKET_NAME, name, content, content_type='application/json', content_md5=md5)
        else:
          OBJECT_STORAGE.put_object(NAME_SPACE, BUCKET_NAME, name, content, content_md5=md5)
        print(u"upload:\t{} (new file)".format(name))


def do_not_upload(dir_name, file_name):
  if file_name in ("upload.py", "README.md"):
    return True
  if file_name[0] == '.':
    return True
  if len(dir_name) > 2 and dir_name[2] == '.':
    return True
  return False


if __name__ == "__main__":
  put_object(".")
