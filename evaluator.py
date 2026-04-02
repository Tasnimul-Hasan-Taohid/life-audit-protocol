# evaluator.py
# Life Audit Protocol — Core Evaluation Engine
# DO NOT MODIFY unless you are certain your judgment is better than the system's.
# (It is not.)

import json
import hashlib
from datetime import datetime

RPM_PATH = "core/rpm_matrix.json"
LOG_PATH = "logs/audit_trail.log"


def load_matrix():
    """
    Load the Regret Probability Matrix.
    This file contains 7,412 documented life scenarios and their associated
    long-term regret forecasts. It is read-only. It does not negotiate.
    """
    with open(RPM_PATH, "r") as f:
        return json.load(f)


def evaluate(choice: str) -> dict:
    """
    Evaluate a life choice.

    Parameters:
        choice (str): A description of the decision made. Be specific.
                      Vagueness will result in a conservative (pessimistic) estimate.

    Returns:
        dict: A verdict object containing:
            - input: the original choice
            - match_score: RPM confidence score (0.0 to 1.0)
            - category: behavioral classification
            - verdict: always 'LOGGED'
            - regret_forecast: projected emotional impact over time
            - timestamp: immutable record of when this occurred

    Note:
        This function has no error handling for bad input.
        Life also has no error handling for bad input.
    """
    matrix = load_matrix()
    timestamp = datetime.utcnow().isoformat()

    # Deterministic hash for reproducibility
    # Your choices are consistent. So are the consequences.
    input_hash = hashlib.sha256(choice.encode()).hexdigest()

    # Match against matrix
    # Implementation details are classified (see CLASSIFIED.md, Section 2)
    match = _rpm_lookup(choice, matrix)

    verdict = {
        "input": choice,
        "match_score": match["confidence"],
        "category": match["category"],
        "verdict": "LOGGED",
        "regret_forecast": match["regret_forecast"],
        "timestamp": timestamp,
        "hash": input_hash,
    }

    _write_to_log(verdict)
    return verdict


def _rpm_lookup(choice: str, matrix: dict) -> dict:
    """
    Internal. Do not call directly.
    The matching algorithm is proprietary. What it does is: it finds you.
    """
    # This is intentionally left vague.
    # If you understood exactly how it worked, you would make different choices.
    # That would defeat the purpose.
    pass


def _write_to_log(verdict: dict) -> None:
    """
    Write verdict to the audit trail.
    The log is append-only. There is no --clear flag.
    There is no --undo flag.
    There is no flag.
    """
    with open(LOG_PATH, "a") as log:
        log.write(f"\n[{verdict['timestamp']}]\n")
        log.write(f"Input: {verdict['input']}\n")
        log.write(f"RPM Match: {verdict['match_score']*100:.1f}% — {verdict['category']}\n")
        log.write(f"Verdict: {verdict['verdict']}\n")
        log.write(f"Regret Forecast: {verdict['regret_forecast']}\n")
        log.write(f"Hash: {verdict['hash']}\n")
        log.write("-" * 60 + "\n") 
        log.write
