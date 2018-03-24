#!/bin/bash

# 编译文档网页
make html
make latexpdf

# 使用 ghp-import 导出_build/html 目录到 gh-pages 分支。注意一定要使用 -n 
# 参数来生成.nojekyll 文件。
# 手动发布，可以利用Travis CI实现自动发布(利用密码验证)，具体参见.travis.yml文件。
ghp-import -n build/html/

# 分别 push master 分支和 gh-pages 分支到 github 。
git add $1
git commit -m $1
git push -u origin master
git push -u origin gh-pages

###############################################################################
# 存在的问题                                                                  #
# 1. 语言问题                                                                 #
#   zh_CN无法正常利用Travis CI，出现no babel option known for language        #
#   'zh_CN'错误，但是可以正常编译。                                           #
# 2. sphinx_rtd_theme主题出现英文字母缺失问题，该主题的目录集中在左侧。       #
#                                                                             #
# 自动发布，仅需要提交到master，一步到位，即：git push -u origin master       #
# 自动触发发布至gh-pages。                                                    #
#                                                                             #
# 自动化生成文档，利用代码生成相应的项目文档。                                #
# 通过 autodoc 可以告知 Sphinx 查看 docstrings 并生成项目的文档。             #
#                                                                             #
# 首先打开 docs/source/conf.py 文件修改配置                                   #
#                                                                             #
# import os                                                                   #
# import sys                                                                  #
# sys.path.insert(0, os.path.abspath('../..'))                                #
###############################################################################
