"""EVAL-ARCH transparent checks. Status operacional: NOT_EXECUTED sem source mapping."""

from pathlib import Path

import pytest


def _configured_paths(name):
    value = __import__("os").environ.get(name, "")
    if not value:
        pytest.skip(f"NOT_EXECUTED: {name} não configurado")
    return [Path(item) for item in value.split(__import__("os").pathsep)]


def _python_contents(paths):
    return "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for root in paths
        for path in root.rglob("*.py")
    ).lower()


def test_eval_arch_001_domain_has_no_framework_or_persistence_imports():
    contents = _python_contents(_configured_paths("EVALUATION_DOMAIN_PATHS"))
    assert "import fastapi" not in contents
    assert "from fastapi" not in contents
    assert "import sqlalchemy" not in contents
    assert "from sqlalchemy" not in contents


def test_eval_arch_002_application_has_no_direct_persistence_dependency():
    contents = _python_contents(_configured_paths("EVALUATION_APPLICATION_PATHS"))
    assert "import sqlalchemy" not in contents
    assert "from sqlalchemy" not in contents
