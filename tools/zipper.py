import zipfile
import os
from pathlib import Path

zf = zipfile.ZipFile("zip/access_log_lambda.zip", "w")

target_dir = str(Path(__file__).parent.parent.joinpath("functions/access_log_lambda"))

for dirname, subdirs, files in os.walk(target_dir):
    if '__pycache__' in subdirs:
        subdirs.remove('__pycache__')
    for filename in files:
        filepath = os.path.join(dirname, filename)
        zf.write(filepath, os.path.relpath(filepath, target_dir))
zf.close()
