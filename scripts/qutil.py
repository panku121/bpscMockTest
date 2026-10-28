# Shared helpers for BPSC TRE-style multiple choice items.
# Option D is always "more than one of the above" and E is "none of the above",
# matching the TRE 3.0 booklet.

MORE_EN = "More than one of the above"
MORE_HI = "उपर्युक्त में से एक से अधिक"
NONE_EN = "None of the above"
NONE_HI = "उपर्युक्त में से कोई नहीं"


def Q(
    section,
    topic,
    q,
    qh,
    options,
    optionsh,
    answer,
    explain,
    passage="",
    passageh="",
    pre=False,
):
    if len(options) != 5 or len(optionsh) != 5:
        raise ValueError(f"need 5 options: {q[:80]}")
    if not (0 <= answer <= 4):
        raise ValueError(f"bad answer {answer}: {q[:80]}")
    if any(not str(o).strip() for o in options):
        raise ValueError(f"empty option: {q[:80]}")
    if len(set(options)) != 5:
        raise ValueError(f"duplicate options: {q[:80]} :: {options}")
    if not explain.strip():
        raise ValueError(f"missing explanation: {q[:80]}")
    return {
        "section": section,
        "topic": topic,
        "q": q.strip(),
        "qh": (qh or "").strip(),
        "options": [str(o).strip() for o in options],
        "optionsh": [str(o).strip() for o in optionsh],
        "answer": answer,
        "explain": explain.strip(),
        "passage": (passage or "").strip(),
        "passageh": (passageh or "").strip(),
        "pre": bool(pre),
    }


def fixed(section, topic, q, qh, abc, abch, answer, explain, passage="", passageh="", pre=False):
    """abc / abch are the three content options (A, B, C). D and E are appended."""
    if len(abc) != 3 or len(abch) != 3:
        raise ValueError(q[:80])
    return Q(
        section,
        topic,
        q,
        qh,
        list(abc) + [MORE_EN, NONE_EN],
        list(abch) + [MORE_HI, NONE_HI],
        answer,
        explain,
        passage,
        passageh,
        pre,
    )


def numeric_q(rng, section, topic, q, qh, correct, explain, unit="", none_p=0.14, spread=None):
    """Integer answer. Sometimes the right value is absent, so the key is E."""
    correct = int(correct)
    cands = []
    deltas = spread or [1, -1, 2, -2, 3, -3, 4, 5, -5, 10, -10, 8, -8]
    for d in deltas:
        v = correct + d
        if v >= 0 and v != correct and v not in cands:
            cands.append(v)
    if correct % 2 == 0:
        half = correct // 2
        if half != correct and half not in cands:
            cands.append(half)
    if correct * 2 not in cands and correct * 2 < 100000:
        cands.append(correct * 2)
    # deterministic but varied order
    rng.shuffle(cands)
    suffix = unit or ""

    def fmt(v):
        return f"{v}{suffix}"

    if none_p and rng.random() < none_p and len(cands) >= 3:
        picks = cands[:3]
        explain2 = explain.rstrip() + f" सही मान {fmt(correct)} है, जो (A), (B), (C) में नहीं है। इसलिए उत्तर (E) है।"
        return Q(
            section,
            topic,
            q,
            qh,
            [fmt(picks[0]), fmt(picks[1]), fmt(picks[2]), MORE_EN, NONE_EN],
            [fmt(picks[0]), fmt(picks[1]), fmt(picks[2]), MORE_HI, NONE_HI],
            4,
            explain2,
        )

    picks = cands[:2]
    slots = [correct, picks[0], picks[1]]
    order = [0, 1, 2]
    rng.shuffle(order)
    shown = [slots[i] for i in order]
    answer = shown.index(correct)
    return Q(
        section,
        topic,
        q,
        qh,
        [fmt(v) for v in shown] + [MORE_EN, NONE_EN],
        [fmt(v) for v in shown] + [MORE_HI, NONE_HI],
        answer,
        explain,
    )


def text_choice(rng, section, topic, q, qh, correct_en, correct_hi, wrongs, explain, none_p=0.0):
    """wrongs is a list of (en, hi). correct is placed in A/B/C."""
    pool = [w for w in wrongs if w[0] != correct_en]
    if len(pool) < 2:
        raise ValueError(f"not enough distractors: {q[:70]}")
    rng.shuffle(pool)
    if none_p and rng.random() < none_p and len(pool) >= 3:
        a, b, c = pool[:3]
        return Q(
            section,
            topic,
            q,
            qh,
            [a[0], b[0], c[0], MORE_EN, NONE_EN],
            [a[1], b[1], c[1], MORE_HI, NONE_HI],
            4,
            explain.rstrip() + f" सही उत्तर है: {correct_hi}। यह (A)–(C) में नहीं है, इसलिए (E)।",
        )
    a, b = pool[:2]
    slots = [(correct_en, correct_hi), a, b]
    rng.shuffle(slots)
    answer = [s[0] for s in slots].index(correct_en)
    return Q(
        section,
        topic,
        q,
        qh,
        [s[0] for s in slots] + [MORE_EN, NONE_EN],
        [s[1] for s in slots] + [MORE_HI, NONE_HI],
        answer,
        explain,
    )
