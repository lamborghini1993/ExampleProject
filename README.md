<!--
 * @Description: 
 * @Author: lamborghini1993
 * @Date: 2020-05-04 14:12:19
 * @UpdateDate: 2020-05-13 20:00:59
 -->

# 1. 搭建完美开发环境

- 需要的库:`pip install pylint autopep8 isort`

## 1.1. editorconfig
### 1.1.1. 简介 [官网](https://EditorConfig.org)
> EditorConfig可以帮助在不同的编辑器和IDE上从事同一项目的多个开发人员保持一致的编码样式。EditorConfig项目包括一个用于定义编码样式的文件格式和一个文本编辑器插件集合，这些文本编辑器插件使编辑器可以读取文件格式并遵循定义的样式。EditorConfig文件易于阅读，并且可以与版本控制系统很好地协同工作。
>
> vscode需要安装`EditorConfig`插件

### 1.1.2. 参数说明
- indent_style:分别设置为tab或space使用硬标签或软标签。该值不区分大小写。
- indent_size:设置为一个整数，该整数定义每个缩进级别使用的列数以及软标签的宽度（如果支持）。如果等于tab，indent_size则应将其设置为制表符大小，该大小应为tab_width（如果指定）；否则，标签大小由编辑器设置。该值不区分大小写。
- tab_width:设置为整数，定义用于表示制表符的列数。该默认值为，indent_size通常不需要指定。
- end_of_line:设置为lf，cr或crlf控制表示换行的方式。该值不区分大小写。
- charset:设置为latin1，utf-8，utf-8-bom，utf-16be或utf-16le控制字符集。utf-8-bom不鼓励使用。
- trim_trailing_whitespace:设置为true删除文件中所有在换行符之前的空白字符，并false确保没有。
- insert_final_newline:设置以true确保文件在保存时以换行符结尾，并false 确保没有。
- root:必须在序言中指定。设置为true停止.editorconfig对当前文件的 文件搜索。该值不区分大小写。

## 1.2. isort
# 2. 简介 [官网](https://github.com/timothycrosley/isort)
> isort是一个Python实用程序/库，用于按字母顺序对导入进行排序，并自动将其分成多个部分和类型。它为各种编辑器提供了命令行实用程序，Python库和插件，可快速对所有导入内容进行排序。它需要Python 3.6+才能运行，但也支持格式化Python 2代码。

### 2.0.1. 相关链接
- [ide插件](https://github.com/timothycrosley/isort/wiki/isort-Plugins)
- [设置说明](https://github.com/timothycrosley/isort/wiki/isort-Settings)


## 2.1. pylint
> Pylint是一种工具，可检查Python代码中的错误，尝试实施编码标准并查找代码气味。它还可以查找某些类型错误，可以建议有关如何重构特定块的建议，并可以为您提供有关代码复杂性的详细信息。
- [Pylint用户手册](http://pylint.pycqa.org/en/latest/)
### 2.1.1. 生成pylint配置文件
`python3 -m pylint --generate-rcfile > pylint.conf`
### 2.1.2. pylint配置外部路径
`pylint.conf`文件中init-hook添加如下：
`init-hook="import sys;sys.path.append("ExtraPath");"`


# 3. python字节码混淆
### 3.0.3. PyArmor
- PyArmor 是一个用于加密和保护 Python 脚本的工具
- [github](https://github.com/dashingsoft/pyarmor)
- [使用手册](https://pyarmor.readthedocs.io/zh/latest/)

### 3.0.4. code_obfuscate
https://github.com/c0cc/code_obfuscate


## 3.1. floss反混淆
- https://github.com/fireeye/flare-floss

## 3.2. opy、pyminifier  
- 字符混淆
