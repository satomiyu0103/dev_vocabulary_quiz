# web-static-template

Cloudflare Pages 向けの静的 Web サイトテンプレ（**lite+** — `.cursor` 運用基盤付き）。

## 新規プロジェクト

1. `Development/Web_apps/<project_name>/` を作成
2. 本テンプレから `AGENTS.md` `README.md` `public/` をコピー
3. `git init` → commit
4. GitHub push → Cloudflare Pages（出力 `public`、ビルドなし）
5. `dev-projects-manifest.json` に登録（`deploy.url` を記録）

## 配布（Documents 同居時）

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .cursor/scripts/sync-dev-template.ps1 publish --template web
```

## 関連

- [development-layout.md](../../doc/life/playbook/development-layout.md)
- [dev_task_entry_web.mdc](../../.cursor/rules/dev_task_entry_web.mdc)
