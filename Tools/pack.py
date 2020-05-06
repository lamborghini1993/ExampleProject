# -*- coding:utf-8 -*-
'''
@Description: 打包工具
编译成pyc，然后加密
@Author: lamborghini1993
@Date: 2020-05-04 15:01:42
@UpdateDate: 2020-05-06 19:05:18
'''

import os
import py_compile
import zipfile
import shutil

from Crypto.Cipher import Blowfish


class PyEncrypt:
    KEY = "D*5Kh$rjh_+)(763{|GLG!~@HTH4ggr".encode("utf-8")

    def __init__(self):
        self.scriptPath = os.path.abspath("./Script/")
        self.flsPath = os.path.abspath("./Temp")
        self.blowfish = Blowfish.new(self.KEY, Blowfish.MODE_ECB)
        self.Compile()

    def Compile(self):
        lstPYCFile = []
        curPath = os.getcwd()
        os.chdir(self.scriptPath)
        for rootPath, dirPaths, filenames in os.walk("."):
            if rootPath == ".":
                rootPath = ""
            else:
                rootPath = os.path.normpath(rootPath)
            for filename in filenames:
                if not filename.endswith(".py"):
                    continue
                pypath = os.path.join(self.scriptPath, rootPath, filename)
                pycpath = os.path.join(self.flsPath, rootPath, filename + "c")
                py_compile.compile(pypath, pycpath)
                self.Rewrite(pycpath)
                lstPYCFile.append(pycpath)
                print(pypath, "---->", pycpath)
        os.chdir(curPath)

        self.ZipPath(lstPYCFile)

    def Encrypt(self, code: bytes) -> bytes:
        l = len(code)
        if l % 8:
            code += b" " * (8 - l % 8)
        encode = self.blowfish.encrypt(code)
        return encode

    def Decrypt(self, encode: bytes) -> bytes:
        return self.blowfish.decrypt(encode)

    def Rewrite(self, filename: str):
        with open(filename, "rb+") as f:
            code = f.read()
            f.seek(0)
            f.truncate()
            f.write(self.Encrypt(code))

    def TestDecrypt(self):
        enfilename = "./Temp/main_en.pyc"
        filename = "./Temp/main_decrypt.pyc"
        code = None
        with open(enfilename, "rb") as f:
            code = f.read()
        decode = self.blowfish.decrypt(code)
        with open(filename, "wb") as f:
            f.write(decode)

    def ZipPath(self, pycList: list):
        pre = len(self.flsPath)
        myflsfile = "Script.fls"
        with zipfile.ZipFile(myflsfile, "w") as myzip:
            for filename in pycList:
                arcname = filename[pre:]
                myzip.write(filename, arcname)
        shutil.rmtree(self.flsPath)


if __name__ == "__main__":
    PyEncrypt()
