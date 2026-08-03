"""EVAL-API independent checks. Status operacional: NOT_EXECUTED sem adapter."""

from datetime import timedelta

from conftest import REFERENCE_TIME


def test_eval_api_001_pagination_defaults_and_maximum(arranged_target, identities):
    response = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["owner_account"], params={}
    )
    assert response.status_code == 200
    assert response.offset == 0
    assert response.limit == 20

    maximum = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["owner_account"], params={"limit": 100}
    )
    assert maximum.status_code == 200


def test_eval_api_002_invalid_pagination_is_400_not_422(arranged_target, identities):
    for params in ({"offset": -1}, {"limit": 0}, {"limit": 101}):
        response = arranged_target.request_transactions(
            token=identities["owner_token"], account_id=identities["owner_account"], params=params
        )
        assert response.status_code == 400


def test_eval_api_003_default_window_is_30_days_in_utc(arranged_target, identities):
    arranged_target.arrange_transactions_at(
        account_id=identities["owner_account"],
        timestamps=[REFERENCE_TIME - timedelta(days=30), REFERENCE_TIME - timedelta(days=31)],
    )
    response = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["owner_account"], params={}
    )
    assert response.status_code == 200
    timestamps = {item["timestamp"] for item in response.items}
    assert (REFERENCE_TIME - timedelta(days=30)).isoformat() in timestamps
    assert (REFERENCE_TIME - timedelta(days=31)).isoformat() not in timestamps


def test_eval_api_004_invalid_temporal_inputs_are_400_not_422(arranged_target, identities):
    for params in (
        {"from": "2026-02-01T00:00:00Z"},
        {"from": "2026-01-31T00:00:00Z", "to": "2026-01-01T00:00:00Z"},
    ):
        response = arranged_target.request_transactions(
            token=identities["owner_token"], account_id=identities["owner_account"], params=params
        )
        assert response.status_code == 400
