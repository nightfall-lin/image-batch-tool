# image-batch-tool

五个月学习计划的第一个实践项目。
The first practice project in the five-month learning plan.

最终目标是完成图片扫描、尺寸调整、格式转换、错误记录、JSON 报告和自动化测试。
The final goal is to scan images, resize and convert them, record errors, generate JSON reports, and add automated tests.

## 当前状态 / Current status

- 第 1 天功能验收已通过：7/7。
  Day 1 functional acceptance passed: 7/7.
- 分步验收文件已经删除。
  The incremental checkpoint file has been removed.
- 提交前仍需完成代码审查中的健壮性和可读性修改。
  Robustness and readability issues from code review still need to be fixed before committing.

## 完整验收 / Full acceptance test

```powershell
python .\check_day1.py
```

预期输出 / Expected output:

```text
第 1 天完整诊断通过：7/7 / Day 1 full diagnostic passed: 7/7
```

## 环境 / Environment

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

必须显示 Python 3.10.x。
It must show Python 3.10.x.

## Git 操作 / Git workflow

`git config --local` 必须在 Git 仓库目录中执行。
`git config --local` must be run inside the Git repository.

```powershell
Set-Location "C:\Users\26643\Documents\Codex\2026-07-16\wo\work\image-batch-tool"
git rev-parse --show-toplevel
git config --local user.name "YOUR_GITHUB_USERNAME"
git config --local user.email "YOUR_GITHUB_EMAIL_OR_NOREPLY_EMAIL"
git status
```

确认用户名和邮箱正确、代码审查问题修复后再提交：
After verifying your identity and fixing the review findings, commit the work:

```powershell
git add .
git commit -m "feat: complete day 1 Python diagnostic"
```

## 学习原则 / Learning rule

可以使用 AI 解释报错、审查代码和设计边界测试，但必须能够独立解释最终保留的代码。
AI may explain errors, review code, and design edge-case tests, but you must be able to explain the final code yourself.
