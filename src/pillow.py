"""
图像处理库

安装:
pip3 install pillow

参考:
官网: https://pillow.readthedocs.io/en/stable/
"""

from PIL import Image, ImageDraw
from io import BytesIO

# 绘制 200 * 200 的空白底图
background = Image.new('RGBA', (200, 200), (0xff,) * 4)

# 打开网络上的图片
img = Image.open(BytesIO(requests.get('https://xxx/xxx/xxx.png').content))

# 粘贴图片到指定位置（透明部分变白）
background.paste(img, (2, 2))

# 粘贴图片到指定位置（保留透明部分）
background.paste(img, (2, 2), mask=img)

# 让图片变透明
mask = Image.new('RGBA', img.size)
img = Image.blend(img, mask, 0.3)

# 画圆圈
img = Image.new('RGBA', (200, 200), (0xff,) * 4)
img_draw = ImageDraw.Draw(img)
img_draw.ellipse((0, 0, img.size[0], avatar.size[1]), outline='#000', width=2)


def resize(img, zoom):
        """放大图像
        单纯的放大比例，例如原先 1*1 的像素会变成 2*2 的像素

        Args:
            img: Image 要放大的底图
            zoom: number 放大倍率

        Returns:
            Image 放大后的底图
        """
        size = img.size
        new_img = Image.new('RGBA', (size[0] * zoom, size[1] * zoom), (0xff,) * 4)

        print('正在放大底图...')
        # 遍历所有行
        for y in range(size[1]):
            row = []
            # 把每个像素复制 zoom 份
            for x in range(size[0]):
                for _ in range(zoom):
                    row.append(img.getpixel((x, y)))
            # 把每个扩充好的行重复粘贴 zoom 份
            for new_y in range(zoom * y - zoom, zoom * y):
                for new_x, pixel in enumerate(row):
                    # print(new_x, new_y, pixel)
                    new_img.putpixel((new_x, new_y), pixel)
            print(f'{y}/{size[1]}')

        return new_img