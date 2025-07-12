"""Utilities for creating common agent setups."""
from __future__ import annotations

import re
from typing import List

from .types import Agent


def _sanitize_name(name: str) -> str:
    """Return a safe identifier for a function name."""
    slug = re.sub(r"[^a-zA-Z0-9_]", "_", name.strip())
    slug = re.sub(r"_+", "_", slug)
    return slug.strip("_").lower()


def create_triage_agent(
    agents: List[Agent],
    *,
    name: str = "Triage Agent",
    instructions: str = "You triage requests and hand off to the appropriate agent.",
    add_backlinks: bool = False,
) -> Agent:
    """Return a triage ``Agent`` that can hand off to ``agents``.

    Each agent is exposed as a tool named ``transfer_to_<agent>`` which returns
    the corresponding agent. If ``add_backlinks`` is ``True`` each target agent
    also receives a ``transfer_to_<triage_agent>`` tool so it can hand back
    control.
    """

    triage_agent = Agent(name=name, instructions=instructions)
    transfer_functions = []

    for target in agents:
        fn_name = f"transfer_to_{_sanitize_name(target.name)}"

        def make_transfer(tgt):
            def _transfer():
                """Transfer control to the agent."""
                return tgt

            return _transfer

        func = make_transfer(target)
        func.__name__ = fn_name
        transfer_functions.append(func)

        if add_backlinks:
            back_fn_name = f"transfer_to_{_sanitize_name(triage_agent.name)}"

            def make_backlink():
                def _backlink():
                    """Return the triage agent."""
                    return triage_agent

                return _backlink

            back_func = make_backlink()
            back_func.__name__ = back_fn_name
            if back_func not in target.functions:
                target.functions.append(back_func)

    triage_agent.functions = transfer_functions
    return triage_agent

__all__ = ["create_triage_agent"]
