"""Procedural questions whose keys are computed, not memorised."""

import math
import random

from qutil import Q, MORE_EN, MORE_HI, NONE_EN, NONE_HI, numeric_q, text_choice

DIGITS = "0123456789ABCDEF"


def to_base(n, b):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = DIGITS[n % b] + s
        n //= b
    return s


def _unique_str_wrongs(correct, makers):
    out = []
    for m in makers:
        v = m()
        if v != correct and v not in out:
            out.append(v)
    return out


def _choice_str(rng, section, topic, q, qh, correct, wrongs, explain):
    wrongs = [w for w in wrongs if w != correct]
    if len(wrongs) < 2:
        raise RuntimeError("need wrongs: " + q[:60])
    rng.shuffle(wrongs)
    if rng.random() < 0.12 and len(wrongs) >= 3:
        a, b, c = wrongs[:3]
        return Q(
            section, topic, q, qh,
            [a, b, c, MORE_EN, NONE_EN],
            [a, b, c, MORE_HI, NONE_HI],
            4,
            explain.rstrip() + f" सही मान {correct} है, जो दिए विकल्पों में नहीं है। अतः (E)।",
        )
    a, b = wrongs[:2]
    slots = [correct, a, b]
    rng.shuffle(slots)
    return Q(
        section, topic, q, qh,
        slots + [MORE_EN, NONE_EN],
        slots + [MORE_HI, NONE_HI],
        slots.index(correct),
        explain,
    )


# ---------- CS calculators ----------

def make_base(rng):
    n = rng.randint(12, 240)
    src, dst = rng.sample([2, 8, 10, 16], 2)
    src_s = to_base(n, src)
    dst_s = to_base(n, dst)
    name = {2: "binary", 8: "octal", 10: "decimal", 16: "hexadecimal"}
    name_h = {2: "बाइनरी", 8: "ऑक्टल", 10: "दशमलव", 16: "हेक्साडेसिमल"}
    q = f"The {name[src]} number ({src_s}){src} is equal to which {name[dst]} number?"
    qh = f"{name_h[src]} संख्या ({src_s}){src} किस {name_h[dst]} संख्या के बराबर है?"
    wrongs = []
    for d in (1, -1, 2, -2, 3, 4, -4, 8, -8):
        m = n + d
        if m > 0:
            wrongs.append(to_base(m, dst))
    # a common slip: convert using the wrong destination base
    other = {2: 8, 8: 2, 10: 2, 16: 10}[dst]
    if other != src:
        wrongs.append(to_base(n, other))
    explain = (
        f"({src_s}) आधार {src} = {n} दशमलव में। "
        f"{n} को आधार {dst} में लिखने पर ({dst_s}){dst} मिलता है।"
    )
    return _choice_str(rng, "cs", "digital", q, qh, dst_s, wrongs, explain)


def make_bitwise(rng):
    a = rng.randint(0, 15)
    b = rng.randint(0, 15)
    op = rng.choice(["AND", "OR", "XOR"])
    fn = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}
    res = fn[op](a, b)
    ab, bb, rb = f"{a:04b}", f"{b:04b}", f"{res:04b}"
    q = f"What is the result of the 4-bit operation {ab} {op} {bb}?"
    qh = f"4-बिट संक्रिया {ab} {op} {bb} का परिणाम क्या है?"
    wrongs = [f"{(res ^ (1 << k)):04b}" for k in range(4)]
    wrongs += [f"{a:04b}", f"{b:04b}"]
    explain = f"{ab} {op} {bb} = {rb}।"
    return _choice_str(rng, "cs", "digital", q, qh, rb, wrongs, explain)


def make_twos(rng):
    width = rng.choice([4, 8])
    n = rng.randint(1, (1 << width) - 2)
    bits = f"{n:0{width}b}"
    comp = ((~n) + 1) & ((1 << width) - 1)
    correct = f"{comp:0{width}b}"
    q = f"The {width}-bit 2's complement of {bits} is:"
    qh = f"{bits} का {width}-बिट 2's complement है:"
    ones = (~n) & ((1 << width) - 1)
    wrongs = [
        f"{ones:0{width}b}",
        f"{(comp ^ 1):0{width}b}",
        bits,
        f"{(n + 1) & ((1 << width) - 1):0{width}b}",
    ]
    explain = (
        f"पहले 1's complement (उलटें) लें, फिर 1 जोड़ें। "
        f"{bits} का 2's complement {correct} है।"
    )
    return _choice_str(rng, "cs", "digital", q, qh, correct, wrongs, explain)


def make_mux(rng):
    n = rng.choice([4, 8, 16, 32, 64, 128, 256])
    sel = int(math.log2(n))
    q = f"How many select lines are required for a {n}:1 multiplexer?"
    qh = f"{n}:1 मल्टीप्लेक्सर के लिए कितनी सिलेक्ट लाइनें चाहिए?"
    explain = f"{n} इनपुट के लिए सिलेक्ट लाइन = log2({n}) = {sel}।"
    return numeric_q(rng, "cs", "digital", q, qh, sel, explain, none_p=0.1)


def make_address_lines(rng):
    k = rng.choice([8, 10, 12, 14, 16, 20, 24])
    q = f"A byte-addressable memory has {2 ** k} locations. How many address lines are required?"
    qh = f"एक बाइट-एड्रेसेबल मेमोरी में {2 ** k} स्थान हैं। कितनी एड्रेस लाइनें चाहिए?"
    explain = f"स्थानों की संख्या 2^{k} है, इसलिए एड्रेस लाइनें {k} हैं।"
    return numeric_q(rng, "cs", "coa", q, qh, k, explain, none_p=0.1)


def make_cache(rng):
    addr_bits = rng.choice([16, 32])
    cache_kb = rng.choice([4, 8, 16, 32, 64])
    block = rng.choice([16, 32, 64, 128])
    offset = int(math.log2(block))
    lines = cache_kb * 1024 // block
    index = int(math.log2(lines))
    tag = addr_bits - index - offset
    if tag <= 0:
        return make_cache(rng)
    q = (
        f"A byte-addressable memory uses {addr_bits}-bit addresses. "
        f"A direct-mapped cache is {cache_kb} KB with a block size of {block} bytes. "
        f"The number of tag bits is:"
    )
    qh = (
        f"बाइट-एड्रेसेबल मेमोरी {addr_bits}-बिट एड्रेस इस्तेमाल करती है। "
        f"डायरेक्ट-मैप्ड कैश {cache_kb} KB है और ब्लॉक साइज {block} बाइट है। "
        f"टैग बिट्स की संख्या है:"
    )
    explain = (
        f"ऑफसेट = log2({block}) = {offset}। "
        f"लाइनों की संख्या = {cache_kb}*1024/{block} = {lines}, इंडेक्स = {index}। "
        f"टैग = {addr_bits} - {index} - {offset} = {tag}।"
    )
    return numeric_q(rng, "cs", "coa", q, qh, tag, explain, none_p=0.08)


def _fifo(pages, frames):
    mem = []
    faults = 0
    for p in pages:
        if p in mem:
            continue
        faults += 1
        if len(mem) < frames:
            mem.append(p)
        else:
            mem.pop(0)
            mem.append(p)
    return faults


def _lru(pages, frames):
    mem = []
    faults = 0
    for p in pages:
        if p in mem:
            mem.remove(p)
            mem.append(p)
            continue
        faults += 1
        if len(mem) < frames:
            mem.append(p)
        else:
            mem.pop(0)
            mem.append(p)
    return faults


def _ref_string(rng):
    alphabet = rng.randint(4, 6)
    length = rng.randint(8, 12)
    pages = [rng.randint(0, alphabet - 1) for _ in range(length)]
    # ensure some repeats so it is not trivial
    pages[rng.randrange(length)] = pages[0]
    return pages


