# セキュリティ・プライバシー（静的 Web）

## 公開前提

`public/` 配下は **インターネットに公開** される。コミット前に内容を確認する。

## 禁止

- API キー・トークン・パスワードを `public/` またはリポジトリに含める
- 個人を特定できる情報（PII）を公開 JSON / HTML に含める
- ユーザー入力を `innerHTML` に直書きする

## 推奨

- DOM 更新は `textContent` を優先
- 外部 script / font は最小限。README に出典を記載
- 機微データはサーバ側または非公開ストレージに置く（本テンプレは静的のみ）

## 検証スクリプト

```powershell
python scripts/check_no_sensitive_patterns.py
```

- `scripts/check_no_sensitive_patterns.py` — 秘密情報パターンの検出（`.js`, `.html`, `.css` 含む）

## Agentic セキュリティ

エージェントのツール統制: [agent-governance](../../.cursor/skills/agent-governance/SKILL.md) · [agent-owasp-compliance](../../.cursor/skills/agent-owasp-compliance/SKILL.md)
