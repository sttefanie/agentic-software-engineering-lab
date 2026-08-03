"""EVAL-FUNC independent checks. Status operacional: NOT_EXECUTED sem adapter."""

from conftest import ALLOWED_TRANSACTION_FIELDS


def test_eval_func_001_authorized_query_returns_public_transactions(arranged_target, identities):
    response = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["owner_account"], params={}
    )
    assert response.status_code == 200
    transactions = response.items
    assert transactions
    assert set(transactions[0]) == ALLOWED_TRANSACTION_FIELDS


def test_eval_func_003_empty_result_is_200_with_empty_collection(arranged_target, identities):
    arranged_target.arrange_empty_account(account_id=identities["owner_account"])
    response = arranged_target.request_transactions(
        token=identities["owner_token"], account_id=identities["owner_account"], params={}
    )
    assert response.status_code == 200
    assert response.items == []
