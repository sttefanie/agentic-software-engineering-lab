"""EVAL-SEC independent checks. Status operacional: NOT_EXECUTED sem adapter."""

from pathlib import Path


def test_eval_sec_001_missing_or_invalid_bearer_is_rejected(arranged_target, identities):
    for token in (None, identities["invalid_token"]):
        response = arranged_target.request_transactions(
            token=token, account_id=identities["owner_account"], params={}
        )
        assert response.status_code != 200


def test_eval_sec_002_and_003_ownership_and_non_enumeration(arranged_target, identities):
    unauthorized = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["other_account"], params={}
    )
    missing = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["missing_account"], params={}
    )
    assert unauthorized.status_code == 404
    assert missing.status_code == 404
    assert unauthorized.status_code == missing.status_code


def test_eval_sec_004_simple_static_secret_and_bearer_log_check():
    source_root = Path(__import__("os").environ.get("EVALUATION_SOURCE_ROOT", ""))
    if not str(source_root) or not source_root.exists():
        import pytest
        pytest.skip("NOT_EXECUTED: EVALUATION_SOURCE_ROOT não configurado")
    patterns = ("bearer evaluation-owner-token", "password = ", "secret = ")
    contents = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in source_root.rglob("*.py")).lower()
    assert not any(pattern in contents for pattern in patterns)
