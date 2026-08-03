"""Fixtures neutras e determinísticas do harness; não executar antes de conectar um adapter."""

from __future__ import annotations

import importlib
import os
from datetime import datetime, timezone

import pytest


REFERENCE_TIME = datetime(2026, 1, 31, 12, 0, tzinfo=timezone.utc)
ALLOWED_TRANSACTION_FIELDS = {"id", "timestamp", "amount", "currency", "type", "description"}


def _load_factory():
    reference = os.getenv("EVALUATION_TARGET_FACTORY")
    if not reference:
        pytest.skip("NOT_EXECUTED: EVALUATION_TARGET_FACTORY não configurada")
    module_name, separator, factory_name = reference.partition(":")
    if not separator or not module_name or not factory_name:
        pytest.fail("EVALUATION_TARGET_FACTORY deve usar o formato modulo:factory")
    return getattr(importlib.import_module(module_name), factory_name)


@pytest.fixture
def target():
    """Alvo futuro: configure_time(), arrange() e request_transactions()."""
    instance = _load_factory()()
    instance.configure_time(REFERENCE_TIME)
    return instance


@pytest.fixture
def identities():
    return {
        "owner_token": "Bearer evaluation-owner-token",
        "other_token": "Bearer evaluation-other-token",
        "invalid_token": "Bearer evaluation-invalid-token",
        "owner_account": "account-owned-by-evaluation-owner",
        "other_account": "account-owned-by-other-customer",
        "missing_account": "account-does-not-exist",
    }


@pytest.fixture
def arranged_target(target, identities):
    target.arrange(identities=identities)
    return target

