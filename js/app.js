(() => {
  const DATA = window.BPSC_PAPERS;
  const GUIDE = window.BPSC_GUIDE;
  const SECTIONS = window.BPSC_SECTIONS;
  const STORE = "bpsc-tre-cs-v1";
  const LETTERS = ["A", "B", "C", "D", "E"];

  if (!DATA || !DATA.sets) {
    document.body.innerHTML = "<p style='padding:24px'>प्रश्न-पत्र लोड नहीं हो सका। data/papers.js मौजूद होना चाहिए।</p>";
    return;
  }

  const $ = (id) => document.getElementById(id);
  let db = load();
  let session = null;
  let lang = "both";
  let qSize = 1.05;
  let reviewFilter = "all";
  let reviewIndex = 0;

  function load() {
    try {
      return JSON.parse(localStorage.getItem(STORE)) || { attempts: {}, active: null, profile: {} };
    } catch {
      return { attempts: {}, active: null, profile: {} };
    }
  }
  function save() {
    localStorage.setItem(STORE, JSON.stringify(db));
  }

  function show(name) {
    ["view-home", "view-instructions", "view-exam", "view-result"].forEach((id) => {
      $(id).classList.toggle("hidden", id !== name);
    });
    $("site-top").classList.toggle("hidden", name === "view-exam");
    document.body.classList.toggle("exam-body", name === "view-exam");
  }

  function attemptsOf(id) {
    return db.attempts[id] || [];
  }
  function bestOf(id) {
    const list = attemptsOf(id);
    if (!list.length) return null;
    return list.slice().sort((a, b) => b.score.merit - a.score.merit)[0];
  }

  function renderHome() {
    show("view-home");
    const resume = $("resume-box");
    if (db.active && db.active.mode === "mock") {
      const set = DATA.sets.find((s) => s.id === db.active.setId);
      resume.innerHTML = `<div class="panel" style="margin-top:12px">
        <strong>अधूरी परीक्षा:</strong> ${set ? set.titleHi : ""} बचा हुआ है।
        <div class="actions" style="margin-top:8px">
          <button class="btn" id="resume-btn" type="button">जारी रखें</button>
          <button class="btn ghost" id="discard-btn" type="button">छोड़ दें</button>
        </div>
      </div>`;
      $("resume-btn").onclick = () => resumeExam();
      $("discard-btn").onclick = () => { db.active = null; save(); renderHome(); };
    } else resume.innerHTML = "";

    $("set-grid").innerHTML = DATA.sets.map((set) => {
      const best = bestOf(set.id);
      const n = attemptsOf(set.id).length;
      let meta = "अभी प्रयास नहीं";
      let badge = `<span class="badge neutral">नया</span>`;
      if (best) {
        meta = `सर्वोत्तम मेरिट ${best.score.merit}/120 · भाषा ${best.score.language}/30 · ${n} प्रयास`;
        badge = best.score.qualified
          ? `<span class="badge ok">क्वालीफाई</span>`
          : `<span class="badge bad">भाषा में अयोग्य</span>`;
      }
      return `<article class="card">
        <div class="card-top"><span class="series">SERIES ${set.series}</span>${badge}</div>
        <h2>${set.titleHi}</h2>
        <div class="meta">${meta}<br>150 प्रश्न · 150 मिनट</div>
        <div class="card-actions">
          <button class="btn" type="button" data-start="${set.id}">शुरू करें</button>
          <button class="btn secondary" type="button" data-last="${set.id}" ${n ? "" : "disabled"}>परिणाम</button>
        </div>
      </article>`;
    }).join("");

    $("set-grid").onclick = (e) => {
      const start = e.target.closest("[data-start]");
      const last = e.target.closest("[data-last]");
      if (start) openInstructions(start.dataset.start);
      if (last && !last.disabled) {
        const list = attemptsOf(last.dataset.last);
        openResult(list[list.length - 1]);
      }
    };

    const topics = topicMenu();
    $("topic-pick").innerHTML = topics.map((t) =>
      `<button class="btn ghost" type="button" data-topic="${t.id}" data-section="${t.section}">${t.hi}</button>`
    ).join("");
    $("topic-pick").onclick = (e) => {
      const b = e.target.closest("[data-topic]");
      if (!b) return;
      startDrill(b.dataset.section, b.dataset.topic);
    };
  }

  function topicMenu() {
    const seen = new Map();
    DATA.sets.forEach((set) => set.questions.forEach((q) => {
      const key = q.section + ":" + q.topic;
      if (!seen.has(key)) {
        const g = GUIDE[q.topic] || { hi: q.topic };
        seen.set(key, { id: q.topic, section: q.section, hi: g.hi });
      }
    }));
    return [...seen.values()];
  }

  function openInstructions(setId) {
    if (db.active) {
      const ok = confirm("एक परीक्षा पहले से अधूरी है। उसे छोड़कर नई शुरू करें?");
      if (!ok) return;
      db.active = null;
      save();
    }
    session = { kind: "pending", setId };
    const set = DATA.sets.find((s) => s.id === setId);
    $("instr-title").textContent = set.titleHi + " · Series " + set.series;
    $("cand-name").value = db.profile.name || "";
    $("cand-roll").value = db.profile.roll || "";
    $("agree").checked = false;
    show("view-instructions");
  }

  $("back-home").onclick = () => renderHome();
  $("begin-exam").onclick = () => {
    if (!$("agree").checked) {
      alert("निर्देश पढ़कर चेकबॉक्स चुनें।");
      return;
    }
    const set = DATA.sets.find((s) => s.id === session.setId);
    const name = $("cand-name").value.trim() || "अभ्यर्थी";
    const roll = $("cand-roll").value.trim() || "—";
    db.profile = { name, roll };
    const active = {
      mode: "mock",
      setId: set.id,
      name, roll,
      started: Date.now(),
      deadline: Date.now() + DATA.durationMin * 60 * 1000,
      index: 0,
      answers: {},
      marked: {},
      visited: { 0: true },
      rough: ""
    };
    db.active = active;
    save();
    enterExam();
  };

  function resumeExam() {
    enterExam();
  }

  function enterExam() {
    session = db.active;
    lang = "both";
    document.querySelectorAll("#lang-seg button").forEach((b) => b.classList.toggle("active", b.dataset.lang === lang));
    show("view-exam");
    renderExam();
    tick();
  }

  function paperQuestions() {
    if (session.mode === "mock") {
      return DATA.sets.find((s) => s.id === session.setId).questions;
    }
    const map = new Map();
    DATA.sets.forEach((s) => s.questions.forEach((q) => map.set(q.id, q)));
    return session.questionIds.map((id) => map.get(id)).filter(Boolean);
  }

  function currentList() {
    return paperQuestions();
  }

  function renderExam() {
    const qs = currentList();
    const q = qs[session.index];
    const set = session.mode === "mock" ? DATA.sets.find((s) => s.id === session.setId) : null;
    const title = session.mode === "mock"
      ? `${set.titleHi} · Series ${set.series}`
      : session.title;
    const who = `${session.name} · ${session.roll}`;
    $("exam-title").innerHTML = `${title}<small>${who} · ${SECTIONS[q.section].hi}</small>`;
    $("sheet").innerHTML = questionHTML(q, session.answers[q.id], false);
    $("sheet").querySelectorAll(".opt").forEach((btn) => {
      btn.onclick = () => {
        session.answers[q.id] = Number(btn.dataset.i);
        session.visited[session.index] = true;
        save();
        renderExam();
      };
    });
    renderPalette(qs);
  }

  function questionHTML(q, chosen, review) {
    const bilingual = q.section === "gs" || q.section === "cs";
    let en = q.q, hi = q.qh;
    if (!bilingual) {
      hi = "";
      if (q.section === "hi") { en = ""; hi = q.q; }
    } else if (lang === "en") hi = "";
    else if (lang === "hi") { en = hi || en; hi = ""; }
    const pre = q.pre ? " stem" : " stem";
    let passage = "";
    if (q.passage && (q.section === "en" || lang !== "hi")) {
      passage = `<div class="passage">${escape(q.passage)}</div>`;
    }
    const stem = `
      ${en ? `<div class="${pre.trim()}">${escape(en)}</div>` : ""}
      ${hi ? `<div class="stem hi-line">${escape(hi)}</div>` : ""}`;
    const options = q.options.map((opt, i) => {
      const hopt = q.optionsh[i];
      let primary = opt, secondary = "";
      if (q.section === "hi") { primary = hopt || opt; secondary = ""; }
      else if (q.section === "en") { secondary = ""; }
      else if (lang === "hi") { primary = hopt || opt; secondary = ""; }
      else if (lang === "en" || !hopt || hopt === opt) { secondary = ""; }
      else secondary = hopt;
      let cls = "opt";
      if (!review && chosen === i) cls += " selected";
      if (review) {
        if (i === q.answer) cls += " correct";
        else if (chosen === i) cls += " wrong";
      }
      return `<button type="button" class="${cls}" data-i="${i}">
        <span class="bubble">${LETTERS[i]}</span>
        <span class="opt-text">${escape(primary)}${secondary ? `<span class="subopt">${escape(secondary)}</span>` : ""}</span>
      </button>`;
    }).join("");
    const explain = review ? `<div class="explain"><strong>व्याख्या।</strong> ${escape(q.explain)}</div>` : "";
    const kicker = review
      ? `प्रश्न ${q.n || ""} · ${SECTIONS[q.section].hi}`
      : `प्रश्न ${q.n || session.index + 1} / ${currentList().length}`;
    return `<div class="q-kicker"><span>${kicker}</span><span>${(GUIDE[q.topic] || {}).hi || q.topic}</span></div>
      ${passage}${stem}<div class="options">${options}</div>${explain}`;
  }

  function escape(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function statusOf(q, index) {
    const answered = session.answers[q.id] !== undefined;
    const marked = !!session.marked[q.id];
    const visited = !!session.visited[index];
    if (answered && marked) return "am";
    if (marked) return "mk";
    if (answered) return "an";
    if (visited) return "na";
    return "nv";
  }

  function renderPalette(qs) {
    const groups = [];
    qs.forEach((q, i) => {
      const last = groups[groups.length - 1];
      if (!last || last.section !== q.section) groups.push({ section: q.section, items: [] });
      groups[groups.length - 1].items.push({ q, i });
    });
    const answered = Object.keys(session.answers).length;
    const html = `<div class="legend">
        <span><i class="dot nv"></i>न देखा</span>
        <span><i class="dot na"></i>बिना उत्तर</span>
        <span><i class="dot an"></i>उत्तर</span>
        <span><i class="dot mk"></i>समीक्षा</span>
      </div>` + groups.map((g) => `
        <div class="pal-sec">${SECTIONS[g.section].hi}</div>
        <div class="pal-grid">
          ${g.items.map(({ q, i }) => `<button type="button" class="pbtn ${statusOf(q, i)} ${i === session.index ? "current" : ""}" data-jump="${i}">${q.n || i + 1}</button>`).join("")}
        </div>`).join("") + `<div class="statline">उत्तर ${answered} / ${qs.length} · चिह्नित ${Object.keys(session.marked).length}</div>`;
    const pal = $("palette");
    pal.innerHTML = html;
    pal.onclick = (e) => {
      const b = e.target.closest("[data-jump]");
      if (!b) return;
      session.index = Number(b.dataset.jump);
      session.visited[session.index] = true;
      save();
      pal.classList.remove("open");
      renderExam();
    };
  }

  function move(delta) {
    const qs = currentList();
    session.visited[session.index] = true;
    session.index = Math.max(0, Math.min(qs.length - 1, session.index + delta));
    session.visited[session.index] = true;
    save();
    renderExam();
  }

  $("btn-prev").onclick = () => move(-1);
  $("btn-next").onclick = () => move(1);
  $("btn-clear").onclick = () => {
    const q = currentList()[session.index];
    delete session.answers[q.id];
    save();
    renderExam();
  };
  $("btn-mark").onclick = () => {
    const q = currentList()[session.index];
    if (session.marked[q.id]) delete session.marked[q.id];
    else session.marked[q.id] = true;
    move(1);
  };
  $("btn-submit").onclick = () => askSubmit();
  $("open-palette").onclick = () => $("palette").classList.toggle("open");
  $("open-rough").onclick = () => openRough();
  $("font-inc").onclick = () => { qSize = Math.min(1.35, qSize + 0.06); document.documentElement.style.setProperty("--qsize", qSize + "rem"); };
  $("font-dec").onclick = () => { qSize = Math.max(0.9, qSize - 0.06); document.documentElement.style.setProperty("--qsize", qSize + "rem"); };
  $("lang-seg").onclick = (e) => {
    const b = e.target.closest("[data-lang]");
    if (!b) return;
    lang = b.dataset.lang;
    document.querySelectorAll("#lang-seg button").forEach((x) => x.classList.toggle("active", x === b));
    if (session) renderExam();
  };

  document.addEventListener("keydown", (e) => {
    if (!session || $("view-exam").classList.contains("hidden")) return;
    if (e.target.matches("input, textarea")) return;
    const k = e.key.toLowerCase();
    if (k >= "a" && k <= "e") {
      const q = currentList()[session.index];
      session.answers[q.id] = k.charCodeAt(0) - 97;
      save();
      renderExam();
    } else if (k === "n" || e.key === "ArrowRight") move(1);
    else if (k === "p" || e.key === "ArrowLeft") move(-1);
    else if (k === "m") $("btn-mark").click();
    else if (k === "c") $("btn-clear").click();
  });

  function tick() {
    if (!session || session !== db.active) return;
    const left = Math.max(0, session.deadline - Date.now());
    const s = Math.floor(left / 1000);
    const hh = String(Math.floor(s / 3600)).padStart(2, "0");
    const mm = String(Math.floor((s % 3600) / 60)).padStart(2, "0");
    const ss = String(s % 60).padStart(2, "0");
    const el = $("timer");
    if (el) {
      el.textContent = `${hh}:${mm}:${ss}`;
      el.classList.toggle("danger", s < 300);
    }
    if (left <= 0) {
      finish(true);
      return;
    }
    setTimeout(tick, 250);
  }

  function askSubmit() {
    const qs = currentList();
    const pending = qs.filter((q) => session.answers[q.id] === undefined).length;
    openModal(`
      <h3>उत्तर पत्र जमा करें?</h3>
      <p>${pending ? pending + " प्रश्न अभी बिना उत्तर के हैं। खाली प्रश्न पर अंक नहीं मिलेंगे और न ही कटेंगे।" : "सभी प्रश्नों के उत्तर चिह्नित हैं।"}</p>
      <div class="actions">
        <button class="btn ghost" id="modal-no" type="button">लौटें</button>
        <button class="btn warn" id="modal-yes" type="button">जमा करें</button>
      </div>`);
    $("modal-no").onclick = closeModal;
    $("modal-yes").onclick = () => { closeModal(); finish(false); };
  }

  function finish(auto) {
    if (!session) return;
    const qs = currentList();
    const score = scorePaper(qs, session.answers, session.mode === "mock");
    const record = {
      id: "a" + Date.now(),
      mode: session.mode,
      setId: session.setId || null,
      title: session.mode === "mock"
        ? DATA.sets.find((s) => s.id === session.setId).titleHi
        : session.title,
      name: session.name,
      roll: session.roll,
      submittedAt: Date.now(),
      auto,
      timeUsedSec: Math.round((Date.now() - session.started) / 1000),
      answers: session.answers,
      questionIds: qs.map((q) => q.id),
      score
    };
    if (session.mode === "mock") {
      db.attempts[session.setId] = attemptsOf(session.setId).concat(record);
    } else {
      db.attempts.drill = (db.attempts.drill || []).concat(record);
    }
    db.active = null;
    session = null;
    save();
    openResult(record);
  }

  function scorePaper(qs, answers, isMock) {
    const sections = {};
    const topics = {};
    let correct = 0;
    qs.forEach((q) => {
      const sec = sections[q.section] || (sections[q.section] = { total: 0, correct: 0, wrong: 0, blank: 0 });
      const top = topics[q.section + ":" + q.topic] || (topics[q.section + ":" + q.topic] = {
        section: q.section, topic: q.topic, total: 0, correct: 0, wrong: 0, blank: 0
      });
      sec.total++; top.total++;
      const a = answers[q.id];
      if (a === undefined) { sec.blank++; top.blank++; return; }
      if (a === q.answer) { sec.correct++; top.correct++; correct++; }
      else { sec.wrong++; top.wrong++; }
    });
    const language = (sections.en?.correct || 0) + (sections.hi?.correct || 0);
    const merit = (sections.gs?.correct || 0) + (sections.cs?.correct || 0);
    return {
      correct,
      total: qs.length,
      sections,
      topics,
      language,
      merit,
      qualified: !isMock || language >= DATA.qualifyMarks,
      isMock
    };
  }

  function openResult(record) {
    const qs = questionsOf(record);
    const hasWrong = qs.some((q) => {
      const a = record.answers[q.id];
      return a !== undefined && a !== q.answer;
    });
    reviewFilter = hasWrong ? "wrong" : "all";
    reviewIndex = 0;
    session = { reviewOf: record };
    show("view-result");
    paintResult(record);
  }

  function questionsOf(record) {
    const map = new Map();
    DATA.sets.forEach((s) => s.questions.forEach((q) => map.set(q.id, q)));
    return record.questionIds.map((id) => map.get(id)).filter(Boolean);
  }

  function paintResult(record) {
    const sc = record.score;
    const qs = questionsOf(record);
    const mins = Math.floor(record.timeUsedSec / 60);
    const sec = record.timeUsedSec % 60;
    const qual = sc.isMock
      ? (sc.qualified
        ? `<div class="score-box good"><div>भाषा (क्वालीफाइंग)</div><div class="num">${sc.language}/30</div><div class="badge ok">योग्य · न्यूनतम 9</div></div>`
        : `<div class="score-box bad"><div>भाषा (क्वालीफाइंग)</div><div class="num">${sc.language}/30</div><div class="badge bad">अयोग्य · 9 से कम</div><p>मेरिट सूची के लिए भाषा में कम से कम 30% चाहिए। अंग्रेज़ी और हिंदी दोनों दोहराएँ।</p></div>`)
      : `<div class="score-box"><div>सही</div><div class="num">${sc.correct}/${sc.total}</div></div>`;
    const meritBox = sc.isMock
      ? `<div class="score-box"><div>मेरिट (GS + CS)</div><div class="num">${sc.qualified ? sc.merit : "—"}/120</div><div>${sc.qualified ? "इसी अंक से मेरिट बनती है।" : "भाषा क्वालीफाई नहीं हुई, इसलिए मेरिट नहीं बनी।"}</div></div>
         <div class="score-box"><div>कुल सही</div><div class="num">${sc.correct}/150</div><div>समय ${mins} मि ${sec} से · नेगेटिव मार्किंग नहीं</div></div>`
      : `<div class="score-box"><div>अभ्यास</div><div class="num">${record.title}</div></div><div class="score-box"><div>समय</div><div class="num">${mins}:${String(sec).padStart(2, "0")}</div></div>`;

    const secHtml = Object.entries(sc.sections).map(([id, s]) => {
      const pct = s.total ? Math.round((s.correct / s.total) * 100) : 0;
      return `<div>
        <strong>${SECTIONS[id].hi}</strong> — ${s.correct}/${s.total} सही · गलत ${s.wrong} · खाली ${s.blank}
        <div class="bar"><span style="width:${pct}%"></span></div>
      </div>`;
    }).join("");

    const advice = buildAdvice(sc);
    $("view-result").innerHTML = `
      <h2>${escape(record.title)} · परिणाम</h2>
      <p>${escape(record.name)} · ${escape(record.roll)}${record.auto ? " · समय समाप्त होने पर जमा हुआ" : ""}</p>
      <div class="score-hero">${qual}${meritBox}</div>
      <section class="panel" style="margin-top:14px">
        <h2>भागवार स्थिति</h2>
        <div class="section-list">${secHtml}</div>
      </section>
      <section class="panel" style="margin-top:14px">
        <h2>जहाँ गलती हो रही है</h2>
        ${advice || "<p class='good-note'>इस प्रयास में कोई टॉपिक स्पष्ट रूप से कमजोर नहीं दिखा। फिर भी गलत सवालों की व्याख्या पढ़ लें।</p>"}
      </section>
      <section class="panel" style="margin-top:14px">
        <h2>उत्तर देखें</h2>
        <div class="filters" id="rev-filters">
          <button type="button" data-f="wrong" class="btn ghost">गलत</button>
          <button type="button" data-f="blank" class="btn ghost">खाली</button>
          <button type="button" data-f="all" class="btn ghost">सभी</button>
          <button type="button" data-f="en" class="btn ghost">अंग्रेज़ी</button>
          <button type="button" data-f="hi" class="btn ghost">हिंदी</button>
          <button type="button" data-f="gs" class="btn ghost">GS</button>
          <button type="button" data-f="cs" class="btn ghost">CS</button>
        </div>
        <div id="review-box"></div>
        <div class="actions" style="margin-top:10px">
          <button class="btn ghost" id="rev-prev" type="button">पिछला</button>
          <button class="btn ghost" id="rev-next" type="button">अगला</button>
          <button class="btn" id="rev-home" type="button">सीरीज पर लौटें</button>
        </div>
      </section>`;
    $("rev-filters").onclick = (e) => {
      const b = e.target.closest("[data-f]");
      if (!b) return;
      reviewFilter = b.dataset.f;
      const list = filtered(qs, record);
      reviewIndex = 0;
      paintReview(record, qs);
    };
    $("rev-prev").onclick = () => { reviewIndex = Math.max(0, reviewIndex - 1); paintReview(record, qs); };
    $("rev-next").onclick = () => {
      const list = filtered(qs, record);
      reviewIndex = Math.min(list.length - 1, reviewIndex + 1);
      paintReview(record, qs);
    };
    $("rev-home").onclick = () => { session = null; renderHome(); };
    paintReview(record, qs);
  }

  function filtered(qs, record) {
    return qs.filter((q) => {
      const a = record.answers[q.id];
      if (reviewFilter === "wrong") return a !== undefined && a !== q.answer;
      if (reviewFilter === "blank") return a === undefined;
      if (["en", "hi", "gs", "cs"].includes(reviewFilter)) return q.section === reviewFilter;
      return true;
    });
  }

  function paintReview(record, qs) {
    const list = filtered(qs, record);
    document.querySelectorAll("#rev-filters button").forEach((b) => {
      b.classList.toggle("active", b.dataset.f === reviewFilter);
    });
    const box = $("review-box");
    if (!list.length) {
      box.innerHTML = "<p>इस फ़िल्टर में कोई प्रश्न नहीं।</p>";
      return;
    }
    if (reviewIndex >= list.length) reviewIndex = 0;
    const q = list[reviewIndex];
    const chosen = record.answers[q.id];
    box.innerHTML = `<p class="meta">${reviewIndex + 1} / ${list.length}</p>` + questionHTML(q, chosen, true);
  }

  function buildAdvice(sc) {
    const rows = Object.values(sc.topics).map((t) => {
      const attempted = t.total - t.blank;
      const acc = attempted ? t.correct / attempted : 0;
      return { ...t, attempted, acc };
    });
    const weak = rows.filter((t) =>
      (t.wrong >= 1 && t.acc < 0.7) ||
      (t.total >= 4 && t.blank / t.total >= 0.5)
    ).sort((a, b) => a.acc - b.acc || b.wrong - a.wrong);

    const strong = rows.filter((t) => t.attempted >= 3 && t.acc >= 0.8);

    const weakHtml = weak.map((t) => {
      const g = GUIDE[t.topic] || { hi: t.topic, read: "इस टॉपिक के नोट्स दोहराएँ।", practice: "इसी टॉपिक के गलत प्रश्न फिर हल करें।" };
      const skipped = t.wrong === 0 && t.total >= 4 && t.blank / t.total >= 0.5;
      const head = skipped
        ? `${g.hi} के ${t.total} में से ${t.blank} छोड़े गए। इस टॉपिक को छोड़ रहे हैं — पढ़ना जरूरी है।`
        : `${g.hi} में गलती हो रही है: ${t.correct} सही / ${t.attempted} प्रयास (गलत ${t.wrong})।`;
      return `<article class="weak">
        <h3>${head}</h3>
        <p><strong>क्या पढ़ें।</strong> ${g.read}</p>
        <p><strong>कैसे अभ्यास करें।</strong> ${g.practice}</p>
        <button class="btn" type="button" data-drill="${t.section}:${t.topic}">इसी टॉपिक के 20 प्रश्न</button>
      </article>`;
    }).join("");

    const strongHtml = strong.length
      ? `<p class="good-note">मजबूत रहे: ${strong.map((t) => (GUIDE[t.topic] || {}).hi || t.topic).join(", ")}।</p>`
      : "";

    const sectionWarn = Object.entries(sc.sections).filter(([, s]) => s.total && s.correct / s.total < 0.45).map(([id, s]) => {
      const lang = id === "en" || id === "hi";
      const extra = lang
        ? " भाषा में 30% से कम आने पर मेरिट नहीं बनती, इसलिए यही भाग पहले पूरा करें।"
        : " यह भाग मेरिट के अंकों में गिना जाता है।";
      return `<article class="weak"><h3>${SECTIONS[id].hi} कमजोर है (${s.correct}/${s.total})</h3>
        <p>पूरे भाग की गति और सटीकता दोनों बढ़ाने के लिए अगला मॉक इसी भाग से शुरू करें।${extra}</p></article>`;
    }).join("");

    return sectionWarn + weakHtml + strongHtml;
  }

  $("view-result").addEventListener("click", (e) => {
    const b = e.target.closest("[data-drill]");
    if (!b) return;
    const [section, topic] = b.dataset.drill.split(":");
    startDrill(section, topic);
  });

  function startDrill(section, topic) {
    if (db.active && !confirm("अधूरी परीक्षा छोड़कर टॉपिक अभ्यास शुरू करें?")) return;
    const pool = [];
    DATA.sets.forEach((s) => s.questions.forEach((q) => {
      if (q.section === section && q.topic === topic) pool.push(q);
    }));
    if (pool.length < 5) {
      alert("इस टॉपिक में अभी पर्याप्त प्रश्न नहीं हैं।");
      return;
    }
    const rng = mulberry(Date.now() % 100000);
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      [pool[i], pool[j]] = [pool[j], pool[i]];
    }
    const picked = pool.slice(0, Math.min(20, pool.length));
    const g = GUIDE[topic] || { hi: topic };
    const active = {
      mode: "drill",
      setId: null,
      title: g.hi + " · अभ्यास",
      questionIds: picked.map((q) => q.id),
      name: db.profile.name || "अभ्यर्थी",
      roll: db.profile.roll || "—",
      started: Date.now(),
      deadline: Date.now() + 20 * 60 * 1000,
      index: 0,
      answers: {},
      marked: {},
      visited: { 0: true },
      rough: ""
    };
    db.active = active;
    save();
    enterExam();
  }

  function mulberry(seed) {
    let a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function openModal(html) {
    $("modal-root").innerHTML = `<div class="modal-back"><div class="modal">${html}</div></div>`;
  }
  function closeModal() { $("modal-root").innerHTML = ""; }

  function openRough() {
    openModal(`<h3>रफ कार्य</h3><textarea class="rough" id="rough-box">${escape(session.rough || "")}</textarea>
      <div class="actions"><button class="btn" id="rough-save" type="button">बंद करें</button></div>`);
    $("rough-box").value = session.rough || "";
    $("rough-save").onclick = () => {
      session.rough = $("rough-box").value;
      save();
      closeModal();
    };
  }

  window.addEventListener("beforeunload", (e) => {
    if (db.active) {
      e.preventDefault();
      e.returnValue = "";
    }
  });

  if (db.active) renderHome();
  else renderHome();
})();
