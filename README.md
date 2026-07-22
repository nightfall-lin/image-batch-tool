# image-batch-tool

五个月学习计划的第一个实践项目。
The first practice project in the five-month learning plan.

## 当前状态 / Current status

- Day 1 已完成：输入校验与成绩统计，完整验收 9/9。
  Day 1 completed: input validation and score summary, full acceptance 9/9.
- 当前任务：第 1 周 Day 2，列表推导式、迭代器和生成器。
  Current task: Week 1 Day 2, list comprehensions, iterators, and generators.

## Day 2 目标 / Day 2 objective

实现 `day2_collections.py` 中的两个函数：
Implement the two functions in `day2_collections.py`:

1. `filter_image_names`：从文件名列表中返回图片文件名列表。
   `filter_image_names`: return image filenames from a filename list.
2. `iter_image_names`：逐个产生图片文件名，不预先生成完整结果列表。
   `iter_image_names`: yield image filenames one at a time without building the full result list first.

支持的后缀 / Supported suffixes:

```text
.jpg, .jpeg, .png, .webp
```

扩展名需要忽略大小写，并且返回顺序必须与输入顺序一致。
Extensions must be case-insensitive, and result order must match input order.

本日不要求处理非字符串元素、空列表异常或真实磁盘目录；这些内容稍后再加入。
Today does not require validation for non-string entries, empty-list exceptions, or real disk directories; those will be added later.

## 建议时间安排 / Suggested two-hour schedule

| 时间 / Time | 任务 / Task |
|---|---|
| 20 分钟 / min | 回顾 Day 1 中的 `for`、列表和字典 / Review `for`, lists, and dictionaries from Day 1 |
| 40 分钟 / min | 学习列表推导式、迭代器和 `yield` / Learn list comprehensions, iterators, and `yield` |
| 55 分钟 / min | 独立完成两个函数 / Implement the two functions independently |
| 5 分钟 / min | 运行验收、查看差异、Git 提交 / Run checks, inspect diff, and commit |

## 学习材料 / Learning resources

- [Python 数据结构：列表推导式 / Data Structures: List Comprehensions](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#list-comprehensions)
- [Python 迭代器 / Iterators](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator-types)
- [Python 生成器 / Generators](https://docs.python.org/zh-cn/3/howto/functional.html#generators)

主资源 / Primary resource：依次阅读上面的三个官方页面。先只阅读列表推导式的基本形式、迭代器的 `iter()`/`next()` 说明，以及生成器中包含 `yield` 的示例；总时长控制在 30 分钟。
Read the three official pages in order. Focus only on basic list-comprehension syntax, the `iter()`/`next()` explanation, and generator examples containing `yield`; limit this to 30 minutes.

替代资源 / Alternative resource：在 Bilibili 搜索 `Python 列表推导式 迭代器 生成器`，选择时长 20-40 分钟、包含 `yield` 演示的入门视频。只观看列表推导式、`iter`/`next` 和 `yield` 三段，不必看完整课程。
Search Bilibili for `Python 列表推导式 迭代器 生成器`, choose a 20-40 minute introductory video that demonstrates `yield`, and watch only the three relevant segments rather than the entire course.

开始编码条件 / Start-coding condition：能够口头回答“列表推导式返回列表，`yield` 返回可逐个取值的生成器”后，立即开始实现两个函数；不必先理解生成器表达式、嵌套推导式或自定义迭代器类。
Start coding as soon as you can explain: “a list comprehension returns a list, while `yield` produces a generator that can be consumed one value at a time.” You do not need generator expressions, nested comprehensions, or custom iterator classes yet.

只需理解三个问题：
Focus on only three questions:

1. 列表推导式与普通 `for` 循环都能筛选数据，它们的返回结果有什么区别？
   Both list comprehensions and `for` loops can filter data. How do their results differ?
2. 调用生成器函数时，为什么函数体不会立刻运行完？
   Why does a generator function not run to completion immediately when called?
3. `yield` 和 `return` 的区别是什么？
   What is the difference between `yield` and `return`?

## 验收 / Acceptance

```powershell
python .\check_day2.py
```

预期输出 / Expected output:

```text
第 2 天验收通过：7/7 / Day 2 acceptance passed: 7/7
```

## Git 提交 / Git commit

确认测试通过后：
After tests pass:

```powershell
git add day2_collections.py check_day2.py README.md
git commit -m "feat: add image filename iterators"
git push
```

本仓库的 GitHub 代理配置已经设置。运行推送时保持 Clash 开启即可。
The GitHub proxy is configured for this repository. Keep Clash running when pushing.
