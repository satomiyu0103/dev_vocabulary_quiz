# scripts/ — 検証スクリプト

| スクリプト | 用途 |
|---|---|
| `pre_deploy_check.py` | デプロイ前統合検証（下記 3 つを順に実行） |
| `validate_agent_docs.py` | 必須 agent 文書・skill の存在確認 |
| `check_no_sensitive_patterns.py` | 秘密情報パターンのスキャン |
| `check_public_git_boundary.py` | 公開 Git に載せてはいけないパスの追跡検知 |

## 実行例

```powershell
python scripts/pre_deploy_check.py
```

正本: [TEMPLATE_SETUP.md](../TEMPLATE_SETUP.md) · [web_pre_deploy.md](../doc/ai/guidelines/checklists/web_pre_deploy.md)