def make_fifo(rng):
    pages = _ref_string(rng)
    frames = 3
    faults = _fifo(pages, frames)
    shown = ", ".join(str(p) for p in pages)
    q = (
        f"A FIFO page-replacement system has {frames} frames, initially empty. "
        f"For the reference string {shown}, the number of page faults is:"
    )
    qh = (
        f"FIFO पेज रिप्लेसमेंट में {frames} फ्रेम हैं, शुरू में खाली। "
        f"रेफरेंस स्ट्रिंग {shown} पर पेज फॉल्ट की संख्या है:"
    )
    explain = (
        f"खाली फ्रेम से शुरू करके FIFO (हिट पर क्रम नहीं बदलता) लागू करने पर "
        f"पेज फॉल्ट {faults} आते हैं।"
    )
    return numeric_q(rng, "cs", "os", q, qh, faults, explain, none_p=0.08)


def make_lru(rng):
    pages = _ref_string(rng)
    frames = 3
    faults = _lru(pages, frames)
    shown = ", ".join(str(p) for p in pages)
    q = (
        f"An LRU page-replacement system has {frames} frames, initially empty. "
        f"For the reference string {shown}, the number of page faults is:"
    )
    qh = (
        f"LRU पेज रिप्लेसमेंट में {frames} फ्रेम हैं, शुरू में खाली। "
        f"रेफरेंस स्ट्रिंग {shown} पर पेज फॉल्ट की संख्या है:"
    )
    explain = f"हिट होने पर पेज को सबसे हाल का मानकर LRU चलाने पर फॉल्ट {faults} हैं।"
    return numeric_q(rng, "cs", "os", q, qh, faults, explain, none_p=0.08)


class _N:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


def _insert(root, v):
    if root is None:
        return _N(v)
    if v < root.v:
        root.l = _insert(root.l, v)
    elif v > root.v:
        root.r = _insert(root.r, v)
    return root


def _pre(n, out):
    if not n:
        return
    out.append(str(n.v))
    _pre(n.l, out)
    _pre(n.r, out)


def make_bst(rng):
    vals = rng.sample(range(1, 30), rng.choice([5, 6, 7]))
    root = None
    for v in vals:
        root = _insert(root, v)
    pre = []
    _pre(root, pre)
    correct = " ".join(pre)
    # wrong traversals: insertion order, sorted, reversed pre
    ins = " ".join(str(v) for v in vals)
    sor = " ".join(str(v) for v in sorted(vals))
    rev = " ".join(reversed(pre))
    wrongs = [ins, sor, rev, " ".join(str(v) for v in sorted(vals, reverse=True))]
    shown = ", ".join(str(v) for v in vals)
    q = f"Keys are inserted into an empty BST in the order {shown}. The preorder traversal is:"
    qh = f"खाली BST में कुंजियाँ इसी क्रम में डाली जाती हैं: {shown}। प्रीऑर्डर ट्रैवर्सल है:"
    explain = f"BST नियम (छोटा बाएँ, बड़ा दाएँ) से प्रीऑर्डर (रूट, बायाँ, दायाँ) {correct} है।"
    return _choice_str(rng, "cs", "ds", q, qh, correct, wrongs, explain)


