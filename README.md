# dev_vocabulary_quiz

開発語彙（schema v2）の **4 択クイズ**。Cloudflare Pages で公開する静的 Web アプリ。

## ドキュメント

| 文書 | 内容 |
|---|---|
| [doc/spec/企画書.md](doc/spec/企画書.md) | 背景・フェーズ・データフロー |
| [doc/spec/要件定義書.md](doc/spec/要件定義書.md) | 機能・非機能要件 |
| [doc/spec/README.md](doc/spec/README.md) | spec 索引 |
| [doc/agent/project-overview.md](doc/agent/project-overview.md) | プロジェクト概要 |
| [doc/agent/public-github-boundary.md](doc/agent/public-github-boundary.md) | 公開 Git とローカル運用の境界 |
| [CLOUDFLARE_DEPLOY.md](CLOUDFLARE_DEPLOY.md) | デプロイ手順 |

## データフロー

```text
doc/life/career/dev-vocabulary/   （Documents 正本）
  → tools/build_decks.py
  → export/all_cards_v2.json
  → tools/sync_to_web.ps1
  → public/
  → git push → Cloudflare Pages
```

- カード編集の正本: `Documents/doc/life/career/dev-vocabulary/`
- クイズ UI の作業正本: 本リポジトリの `public/index.html`（sync 前に `export/quiz.html` へ揃える）

## ローカル確認

```powershell
cd public
python -m http.server 8080
```

→ http://localhost:8080/

各モードで 1 問以上回答し、解説パネルまで確認する。詳細: [.cursor/skills/web-local-preview/SKILL.md](.cursor/skills/web-local-preview/SKILL.md)（ローカル専用・公開 GitHub には含まれない）

## 配布前チェック

```powershell
python scripts/validate_export_json.py public/all_cards_v2.json
python scripts/check_public_git_boundary.py
python scripts/pre_deploy_check.py
```

## 公開境界

公開 GitHub（Cloudflare Pages 連携）に **push してよい** のは主に `public/`・`README.md`・`doc/agent/`・`doc/spec/`・`scripts/` など。

**push しない**: `.cursor/` · `AGENTS.md` · `doc/ai/`（[public-github-boundary.md](doc/agent/public-github-boundary.md)）

## デプロイ

手順: [CLOUDFLARE_DEPLOY.md](CLOUDFLARE_DEPLOY.md)  
公開 URL: https://dev-vocabulary-quiz.pages.dev/
