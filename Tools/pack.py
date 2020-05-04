# -*- coding:utf-8 -*-
'''
@Description: 打包工具
@Author: lamborghini1993
@Date: 2020-05-04 15:01:42
@UpdateDate: 2020-05-04 19:47:04
'''

import os
import py_compile
import zipfile
import shutil


def Compile():
    lstPYCFile = []
    scriptPath = os.path.abspath("./Script/")
    flsPath = os.path.abspath("./Temp")
    curPath = os.getcwd()
    print(scriptPath)
    os.chdir(scriptPath)
    for rootPath, dirPaths, filenames in os.walk("."):
        if rootPath == ".":
            rootPath = ""
        else:
            rootPath = os.path.normpath(rootPath)
        for filename in filenames:
            if not filename.endswith(".py"):
                continue
            pypath = os.path.join(scriptPath, rootPath, filename)
            pycpath = os.path.join(flsPath, rootPath, filename + "c")
            py_compile.compile(pypath, pycpath)
            lstPYCFile.append(pycpath)
            print(pypath, "---->", pycpath)
    os.chdir(curPath)

    ZipPath(flsPath, lstPYCFile)


def ZipPath(flsPath: str, pycList: list):
    pre = len(flsPath)
    myzipfile = "Script.zip"
    myflsfile = "Script.fls"
    with zipfile.ZipFile(myzipfile, "w") as myzip:
        for filename in pycList:
            arcname = filename[pre:]
            myzip.write(filename, arcname)
    shutil.rmtree(flsPath)


if __name__ == "__main__":
    Compile()
