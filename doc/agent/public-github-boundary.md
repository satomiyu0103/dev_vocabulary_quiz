# 公開 GitHub とローカル開発の境界（Cloudflare Pages）

## 目的

Cloudflare Pages は **GitHub リポジトリと連携** する。`public/` 以外が公開リポジトリに載ると、エージェント運用ファイルやローカル手順が外部に露出する。本テンプレは **ローカルに .cursor を配布しつつ、公開 Git には載せない** 設計とする。

## 2 層モデル

| 層 | パス例 | ローカル（Documents 同居） | 公開 GitHub（Pages 連携） |
|---|---|---|---|
| **公開サイト** | `public/` | コミット | コミット・push |
| **公開メタ** | `README.md`, `CLOUDFLARE_DEPLOY.md`, `doc/agent/`, `scripts/` | コミット | コミット・push |
| **ローカルエージェント運用** | `.cursor/`, `AGENTS.md`, `doc/ai/`, `doc/reference/`, `TEMPLATE_SETUP.md` | `dev-template-sync` で配布・更新 | **コミットしない**（`.gitignore`） |

正本: リポジトリ直下 [`.gitignore`](../../.gitignore) の「Cursor / local agent ops」節。

## 初回 `git init` 時の注意

```powershell
git init
git add .
git status   # .cursor/ がステージされていないことを確認
git commit -m "chore: initial web-static-template"
```

`git add .` でよい。**除外は `.gitignore` が担当**する（`.cursor/` 等はステージされない）。

## 誤って push した場合

1. 追跡解除: `git rm -r --cached .cursor` 等（[security-and-privacy.md](security-and-privacy.md)）
2. 履歴に残っている場合: `git filter-repo --invert-paths` で該当パスを除去 → `git push --force`（[destructive_ops](../../../../.cursor/rules/destructive_ops.mdc)・復元 branch 作成後）

## テンプレ同期との関係

- `sync-manifest.json` の `overwrite` は **ローカルファイルを更新**する（`.cursor/rules` 等）
- 公開 GitHub へは `.gitignore` により **同期されない**
- テンプレ正本は `Development/dev_templates/web-static-template/`（別 git）。Web プロジェクト git とは分離

## 関連

- [security-and-privacy.md](security-and-privacy.md)
- [TEMPLATE_SETUP.md](../../TEMPLATE_SETUP.md)
- [CLOUDFLARE_DEPLOY.md](../../CLOUDFLARE_DEPLOY.md)
