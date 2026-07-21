"""第 1 天 Python 诊断 / Day 1 Python diagnostic.

先完成 Checkpoint 1：只计算总人数和平均分。
Start with Checkpoint 1: calculate only the total count and average score.

后续检查点会逐步加入及格统计、最高分和输入校验。
Later checkpoints will gradually add pass/fail counts, highest scores,
and input validation.
"""

from typing import Any


def summarize_scores(records: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(records)
    if total == 0: raise ValueError("record cannot be empty")
    if not isinstance(records, list): raise ValueError("not a valid record")
    for stu in records:
        if not isinstance(stu, dict) or "name" not in stu or "score" not in stu: raise ValueError("not a valid record")
        if not stu["name"].strip(): raise ValueError("name is empty")
        if isinstance(stu["score"], bool): raise ValueError("score cannot be a boolean")
        if not isinstance(stu["score"],(int, float)): raise ValueError("score must be a number")
        if stu["score"]<0 or stu["score"]>100: raise ValueError("score must be between 0 and 100")
    total = len(records)
    if total == 0: raise ValueError("record cannot be empty")
    average = round(sum(stu['score']for stu in records)/total,2)
    highest =max(stu["score"]for stu in records)
    top_students =[stu["name"] for stu in records if stu["score"]==highest]
    passed = len([stu for stu in records if stu['score']>= 60])
    failed = total -passed
    return {
        "total": total, 
        "average": average,
        "highest":highest,
        "top_students": top_students,
        "passed": passed,
        "failed": failed,
        }

    """返回成绩摘要 / Return a score summary.

    Checkpoint 1 rules / 第一个检查点规则：
    - records 是包含字典的列表 / records is a list of dictionaries;
    - 每个字典包含 ``score`` / each dictionary contains ``score``;
    - average 保留两位小数 / average is rounded to two decimal places.

    先只返回 ``total`` 和 ``average``。
    Return only ``total`` and ``average`` for now.

    后续检查点 / Later checkpoints:
    - Checkpoint 2: ``passed`` and ``failed``;
    - Checkpoint 3: ``highest`` and ``top_students``;
    - Checkpoint 4: validation and the complete acceptance test.
    """



