import oci
import os
config = oci.config.from_file()

for dir_name, subdir_list, file_list in os.walk('.'):
  for file_name in file_list:
    path = dir_name + "/" + file_name
    if file_name in ("upload.py", "README.md"):
      continue
    if file_name[0] == '.':
      continue
    if len(dir_name) > 2 and dir_name[2] == '.':
      continue
    if os.path.isfile(path):
      name = path[2:]
      print(path[2:])
      filename, file_extension = os.path.splitext(name)
      with open(path, "rb") as in_file:
        ostorage = oci.object_storage.ObjectStorageClient(config)
        if file_extension == '.json':
          ostorage.put_object(ostorage.get_namespace().data,
                            "ociextention",
                            name,
                            in_file,
                            content_type='application/json')
        else:
          ostorage.put_object(ostorage.get_namespace().data,
                              "ociextention",
                              name,
                              in_file)
        print("Finished uploading {}".format(name))
