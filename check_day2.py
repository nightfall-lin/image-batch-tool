"""第 2 天验收 / Day 2 acceptance checks.

This file uses standard-library assertions. pytest is introduced on Day 6.
"""

from copy import deepcopy
from inspect import isgenerator

from day2_collections import filter_image_names, iter_image_names


NAMES = [
    "robot.png",
    "notes.txt",
    "CAMERA.JPG",
    "archive.tar.gz",
    "map.jpeg",
    "preview.WEBP",
    "README",
]
EXPECTED = ["robot.png", "CAMERA.JPG", "map.jpeg", "preview.WEBP"]


def main() -> None:
    original = deepcopy(NAMES)
    filtered = filter_image_names(NAMES)

    assert filtered == EXPECTED
    assert NAMES == original, "输入列表不能被修改 / Input list must not be modified"
    assert filter_image_names([]) == []

    stream = iter_image_names(NAMES)
    assert isgenerator(stream), "必须使用 yield / You must use yield"
    assert next(stream) == "robot.png"
    assert list(stream) == EXPECTED[1:]
    assert list(iter_image_names([])) == []

    print("第 2 天验收通过：7/7 / Day 2 acceptance passed: 7/7")


if __name__ == "__main__":
    main()
