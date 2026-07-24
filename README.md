# image-batch-tool

这是五个月学习计划的第一个实践项目。最终会完成图片扫描、尺寸调整、格式转换、错误记录、JSON 报告和自动化测试。

## 学习进度

- Day 1 已完成：函数、容器、输入校验和异常处理，完整验收 9/9。
- Day 2 已完成：文件名筛选、扩展名大小写处理、迭代器和生成器，完整验收 7/7。
- Day 3 已完成：类、异常和 JSON 文件读写，完整验收 7/7。
- 当前任务：第 1 周 Day 4，虚拟环境、包结构和类型标注。

## 已使用的知识点

### Day 1：函数、容器与输入校验

- 函数定义、参数、返回值和类型标注。
- 列表、字典、循环、`sum`、`max` 与列表筛选。
- `ValueError`：在使用数据前验证类型、字段和值域。
- 条件短路：先验证类型，再调用字符串方法。例如先判断 `isinstance(name, str)`，再使用 `name.strip()`。
- 函数不应修改传入的列表。

### Day 2：文件名筛选、迭代器和生成器

- `str.lower()` 与 `str.endswith()`：忽略扩展名大小写。
- 普通 `for` 循环和列表推导式都可以筛选数据。
- `yield`：逐个生成结果，不需要提前创建完整列表。
- `iter()`、`next()` 和生成器的逐步取值行为。
- 输入顺序需要在筛选后保持不变。

### Day 3：类、异常和 JSON 文件操作

- 使用 `class`、`__init__` 和 `self` 将数据与操作数据的方法组织在一起。
- 使用实例属性保存任务名和图片列表。
- 使用 `to_dict()` 将对象转换为可序列化的普通字典。
- 使用 `json.dumps`、`json.loads` 保存和读取 JSON。
- 使用 `Path.write_text`、`Path.read_text` 和 `encoding="utf-8"` 进行文本文件读写。
- 使用 `ValueError` 拒绝非法名称，使用 `FileNotFoundError` 表示文件不存在。

## Day 4 总目标

今天结束时，你应能解释虚拟环境、Python 包、`__init__.py`、`__all__`、函数类型标注和 `TypedDict` 的作用，并完成一个可导入、可验证的图片信息模块。

今天只有两个 Day 4 文件：

- 实操文件：`image_batch_tool\__init__.py`。这是唯一需要编写代码的文件。
- 验收文件：`check_day4.py`。只运行，不修改。

Day 1–3 文件不要移动或修改，旧的分步检查文件已经删除。

## Day 4 两小时安排

### 第 1 部分：复习 20 分钟

1. 用 5 分钟口头回答：为什么判断非空字符串时，要先判断 `isinstance(name, str)`，再调用 `name.strip()`？
2. 用 5 分钟口头回答：Day 2 为什么使用 `lower()` 处理扩展名？
3. 用 5 分钟查看 `day3_report.py`，找出函数参数、返回类型以及抛出 `ValueError` 的位置。
4. 用 5 分钟运行以下命令，确认 Day 1–3 仍然通过：

   ```powershell
   python .\check_day1.py
   python .\check_day2.py
   python .\check_day3.py
   ```

若其中任何一个失败，先检查是否已进入项目目录及虚拟环境；今天不要改 Day 1–3 的代码。

### 第 2 部分：定向学习 40 分钟

按下面顺序学习。达到每项“停止条件”后立即进入下一项，不继续扩展。

#### 1. 虚拟环境，10 分钟

