"""第 3 天：类、异常和 JSON 文件操作。"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any


class ProcessingReport:
    """保存一次图片处理任务的记录。"""

    def __init__(self, job_name: str) -> None:
        """使用有效的任务名称创建报告。"""
        if not isinstance(job_name, str) or not job_name.strip(): raise ValueError("任务名称需为非空字符串")
        self.job_name = job_name
        self.images = []

        #        raise NotImplementedError("完成 Day 3：初始化报告")

    def add_image(self, image_name: str) -> None:
        """添加一个有效的图片文件名。"""
        if not isinstance(image_name, str) or not image_name.strip() : raise ValueError("图片文件名需为非空字符串")
        self.images.append(image_name)

        #        raise NotImplementedError("完成 Day 3：添加图片")

    def to_dict(self) -> dict[str, Any]:
        """返回可序列化为 JSON 的报告字典。"""
        return{"job_name": self.job_name, "image_count": len(self.images), "images": self.images}

        #        raise NotImplementedError("完成 Day 3：转换为字典")

    def save_json(self, output_path: str | Path) -> None:
        """将报告写入 UTF-8 JSON 文件。"""
        txt = json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
        path = Path(output_path)
        path.write_text(txt, encoding="utf-8")

        #        raise NotImplementedError("完成 Day 3：保存 JSON")


def load_report(input_path: str | Path) -> dict[str, Any]:
    """从 UTF-8 JSON 文件读取报告。

    文件不存在时保留并抛出 FileNotFoundError。"""
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError("报告不存在")
    load = path.read_text(encoding="utf-8")
    return json.loads(load)

    #        raise NotImplementedError("完成 Day 3：读取 JSON")
