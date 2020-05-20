"""
将 svg 转换成 png 或者 pdf

需要安装 cairo 依赖，windows 和 mac 都需要手动安装，而 ubuntu 可以自动安装

安装:
pip3 install cairosvg

参考:
官网 https://cairosvg.org/
"""

import cairosvg
import requests

# 转换网络上的 svg 到 png
svg = requests.get(f'https://xxx/xxx.svg').content
cairosvg.svg2png(bytestring=svg, write_to='result.png')

# 转换本地的 svg 到 pdf
cairosvg.svg2pdf(url='image.svg', write_to='image.pdf')