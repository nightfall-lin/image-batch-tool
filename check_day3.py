"""第 3 天验收：类、异常和 JSON 文件操作。"""

from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable, cast

from day3_report import ProcessingReport, load_report


def expect_exception(
    expected_exception: type[Exception],
    action: Callable[[], object],
) -> None:
    """断言 action 抛出指定异常。"""

    try:
        action()
    except expected_exception:
        return
    except Exception as error:
        raise AssertionError(
            f"期望 {expected_exception.__name__}，实际得到 {type(error).__name__}"
        ) from error

    raise AssertionError(f"期望抛出 {expected_exception.__name__}")


def main() -> None:
    report = ProcessingReport("camera-batch")
    empty_report = {
        "job_name": "camera-batch",
        "image_count": 0,
        "images": [],
    }
    assert report.to_dict() == empty_report

    report.add_image("robot.png")
    report.add_image("CAMERA.JPG")
    saved_report = {
        "job_name": "camera-batch",
        "image_count": 2,
        "images": ["robot.png", "CAMERA.JPG"],
    }
    assert report.to_dict() == saved_report

    expect_exception(ValueError, lambda: ProcessingReport(cast(str, 123)))
    expect_exception(ValueError, lambda: ProcessingReport(""))
    expect_exception(ValueError, lambda: ProcessingReport("   "))

    expect_exception(ValueError, lambda: report.add_image(cast(str, 123)))
    expect_exception(ValueError, lambda: report.add_image(""))
    expect_exception(ValueError, lambda: report.add_image("   "))

    with TemporaryDirectory() as temporary_directory:
        output_path = Path(temporary_directory) / "report.json"
        report.save_json(output_path)
        assert output_path.exists()

        raw_content = output_path.read_text(encoding="utf-8")
        assert json.loads(raw_content) == saved_report
        assert load_report(output_path) == saved_report

        missing_path = Path(temporary_directory) / "missing.json"
        expect_exception(FileNotFoundError, lambda: load_report(missing_path))

    requirements = [
        "1/7：创建空报告后，任务名、图片数和图片列表正确。",
        "2/7：添加两张图片后，顺序和图片数正确。",
        "3/7：非法任务名抛出 ValueError。",
        "4/7：非法图片名抛出 ValueError。",
        "5/7：save_json 创建 UTF-8 JSON 文件。",
        "6/7：保存内容和 load_report 读取内容与 to_dict 结果一致。",
        "7/7：读取不存在文件抛出 FileNotFoundError。",
    ]
    print("第 3 天验收通过：7/7")
    print("\n".join(requirements))


if __name__ == "__main__":
    main()
