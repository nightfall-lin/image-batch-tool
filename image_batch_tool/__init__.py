"""图片批处理工具的公共接口。"""

from pathlib import Path
from typing import TypedDict

__all__ = ["ImageRecord", "build_image_record", "format_image_record"]


class ImageRecord(TypedDict):
    """一张图片的基础信息。"""

    name: str
    size_bytes: int
    suffix: str


def build_image_record(name: str, size_bytes: int) -> ImageRecord:
    """校验输入，并生成图片信息字典。

    Day 4 实操：按照 README 的“编码任务”完成此函数。
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("非法")
    if not isinstance(size_bytes, int) or isinstance(size_bytes, bool) or size_bytes < 0:
        raise ValueError("非法")
    suffix = Path(name).suffix.lower()
    if len(suffix) < 1:
        suffix = ""
    return {"name": name, "size_bytes": size_bytes, "suffix": suffix}


def format_image_record(record: ImageRecord) -> str:
    """把图片信息格式化为一行可读文本。

    Day 4 实操：按照 README 的“编码任务”完成此函数。
    """
    return f"{record['name']} | {record['suffix']} | {record['size_bytes']} bytes"
