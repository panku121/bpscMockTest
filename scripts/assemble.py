"""Build 18 original TRE-pattern mock papers into data/papers.js."""

import json
import random
import sys
from collections import OrderedDict, Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bank_cs import build_cs
from bank_en import build_english
from bank_gs import build_gs
from bank_hi import build_hindi
from gen_calc import CS_MAKERS, GS_MATH, GS_SCI


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "papers.js"


def take(pool, n, rng, used):
    if n > len(pool):
        raise RuntimeError(f"need {n} from pool of {len(pool)}")
    tiers = {}
    for q in pool:
        tiers.setdefault(used[q["q"]], []).append(q)
    chosen = []
    seen = set()
    for k in sorted(tiers):
        bucket = tiers[k][:]
        rng.shuffle(bucket)
        for q in bucket:
            if q["q"] in seen:
                continue
            chosen.append(q)
            seen.add(q["q"])
            if len(chosen) == n:
                break
        if len(chosen) == n:
            break
    if len(chosen) != n:
        raise RuntimeError("take failed")
    for q in chosen:
        used[q["q"]] += 1
    return chosen


def gen_unique(rng, makers, n, seen):
    out = []
    local = set()
    guard = 0
    while len(out) < n and guard < n * 80:
        guard += 1
        try:
            item = rng.choice(makers)(rng)
        except Exception:
            continue
        key = item["q"]
        if key in seen or key in local:
            continue
        local.add(key)
        seen.add(key)
        out.append(item)
    if len(out) < n:
        raise RuntimeError(f"only generated {len(out)} of {n}")
    return out


def _remap_letters(text, order):
    """order[new_index] = old_index. Rewrite (A)(B)(C) to follow the shuffle."""
    trans = { "ABC"[old]: "ABC"[order.index(old)] for old in range(3) }
    out = text
    for old, new in trans.items():
        out = out.replace(f"({old})", f"(#{new})")
    return out.replace("(#", "(")


def settle_options(q, rng):
    """Keep D/E fixed. Shuffle A–C so the key is not predictably option A."""
    order = [0, 1, 2]
    rng.shuffle(order)
    options = [q["options"][i] for i in order] + q["options"][3:]
    optionsh = [q["optionsh"][i] for i in order] + q["optionsh"][3:]
    explain = _remap_letters(q["explain"], order)
    if q["answer"] >= 3:
        answer = q["answer"]
    else:
        answer = order.index(q["answer"])
    if len(set(options)) != 5:
        return q
    q = dict(q)
    q["options"] = options
    q["optionsh"] = optionsh
    q["answer"] = answer
    q["explain"] = explain
    return q


def clone(q, n, set_id, rng):
    q = settle_options(q, rng)
    return {
        "id": f"{set_id}-q{n:03d}",
        "n": n,
        "section": q["section"],
        "topic": q["topic"],
        "q": q["q"],
        "qh": q["qh"],
        "options": list(q["options"]),
        "optionsh": list(q["optionsh"]),
        "answer": q["answer"],
        "explain": q["explain"],
        "passage": q.get("passage") or "",
        "passageh": q.get("passageh") or "",
        "pre": bool(q.get("pre")),
    }


def build_papers():
    english = build_english()
    groups_map = OrderedDict()
    grammar = []
    for q in english:
        if q["passage"]:
            groups_map.setdefault(q["passage"], []).append(q)
        else:
            grammar.append(q)
    passages = list(groups_map.values())
    for g in passages:
        if len(g) != 5:
            raise RuntimeError(f"passage group size {len(g)}")

    hindi = build_hindi()
    gs_facts = build_gs()
    cs_bank = build_cs()

    used = Counter()
    seen_calc = set()
    papers = []

    # 15 papers start with a passage; 3 are grammar-only. Spread the grammar papers.
    grammar_only = {4, 9, 14}

    for i in range(18):
        rng = random.Random(2026_03_22 + i * 97)
        set_id = f"m{i+1:02d}"
        if i in grammar_only:
            en_qs = take(grammar, 8, rng, used)
        else:
            # cycle passages, least-used passage group first
            groups_ranked = sorted(passages, key=lambda g: used[g[0]["passage"]])
            group = groups_ranked[0]
            for q in group:
                used[q["q"]] += 1
                used[q["passage"]] += 1
            en_qs = list(group) + take(grammar, 3, rng, used)

        hi_qs = take(hindi, 22, rng, used)
        rng.shuffle(hi_qs)

        gs_qs = (
            gen_unique(rng, GS_MATH, 14, seen_calc)
            + gen_unique(rng, GS_SCI, 4, seen_calc)
            + take(gs_facts, 22, rng, used)
        )
        rng.shuffle(gs_qs)

        cs_qs = gen_unique(rng, CS_MAKERS, 50, seen_calc) + take(cs_bank, 30, rng, used)
        rng.shuffle(cs_qs)

        ordered = en_qs + hi_qs + gs_qs + cs_qs
        if len(ordered) != 150:
            raise RuntimeError(f"{set_id} has {len(ordered)}")
        questions = [clone(q, n, set_id, rng) for n, q in enumerate(ordered, start=1)]
        # section boundaries
        sections = [q["section"] for q in questions]
        if sections[:8] != ["en"] * 8 or sections[8:30] != ["hi"] * 22:
            raise RuntimeError(set_id + " language layout")
        if sections[30:70] != ["gs"] * 40 or sections[70:] != ["cs"] * 80:
            raise RuntimeError(set_id + " gs/cs layout")

        papers.append({
            "id": set_id,
            "number": i + 1,
            "title": f"Mock Test {i+1:02d}",
            "titleHi": f"मॉक टेस्ट {i+1:02d}",
            "series": "ABCD"[i % 4],
            "questions": questions,
        })
        print(f"built {set_id}")

    return papers


def main():
    papers = build_papers()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "pattern": "BPSC TRE 3.0 · Computer Science · Class 11-12",
        "durationMin": 150,
        "total": 150,
        "qualifyMarks": 9,
        "negative": False,
        "sets": papers,
    }
    text = "window.BPSC_PAPERS = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    OUT.write_text(text, encoding="utf-8")
    print("wrote", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
