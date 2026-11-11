#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd -- "$(dirname -- "$0")/.." && pwd -P)"
SOURCE="$ROOT/.agents/skills"

usage() {
  echo "Usage: bash scripts/install.sh --user"
  echo "   or: bash scripts/install.sh --project /path/to/project"
  echo "Creates symlinks; never overwrites existing skills."
}

if [[ $# -eq 1 && "$1" == "--help" ]]; then
  usage
  exit 0
elif [[ $# -eq 1 && "$1" == "--user" ]]; then
  TARGET="$HOME/.agents/skills"
elif [[ $# -eq 2 && "$1" == "--project" ]]; then
  [[ -d "$2" ]] || { echo "ERROR: Project directory not found: $2" >&2; exit 2; }
  PROJECT="$(cd -- "$2" && pwd -P)"
  TARGET="$PROJECT/.agents/skills"
else
  usage >&2
  exit 2
fi

[[ -d "$SOURCE" ]] || { echo "ERROR: Missing skills directory." >&2; exit 1; }
shopt -s nullglob
count=0

# Check ALL conflicts before creating any symlink.
for skill in "$SOURCE"/*; do
  [[ -d "$skill" && -f "$skill/SKILL.md" ]] || {
    echo "ERROR: Invalid skill directory: $skill" >&2; exit 1;
  }
  count=$((count + 1))
  dest="$TARGET/$(basename -- "$skill")"
  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ -L "$dest" && "$dest" -ef "$skill" ]]; then
      continue
    fi
    echo "ERROR: Existing entry will not be overwritten: $dest" >&2
    exit 1
  fi
done

(( count > 0 )) || { echo "ERROR: No skills found." >&2; exit 1; }
mkdir -p -- "$TARGET"

for skill in "$SOURCE"/*; do
  name="$(basename -- "$skill")"
  dest="$TARGET/$name"
  if [[ -L "$dest" && "$dest" -ef "$skill" ]]; then
    echo "EXISTS: $name"
  else
    ln -s -- "$skill" "$dest"
    echo "INSTALLED: $name"
  fi
done
echo "Registered $count skills in $TARGET"
