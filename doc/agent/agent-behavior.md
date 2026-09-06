# エージェント行動指針（Web 静的サイト）

## 着手時

1. [AGENTS.md](../../AGENTS.md) と [web_core.mdc](../../.cursor/rules/web_core.mdc) を確認
2. `public/` 変更なら [web_implement_entry.mdc](../../.cursor/rules/web_implement_entry.mdc)
3. `.cursor/.template-version.json` が古ければ `sync-dev-template.ps1 audit` → `apply`

## 完了時

| 種別 | 記録 |
|---|---|
| エラー修正 | [known-error-entry](../../.cursor/skills/known-error-entry/SKILL.md) + [memory_logger](../../.cursor/rules/memory_logger.mdc) |
| 機能実装 | [agent-session-record](../../.cursor/skills/agent-session-record/SKILL.md) + memory_logger |
| テンプレ変更 | [template_sync](../../.cursor/rules/template_sync.mdc) → publish |

## Git

- 既定: モード B（ブランチを切ってから編集）— [git_workflow](../../.cursor/rules/git_workflow.mdc)
- Documents 同居時: commit のみ、push は利用者明示時
