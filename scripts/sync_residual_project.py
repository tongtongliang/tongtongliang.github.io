#!/usr/bin/env python3
"""Copy the published project page from the paper repository into this site."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

REPO = "https://github.com/tongtongliang/residual-stream-burden.git"
DEST = Path(__file__).resolve().parents[1] / "residual-stream-burden"


def sync(source):
    docs = source / "docs"
    files = json.loads((docs / ".project-page-files.json").read_text())
    for name in files:
        path = Path(name)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"Invalid upstream path: {name}")
        if not (docs / path).is_file():
            raise FileNotFoundError(docs / path)
    if "index.html" not in files:
        raise ValueError("Upstream manifest is missing index.html")
    for name in files:
        if name == ".nojekyll":
            continue
        target = DEST / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(docs / name, target)
    commit = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    (DEST / ".upstream.json").write_text(json.dumps(
        {"repository": REPO, "commit": commit, "directory": "docs"}, indent=2
    ) + "\n")
    print(f"Synced project page from {commit} to {DEST}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Existing paper repository checkout")
    args = parser.parse_args()
    if args.source:
        sync(args.source.resolve())
    else:
        with tempfile.TemporaryDirectory(prefix="residual-project-") as directory:
            source = Path(directory) / "repo"
            subprocess.run(["git", "clone", "--depth", "1", REPO, str(source)], check=True)
            sync(source)
