#!/usr/bin/env bash
# 鮮度マーカー(最終更新日・stars)をローカルで再取得し、README / research-notes を更新する。
#
# 使い方:
#   ./scripts/refresh.sh
#
# 前提: gh CLI が認証済み(`gh auth status` で確認)、python3 が利用可能。
# cron / launchd に登録すれば完全自動更新も可能(README 末尾参照)。
set -euo pipefail

cd "$(dirname "$0")/.."

echo "[1/2] GitHub API でメタデータを再取得中..."
python3 data/enrich.py

echo "[2/2] README / research-notes を再生成中..."
python3 data/gen.py

echo "完了。変更があれば git diff で確認してください。"
