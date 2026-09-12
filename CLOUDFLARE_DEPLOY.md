# Cloudflare Pages デプロイ手順

1. GitHub にリポジトリを push（公開境界: [doc/agent/public-github-boundary.md](doc/agent/public-github-boundary.md)）
2. 配布前: `python scripts/validate_export_json.py public/all_cards_v2.json`
3. Cloudflare Dashboard → Workers & Pages → Connect to Git
4. Build command: （空）
5. Build output directory: `public`
6. 公開 URL を `dev-projects-manifest.json` の `deploy.url` に記録（Documents 秘書層の [dev-projects-manifest.json](../../.cursor/scripts/dev-projects-manifest.json)）
## デプロイ後

- ブラウザで公開 URL を開き、コンソールエラーが無いことを確認
- URL を manifest に記録したら `update-dev-project-index.ps1` で索引を再生成
