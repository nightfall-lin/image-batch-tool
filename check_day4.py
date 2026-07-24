"""Day 4 自动验收：虚拟环境、包结构、类型标注和函数行为。"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import cast, get_type_hints, is_typeddict

import image_batch_tool
from image_batch_tool import ImageRecord, build_image_record, format_image_record


PROJECT_ROOT = Path(__file__).resolve().parent
EXPECTED_PYTHON = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"


def same_path(left: Path, right: Path) -> bool:
    """在 Windows 上忽略路径大小写后比较两个绝对路径。"""
    return os.path.normcase(str(left.resolve())) == os.path.normcase(str(right.resolve()))


def expect_value_error(action: object, description: str) -> None:
    """确认一个无参数可调用对象会抛出 ValueError。"""
    if not callable(action):
        raise AssertionError(f"{description}：测试代码不是可调用对象")
    try:
        action()
    except ValueError:
        return
    except Exception as error:
        raise AssertionError(
            f"{description}：应抛出 ValueError，实际抛出 {type(error).__name__}"
        ) from error
    raise AssertionError(f"{description}：没有抛出 ValueError")


def check_1_python_version() -> None:
    assert sys.version_info[:2] == (3, 10), (
        f"要求 Python 3.10，当前是 {sys.version_info.major}.{sys.version_info.minor}"
    )


def check_2_virtual_environment() -> None:
    assert sys.prefix != sys.base_prefix, "当前没有进入虚拟环境，请先激活 .venv"


def check_3_project_interpreter() -> None:
    assert same_path(Path(sys.executable), EXPECTED_PYTHON), (
        f"当前解释器是 {sys.executable}，要求使用 {EXPECTED_PYTHON}"
    )


def check_4_public_api() -> None:
    expected = {"ImageRecord", "build_image_record", "format_image_record"}
    assert set(image_batch_tool.__all__) == expected, (
        f"__all__ 应只公开 {sorted(expected)}，实际为 {image_batch_tool.__all__}"
    )
    for name in expected:
        assert hasattr(image_batch_tool, name), f"包中缺少公共名称 {name}"


def check_5_typed_dict() -> None:
    assert is_typeddict(ImageRecord), "ImageRecord 必须使用 TypedDict 定义"
    assert get_type_hints(ImageRecord) == {
        "name": str,
        "size_bytes": int,
        "suffix": str,
    }, "ImageRecord 的三个字段或字段类型不正确"


def check_6_function_annotations() -> None:
    assert get_type_hints(build_image_record) == {
        "name": str,
        "size_bytes": int,
        "return": ImageRecord,
    }, "build_image_record 的参数或返回类型标注不正确"
    assert get_type_hints(format_image_record) == {
        "record": ImageRecord,
        "return": str,
    }, "format_image_record 的参数或返回类型标注不正确"


def check_7_valid_record() -> None:
    assert build_image_record("Robot.PNG", 2048) == {
        "name": "Robot.PNG",
        "size_bytes": 2048,
        "suffix": ".png",
    }, "合法输入没有生成要求的字典，注意扩展名必须转为小写"


def check_8_invalid_names() -> None:
    invalid_names = ["", "   ", cast(str, 123), cast(str, None)]
    for name in invalid_names:
        expect_value_error(
            lambda name=name: build_image_record(name, 10),
            f"非法文件名 {name!r}",
        )


def check_9_invalid_sizes() -> None:
    invalid_sizes = [-1, cast(int, 1.5), cast(int, "10"), cast(int, True)]
    for size in invalid_sizes:
        expect_value_error(
            lambda size=size: build_image_record("photo.jpg", size),
            f"非法文件大小 {size!r}",
        )


def check_10_format_record() -> None:
    record: ImageRecord = {
        "name": "Robot.PNG",
        "size_bytes": 2048,
        "suffix": ".png",
    }
    assert format_image_record(record) == "Robot.PNG | .png | 2048 bytes", (
        "格式必须严格为：文件名 | 小写扩展名 | 字节数 bytes"
    )


def main() -> None:
    checks = [
        ("Python 版本是 3.10", check_1_python_version),
        ("已进入虚拟环境", check_2_virtual_environment),
        ("解释器来自项目 .venv", check_3_project_interpreter),
        ("包可以导入且公共接口正确", check_4_public_api),
        ("ImageRecord 字段及类型正确", check_5_typed_dict),
        ("两个函数的类型标注正确", check_6_function_annotations),
        ("合法输入生成正确记录", check_7_valid_record),
        ("非法文件名均被拒绝", check_8_invalid_names),
        ("非法文件大小及 True 均被拒绝", check_9_invalid_sizes),
        ("记录被格式化为指定文本", check_10_format_record),
    ]
    passed = 0

    for number, (description, check) in enumerate(checks, start=1):
        try:
            check()
        except Exception as error:
            print(f"[失败 {number}/10] {description}")
            print(f"  原因：{type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"[通过 {number}/10] {description}")

    print(f"\nDay 4 验收结果：{passed}/10")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
