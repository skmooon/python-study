"""只读检查解释器和练习文件，不安装依赖、不修改环境。"""

import platform
import sys
from pathlib import Path


def main() -> int:
    print(f"Python 版本：{platform.python_version()}")
    print(f"解释器：{sys.executable}")
    if sys.version_info < (3, 10):
        print("需要 Python 3.10 或以上；本机建议使用 py -3.13。")
        return 1
    root = Path(__file__).resolve().parent
    for name in ("exercises.py", "check.py"):
        if not (root / name).is_file():
            print(f"缺少练习文件：{name}")
            return 1
    print("环境检查通过。现在打开 exercises.py，实现 max_number。")
    print("环境通过不代表练习已完成；第一阶段无需第三方依赖。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
