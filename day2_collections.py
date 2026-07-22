"""第 2 天：列表推导式、迭代器和生成器。

Day 2: list comprehensions, iterators, and generators.
"""

from collections.abc import Generator


IMAGE_SUFFIXES = (".jpg", ".jpeg", ".png", ".webp")


def filter_image_names(names: list[str]) -> list[str]:
    """返回图片文件名列表 / Return a list of image filenames.

    文件后缀不区分大小写，返回顺序与输入相同。
    Extensions are case-insensitive and input order is preserved.
    """
    res = []
    for n in names :
        if n.lower().endswith(IMAGE_SUFFIXES):
            res.append(n)
    return res
    raise NotImplementedError("Complete Day 2: filter image names")


def iter_image_names(names: list[str]) -> Generator[str, None, None]:
    """逐个产生图片文件名 / Yield image filenames one at a time.

    使用 ``yield``，不要先创建完整的图片列表。
    Use ``yield`` instead of building the entire image list first.
    """
    for n in names:
        if n.lower().endswith(IMAGE_SUFFIXES):
            yield n

