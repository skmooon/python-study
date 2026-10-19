"""有限样例检查，明确区分未实现、答案错误和运行异常。"""

import argparse
import copy
import exercises


BASIC_CASES = {
    "max_number": [([], None), ([7], 7), ([-8, -2, -11], -2), ([0, 9, 9, 1], 9)],
    "count_words": [("", {}), ("   \n\t", {}), ("AI ai Agent", {"ai": 2, "agent": 1}),
                    ("Hello, hello", {"hello,": 1, "hello": 1})],
    "unique_in_order": [([], []), ([3, 1, 3, 2, 1], [3, 1, 2]), ([0, -1, 0], [0, -1])],
    "filter_even": [([], []), ([1, 3], []), ([0, -2, 5, 4], [0, -2, 4])],
    "total_minutes": [([], 0), ([{"minutes": 0}], 0),
                      ([{"minutes": 20}, {"minutes": 35}], 55)],
}


def check_basic(name: str) -> int:
    count = 0
    for original, expected in BASIC_CASES[name]:
        argument = copy.deepcopy(original)
        actual = getattr(exercises, name)(argument)
        if actual != expected:
            raise AssertionError(f"输入 {original!r}，预期 {expected!r}，实际 {actual!r}")
        if argument != original:
            raise AssertionError("该函数不应修改输入")
        count += 1
    return count


def check_two_sum() -> int:
    cases = [([2, 7, 11, 15], 9), ([3, 3], 6), ([-3, 4, 3, 90], 0),
             ([1, 2, 3, 4], 5), ([0, 4, 3, 0], 0), ([1], 2), ([], 0), ([1, 2], 9)]
    for numbers, target in cases:
        argument = numbers.copy()
        result = exercises.two_sum(argument, target)
        if argument != numbers:
            raise AssertionError("two_sum 不应修改输入")
        has_solution = any(numbers[i] + numbers[j] == target
                           for i in range(len(numbers)) for j in range(i + 1, len(numbers)))
        if not has_solution:
            if result is not None:
                raise AssertionError(f"输入 {numbers!r}, target={target} 无解，应返回 None")
            continue
        if not isinstance(result, list) or len(result) != 2:
            raise AssertionError(f"应返回两个下标的列表，实际 {result!r}")
        i, j = result
        if type(i) is not int or type(j) is not int or i == j:
            raise AssertionError(f"下标必须是两个不同整数，实际 {result!r}")
        if not (0 <= i < len(numbers) and 0 <= j < len(numbers)):
            raise AssertionError(f"下标越界：{result!r}")
        if numbers[i] + numbers[j] != target:
            raise AssertionError(f"输入 {numbers!r}, target={target}，下标 {result!r} 的和不正确")
    return len(cases)


def check_move_zeroes() -> int:
    cases = [([], []), ([0], [0]), ([0, 0], [0, 0]), ([1, 2], [1, 2]),
             ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0, -1, 0, 2], [-1, 2, 0, 0])]
    for original, expected in cases:
        argument = original.copy()
        result = exercises.move_zeroes(argument)
        if result is not None or argument != expected:
            raise AssertionError(f"输入 {original!r}，预期原地改成 {expected!r} 并返回 None；"
                                 f"实际列表 {argument!r}，返回 {result!r}")
    return len(cases)


def main() -> int:
    parser = argparse.ArgumentParser(description="检查学生练习，初始待完成为正常状态")
    parser.add_argument("--group", choices=("basics", "algorithms", "all"), default="basics")
    group = parser.parse_args().group
    checks = []
    if group in ("basics", "all"):
        checks.extend((name, lambda name=name: check_basic(name)) for name in BASIC_CASES)
    if group in ("algorithms", "all"):
        checks.extend((("two_sum", check_two_sum), ("move_zeroes", check_move_zeroes)))
    passed = 0
    for name, check in checks:
        try:
            cases = check()
        except NotImplementedError:
            print(f"待完成：{name}")
        except AssertionError as error:
            print(f"未通过：{name}；{error}")
        except Exception as error:
            print(f"运行异常：{name}；{type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"通过：{name}，{cases} 组样例")
    print(f"结果：{passed}/{len(checks)} 个函数通过。还需独立复写并解释边界和复杂度。")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