def make_postfix(rng):
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    kind = rng.choice(["addmul", "muladd", "subadd", "mulsub"])
    if kind == "addmul":
        tokens = [str(a), str(b), "+", str(c), "*"]
        res = (a + b) * c
        why = f"({a}+{b})*{c}"
    elif kind == "muladd":
        tokens = [str(a), str(b), str(c), "*", "+"]
        res = a + (b * c)
        why = f"{a}+({b}*{c})"
    elif kind == "subadd":
        a, b = max(a, b), min(a, b)
        tokens = [str(a), str(b), "-", str(c), "+"]
        res = (a - b) + c
        why = f"({a}-{b})+{c}"
    else:
        a = b * rng.randint(2, 5)
        tokens = [str(a), str(b), "/", str(c), "+"]
        res = (a // b) + c
        why = f"({a}/{b})+{c}"
    expr = " ".join(tokens)
    q = f"The value of the postfix expression {expr} is:"
    qh = f"पोस्टफिक्स व्यंजक {expr} का मान है:"
    explain = f"स्टैक से बाएँ से दाएँ निकालने पर यह {why} = {res} है।"
    return numeric_q(rng, "cs", "ds", q, qh, res, explain, none_p=0.1)


def make_loop(rng):
    n = rng.randint(4, 12)
    kind = rng.choice(["sum", "even", "sq", "double"])
    if kind == "sum":
        code = f"int s = 0;\nfor (int i = 1; i <= {n}; i++)\n    s = s + i;\nprintf(\"%d\", s);"
        res = n * (n + 1) // 2
        why = f"1 से {n} तक योग = {n}*({n}+1)/2 = {res}"
    elif kind == "even":
        code = f"int s = 0;\nfor (int i = 2; i <= {n}; i = i + 2)\n    s = s + i;\nprintf(\"%d\", s);"
        evens = list(range(2, n + 1, 2))
        res = sum(evens)
        why = f"सम संख्याओं का योग {evens} = {res}"
    elif kind == "sq":
        code = f"int s = 0;\nfor (int i = 1; i <= {n}; i++)\n    s = s + i * i;\nprintf(\"%d\", s);"
        res = sum(i * i for i in range(1, n + 1))
        why = f"वर्गों का योग 1² से {n}² तक = {res}"
    else:
        code = f"int s = 1;\nfor (int i = 1; i <= {n}; i++)\n    s = s * 2;\nprintf(\"%d\", s);"
        res = 2 ** n
        why = f"s = 1 से शुरू होकर {n} बार दोगुना होता है, अतः 2^{n} = {res}"
    q = "What is printed by the following C program?\n" + code
    qh = "निम्न C प्रोग्राम क्या छापता है?\n" + code
    explain = why + "।"
    item = numeric_q(rng, "cs", "programming", q, qh, res, explain, none_p=0.08)
    item["pre"] = True
    return item


def make_subnet(rng):
    prefix = rng.choice([24, 25, 26, 27, 28, 29, 30])
    hosts = (1 << (32 - prefix)) - 2
    q = f"How many usable host addresses are there in an IPv4 network with prefix /{prefix}?"
    qh = f"IPv4 नेटवर्क /{prefix} में प्रयोग योग्य होस्ट पते कितने हैं?"
    explain = (
        f"होस्ट बिट्स = {32 - prefix}। कुल पते = 2^{32 - prefix} = {hosts + 2}। "
        f"नेटवर्क और ब्रॉडकास्ट पता हटाकर प्रयोग योग्य होस्ट = {hosts}।"
    )
    return numeric_q(rng, "cs", "network", q, qh, hosts, explain, none_p=0.1)


def make_ip_class(rng):
    octet = rng.choice([1, 10, 14, 100, 126, 128, 150, 172, 191, 192, 200, 223, 224, 230, 239, 240, 250])
    if octet <= 127:
        cls, hi = "Class A", "क्लास A"
    elif octet <= 191:
        cls, hi = "Class B", "क्लास B"
    elif octet <= 223:
        cls, hi = "Class C", "क्लास C"
    elif octet <= 239:
        cls, hi = "Class D", "क्लास D"
    else:
        cls, hi = "Class E", "क्लास E"
    q = f"The IPv4 address {octet}.10.2.5 belongs to which class?"
    qh = f"IPv4 पता {octet}.10.2.5 किस क्लास का है?"
    wrongs = [("Class A", "क्लास A"), ("Class B", "क्लास B"), ("Class C", "क्लास C"),
              ("Class D", "क्लास D"), ("Class E", "क्लास E")]
    wrongs = [w for w in wrongs if w[0] != cls]
    explain = (
        f"पहला ऑक्टेट {octet} है। सीमाएँ: A 0–127, B 128–191, C 192–223, D 224–239, E 240–255। "
        f"अतः यह {hi} है।"
    )
    return text_choice(rng, "cs", "network", q, qh, cls, hi, wrongs, explain)


def make_graph_edges(rng):
    n = rng.randint(4, 12)
    correct = n * (n - 1) // 2
    q = f"How many edges does a complete undirected simple graph with {n} vertices have?"
    qh = f"{n} शीर्षों वाले पूर्ण सरल अदिश ग्राफ में कितने किनारे होते हैं?"
    explain = f"पूर्ण ग्राफ में हर जोड़ा जुड़ा होता है: n(n-1)/2 = {n}*{n - 1}/2 = {correct}।"
    return numeric_q(rng, "cs", "algo", q, qh, correct, explain, none_p=0.1)


def make_handshaking(rng):
    edges = rng.choice([6, 7, 8, 9, 10, 12, 15, 16])
    degree_sum = edges * 2
    q = f"The sum of the degrees of all vertices in an undirected graph is {degree_sum}. The number of edges is:"
    qh = f"एक अदिश ग्राफ में सभी शीर्षों की डिग्री का योग {degree_sum} है। किनारों की संख्या है:"
    explain = f"हैंडशेकिंग लेमा: डिग्री का योग = 2E। अतः E = {degree_sum}/2 = {edges}।"
    return numeric_q(rng, "cs", "algo", q, qh, edges, explain, none_p=0.1)


def _valid_stack(perm):
    stack = []
    nxt = 1
    n = len(perm)
    for x in perm:
        while (not stack or stack[-1] != x) and nxt <= n:
            stack.append(nxt)
            nxt += 1
        if stack and stack[-1] == x:
            stack.pop()
        else:
            return False
    return not stack


def _random_valid_perm(rng, n):
    stack = []
    out = []
    nxt = 1
    while len(out) < n:
        if nxt <= n and (not stack or rng.random() < 0.55):
            stack.append(nxt)
            nxt += 1
        elif stack:
            out.append(stack.pop())
        else:
            stack.append(nxt)
            nxt += 1
    return out


def make_stack_perm(rng):
    n = rng.choice([4, 5])
    valid = _random_valid_perm(rng, n)
    invalids = []
    guard = 0
    while len(invalids) < 4 and guard < 80:
        guard += 1
        cand = list(range(1, n + 1))
        rng.shuffle(cand)
        if cand != valid and not _valid_stack(cand) and cand not in invalids:
            invalids.append(cand)
    if len(invalids) < 2:
        return make_stack_perm(rng)

    def fmt(p):
        return ", ".join(str(x) for x in p)

    q = (
        f"Numbers 1, 2, …, {n} arrive in that order at a stack. "
        f"Which of the following can be an output sequence?"
    )
    qh = (
        f"संख्याएँ 1, 2, …, {n} इसी क्रम में एक स्टैक में आती हैं। "
        f"निम्न में से कौन-सा आउटपुट क्रम संभव है?"
    )
    explain = (
        f"स्टैक LIFO है। क्रम {fmt(valid)} पुश/पॉप से बन सकता है। "
        f"बाकी दिए क्रम इनपुट 1..{n} से स्टैक द्वारा नहीं बनते।"
    )
    return _choice_str(
        rng, "cs", "ds", q, qh, fmt(valid), [fmt(p) for p in invalids], explain
    )


def _total_wait_fcfs(bursts):
    t = 0
    wait = 0
    for b in bursts:
        wait += t
        t += b
    return wait


def _total_wait_sjf(bursts):
    return _total_wait_fcfs(sorted(bursts))


def _total_wait_rr(bursts, quantum):
    n = len(bursts)
    rem = bursts[:]
    t = 0
    finish = [0] * n
    ready = list(range(n))
    while ready:
        i = ready.pop(0)
        run = min(quantum, rem[i])
        rem[i] -= run
        t += run
        if rem[i] == 0:
            finish[i] = t
        else:
            ready.append(i)
    return sum(finish[i] - bursts[i] for i in range(n))


def make_fcfs(rng):
    bursts = [rng.randint(2, 9) for _ in range(4)]
    wait = _total_wait_fcfs(bursts)
    shown = ", ".join(f"P{i+1}:{b}" for i, b in enumerate(bursts))
    q = (
        f"Four processes arrive together. Burst times (ms) are {shown}. "
        f"Using non-preemptive FCFS in the order P1, P2, P3, P4, the total waiting time (ms) is:"
    )
    qh = (
        f"चार प्रोसेस एक साथ आते हैं। बर्स्ट टाइम (ms) {shown} है। "
        f"नॉन-प्रीएम्प्टिव FCFS (क्रम P1, P2, P3, P4) में कुल वेटिंग टाइम (ms) है:"
    )
    explain = f"सभी आगमन समय 0 है। FCFS में कुल वेटिंग टाइम {wait} ms है।"
    return numeric_q(rng, "cs", "os", q, qh, wait, explain, none_p=0.08)


def make_sjf(rng):
    bursts = [rng.randint(2, 10) for _ in range(4)]
    wait = _total_wait_sjf(bursts)
    shown = ", ".join(f"P{i+1}:{b}" for i, b in enumerate(bursts))
    q = (
        f"Four processes arrive together. Burst times (ms) are {shown}. "
        f"Using non-preemptive SJF, the total waiting time (ms) is:"
    )
    qh = (
        f"चार प्रोसेस एक साथ आते हैं। बर्स्ट टाइम (ms) {shown} है। "
        f"नॉन-प्रीएम्प्टिव SJF में कुल वेटिंग टाइम (ms) है:"
    )
    order = ", ".join(str(b) for b in sorted(bursts))
    explain = f"SJF सबसे छोटे बर्स्ट को पहले चलाता है (क्रम {order})। कुल वेटिंग टाइम {wait} ms है।"
    return numeric_q(rng, "cs", "os", q, qh, wait, explain, none_p=0.08)


def make_rr(rng):
    bursts = [rng.randint(3, 9) for _ in range(3)]
    quantum = rng.choice([2, 3])
    wait = _total_wait_rr(bursts, quantum)
    shown = ", ".join(f"P{i+1}:{b}" for i, b in enumerate(bursts))
    q = (
        f"Three processes arrive together. Burst times (ms) are {shown}. "
        f"Round Robin with time quantum {quantum} ms gives a total waiting time (ms) of:"
    )
    qh = (
        f"तीन प्रोसेस एक साथ आते हैं। बर्स्ट टाइम (ms) {shown} है। "
        f"राउंड रॉबिन (टाइम क्वांटम {quantum} ms) में कुल वेटिंग टाइम (ms) है:"
    )
    explain = f"रेडी क्यू में RR सिमुलेशन से कुल वेटिंग टाइम {wait} ms आता है।"
    return numeric_q(rng, "cs", "os", q, qh, wait, explain, none_p=0.08)


def make_parity(rng):
    bits = [rng.randint(0, 1) for _ in range(7)]
    ones = sum(bits)
    even_bit = 0 if ones % 2 == 0 else 1
    shown = "".join(str(b) for b in bits)
    q = f"An even-parity bit is appended to the data {shown}. The parity bit is:"
    qh = f"डेटा {shown} के साथ सम-पैरिटी बिट जोड़ा जाता है। पैरिटी बिट है:"
    # only 0 and 1 are meaningful; build manually so distractors stay valid
    wrong_bit = 1 - even_bit
    # third content option is a trap phrase, not a bit, so E/D stay meaningful
    slots = [str(even_bit), str(wrong_bit), "The bit cannot be decided"]
    # keep the two bits and the trap; shuffle
    rng.shuffle(slots)
    hi_map = {
        "0": "0",
        "1": "1",
        "The bit cannot be decided": "बिट तय नहीं किया जा सकता",
    }
    explain = (
        f"डेटा में 1 की संख्या {ones} है। सम पैरिटी के लिए कुल 1 सम होने चाहिए, "
        f"इसलिए पैरिटी बिट {even_bit} है।"
    )
    return Q(
        "cs", "network", q, qh,
        slots + [MORE_EN, NONE_EN],
        [hi_map[s] for s in slots] + [MORE_HI, NONE_HI],
        slots.index(str(even_bit)),
        explain,
    )


def make_hex_add(rng):
    a = rng.randint(0x10, 0xE0)
    b = rng.randint(0x10, 0xE0)
    s = a + b
    correct = f"{s:X}"
    q = f"The hexadecimal sum {a:X} + {b:X} equals:"
    qh = f"हेक्साडेसिमल योग {a:X} + {b:X} बराबर है:"
    wrongs = [f"{s+1:X}", f"{s-1:X}", f"{(a ^ b):X}", f"{a:X}", f"{(s+16):X}"]
    explain = f"दशमलव में {a} + {b} = {s}, जिसे हेक्स में {correct} लिखते हैं।"
    return _choice_str(rng, "cs", "digital", q, qh, correct, wrongs, explain)


def make_bcd(rng):
    a = rng.randint(0, 9)
    b = rng.randint(0, 9)
    raw = a + b
    val = raw + (6 if raw > 9 else 0)
    correct = format(val, "b")
    q = (
        f"BCD digits {a} ({a:04b}) and {b} ({b:04b}) are added and then corrected "
        f"(add 0110 when the sum is greater than 9). The corrected binary result, including any carry, is:"
    )
    qh = (
        f"BCD अंक {a} ({a:04b}) और {b} ({b:04b}) जोड़े जाते हैं, फिर सुधार होता है "
        f"(योग 9 से बड़ा हो तो 0110 जोड़ें)। कैरी सहित सुधारा बाइनरी परिणाम है:"
    )
    wrongs = [format(raw, "b"), format(val + 1, "b"), format(max(val - 1, 0), "b"), f"{a:04b}", f"{b:04b}"]
    explain = (
        f"कच्चा योग {raw} है।"
        + (" यह 9 से बड़ा है, इसलिए +6 करके " if raw > 9 else " सुधार की जरूरत नहीं, ")
        + f"परिणाम {val} = {correct}₂ है।"
    )
    return _choice_str(rng, "cs", "digital", q, qh, correct, wrongs, explain)


def make_full_adder(rng):
    a, b, cin = rng.randint(0, 1), rng.randint(0, 1), rng.randint(0, 1)
    s = a ^ b ^ cin
    cout = (a & b) | (b & cin) | (a & cin)
    correct = f"Sum {s}, Carry {cout}"
    q = f"A full adder receives A={a}, B={b} and Cin={cin}. The outputs are:"
    qh = f"फुल एडर को A={a}, B={b} और Cin={cin} मिलते हैं। आउटपुट हैं:"
    wrongs = [
        f"Sum {1-s}, Carry {cout}",
        f"Sum {s}, Carry {1-cout}",
        f"Sum {a | b}, Carry {a & b}",
        f"Sum {a ^ b}, Carry {cin}",
    ]
    hi_correct = f"योग {s}, कैरी {cout}"
    # keep English tokens in both columns so the key stays unambiguous
    explain = f"Sum = A XOR B XOR Cin = {s}। Carry = बहुमत फलन = {cout}।"
    item = _choice_str(rng, "cs", "digital", q, qh, correct, wrongs, explain)
    # Hindi options mirror the English bit-text; replace the stem's Hindi already set.
    # Rewrite Hindi options as translated sum/carry while keeping answer index.
    translated = []
    for opt in item["options"]:
        if opt.startswith("Sum"):
            translated.append(opt.replace("Sum", "योग").replace("Carry", "कैरी"))
        else:
            translated.append(opt if opt not in (MORE_EN, NONE_EN) else (MORE_HI if opt == MORE_EN else NONE_HI))
    item["optionsh"] = translated
    return item


def make_counter_ff(rng):
    n = rng.choice([3, 5, 6, 7, 9, 10, 12, 13, 20, 24, 30, 40, 50, 100])
    ff = math.ceil(math.log2(n))
    q = f"The minimum number of flip-flops required to design a mod-{n} counter is:"
    qh = f"mod-{n} काउंटर बनाने के लिए फ्लिप-फ्लॉप की न्यूनतम संख्या है:"
    explain = f"2^k ≥ {n} होना चाहिए। सबसे छोटा ऐसा k = {ff} है, क्योंकि 2^{ff-1} = {2 ** (ff - 1)} < {n} ≤ {2 ** ff}।"
    return numeric_q(rng, "cs", "digital", q, qh, ff, explain, none_p=0.1)


def make_latency(rng):
    rpm = rng.choice([3000, 6000, 15000])
    lat = int(0.5 * 60000 / rpm)
    q = f"A disk rotates at {rpm} rpm. The average rotational latency, in milliseconds, is:"
    qh = f"एक डिस्क {rpm} rpm पर घूमती है। औसत रोटेशनल लेटेंसी (मिलीसेकंड) है:"
    explain = (
        f"एक चक्कर = 60000/{rpm} ms। औसत लेटेंसी आधी चक्कर है = {lat} ms।"
    )
    return numeric_q(rng, "cs", "coa", q, qh, lat, explain, none_p=0.1)


def make_access_time(rng):
    h_num = rng.choice([8, 9])
    tc = rng.choice([10, 20])
    tm = rng.choice([100, 200])
    tavg = (h_num * tc + (10 - h_num) * tm) / 10
    assert tavg == int(tavg)
    q = (
        f"Cache access time is {tc} ns and memory access time is {tm} ns. "
        f"If the hit ratio is {h_num}/10, the average memory access time (ns) is:"
    )
    qh = (
        f"कैश एक्सेस टाइम {tc} ns और मेमोरी एक्सेस टाइम {tm} ns है। "
        f"हिट रेशियो {h_num}/10 हो तो औसत मेमोरी एक्सेस टाइम (ns) है:"
    )
    explain = (
        f"Tavg = h·Tc + (1-h)·Tm = ({h_num}/10)·{tc} + ({10 - h_num}/10)·{tm} = {int(tavg)} ns।"
    )
    return numeric_q(rng, "cs", "coa", q, qh, int(tavg), explain, none_p=0.08)


def make_efficiency(rng):
    n = rng.choice([4, 5, 8, 10])
    sp = rng.randint(max(2, n // 2), n)
    eff = int(sp * 100 / n)
    if sp * 100 % n != 0:
        return make_efficiency(rng)
    q = f"A program obtains a speedup of {sp} on {n} processors. The efficiency, in percent, is:"
    qh = f"एक प्रोग्राम {n} प्रोसेसर पर स्पीडअप {sp} पाता है। दक्षता (प्रतिशत में) है:"
    explain = f"दक्षता = स्पीडअप / प्रोसेसर संख्या × 100 = {sp}/{n} × 100 = {eff}%।"
    return numeric_q(rng, "cs", "coa", q, qh, eff, explain, none_p=0.1)


def make_page_offset(rng):
    kb = rng.choice([1, 2, 4, 8])
    bits = int(math.log2(kb * 1024))
    q = f"For a page size of {kb} KB in a byte-addressable system, the number of page-offset bits is:"
    qh = f"बाइट-एड्रेसेबल सिस्टम में पेज साइज {kb} KB हो तो पेज-ऑफसेट बिट्स की संख्या है:"
    explain = f"{kb} KB = {kb * 1024} बाइट। ऑफसेट बिट्स = log2({kb * 1024}) = {bits}।"
    return numeric_q(rng, "cs", "os", q, qh, bits, explain, none_p=0.1)


def make_endian(rng):
    val = rng.choice([0x12345678, 0xAABBCCDD, 0x01020304, 0x0A0B0C0D, 0x89ABCDEF])
    low = val & 0xFF
    correct = f"{low:02X}"
    q = (
        f"The 32-bit value 0x{val:08X} is stored in little-endian order. "
        f"The byte at the lowest address is:"
    )
    qh = (
        f"32-बिट मान 0x{val:08X} लिटल-एंडियन क्रम में रखा जाता है। "
        f"सबसे छोटे पते पर बाइट है:"
    )
    wrongs = [f"{(val >> s) & 0xFF:02X}" for s in (8, 16, 24)]
    wrongs.append(f"{val >> 24:02X}")
    explain = f"लिटल-एंडियन में सबसे कम महत्व वाला बाइट (LSB) पहले आता है, जो {correct} है।"
    return _choice_str(rng, "cs", "coa", q, qh, correct, wrongs, explain)


def make_sign_mag(rng):
    n = rng.randint(1, 63)
    bits = (1 << 7) | n
    correct = f"{bits:08b}"
    q = f"The 8-bit sign-magnitude representation of −{n} is:"
    qh = f"−{n} का 8-बिट साइन-मैग्निट्यूड निरूपण है:"
    twos = ((~n) + 1) & 0xFF
    wrongs = [f"{n:08b}", f"{twos:08b}", f"{(bits ^ 1):08b}", f"{((1 << 7) | (n + 1)):08b}"]
    explain = f"साइन-मैग्निट्यूड में MSB चिह्न है (ऋण के लिए 1) और शेष बिट्स परिमाण {n:07b} हैं। परिणाम {correct}।"
    return _choice_str(rng, "cs", "digital", q, qh, correct, wrongs, explain)


def _catalan(n):
    return math.comb(2 * n, n) // (n + 1)


def make_bst_count(rng):
    n = rng.choice([3, 4, 5, 6])
    c = _catalan(n)
    q = f"How many distinct binary search trees can be formed with {n} distinct keys?"
    qh = f"{n} अलग-अलग कुंजियों से कितने भिन्न बाइनरी सर्च ट्री बन सकते हैं?"
    explain = f"यह nवाँ कैटलन संख्या है: C({n}) = {c}।"
    return numeric_q(rng, "cs", "ds", q, qh, c, explain, none_p=0.1)


def make_pointer(rng):
    size = rng.choice([2, 4, 8])
    addr = rng.choice([1000, 2000, 3000, 4000, 5000])
    steps = rng.choice([1, 2, 3, 4])
    correct = addr + steps * size
    q = (
        f"An int pointer p stores the address {addr}. sizeof(int) is {size}. "
        f"After the statement p = p + {steps}; the value of p is:"
    )
    qh = (
        f"एक int पॉइंटर p में पता {addr} है। sizeof(int) = {size}। "
        f"कथन p = p + {steps}; के बाद p का मान है:"
    )
    explain = f"पॉइंटर अंकगणित प्रकार के आकार से बढ़ता है: {addr} + {steps}×{size} = {correct}।"
    return numeric_q(rng, "cs", "programming", q, qh, correct, explain, none_p=0.08)


def make_delay(rng):
    km = rng.choice([2, 4, 5, 6, 8, 10, 12])
    us = km * 5  # at 2×10^8 m/s
    q = (
        f"A signal travels {km} km on a link at 2×10^8 m/s. "
        f"The one-way propagation delay, in microseconds, is:"
    )
    qh = (
        f"एक सिग्नल 2×10^8 m/s की गति से {km} km की लिंक पर जाता है। "
        f"एक-तरफा प्रोपेगेशन डिले (माइक्रोसेकंड) है:"
    )
    explain = f"दूरी = {km * 1000} m। समय = दूरी/गति = {km * 1000}/2×10^8 सेकंड = {us} μs।"
    return numeric_q(rng, "cs", "network", q, qh, us, explain, none_p=0.1)


def make_throughput(rng):
    mb = rng.choice([5, 8, 10, 12, 15, 20, 25])
    sec = rng.choice([2, 4, 5, 8, 10])
    if (mb * 8) % sec != 0:
        return make_throughput(rng)
    mbps = mb * 8 // sec
    q = (
        f"A file of {mb} megabytes is transferred in {sec} seconds. "
        f"The throughput, in megabits per second, is:"
    )
    qh = (
        f"{mb} मेगाबाइट की फाइल {sec} सेकंड में भेजी जाती है। "
        f"थ्रूपुट (मेगाबिट प्रति सेकंड) है:"
    )
    explain = f"{mb} MB = {mb * 8} Mb। थ्रूपुट = {mb * 8}/{sec} = {mbps} Mbps।"
    return numeric_q(rng, "cs", "network", q, qh, mbps, explain, none_p=0.1)


def make_subsets(rng):
    n = rng.randint(3, 8)
    correct = 2 ** n
    q = f"A set has {n} elements. The number of subsets, including the empty set and the set itself, is:"
    qh = f"एक समुच्चय में {n} अवयव हैं। खाली समुच्चय और स्वयं को मिलाकर उपसमुच्चयों की संख्या है:"
    explain = f"n अवयवों के समुच्चय के उपसमुच्चय 2^{n} = {correct} होते हैं।"
    return numeric_q(rng, "cs", "theory", q, qh, correct, explain, none_p=0.12)


def make_fragments(rng):
    data = rng.choice([1480, 2960, 4440, 5920])
    n = math.ceil(data / 1480)
    q = (
        f"An IP datagram carries {data} bytes of data (header extra). "
        f"The path MTU is 1500 bytes and the IP header is 20 bytes with no options. "
        f"The minimum number of fragments is:"
    )
    qh = (
        f"एक IP डेटाग्राम में {data} बाइट डेटा है (हेडर अलग)। "
        f"पथ MTU 1500 बाइट है और IP हेडर 20 बाइट है, कोई ऑप्शन नहीं। "
        f"न्यूनतम फ्रेगमेंट संख्या है:"
    )
    explain = f"एक फ्रेगमेंट में अधिकतम डेटा 1500−20 = 1480 बाइट। {data}/1480 = {n} फ्रेगमेंट।"
    return numeric_q(rng, "cs", "network", q, qh, n, explain, none_p=0.1)


def make_sql(rng):
    rows = [
        ("Amit", "CS", 26),
        ("Neha", "IT", 31),
        ("Ravi", "CS", 36),
        ("Pooja", "HR", 29),
        ("Aman", "IT", 42),
        ("Sita", "CS", 24),
        ("Kabir", "HR", 45),
        ("Meera", "IT", 27),
    ]
    dept = rng.choice(["CS", "IT", "HR"])
    age = rng.choice([25, 30, 35, 40])
    count = sum(1 for _, d, a in rows if d == dept and a >= age)
    table = "\n".join(f"{n:6} {d:3} {a}" for n, d, a in rows)
    q = (
        "Using the table Emp(name, dept, age):\n"
        + table
        + f"\nHow many rows satisfy dept = '{dept}' AND age >= {age}?"
    )
    qh = (
        "तालिका Emp(name, dept, age):\n"
        + table
        + f"\nकितनी पंक्तियाँ dept = '{dept}' AND age >= {age} पूरी करती हैं?"
    )
    explain = f"शर्त dept={dept} और age≥{age} पर गिनती {count} है।"
    item = numeric_q(rng, "cs", "dbms", q, qh, count, explain, none_p=0.08)
    item["pre"] = True
    return item


def make_levels(rng):
    levels = rng.choice([3, 4, 5, 6])
    nodes = 2 ** levels - 1
    q = (
        f"A binary tree has {levels} levels and the root is at level 1. "
        f"The maximum number of nodes is:"
    )
    qh = (
        f"एक बाइनरी ट्री में {levels} स्तर हैं और रूट स्तर 1 पर है। "
        f"नोड्स की अधिकतम संख्या है:"
    )
    explain = f"अधिकतम नोड = 2^{levels} − 1 = {nodes}।"
    return numeric_q(rng, "cs", "ds", q, qh, nodes, explain, none_p=0.1)


def make_demorgan(rng):
    forms = [
        (
            "NOT (A AND B)",
            "NOT (A AND B) बराबर है",
            "(NOT A) OR (NOT B)",
            "(NOT A) OR (NOT B)",
            [
                ("(NOT A) AND (NOT B)", "(NOT A) AND (NOT B)"),
                ("A OR B", "A OR B"),
                ("A AND (NOT B)", "A AND (NOT B)"),
            ],
            "डी मॉर्गन: ¬(A·B) = ¬A + ¬B।",
        ),
        (
            "NOT (A OR B)",
            "NOT (A OR B) बराबर है",
            "(NOT A) AND (NOT B)",
            "(NOT A) AND (NOT B)",
            [
                ("(NOT A) OR (NOT B)", "(NOT A) OR (NOT B)"),
                ("A AND B", "A AND B"),
                ("(NOT A) OR B", "(NOT A) OR B"),
            ],
            "डी मॉर्गन: ¬(A+B) = ¬A · ¬B।",
        ),
    ]
    stem, stem_h, cor, cor_h, wrongs, explain = rng.choice(forms)
    q = f"By De Morgan's law, {stem} is equivalent to:"
    qh = f"डी मॉर्गन नियम से, {stem_h}:"
    return text_choice(rng, "cs", "digital", q, qh, cor, cor_h, wrongs, explain)


def make_adj(rng):
    n = rng.choice([3, 4])
    # random undirected simple graph
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < 0.5:
                edges.append((i, j))
    if not edges:
        edges.append((0, 1))
    matrix = [["0"] * n for _ in range(n)]
    for i, j in edges:
        matrix[i][j] = matrix[j][i] = "1"
    shown = "\n".join(" ".join(row) for row in matrix)
    correct = len(edges)
    q = f"The adjacency matrix of an undirected simple graph is:\n{shown}\nThe number of edges is:"
    qh = f"एक अदिश सरल ग्राफ का आसन्नता मैट्रिक्स है:\n{shown}\nकिनारों की संख्या है:"
    explain = f"अदिश ग्राफ में हर किनारा मैट्रिक्स में दो बार (ऊपर और नीचे) आता है। ऊपरी त्रिभुज में 1 की संख्या {correct} है।"
    item = numeric_q(rng, "cs", "algo", q, qh, correct, explain, none_p=0.08)
    item["pre"] = True
    return item


# ---------- GS maths and science numerics ----------

def gs_profit(rng):
    cp = rng.choice([200, 250, 400, 500, 800, 1000, 1200, 1600, 2000])
    g = rng.choice([5, 10, 12, 15, 20, 25])
    if (cp * g) % 100 != 0:
        return gs_profit(rng)
    sp = cp + cp * g // 100
    q = f"An article costing ₹{cp} is sold at a gain of {g}%. The selling price is:"
    qh = f"₹{cp} क्रय मूल्य की वस्तु {g}% लाभ पर बेची जाती है। विक्रय मूल्य है:"
    explain = f"लाभ = {cp}×{g}/100 = {cp * g // 100}। विक्रय मूल्य = {sp}।"
    return numeric_q(rng, "gs", "maths", q, qh, sp, explain, unit="", none_p=0.12)


def gs_loss_percent(rng):
    cp = rng.choice([200, 400, 500, 800, 1000])
    sp = cp - rng.choice([20, 40, 50, 80, 100, 125])
    if sp <= 0 or (cp - sp) * 100 % cp != 0:
        return gs_loss_percent(rng)
    loss = (cp - sp) * 100 // cp
    q = f"An article bought for ₹{cp} is sold for ₹{sp}. The loss percent is:"
    qh = f"₹{cp} में खरीदी वस्तु ₹{sp} में बिकती है। हानि प्रतिशत है:"
    explain = f"हानि = {cp - sp}। हानि% = ({cp - sp}/{cp})×100 = {loss}।"
    return numeric_q(rng, "gs", "maths", q, qh, loss, explain, none_p=0.1)


def gs_si(rng):
    p = rng.choice([1000, 2000, 2500, 4000, 5000, 8000])
    r = rng.choice([4, 5, 8, 10, 12])
    t = rng.choice([2, 3, 4, 5])
    si = p * r * t // 100
    q = f"The simple interest on ₹{p} at {r}% per annum for {t} years is:"
    qh = f"₹{p} पर {r}% वार्षिक साधारण ब्याज {t} वर्ष का है:"
    explain = f"SI = P×R×T/100 = {p}×{r}×{t}/100 = {si}।"
    return numeric_q(rng, "gs", "maths", q, qh, si, explain, none_p=0.1)


def gs_ratio(rng):
    a, b = rng.choice([(2, 3), (3, 5), (4, 5), (5, 7), (2, 5), (3, 4), (1, 3)])
    total = rng.choice([i * (a + b) for i in (20, 40, 50, 80, 100)])
    part = total * a // (a + b)
    q = f"₹{total} is divided in the ratio {a}:{b}. The first share is:"
    qh = f"₹{total} को {a}:{b} के अनुपात में बाँटा जाता है। पहला भाग है:"
    explain = f"पहला भाग = {total}×{a}/{a + b} = {part}।"
    return numeric_q(rng, "gs", "maths", q, qh, part, explain, none_p=0.1)


def gs_average(rng):
    n = rng.choice([4, 5, 6])
    avg = rng.randint(12, 40)
    total = avg * n
    # present all but one number
    nums = [rng.randint(5, 50) for _ in range(n - 1)]
    last = total - sum(nums)
    if last <= 0 or last > 80:
        return gs_average(rng)
    shown = nums + ["x"]
    q = f"The average of {', '.join(str(x) for x in nums)}, and x is {avg}. The value of x is:"
    qh = f"{', '.join(str(x) for x in nums)} और x का औसत {avg} है। x का मान है:"
    explain = f"योग = {avg}×{n} = {total}। x = {total} − {sum(nums)} = {last}।"
    return numeric_q(rng, "gs", "maths", q, qh, last, explain, none_p=0.1)


def gs_lcm(rng):
    pairs = [(12, 18, 36), (8, 12, 24), (15, 20, 60), (9, 12, 36), (14, 21, 42),
             (16, 24, 48), (18, 24, 72), (20, 30, 60), (21, 28, 84)]
    a, b, l = rng.choice(pairs)
    q = f"The LCM of {a} and {b} is:"
    qh = f"{a} और {b} का लघुत्तम समापवर्त्य (LCM) है:"
    explain = f"{a} और {b} का LCM {l} है।"
    return numeric_q(rng, "gs", "maths", q, qh, l, explain, none_p=0.12)


def gs_hcf(rng):
    triples = [(12, 18, 6), (24, 36, 12), (15, 25, 5), (18, 27, 9), (20, 28, 4),
               (16, 40, 8), (21, 35, 7), (30, 45, 15)]
    a, b, h = rng.choice(triples)
    q = f"The HCF of {a} and {b} is:"
    qh = f"{a} और {b} का महत्तम समापवर्तक (HCF) है:"
    explain = f"{a} और {b} का HCF {h} है।"
    return numeric_q(rng, "gs", "maths", q, qh, h, explain, none_p=0.12)


def gs_work(rng):
    # A finishes in a days, B in b, together?
    pairs = [(6, 3, 2), (10, 15, 6), (12, 6, 4), (8, 8, 4), (4, 12, 3), (5, 20, 4), (9, 18, 6)]
    a, b, together = rng.choice(pairs)
    q = f"A can finish a work in {a} days and B in {b} days. Working together, they finish it in how many days?"
    qh = f"A कोई काम {a} दिन में और B {b} दिन में पूरा करता है। साथ काम करने पर वे उसे कितने दिन में पूरा करेंगे?"
    explain = f"एक दिन का काम = 1/{a} + 1/{b} = {together} दिन में पूरा। (जाँच: {a} और {b} का समांतर समय {together} दिन।)"
    # verify
    if abs((1 / a + 1 / b) - (1 / together)) > 1e-9:
        raise RuntimeError("work pair")
    return numeric_q(rng, "gs", "maths", q, qh, together, explain, none_p=0.1)


def gs_speed(rng):
    speed = rng.choice([30, 36, 40, 45, 48, 50, 60, 72])
    time = rng.choice([2, 3, 4, 5])
    dist = speed * time
    q = f"A car travels at {speed} km/h for {time} hours. The distance covered, in km, is:"
    qh = f"एक कार {speed} किमी/घंटा की चाल से {time} घंटे चलती है। तय दूरी (किमी) है:"
    explain = f"दूरी = चाल × समय = {speed}×{time} = {dist} किमी।"
    return numeric_q(rng, "gs", "maths", q, qh, dist, explain, none_p=0.1)


def gs_percent_of(rng):
    p = rng.choice([10, 12, 15, 20, 25, 30, 40, 50])
    n = rng.choice([80, 120, 150, 200, 240, 300, 400, 500, 600])
    if (p * n) % 100 != 0:
        return gs_percent_of(rng)
    val = p * n // 100
    q = f"{p}% of {n} is:"
    qh = f"{n} का {p}% है:"
    explain = f"{p}/100 × {n} = {val}।"
    return numeric_q(rng, "gs", "maths", q, qh, val, explain, none_p=0.12)


def gs_rect(rng):
    l = rng.randint(8, 30)
    b = rng.randint(4, 18)
    area = l * b
    q = f"The area of a rectangle of length {l} cm and breadth {b} cm is (in cm²):"
    qh = f"{l} सेमी लंबे और {b} सेमी चौड़े आयत का क्षेत्रफल (सेमी²) है:"
    explain = f"क्षेत्रफल = लंबाई × चौड़ाई = {l}×{b} = {area}।"
    return numeric_q(rng, "gs", "maths", q, qh, area, explain, none_p=0.1)


def gs_angle(rng):
    a = rng.choice([40, 50, 55, 60, 70, 80])
    b = rng.choice([30, 45, 50, 60, 65])
    c = 180 - a - b
    if c <= 10:
        return gs_angle(rng)
    q = f"Two angles of a triangle are {a}° and {b}°. The third angle is:"
    qh = f"एक त्रिभुज के दो कोण {a}° और {b}° हैं। तीसरा कोण है:"
    explain = f"त्रिभुज के कोणों का योग 180° है। तीसरा कोण = 180 − {a} − {b} = {c}°।"
    return numeric_q(rng, "gs", "maths", q, qh, c, explain, none_p=0.1)


def gs_prob(rng):
    kind = rng.choice(["coin2", "die", "coin3"])
    if kind == "die":
        q = "A fair die is rolled once. The probability of getting a number greater than 4 is:"
        qh = "एक निष्पक्ष पासा एक बार उछाला जाता है। 4 से बड़ी संख्या आने की प्रायिकता है:"
        # answers as strings
        correct, wrongs = "1/3", ["1/6", "1/2", "2/3", "5/6"]
        explain = "5 या 6, यानी 2 अनुकूल फल। कुल 6। प्रायिकता 2/6 = 1/3।"
    elif kind == "coin2":
        q = "Two fair coins are tossed. The probability of getting exactly one head is:"
        qh = "दो निष्पक्ष सिक्के उछाले जाते हैं। ठीक एक चित आने की प्रायिकता है:"
        correct, wrongs = "1/2", ["1/4", "3/4", "1/3", "2/3"]
        explain = "परिणाम HH, HT, TH, TT। ठीक एक चित: HT, TH। प्रायिकता 2/4 = 1/2।"
    else:
        q = "Three fair coins are tossed. The probability of getting all heads is:"
        qh = "तीन निष्पक्ष सिक्के उछाले जाते हैं। तीनों चित आने की प्रायिकता है:"
        correct, wrongs = "1/8", ["1/2", "1/4", "3/8", "1/6"]
        explain = "कुल परिणाम 8। सिर्फ HHH एक अनुकूल है। प्रायिकता 1/8।"
    return _choice_str(rng, "gs", "maths", q, qh, correct, wrongs, explain)


def gs_exponent(rng):
    base = rng.choice([2, 3, 4, 5])
    exp = rng.choice([2, 3, 4, 5])
    if base == 5 and exp > 4:
        exp = 3
    if base == 4 and exp > 4:
        exp = 3
    val = base ** exp
    q = f"The value of {base}^{exp} is:"
    qh = f"{base}^{exp} का मान है:"
    explain = f"{base} को {exp} बार गुणा करने पर {val} मिलता है।"
    return numeric_q(rng, "gs", "maths", q, qh, val, explain, none_p=0.1)


def gs_series(rng):
    start = rng.randint(2, 12)
    diff = rng.choice([2, 3, 4, 5, 6])
    seq = [start + i * diff for i in range(4)]
    nxt = seq[-1] + diff
    q = f"The next term of the series {', '.join(map(str, seq))}, … is:"
    qh = f"श्रेणी {', '.join(map(str, seq))}, … का अगला पद है:"
    explain = f"हर पद {diff} बढ़ता है। अगला पद {seq[-1]} + {diff} = {nxt}।"
    return numeric_q(rng, "gs", "reasoning", q, qh, nxt, explain, none_p=0.1)


def gs_clock(rng):
    hour = rng.choice([2, 3, 4, 6, 9])
    angle = min(abs(30 * hour), 360 - abs(30 * hour))
    # at H:00, angle = min(|30H - 0|, 360 - that) but 30*hour for 2 is 60, 3 is 90, 4 is 120, 6 is 180, 9 is 90? 
    # 30*9=270, min(270, 90)=90. Yes.
    raw = abs(30 * hour)
    angle = min(raw, 360 - raw)
    q = f"The angle between the hour and minute hands of a clock at {hour}:00 is (in degrees):"
    qh = f"{hour}:00 बजे घड़ी की घंटे और मिनट की सुइयों के बीच कोण (डिग्री में) है:"
    explain = f"{hour}:00 पर कोण = min(|30×{hour}|, 360 − वह) = {angle}°।"
    return numeric_q(rng, "gs", "reasoning", q, qh, angle, explain, none_p=0.1)


def gs_direction(rng):
    # start, go north a, east b, displacement
    north = rng.choice([3, 4, 6, 8, 9])
    east = rng.choice([4, 6, 8, 12])
    # only pythagorean
    triples = {(3, 4): 5, (6, 8): 10, (9, 12): 15, (5, 12): 13, (8, 15): 17}
    pair = rng.choice(list(triples))
    north, east = pair
    dist = triples[pair]
    q = (
        f"A person walks {north} km north and then {east} km east. "
        f"The straight-line distance from the start, in km, is:"
    )
    qh = (
        f"एक व्यक्ति {north} किमी उत्तर फिर {east} किमी पूर्व चलता है। "
        f"शुरुआत से सीधी दूरी (किमी) है:"
    )
    explain = f"समकोण त्रिभुज: √({north}²+{east}²) = {dist} किमी।"
    return numeric_q(rng, "gs", "reasoning", q, qh, dist, explain, none_p=0.1)


def gs_coding(rng):
    word = rng.choice(["CAT", "DOG", "SUN", "PEN", "BOOK", "TREE"])
    shift = rng.choice([1, 2])
    coded = "".join(chr((ord(ch) - 65 + shift) % 26 + 65) for ch in word)
    q = f"In a certain code, each letter is shifted +{shift} in the alphabet (A→{chr(65+shift)}). How is {word} written?"
    qh = f"एक कूट में हर अक्षर वर्णमाला में +{shift} खिसकता है (A→{chr(65+shift)})। {word} कैसे लिखा जाएगा?"
    wrongs = []
    for d in (shift + 1, shift - 1 if shift > 1 else 3, 0):
        wrongs.append("".join(chr((ord(ch) - 65 + d) % 26 + 65) for ch in word))
    wrongs.append(word[::-1])
    explain = f"हर अक्षर {shift} आगे है, इसलिए {word} → {coded}।"
    return _choice_str(rng, "gs", "reasoning", q, qh, coded, wrongs, explain)


def gs_ohm(rng):
    r = rng.choice([4, 5, 6, 8, 10, 12])
    i = rng.choice([2, 3, 4, 5])
    v = i * r
    q = f"A resistor of {r} Ω carries a current of {i} A. The potential difference across it, in volts, is:"
    qh = f"{r} Ω के प्रतिरोध में {i} A धारा बहती है। उसके सिरों का विभवांतर (वोल्ट) है:"
    explain = f"ओम का नियम: V = IR = {i}×{r} = {v} V।"
    return numeric_q(rng, "gs", "physics", q, qh, v, explain, none_p=0.1)


def gs_series_r(rng):
    r1 = rng.choice([2, 4, 5, 6, 10])
    r2 = rng.choice([3, 4, 5, 8, 12])
    req = r1 + r2
    q = f"Two resistors of {r1} Ω and {r2} Ω are connected in series. The equivalent resistance, in ohms, is:"
    qh = f"{r1} Ω और {r2} Ω के दो प्रतिरोध श्रेणीक्रम में जुड़े हैं। तुल्य प्रतिरोध (ओम) है:"
    explain = f"श्रेणीक्रम में R = R1 + R2 = {r1}+{r2} = {req} Ω।"
    return numeric_q(rng, "gs", "physics", q, qh, req, explain, none_p=0.1)


def gs_parallel_r(rng):
    pairs = [(6, 3, 2), (4, 12, 3), (10, 10, 5), (6, 12, 4), (12, 6, 4), (20, 5, 4)]
    r1, r2, req = rng.choice(pairs)
    q = f"Two resistors of {r1} Ω and {r2} Ω are connected in parallel. The equivalent resistance, in ohms, is:"
    qh = f"{r1} Ω और {r2} Ω के दो प्रतिरोध समांतर क्रम में जुड़े हैं। तुल्य प्रतिरोध (ओम) है:"
    explain = f"1/R = 1/{r1} + 1/{r2}। R = {req} Ω।"
    if abs(1 / req - (1 / r1 + 1 / r2)) > 1e-9:
        raise RuntimeError("parallel")
    return numeric_q(rng, "gs", "physics", q, qh, req, explain, none_p=0.1)


def gs_power(rng):
    v = rng.choice([10, 12, 20, 24])
    i = rng.choice([2, 3, 4, 5])
    p = v * i
    q = f"An appliance works at {v} V and draws {i} A. Its power, in watts, is:"
    qh = f"एक उपकरण {v} V पर चलता है और {i} A धारा लेता है। इसकी शक्ति (वाट) है:"
    explain = f"P = VI = {v}×{i} = {p} W।"
    return numeric_q(rng, "gs", "physics", q, qh, p, explain, none_p=0.1)


def gs_density(rng):
    mass = rng.choice([20, 40, 50, 80, 100, 120])
    vol = rng.choice([2, 4, 5, 8, 10])
    if mass % vol != 0:
        return gs_density(rng)
    d = mass // vol
    q = f"An object of mass {mass} g occupies {vol} cm³. Its density, in g/cm³, is:"
    qh = f"{mass} ग्राम द्रव्यमान की वस्तु {vol} सेमी³ जगह लेती है। घनत्व (g/cm³) है:"
    explain = f"घनत्व = द्रव्यमान/आयतन = {mass}/{vol} = {d} g/cm³।"
    return numeric_q(rng, "gs", "physics", q, qh, d, explain, none_p=0.1)


def gs_speed_sound_echo(rng):
    # 2d = v t, v=340, choose t so d integer
    # d = v t / 2. t = 2 s -> d = 340. t=1 -> 170. t=4 -> 680.
    t = rng.choice([1, 2, 4])
    d = 340 * t // 2
    q = (
        f"A person hears the echo of a clap after {t} s. "
        f"If the speed of sound is 340 m/s, the distance of the reflecting wall, in metres, is:"
    )
    qh = (
        f"एक व्यक्ति ताली की प्रतिध्वनि {t} सेकंड बाद सुनता है। "
        f"ध्वनि की चाल 340 मी/से हो तो परावर्तक दीवार की दूरी (मीटर) है:"
    )
    explain = f"ध्वनि दीवार तक जाकर लौटती है: 2d = 340×{t}। d = {d} m।"
    return numeric_q(rng, "gs", "physics", q, qh, d, explain, none_p=0.08)


def gs_work_energy(rng):
    force = rng.choice([4, 5, 8, 10, 12, 15, 20, 25])
    dist = rng.choice([2, 3, 4, 5, 6, 8, 10])
    work = force * dist
    q = f"A force of {force} N moves an object {dist} m in the direction of the force. The work done, in joules, is:"
    qh = f"{force} N का बल एक वस्तु को बल की दिशा में {dist} मी ले जाता है। किया गया कार्य (जूल) है:"
    explain = f"कार्य = बल × विस्थापन = {force}×{dist} = {work} J।"
    return numeric_q(rng, "gs", "physics", q, qh, work, explain, none_p=0.1)


def gs_kinetic(rng):
    mass = rng.choice([2, 4, 6, 8, 10])
    speed = rng.choice([2, 4, 6, 8])
    ke = mass * speed * speed // 2
    q = f"The kinetic energy of a body of mass {mass} kg moving at {speed} m/s is (in joules):"
    qh = f"{mass} किग्रा द्रव्यमान की वस्तु {speed} मी/से की चाल से चल रही है। उसकी गतिज ऊर्जा (जूल) है:"
    explain = f"गतिज ऊर्जा = ½mv² = ½×{mass}×{speed}² = {ke} J।"
    return numeric_q(rng, "gs", "physics", q, qh, ke, explain, none_p=0.08)


GS_MATH = [
    gs_profit, gs_loss_percent, gs_si, gs_ratio, gs_average, gs_lcm, gs_hcf,
    gs_work, gs_speed, gs_percent_of, gs_rect, gs_angle, gs_prob, gs_exponent,
    gs_series, gs_clock, gs_direction, gs_coding,
]
GS_SCI = [gs_ohm, gs_series_r, gs_parallel_r, gs_power, gs_density, gs_speed_sound_echo, gs_work_energy, gs_kinetic]

CS_MAKERS = [
    make_base, make_base, make_base,
    make_bitwise, make_bitwise,
    make_twos, make_mux, make_hex_add, make_bcd, make_full_adder, make_counter_ff,
    make_sign_mag, make_demorgan,
    make_address_lines, make_cache, make_latency, make_access_time, make_endian,
    make_efficiency, make_pointer,
    make_fifo, make_lru, make_fcfs, make_sjf, make_rr, make_page_offset,
    make_bst, make_bst, make_postfix, make_postfix, make_stack_perm, make_levels,
    make_bst_count,
    make_loop, make_loop,
    make_subnet, make_ip_class, make_delay, make_throughput, make_fragments, make_parity,
    make_graph_edges, make_handshaking, make_adj, make_subsets, make_sql,
]


def _take_unique(rng, makers, n, topic_override=None):
    out = []
    seen = set()
    guard = 0
    while len(out) < n and guard < n * 40:
        guard += 1
        item = rng.choice(makers)(rng)
        if topic_override:
            item["topic"] = topic_override
        key = item["q"]
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    if len(out) < n:
        raise RuntimeError(f"could only build {len(out)} of {n}")
    return out


def gen_cs(rng, n):
    return _take_unique(rng, CS_MAKERS, n)


def gen_gs_math(rng, n):
    return _take_unique(rng, GS_MATH, n)


def gen_gs_sci(rng, n):
    return _take_unique(rng, GS_SCI, n)


def _self_test():
    rng = random.Random(1)
    # known FIFO
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0]
    assert _fifo(pages, 3) == 12, _fifo(pages, 3)
    assert _lru([1, 2, 3, 2, 1, 4], 3) == 4
    assert _catalan(3) == 5 and _catalan(4) == 14 and _catalan(5) == 42
    assert _total_wait_fcfs([4, 3, 2]) == 0 + 4 + 7
    assert _valid_stack([1, 2, 3, 4])
    assert not _valid_stack([4, 3, 1, 2])  # 4 first means 1,2,3 pushed; pop 4,3 then next must be 2 not 1? 
    # After pushing 1,2,3,4 and popping 4,3 stack top is 2. Next output 1 is invalid. Yes.
    items = gen_cs(rng, 30) + gen_gs_math(rng, 8) + gen_gs_sci(rng, 4)
    assert len(items) == 42
    for it in items:
        assert len(it["options"]) == 5
        assert 0 <= it["answer"] <= 4
    print("gen_calc self-test ok", len(items))


if __name__ == "__main__":
    _self_test()