主资源：[Python 官方文档：创建虚拟环境](https://docs.python.org/zh-cn/3/library/venv.html#creating-virtual-environments)。只看虚拟环境的用途、创建命令和 Windows 激活命令。

替代资源：在 Bilibili 搜索 `Python venv 虚拟环境 Windows 激活`，只看 `.venv\Scripts\Activate.ps1` 相关片段。

停止条件：能解释“虚拟环境让项目使用独立的 Python 解释器和依赖目录”，并知道激活命令是什么。不学习 conda、Poetry、uv 或 Docker。

#### 2. Python 包，10 分钟

主资源：[Python 官方教程：包](https://docs.python.org/zh-cn/3/tutorial/modules.html#packages)。只看“目录中为什么有 `__init__.py`”以及如何 `import` 包。

替代资源：在 Bilibili 搜索 `Python 包 __init__.py import`，只看包目录和导入示例。

停止条件：能解释为什么 `image_batch_tool` 是包，以及 `from image_batch_tool import ...` 会读取哪个文件。不学习发布 PyPI、`setup.py` 或复杂导入机制。

#### 3. 函数类型标注，10 分钟

主资源：[Python 官方教程：函数标注](https://docs.python.org/zh-cn/3/tutorial/controlflow.html#function-annotations)。只看参数后面的 `: 类型` 与箭头后的 `-> 返回类型`。

替代资源：在 Bilibili 搜索 `Python 类型标注 参数 返回值`，只看函数定义示例。

停止条件：能读懂 `def build_image_record(name: str, size_bytes: int) -> ImageRecord:`。不学习 mypy 配置或泛型。

#### 4. TypedDict，10 分钟

主资源：[Python 官方文档：TypedDict](https://docs.python.org/zh-cn/3/library/typing.html#typing.TypedDict)。只看类形式的定义方法和字段类型。

替代资源：在 Bilibili 搜索 `Python TypedDict 类型标注`，只看一个类形式示例。

停止条件：能解释 `ImageRecord` 运行时仍是普通字典，但类型工具知道它应该有哪些键。不学习 `Required`、`NotRequired` 或继承。

也可以一次搜索 `Python venv 包 __init__.py TypedDict 类型标注`，但总观看时间仍不得超过 40 分钟。

### 第 3 部分：独立编码 55 分钟

只打开并修改 `image_batch_tool\__init__.py`。不要复制完整答案，让现有骨架、下面的步骤和验收反馈引导你完成。

#### 任务 A：完成 `build_image_record`，建议 35 分钟

函数签名保持不变：

```python
def build_image_record(name: str, size_bytes: int) -> ImageRecord:
```

严格按以下顺序实现：

1. 删除函数中的 `raise NotImplementedError(...)`。
2. 验证 `name`：必须是 `str`，并且去掉首尾空白后不能是空字符串，否则抛出 `ValueError`。
3. 验证 `size_bytes`：必须是 `int`、不能是 `bool`、并且不能小于 `0`，否则抛出 `ValueError`。
4. 使用文件顶部已经导入的 `Path`。表达式 `Path(name).suffix` 能取得扩展名。
5. 对扩展名调用 `.lower()`。例如 `Robot.PNG` 得到 `.png`，没有扩展名时得到空字符串。
6. 返回一个包含且只包含 `name`、`size_bytes`、`suffix` 三个键的字典，不要修改原始文件名。

合法示例：

```python
build_image_record("Robot.PNG", 2048)
```

应返回：

```python
{
    "name": "Robot.PNG",
    "size_bytes": 2048,
    "suffix": ".png",
}
```

关键提示：Python 中 `True` 是 `bool`，同时 `isinstance(True, int)` 也是 `True`。因此只检查 `int` 不够，还要单独拒绝 `bool`。

#### 任务 B：完成 `format_image_record`，建议 10 分钟

函数签名保持不变：

```python
def format_image_record(record: ImageRecord) -> str:
```

严格按以下顺序实现：

1. 删除函数中的 `raise NotImplementedError(...)`。
2. 分别读取 `record["name"]`、`record["suffix"]` 和 `record["size_bytes"]`。
3. 使用 f-string 返回一行字符串，竖线两侧各有一个空格。
4. 不打印内容，不修改字典，只返回字符串。

指定结果必须完全一致：

```text
Robot.PNG | .png | 2048 bytes
```

#### 任务 C：自行检查，建议 10 分钟

1. 确认没有修改 `ImageRecord`、函数名、参数名或类型标注。
2. 确认两个 `NotImplementedError` 都已删除。
3. 确认代码缩进统一为 4 个空格。
4. 运行验收命令；若未通过，只根据失败项修改实操文件，再重新运行。

### 第 4 部分：验收与 Git，5 分钟

在 PowerShell 中逐行执行：

```powershell
Set-Location "C:\Users\26643\Documents\Codex\2026-07-16\wo\work\image-batch-tool"
.\.venv\Scripts\Activate.ps1
python .\check_day4.py
```

验收必须达到 `10/10`。检查文件会一次显示所有项目的通过或失败状态，不需要逐项向 AI 汇报。

## Day 4 验收标准

| 分数 | 具体要求 |
|---|---|
| 1/10 | 当前 Python 主版本和次版本必须是 3.10。 |
| 2/10 | `sys.prefix` 与 `sys.base_prefix` 不同，证明已进入虚拟环境。 |
| 3/10 | 当前解释器必须是本项目 `.venv\Scripts\python.exe`。 |
| 4/10 | `image_batch_tool` 能导入，`__all__` 只公开 `ImageRecord`、`build_image_record`、`format_image_record`。 |
| 5/10 | `ImageRecord` 必须是 `TypedDict`，并准确声明 `name: str`、`size_bytes: int`、`suffix: str`。 |
| 6/10 | 两个函数的参数和返回值类型标注必须与骨架一致。 |
| 7/10 | `build_image_record("Robot.PNG", 2048)` 返回指定的三键字典，扩展名为 `.png`。 |
| 8/10 | 空字符串、纯空格、整数和 `None` 作为文件名时都抛出 `ValueError`。 |
| 9/10 | 负数、浮点数、字符串和 `True` 作为文件大小时都抛出 `ValueError`。 |
| 10/10 | `format_image_record` 严格返回 `Robot.PNG | .png | 2048 bytes`。 |

只有终端最后显示 `Day 4 验收结果：10/10` 才算完成。代码能编译但未达到 10/10，不算完成。

## Git 提交

达到 `10/10` 后执行：

```powershell
git status
git add image_batch_tool\__init__.py check_day4.py README.md
git commit -m "feat: add typed image record package"
git push
```

最后再运行 `git status`，理想结果应包含：

```text
nothing to commit, working tree clean
```

Day 4 不要求你再与 AI 进行中途对话。完成后保留终端中的 `10/10` 和 `git push` 结果，即可直接进入 Day 5。
