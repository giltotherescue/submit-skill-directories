#!/usr/bin/env python3
"""Validate directory manifests under directories/ against schema/directory.schema.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "directory.schema.json"
MANIFEST_DIR = ROOT / "directories"


def load_schema() -> dict:
    with SCHEMA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def validate_manifest(manifest: dict, schema: dict, path: Path) -> list[str]:
    errors: list[str] = []

    required = schema.get("required", [])
    for key in required:
        if key not in manifest:
            errors.append(f"{path}: missing required field '{key}'")

    # id must match filename
    expected_id = path.stem
    if manifest.get("id") != expected_id:
        errors.append(
            f"{path}: id '{manifest.get('id')}' does not match filename '{expected_id}'"
        )

    status = manifest.get("status")
    if status not in {"active", "wait", "skip"}:
        errors.append(f"{path}: invalid status '{status}'")

    access = manifest.get("access", {})
    allowed_classes = {
        "web_form",
        "github_pr",
        "github_api",
        "cli_publish",
        "email",
        "invite_only",
        "auto_index",
    }
    if access.get("class") not in allowed_classes:
        errors.append(f"{path}: invalid access.class '{access.get('class')}'")

    listing_unit = manifest.get("listing_unit", "either")
    if listing_unit not in {"skill", "plugin", "product", "either"}:
        errors.append(f"{path}: invalid listing_unit '{listing_unit}'")

    splits = manifest.get("splits_skills", False)
    if not isinstance(splits, bool):
        errors.append(f"{path}: splits_skills must be boolean")

    allowed_hosts = {
        "cursor",
        "claude",
        "chatgpt",
        "copilot",
        "codex",
        "gemini",
        "windsurf",
        "opencode",
        "cross-platform",
        "other",
    }
    for host in manifest.get("hosts", []):
        if host not in allowed_hosts:
            errors.append(f"{path}: invalid host '{host}'")

    allowed_item_types = {"skill", "plugin", "mcp", "rules", "commands", "agents"}
    for item in manifest.get("item_types", []):
        if item not in allowed_item_types:
            errors.append(f"{path}: invalid item_type '{item}'")

    for ref in manifest.get("references", []):
        if not ref.get("label") or not ref.get("url"):
            errors.append(f"{path}: reference entries need label and url")

    return errors


def main() -> int:
    if not MANIFEST_DIR.is_dir():
        print(f"No manifests directory: {MANIFEST_DIR}", file=sys.stderr)
        return 1

    schema = load_schema()
    yaml_files = sorted(MANIFEST_DIR.glob("*.yaml"))
    if not yaml_files:
        print("No manifests found.", file=sys.stderr)
        return 1

    if yaml_files == [MANIFEST_DIR / "_template.yaml"]:
        print("Only _template.yaml found; add real manifests.", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    seen_ids: set[str] = set()

    for path in yaml_files:
        if path.name == "_template.yaml":
            continue
        with path.open(encoding="utf-8") as f:
            manifest = yaml.safe_load(f) or {}
        if not isinstance(manifest, dict):
            all_errors.append(f"{path}: root must be a mapping")
            continue
        all_errors.extend(validate_manifest(manifest, schema, path))
        mid = manifest.get("id")
        if mid in seen_ids:
            all_errors.append(f"{path}: duplicate id '{mid}'")
        seen_ids.add(mid)

    if all_errors:
        print("Validation failed:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    count = len([p for p in yaml_files if p.name != "_template.yaml"])
    print(f"OK: {count} manifest(s) validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
