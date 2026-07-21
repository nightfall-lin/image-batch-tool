from typing import Any


def summarize_scores(records: list[dict[str, Any]]) -> dict[str, Any]:
    """返回成绩摘要 / Return a score summary."""
    if not records: raise ValueError("record cannot be empty")
    if not isinstance(records, list): raise ValueError("not a valid record")
    total = len(records)
    for stu in records:
        if not isinstance(stu, dict) or "name" not in stu or "score" not in stu: raise ValueError("not a valid record")
        if not isinstance(stu["name"], str) or not stu["name"].strip(): raise ValueError("name should be a non-empty string")
        if isinstance(stu["score"], bool): raise ValueError("score cannot be a boolean")
        if not isinstance(stu["score"],(int, float)): raise ValueError("score must be a number")
        if stu["score"]<0 or stu["score"]>100: raise ValueError("score must be between 0 and 100")
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





