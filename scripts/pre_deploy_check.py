"""デプロイ前の統合検証（agent docs / 秘密情報 / 公開 Git 境界）。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = (
    "validate_agent_docs.py",
    "check_no_sensitive_patterns.py",
    "check_public_git_boundary.py",
)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    scripts_dir = repo_root / "scripts"
    failed: list[str] = []

    for name in SCRIPTS:
        script = scripts_dir / name
        if not script.is_file():
            print(f"ERROR: missing script: {name}", file=sys.stderr)
            failed.append(name)
            continue
        print(f"== {name} ==")
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=repo_root,
            check=False,
        )
        if result.returncode != 0:
            failed.append(name)

    if failed:
        print(f"FAILED: {', '.join(failed)}", file=sys.stderr)
        sys.exit(1)

    print("OK: all pre-deploy checks passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
