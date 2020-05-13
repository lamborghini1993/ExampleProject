# -*- coding:utf-8 -*-
'''
@Description:
@Author: lamborghini1993
@Date: 2020-05-04 14:28:58
@UpdateDate: 2020-05-13 15:39:08
'''

import sys

# 直接用脚本
sys.path.append("Script")

# 未加密-fls
# sys.path.append("Script.fls")

# 加密-fls
# import zipfile
# from Crypto.Cipher import Blowfish
# import types
# import marshal
# KEY = "D*5Kh$rjh_+)(763{|GLG!~@HTH4ggr".encode("utf-8")
# blowfish = Blowfish.new(KEY, Blowfish.MODE_ECB)

# with zipfile.ZipFile("Script.fls", "r") as myzip:
#     for x in myzip.infolist():
#         with myzip.open(x.filename) as myfile:
#             encode = myfile.read()
#             code = blowfish.decrypt(encode)
#             new_module = types.ModuleType(x.filename)
#             sys.modules[x.filename] = new_module
#             co = marshal.loads(code[16:])
#             # import 顺序问题
#             exec(co, new_module.__dict__)

# # pyarmor加密为fls
# sys.path.append("pyarmor.fls")

import main
main.Start()
