"""完整验收 / Full acceptance checks for Day 1.

先完成 check_day1_step1.py，再运行本文件。
Complete check_day1_step1.py first, then run this file.

This intentionally uses plain assertions. pytest is introduced later in Week 1.
"""

from copy import deepcopy

from day1_diagnostic import summarize_scores


def expect_value_error(value: object) -> None:
    try:
        summarize_scores(value)  # type: ignore[arg-type]
    except ValueError:
        return
    raise AssertionError(f"Expected ValueError for {value!r}")


def main() -> None:
    records = [
        {"name": "Alice", "score": 88},
        {"name": "Bob", "score": 55},
        {"name": "Carol", "score": 88.0},
    ]
    original = deepcopy(records)
    result = summarize_scores(records)

    assert result == {
        "total": 3,
        "average": 77.0,
        "highest": 88,
        "top_students": ["Alice", "Carol"],
        "passed": 2,
        "failed": 1,
    }
    assert records == original, "The function must not mutate its input"

    single = summarize_scores([{"name": "Dana", "score": 60}])
    assert single["average"] == 60
    assert single["passed"] == 1
    assert single["failed"] == 0

    expect_value_error([])
    expect_value_error("not a list")
    expect_value_error([{"name": "", "score": 70}])
    expect_value_error([{"name": "Eve"}])
    expect_value_error([{"name": "Eve", "score": True}])
    expect_value_error([{"name": "Eve", "score": 101}])
    expect_value_error(None)
    expect_value_error([{"name": 123, "score": 70}])

    print("第 1 天完整诊断通过：9/9 / Day 1 full diagnostic passed: 9/9")


if __name__ == "__main__":
    main()
