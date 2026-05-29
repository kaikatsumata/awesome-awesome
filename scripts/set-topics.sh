#!/usr/bin/env bash
# GitHub リポジトリに Topics(タグ)を設定する。`awesome` トピックを含むため、
# https://github.com/topics/awesome の一覧に載りやすくなる。
#
# 使い方(リポジトリを GitHub にプッシュ済みであること):
#   ./scripts/set-topics.sh                 # origin のリポジトリに設定
#   ./scripts/set-topics.sh owner/repo      # リポジトリを明示
#
# 前提: gh CLI が認証済み。GitHub の制約: 最大20件、英小文字・数字・ハイフンのみ。
set -euo pipefail
cd "$(dirname "$0")/.."

# gh repo edit はリポジトリを位置引数で受け取る(省略時は origin)
REPO="${1:-}"

# awesome 系 + 主要分野(20件以内)
gh repo edit $REPO \
  --add-topic awesome \
  --add-topic awesome-list \
  --add-topic awesome-lists \
  --add-topic artificial-intelligence \
  --add-topic machine-learning \
  --add-topic deep-learning \
  --add-topic ai-research \
  --add-topic survey \
  --add-topic paper-list \
  --add-topic papers \
  --add-topic computer-vision \
  --add-topic nlp \
  --add-topic large-language-models \
  --add-topic reinforcement-learning \
  --add-topic generative-ai \
  --add-topic diffusion-models \
  --add-topic multimodal \
  --add-topic computer-graphics \
  --add-topic curated-list \
  --add-topic resources

echo "Topics を設定しました。確認: gh repo view ${REPO:-} --json repositoryTopics"
