"""テキストファイル中に秘密情報のパターンが含まれていないかチェックするスクリプト。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_API_KEY_RE = r"""(?:api[_-]?key|apikey)\s*[:=]\s*["']?[A-Za-z0-9_\-]{20,}"""
_SECRET_RE = r"""(?:secret|password|passwd|pwd)\s*[:=]\s*["']?[A-Za-z0-9_\-]{8,}"""
_TOKEN_RE = r"""(?:token|bearer)\s*[:=]\s*["']?[A-Za-z0-9_\-\.]{20,}"""
_ENV_RE = r"""^[A-Z_]+\s*=\s*["']?[A-Za-z0-9_\-]{16,}["']?\s*$"""

SENSITIVE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("AWS Access Key", re.compile(r"AKIA[0-9A-Z]{16}", re.IGNORECASE)),
    ("Generic API Key", re.compile(_API_KEY_RE, re.IGNORECASE)),
    ("Generic Secret", re.compile(_SECRET_RE, re.IGNORECASE)),
    ("Generic Token", re.compile(_TOKEN_RE, re.IGNORECASE)),
    ("Private Key Header", re.compile(r"-----BEGIN\s+(RSA\s+)?PRIVATE\sKEY-----")),
    (".env file content", re.compile(_ENV_RE, re.MULTILINE)),
]

TEXT_EXTENSIONS = {
    ".py",
    ".js",
    ".html",
    ".css",
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".toml",
    ".json",
    ".cfg",
    ".ini",
    ".sh",
    ".bash",
    ".env",
}

SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "node_modules"}
SKIP_FILES = {".env.example", "check_no_sensitive_patterns.py"}
SKIP_PATH_PARTS = {".cursor/skills/llm-security/rules"}


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS


def scan_file(path: Path) -> list[tuple[str, int, str]]:
    findings: list[tuple[str, int, str]] = []
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except (OSError, UnicodeDecodeError):
        return findings

    for line_num, line in enumerate(content.splitlines(), start=1):
        for pattern_name, pattern in SENSITIVE_PATTERNS:
            if pattern.search(line):
                findings.append((pattern_name, line_num, line.strip()[:100]))
    return findings


def main() -> None:
    repo_root = Path(".")
    all_findings: list[tuple[str, str, int, str]] = []

    for path in sorted(repo_root.rglob("*")):
        if any(skip in path.parts for skip in SKIP_DIRS):
            continue
        path_str = str(path).replace("\\", "/")
        if any(part in path_str for part in SKIP_PATH_PARTS):
            continue
        if not path.is_file():
            continue
        if path.name in SKIP_FILES:
            continue
        if not is_text_file(path):
            continue

        for pattern_name, line_num, line_content in scan_file(path):
            all_findings.append((str(path), pattern_name, line_num, line_content))

    if all_findings:
        print("ERROR: Potential sensitive patterns detected:")
        for filepath, pattern_name, line_num, line_content in all_findings:
            print(f"  {filepath}:{line_num} [{pattern_name}] {line_content}")
        sys.exit(1)

    print("OK: No sensitive patterns detected.")


if __name__ == "__main__":
    main()
