# image-batch-tool

这是五个月学习计划的第一个实践项目。最终会完成图片扫描、尺寸调整、格式转换、错误记录、JSON 报告和自动化测试。

## 学习进度

- Day 1 已完成：函数、容器、输入校验和异常处理，完整验收 9/9。
- Day 2 已完成：文件名筛选、扩展名大小写处理、迭代器和生成器，完整验收 7/7。
- 当前任务：第 1 周 Day 3，类、异常和 JSON 文件操作。

## 已使用的知识点

### Day 1：函数、容器与输入校验

- 函数定义、参数、返回值和类型标注。
- 列表、字典、循环、`sum`、`max` 与列表筛选。
- `ValueError`：在使用数据前验证类型、字段和值域。
- 条件短路：先验证类型，再调用字符串方法，例如先判断 `isinstance(name, str)`，再使用 `name.strip()`。
- 函数不应修改传入的列表。

### Day 2：文件名筛选、迭代器和生成器

- `str.lower()` 与 `str.endswith()`：忽略扩展名大小写。
- 普通 `for` 循环和列表推导式都可以筛选数据。
- `yield`：逐个生成结果，不需要提前创建完整列表。
- `iter()`、`next()` 和生成器的逐步取值行为。
- 输入顺序需要在筛选后保持不变。

## Day 3 目标

在 `day3_report.py` 中完成以下内容：

1. `ProcessingReport` 类：保存一个图片处理任务的名称和图片文件名。
2. `add_image` 方法：添加有效的图片文件名。
3. `to_dict` 方法：把对象转换为普通字典。
4. `save_json` 方法：将报告保存为 UTF-8 编码的 JSON 文件。
5. `load_report` 函数：从 JSON 文件读取报告内容。

今天只处理字符串名称、JSON 文件读写和 `FileNotFoundError`。不处理真实图片、不扫描目录、不创建复杂继承结构。

## 完成任务需要学习的知识

### 主学习资源

按下面顺序阅读官方中文文档，总时长控制在 40 分钟：

1. [类的初步认识](https://docs.python.org/zh-cn/3/tutorial/classes.html#a-first-look-at-classes)：只阅读类定义、实例属性、`__init__` 和实例方法。
2. [处理异常](https://docs.python.org/zh-cn/3/tutorial/errors.html#handling-exceptions)：重点理解 `raise ValueError` 和 `FileNotFoundError`。
3. [`pathlib.Path.read_text` 与 `pathlib.Path.write_text`](https://docs.python.org/zh-cn/3/library/pathlib.html#pathlib.Path.read_text)：只了解使用 UTF-8 读取和写入文本。
4. [json 模块](https://docs.python.org/zh-cn/3/library/json.html)：只看 `json.dumps`、`json.loads`、`ensure_ascii=False` 和 `indent=2`。

停止学习条件：能够解释“类用来把数据和操作数据的方法放在一起”“`self` 表示当前对象”“JSON 是可保存到文件的字典/列表格式”后，立即开始编码。

### 替代学习资源

在 Bilibili 搜索 `Python 类 JSON 文件读写 异常处理`，选择包含 `__init__`、`self`、`json.dump` 或 `json.dumps` 演示的视频。只看这些片段，不需要学习继承、魔术方法、装饰器或复杂异常层级。

## 建议的两小时安排

| 时间 | 任务 |
|---|---|
| 20 分钟 | 回顾 Day 1 的 `ValueError`、字典和列表；回顾 Day 2 的文件名列表。 |
| 40 分钟 | 按主学习资源阅读类、异常、`Path` 与 JSON 的指定范围。 |
| 55 分钟 | 独立实现 `day3_report.py`，按下面的推荐顺序逐步完成。 |
| 5 分钟 | 运行验收、查看 Git 差异并提交。 |

推荐实现顺序：

1. 先完成 `__init__` 和 `to_dict`。
2. 再完成 `add_image` 的参数校验和追加逻辑。
3. 再实现 `save_json`。
4. 最后实现 `load_report`。

## 验收标准

运行命令：

```powershell
python .\check_day3.py
```

验收总分为 7/7，每一项含义如下：

| 项目 | 具体要求 |
|---|---|
| 1/7 | 用有效任务名创建 `ProcessingReport` 后，`to_dict()` 返回任务名、图片数为 0、图片列表为空。 |
| 2/7 | 连续调用两次 `add_image` 后，图片列表保留输入顺序，图片数正确。 |
| 3/7 | 任务名不是字符串、为空字符串或只有空白字符时，构造函数必须抛出 `ValueError`。 |
| 4/7 | 图片名不是字符串、为空字符串或只有空白字符时，`add_image` 必须抛出 `ValueError`。 |
| 5/7 | `save_json` 必须创建指定的 JSON 文件，并使用 UTF-8 编码。 |
| 6/7 | 保存的 JSON 内容必须与 `to_dict()` 结果一致，`load_report` 读取后也必须返回同一内容。 |
| 7/7 | 读取不存在的文件时，`load_report` 必须抛出 `FileNotFoundError`。 |

预期输出会逐项显示以上 7 个要求的通过状态。

## Git 提交

确认 Day 3 的 7/7 全部通过后：

```powershell
git add day3_report.py check_day3.py README.md
git commit -m "feat: add JSON processing reports"
git push
```

本仓库已配置 GitHub 代理。推送前保持 Clash 运行即可。
