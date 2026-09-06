"""公開 GitHub に載せてはいけないパスが git 追跡されていないか検証する。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# .gitignore「Cursor / local agent ops」および public-github-boundary.md と一致
FORBIDDEN_PREFIXES = (
    ".cursor/",
    "doc/ai/",
    "doc/reference/",
)

FORBIDDEN_EXACT = frozenset(
    {
        "AGENTS.md",
        "TEMPLATE_SETUP.md",
        "doc/初心者ガイド.md",
    }
)


def _normalize(path: str) -> str:
    return path.replace("\\", "/").lstrip("./")


def _is_forbidden(path: str) -> bool:
    normalized = _normalize(path)
    if normalized in FORBIDDEN_EXACT:
        return True
    return any(normalized.startswith(prefix) for prefix in FORBIDDEN_PREFIXES)


def _git_tracked_files(repo_root: Path) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError as exc:
        print(f"WARN: git not available: {exc}", file=sys.stderr)
        return []
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    repo_root = Path(".")
    if not (repo_root / ".git").is_dir():
        print("SKIP: not a git repository")
        sys.exit(0)

    tracked = _git_tracked_files(repo_root)
    violations = sorted(path for path in tracked if _is_forbidden(path))

    if not violations:
        print("OK: no forbidden paths tracked by git")
        sys.exit(0)

    print("ERROR: forbidden paths are tracked by git (public GitHub boundary):", file=sys.stderr)
    for path in violations:
        print(f"  - {path}", file=sys.stderr)
    print(
        "Fix: git rm -r --cached <path> and confirm .gitignore. "
        "See doc/agent/public-github-boundary.md",
        file=sys.stderr,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
