# Python 基础练习使用说明

这里只放第一阶段练习，不提前生成完整 Agent 项目。打开 `exercises.py`，逐个替换 `raise NotImplementedError`；不要修改 `check.py` 来让检查通过。所有练习仅用标准库，无模型费用。

## 运行

本机优先用已安装的 Windows Python 3.13。PowerShell：

```powershell
Set-Location -LiteralPath 'D:\Plan\python_basics'
py -3.13 -X utf8 environment_check.py
py -3.13 -X utf8 check.py --group basics
py -3.13 -X utf8 check.py --group algorithms
py -3.13 -X utf8 check.py --group all
```

初始每项会显示“待完成”，总检查返回非零退出码，表示作业尚未完成，不是环境安装失败。完成后会显示通过或具体失败输入。检查是有限样例，不证明掌握或穷尽正确性；还要独立复写、解释复杂度和补充边界。

命令中的 `-X utf8` 让检查输出使用 UTF-8，避免中文反馈在部分终端出现乱码。

## 基础组

| 函数 | 任务 | 限制或边界 |
| --- | --- | --- |
| `max_number` | 返回最大整数 | 空列表返回 None；不用 max；注意全负数 |
| `count_words` | 按空白分词，统计小写词频 | 多个空白忽略；标点保留；空文本返回空字典 |
| `unique_in_order` | 保留首次出现顺序去重 | 输入整数列表，不修改原输入 |
| `filter_even` | 返回偶数列表 | 保留顺序，不修改原输入 |
| `total_minutes` | 汇总记录中的 minutes | 记录保证含非负整数 minutes；空列表返回 0 |

先循环再考虑列表推导式。建议顺序：最大值 → 偶数过滤 → 总分钟 → 词频 → 去重。

## 算法组

| 函数 | 任务 | 约定 |
| --- | --- | --- |
| `two_sum` | 返回两个不同元素的下标，其和等于 target | 无解返回 None；多解返回任意一组；先暴力后用字典 |
| `move_zeroes` | 将 0 移到末尾，其他元素保序 | 修改原列表、额外空间 O(1)，返回 None |

算法组为已有题目的 Python 复习。检查验证结果和接口约定；O(1) 空间与时间复杂度需要阅读实现并解释，检查不自动判定。

## 独立验收

1. 先写自己的尝试，卡住记录输入、输出和具体问题。
2. 看提示后关闭参考重写。
3. 通过检查，再补一个自己想的边界输入。
4. 隔一天复写，并讲清变量作用域、修改原列表与返回新列表的区别。

将证据填入上一级的进度记录。练习目前只是骨架，不能记为已完成。

## 第二周环境

第一周无需虚拟环境；第二周再学习并创建：

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe --version
```

直接调用虚拟环境解释器即可，不必为激活环境修改系统执行策略。进入 FastAPI 阶段才安装第三方依赖并记录版本。
