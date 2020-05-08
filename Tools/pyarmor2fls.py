# -*- coding:utf-8 -*-
'''
@Description: pyarmor加密脚本打包成fls
@Author: lamborghini1993
@Date: 2020-05-08 17:46:04
@UpdateDate: 2020-05-08 19:33:19
'''

import os
import shutil
import zipfile

from pyarmor.pyarmor import main as call_pyarmor

call_pyarmor(['obfuscate', '--recursive', '--output', 'dist', 'Script/main.py'])

shutil.move("dist/pytransform", "pytransform")

start_dir = "dist"
zf = zipfile.ZipFile("pyarmor.fls", "w", zipfile.ZIP_DEFLATED)
for root_path, _, file_names in os.walk(start_dir):
    for filename in file_names:
        file1 = os.path.join(root_path, filename)
        file2 = file1[len(start_dir) + 1:]
        zf.write(file1, file2)
zf.close()

shutil.rmtree("dist")
