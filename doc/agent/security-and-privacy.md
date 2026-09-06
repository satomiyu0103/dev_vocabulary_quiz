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

## `.gitignore` で除外するもの

リポジトリ直下の [`.gitignore`](../../.gitignore) が次を除外する（コミット前の二重防御）。

| 区分 | パターン例 | 理由 |
|---|---|---|
| 環境変数・秘密 | `.env`, `.env.*`, `.dev.vars*` | ローカル秘密。`.env.example` / `.dev.vars.example` は **コミット可** |
| 鍵・認証情報 | `*.pem`, `*.key`, `credentials.json`, `token.json`, `secrets/` | 秘密情報の誤コミット防止 |
| Cloudflare ローカル | `.wrangler/` | Wrangler のローカル状態 |
| Playwright | `.playwright-cli/`, `*.auth-state.json` | ブラウザ自動化の認証状態 |
| 実行環境 | `__pycache__/`, `.venv/`, `node_modules/` | 検証スクリプト・将来ツールの生成物 |
| Cursor / ローカル運用 | `.cursor/`, `AGENTS.md`, `doc/ai/` 等 | 公開 GitHub（Cloudflare Pages）には **push しない**。詳細: [public-github-boundary.md](public-github-boundary.md) |

## 検証スクリプト

```powershell
python scripts/check_no_sensitive_patterns.py
```

- `scripts/check_no_sensitive_patterns.py` — 秘密情報パターンの検出（`.js`, `.html`, `.css` 含む）

## Agentic セキュリティ

ローカルの `.cursor/skills/` に agent-governance · agent-owasp-compliance を配置（公開 GitHub には含めない）。
