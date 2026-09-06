# Cloudflare Pages デプロイ手順

企画・受け入れ基準: [doc/spec/テスト設計書.md](doc/spec/テスト設計書.md) §9

1. GitHub にリポジトリを push
2. Cloudflare Dashboard → Workers & Pages → Connect to Git
3. Build command: （空）
4. Build output directory: `public`
5. 公開 URL を `dev-projects-manifest.json` の `deploy.url` に記録（Documents 秘書層の [dev-projects-manifest.json](../../.cursor/scripts/dev-projects-manifest.json)）

## デプロイ後

- ブラウザで公開 URL を開き、コンソールエラーが無いことを確認
- URL を manifest に記録したら `update-dev-project-index.ps1` で索引を再生成
