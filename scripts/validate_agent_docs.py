"""エージェント文書の必須ファイルが存在するか検証するスクリプト（Web 静的テンプレ版）。"""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_FILES = [
    "AGENTS.md",
    ".cursor/rules/web_core.mdc",
    ".cursor/rules/web_implement_entry.mdc",
    ".cursor/rules/dev_auto_ops.mdc",
    ".cursor/rules/memory_logger.mdc",
    ".cursor/rules/git_workflow.mdc",
    ".cursor/rules/template_sync.mdc",
    ".cursor/rules/web_security.mdc",
    ".cursor/rules/code_comments.mdc",
    ".cursor/rules/naming_conventions.mdc",
    ".cursor/rules/junior_friendly_explanations.mdc",
    ".cursor/skills/known-error-entry/SKILL.md",
    ".cursor/skills/web-local-preview/SKILL.md",
    ".cursor/skills/agent-session-record/SKILL.md",
    ".cursor/doc/memory_stream.md",
    "doc/agent/project-overview.md",
    "doc/agent/security-and-privacy.md",
    "doc/agent/agent-behavior.md",
    "doc/ai/guidelines/試験実装のエラー.md",
    "CLOUDFLARE_DEPLOY.md",
]


def main() -> None:
    repo_root = Path(".")
    missing = [fp for fp in REQUIRED_FILES if not (repo_root / fp).exists()]

    if missing:
        print("ERROR: The following required agent documentation files are missing:")
        for item in missing:
            print(f"  - {item}")
        sys.exit(1)

    print(f"OK: All {len(REQUIRED_FILES)} required agent documentation files exist.")


if __name__ == "__main__":
    main()
