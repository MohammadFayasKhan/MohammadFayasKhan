#!/usr/bin/env python3
"""Generates animated light/dark SVG assets for the profile README (v2).
Run from the repo root: python generate_assets.py
Output: assets/*.svg (light) and assets/dark/*.svg (dark)"""
import os

W = 900
FONT = "'JetBrains Mono',SFMono-Regular,Consolas,monospace"
THEMES = {
    "light": dict(ink="#0d1117", mut="#57606a", line="#d0d7de", acc="#7C3AED", card="#f6f8fa", ok="#1a7f37"),
    "dark":  dict(ink="#e6edf3", mut="#8b949e", line="#30363d", acc="#A78BFA", card="#161b22", ok="#3fb950"),
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def svg(h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" '
            f'width="{W}" height="{h}" font-family="{FONT}">{body}</svg>')

def T(x, y, s, fill, size=13, w=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" '
            f'fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')

def G(delay, inner):
    return (f'<g opacity="0">{inner}<animate attributeName="opacity" from="0" to="1" '
            f'dur="0.6s" begin="{delay}s" fill="freeze"/></g>')

def box(x, y, w, h, c, r=10):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{c["card"]}" stroke="{c["line"]}"/>')

def chip(x, y, s, c, fill=None):
    w = len(s) * 6.8 + 18
    return (f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="22" rx="11" fill="none" stroke="{c["acc"]}"/>'
            + T(round(x + w / 2), y + 15, s, fill or c["acc"], 11, 700, "middle")), w

# ---------- section dividers ----------
def section(c, n, title):
    label = f"// {title}"
    cx = 58 + len(label) * 13.2 + 6
    body = G(0, T(0, 44, f"{n:02d}", c["acc"], 28, 700) + T(58, 44, label, c["ink"], 22, 700))
    body += (f'<rect x="{cx:.0f}" y="26" width="10" height="22" fill="{c["acc"]}">'
             f'<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    body += (f'<rect x="0" y="62" width="0" height="2" fill="{c["line"]}">'
             f'<animate attributeName="width" from="0" to="{W}" dur="1.2s" fill="freeze"/></rect>')
    body += (f'<rect x="0" y="62" width="0" height="2" fill="{c["acc"]}">'
             f'<animate attributeName="width" from="0" to="90" dur="0.8s" fill="freeze"/></rect>')
    return 72, body

# ---------- 01 whoami ----------
def whoami(c):
    lines = [
        ("cmd", "whoami"),
        ("out", "Mohammad Fayas Khan | Phagwara, Punjab, India"),
        ("cmd", "cat education.txt"),
        ("out", "B.Tech CSE @ Lovely Professional University | 2024 - 2028"),
        ("out", "CGPA 9.66 | University Honor Roll 2025 | AI/ML Minor"),
        ("cmd", "cat focus.txt"),
        ("out", "AI/ML engineer: computer vision, LLMs, agentic AI, RAG"),
        ("out", "builds: field rover robotics, browser agents, full-stack AI apps"),
        ("out", "principle: keep critical logic deterministic, outside the LLM"),
        ("cmd", "cat leadership.txt"),
        ("out", "Team Leader, Team Innovex: top 30 of 900+ hardware teams, GearUp S5"),
        ("cmd", "ls interests/"),
        ("out", "DSA in C++ (Striver A2Z) | open source (GSSoC '26) | IoT + embedded"),
        ("cmd", "status"),
        ("ok", "open to SWE internships, AI/ML roles, open source collabs"),
    ]
    h = 40 + len(lines) * 28 + 10
    body = box(0, 0, W, h, c)
    for i, (k, s) in enumerate(lines):
        y = 40 + i * 28
        if k == "cmd":
            inner = T(24, y, "$", c["acc"], 14, 700) + T(42, y, s, c["ink"], 14, 700)
        elif k == "out":
            inner = T(42, y, s, c["mut"], 14)
        else:
            inner = T(42, y, "✓ " + s, c["ok"], 14, 700)
        body += G(i * 0.3, inner)
    return h, body

# ---------- 02 system map ----------
def ecosystem(c):
    cols = [
        ("EDGE", ["ESP32-CAM Rover", "Sensors + 4-DOF Arm", "ESP8266 Nodes"]),
        ("MODELS", ["EfficientNetV2-S", "YOLO + Mobile-UNet", "RandomForest"]),
        ("BACKEND", ["FastAPI", "Pydantic Guardrails", "Groq + Gemini Chain"]),
        ("APPS", ["React Dashboards", "LPU UMS Agent", "Code Explain"]),
    ]
    xs = [0, 240, 480, 720]
    bw, bh = 180, 46
    ys = [50 + i * 70 for i in range(3)]
    body = ""
    def edge(x1, y1, x2, y2):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c["acc"]}" '
                f'stroke-width="1.5" stroke-dasharray="6 6" opacity="0.8">'
                f'<animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.5s" repeatCount="indefinite"/></line>')
    for k in range(3):
        for r in range(3):
            body += edge(xs[k] + bw, ys[r] + bh // 2, xs[k + 1], ys[r] + bh // 2)
    body += edge(xs[2] + bw, ys[0] + bh // 2, xs[3], ys[1] + bh // 2)
    body += edge(xs[2] + bw, ys[0] + bh // 2, xs[3], ys[2] + bh // 2)
    for k, (title, items) in enumerate(cols):
        inner = T(xs[k], 28, title, c["mut"], 12, 700)
        for r, it in enumerate(items):
            inner += box(xs[k], ys[r], bw, bh, c) + T(xs[k] + bw / 2, ys[r] + 28, it, c["ink"], 12, 700, "middle")
        body += G(k * 0.3, inner)
    return 270, body

# ---------- 03 projects ----------
def projects(c):
    items = [
        ("Crop Intelligence Rover", "Sep - Oct 2026", "Leaf disease detection + field risk monitoring",
         "EfficientNetV2-S, YOLO, Mobile-UNet, Grad-CAM", "ESP32 + ESP32-CAM rover, 4-DOF arm, XiaoZhi voice",
         ["95.13% acc", "0.9354 F1", "38 classes"]),
        ("LPU UMS Agent", "Aug - Oct 2026", "Agentic Chrome extension for live UMS sessions",
         "Attendance, exam date-sheet, seating plan automation", "Closed-loop agent, IndexedDB privacy, MV3",
         ["139 tests", "3-LLM chain", "3 workflows"]),
        ("Code Explain", "Jun - Jul 2026", "AI code tutor, live on Render",
         "Explanations, complexity analysis, traces, quizzes, chat", "Pydantic validation, self-repair, Groq + Gemini",
         ["5 endpoints", "3 models", "Docker"]),
        ("Smart Crop Intelligence", "CSE274", "IoT + ML precision agriculture, deployed",
         "RandomForest on sensor-only features, HF Spaces", "ESP8266 + DHT11 + rain + soil moisture sensing",
         ["93.18% acc", "27.6ms", "22 crops"]),
        ("CPU Sched", "Open source", "Interactive CPU scheduling simulator",
         "FCFS, SJF, SRTF, Round Robin, Priority + Gantt", "React 18, Vite, Zustand, pure scheduling functions",
         ["5 algorithms", "MIT", "Live"]),
        ("HomeKit Socket", "ESP8266", "On-chip Apple HomeKit server",
         "Full HAP server on-chip, no cloud or bridge", "Siri, iPhone, Watch, HomePod, active-LOW relay safety",
         ["80 lines", "C++", "0 cloud"]),
        ("Face Attendance", "Full stack", "Facial recognition + geotagging attendance",
         "dlib face recognition, real-time detection dashboard", "FastAPI, React, Tailwind CSS, SQLite",
         ["dlib", "Geotag", "Live"]),
        ("Hackathon Builds", "Web-A-Thon + AIESEC", "Budget Tracker + PC Building platform",
         "Budget Tracker for Students (ReactJS + NodeJS)", "Hack-A-Throne 1.0: PC building web frontend",
         ["React", "Node.js", "2 events"]),
    ]
    body = ""
    for i, (name, when, tag, d1, d2, chips) in enumerate(items):
        x, y = (i % 2) * 465, (i // 2) * 170
        inner = box(x, y, 435, 150, c)
        inner += T(x + 20, y + 34, name, c["ink"], 15, 700) + T(x + 415, y + 34, when, c["mut"], 11, 400, "end")
        inner += T(x + 20, y + 56, tag, c["acc"], 12, 700)
        inner += T(x + 20, y + 80, d1, c["mut"], 11) + T(x + 20, y + 98, d2, c["mut"], 11)
        cx = x + 20
        for s in chips:
            ch, w = chip(cx, y + 112, s, c)
            inner += ch
            cx += w + 8
        body += G(i * 0.2, inner)
    return 4 * 170 - 20, body

# ---------- 04 deep dives (animated flow diagrams) ----------
def flow(c, title, steps, notes):
    n = len(steps)
    gap = 28
    bw = (W - gap * (n - 1)) / n
    y, bh = 54, 66
    body = T(0, 26, title, c["acc"], 13, 700)
    for i, (lab, sub) in enumerate(steps):
        x = i * (bw + gap)
        inner = box(f"{x:.0f}", y, f"{bw:.0f}", bh, c)
        inner += T(f"{x + bw / 2:.0f}", y + 28, lab, c["ink"], 12, 700, "middle")
        inner += T(f"{x + bw / 2:.0f}", y + 48, sub, c["mut"], 10, 400, "middle")
        body += G(i * 0.25, inner)
        if i < n - 1:
            x1, x2, ym = x + bw, x + bw + gap, y + bh / 2
            body += (f'<line x1="{x1:.0f}" y1="{ym}" x2="{x2:.0f}" y2="{ym}" stroke="{c["line"]}" stroke-width="2"/>'
                     f'<circle r="3.5" fill="{c["acc"]}"><animateMotion dur="1.6s" begin="{i * 0.3}s" '
                     f'repeatCount="indefinite" path="M {x1:.0f} {ym} L {x2:.0f} {ym}"/></circle>')
    for j, line in enumerate(notes):
        body += G(1.5 + j * 0.3, T(0, 152 + j * 20, "▸ " + line, c["mut"], 12))
    return 152 + len(notes) * 20 + 4, body

def rover(c):
    return flow(c, "// ROVER | inference pipeline", [
        ("ESP32-CAM", "capture + sensors"), ("EfficientNetV2-S", "38-class classify"),
        ("YOLO", "lesion detection"), ("Mobile-UNet", "leaf segmentation"),
        ("Grad-CAM", "why it flagged"), ("Dashboard", "FastAPI + React")],
        ["~54K training images | 95.13% test accuracy | 0.9354 macro F1",
         "4-DOF arm for close-up inspection | XiaoZhi voice-based field interaction",
         "field-risk insights fuse image predictions with live sensor telemetry"])

def agent(c):
    return flow(c, "// UMS AGENT | closed-loop control", [
        ("Observe", "DOM-first extract"), ("Ground", "IoU + text sim"),
        ("Act", "browser action"), ("Re-observe", "read page again"),
        ("Verify", "discrepancy check"), ("Report", "deterministic math")],
        ["human-controlled CAPTCHA and security steps | no credential or cookie handling",
         "attendance calculations stay deterministic and outside the LLM",
         "IndexedDB local-first storage | stateless FastAPI | 139 automated tests"])

def gateway(c):
    return flow(c, "// CODE EXPLAIN | LLM gateway", [
        ("Request", "React + Monaco"), ("Validate", "Pydantic schema"),
        ("Route", "provider layer"), ("Groq + Gemini", "3 models"),
        ("Self-repair", "one-shot fix"), ("Response", "stateless API")],
        ["automatic fallback across 3 models with exponential-backoff retries",
         "5 FastAPI endpoints: explain, commentary, complexity, traces, quizzes + chat",
         "multi-stage Docker build | live on Render | client-side history"])

# ---------- 05 telemetry ----------
def telemetry(c):
    tiles = [
        ("9.66", "CGPA | Honor Roll"), ("95.13%", "leaf classifier acc"),
        ("0.9354", "macro F1 score"), ("~54K", "training images"),
        ("139", "automated tests"), ("3", "LLM fallback chain"),
        ("Top 30", "of 900+ teams"), ("50 hrs", "LLM + agentic AI"),
    ]
    body = ""
    for i, (num, label) in enumerate(tiles):
        x, y = (i % 4) * 230, (i // 4) * 112
        inner = box(x, y, 210, 92, c)
        inner += T(x + 18, y + 44, num, c["acc"], 28, 700)
        inner += T(x + 18, y + 70, label, c["mut"], 11)
        body += G(i * 0.15, inner)
    return 204, body

# ---------- 06 the route ----------
def route(c):
    ms = [
        ("Aug 2024", "Joined LPU, B.Tech CSE"), ("Aug 2025", "OCI AI Foundations"),
        ("Nov 2025", "University Honor Roll"), ("Dec 2025", "NASSCOM ML + Imaging"),
        ("Jun 2026", "AI Engineer Launchpad"), ("Jul 2026", "Code Explain shipped"),
        ("Aug 2026", "LPU UMS Agent"), ("Sep 2026", "GearUp Top 30 + Oracle AI"),
        ("Oct 2026", "Crop Intelligence Rover"),
    ]
    body = f'<line x1="20" y1="110" x2="880" y2="110" stroke="{c["line"]}" stroke-width="2"/>'
    body += (f'<line x1="20" y1="110" x2="20" y2="110" stroke="{c["acc"]}" stroke-width="2">'
             f'<animate attributeName="x2" from="20" to="880" dur="3s" fill="freeze"/></line>')
    for i, (d, lab) in enumerate(ms):
        x = 80 + i * 92
        up = i % 2 == 0
        inner = f'<circle cx="{x}" cy="110" r="6" fill="{c["acc"]}"/>'
        inner += (f'<circle cx="{x}" cy="110" r="6" fill="none" stroke="{c["acc"]}">'
                  f'<animate attributeName="r" from="6" to="16" dur="2s" repeatCount="indefinite"/>'
                  f'<animate attributeName="opacity" from="0.6" to="0" dur="2s" repeatCount="indefinite"/></circle>')
        if up:
            inner += f'<line x1="{x}" y1="104" x2="{x}" y2="88" stroke="{c["line"]}"/>'
            inner += T(x, 62, d, c["acc"], 12, 700, "middle") + T(x, 80, lab, c["ink"], 11, 400, "middle")
        else:
            inner += f'<line x1="{x}" y1="116" x2="{x}" y2="132" stroke="{c["line"]}"/>'
            inner += T(x, 152, d, c["acc"], 12, 700, "middle") + T(x, 170, lab, c["ink"], 11, 400, "middle")
        body += G(i * 0.3, inner)
    return 196, body

# ---------- 07 credentials ----------
def credentials(c):
    certs = [
        ("ORACLE", "Agentic AI Certified", "Foundations Associate", "Sep 2026"),
        ("NASSCOM FOUNDATION", "Machine Learning and", "Image Processing", "Dec 2025"),
        ("ORACLE", "OCI 2025 Certified AI", "Foundations Associate", "Aug 2025"),
    ]
    body = ""
    for i, (org, l1, l2, d) in enumerate(certs):
        x = i * 310
        inner = box(x, 0, 280, 110, c)
        inner += T(x + 20, 28, org, c["mut"], 11, 700) + T(x + 260, 28, d, c["acc"], 11, 700, "end")
        inner += T(x + 20, 62, l1, c["ink"], 14, 700) + T(x + 20, 82, l2, c["ink"], 14, 700)
        body += G(i * 0.25, inner)
    rows = [
        ("Jun - Jul 2026", "AI Engineer Launchpad | LPU", "50 hrs, 5 weeks: LLMs, RAG, tool calling, LoRA/QLoRA, guardrails"),
        ("Sep 2026", "Team Leader, Team Innovex | GearUp S5", "top 30 hardware teams out of 900+ participants"),
        ("Nov 2025", "University Honor Roll 2025 | LPU", "academic session 2023-24, current CGPA 9.66 / 10"),
        ("2026", "Open Source Contributor | GSSoC '26", "GirlScript Summer of Code, open source track"),
        ("2025", "JPMorgan Chase Code For Good", "HackerRank round cleared, HireVue invitation received"),
    ]
    for i, (when, role, desc) in enumerate(rows):
        y = 134 + i * 66
        inner = box(0, y, W, 56, c)
        inner += T(24, y + 34, when, c["acc"], 12, 700)
        inner += T(200, y + 25, role, c["ink"], 13, 700) + T(200, y + 44, desc, c["mut"], 11)
        body += G(0.8 + i * 0.25, inner)
    return 134 + 5 * 66 - 10, body

def academics(c):
    sems = [("SEM 1", 9.55, "Python, Computing, Engineering Maths"),
            ("SEM 2", 9.63, "DBMS, Software Eng, Programming, Discrete"),
            ("SEM 3", 9.76, "OOP, DSA, Networks, Probability + Stats"),
            ("SEM 4", 9.72, "OS, DAA, Theory of Computation, COA"),
            ("CGPA", 9.66, "University Honor Roll | AI/ML Minor")]
    body = T(0, 14, "TGPA (bar scale 8.0 to 10.0)", c["mut"], 11, 700)
    for i, (lab, v, subj) in enumerate(sems):
        y = 30 + i * 38
        wbar = (v - 8) / 2 * 400
        inner = T(0, y + 18, lab, c["acc"] if lab == "CGPA" else c["ink"], 12, 700)
        inner += f'<rect x="70" y="{y + 4}" width="400" height="18" rx="9" fill="{c["card"]}" stroke="{c["line"]}"/>'
        inner += (f'<rect x="70" y="{y + 4}" width="0" height="18" rx="9" fill="{c["acc"]}">'
                  f'<animate attributeName="width" from="0" to="{wbar:.0f}" dur="1.2s" begin="{i * 0.2}s" fill="freeze"/></rect>')
        inner += T(488, y + 18, f"{v:.2f}", c["ink"], 13, 700) + T(550, y + 18, subj, c["mut"], 11)
        body += G(i * 0.2, inner)
    edu = [
        ("Lovely Professional University", "B.Tech CSE | 2024 - 2028", "CGPA 9.66 | Phagwara, Punjab"),
        ("Sri Chaitanya", "Intermediate (Science) | 2022 - 2024", "95.7% | Vijayawada, Andhra Pradesh"),
        ("Komma Reddy High School", "Matriculation | 2021 - 2022", "95.6% | Bantumilli, Andhra Pradesh"),
    ]
    for i, (n, l1, l2) in enumerate(edu):
        x = i * 310
        inner = box(x, 240, 280, 86, c)
        inner += T(x + 20, 268, n, c["ink"], 13, 700) + T(x + 20, 290, l1, c["acc"], 11, 700) + T(x + 20, 308, l2, c["mut"], 11)
        body += G(1.2 + i * 0.25, inner)
    return 330, body

# ---------- 08 stack ----------
def stack(c):
    groups = [
        ("LANGUAGES", ["C++", "Python", "C", "Java", "JavaScript", "TypeScript", "SQL"]),
        ("AI / ML", ["PyTorch", "scikit-learn", "OpenCV", "YOLO", "EfficientNetV2", "Grad-CAM", "Hugging Face", "Pandas", "NumPy"]),
        ("AGENTIC AI", ["LangChain", "LangGraph", "RAG", "Tool Calling", "LoRA/QLoRA", "Structured Outputs", "Guardrails", "LLM Evals"]),
        ("WEB", ["React", "Vite", "Tailwind", "FastAPI", "Pydantic", "Node.js", "Express", "Chrome MV3"]),
        ("DATA", ["PostgreSQL", "MySQL", "SQLite", "Firebase", "Supabase", "IndexedDB"]),
        ("ROBOTICS / IoT", ["ESP32", "ESP32-CAM", "ESP8266", "Arduino", "Blynk", "Sensors"]),
        ("CORE CS", ["DSA", "OOP", "DBMS", "OS", "Networks", "DAA"]),
        ("DEVOPS", ["Docker", "Git", "GitHub", "Linux", "Vercel", "Render", "Selenium"]),
    ]
    y = 10
    body = ""
    for gi, (label, items) in enumerate(groups):
        y0, x = y, 170
        inner = T(0, y0 + 19, label, c["acc"], 12, 700)
        for it in items:
            w = len(it) * 7.4 + 22
            if x + w > W:
                x, y = 170, y + 36
            inner += (f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="28" rx="14" '
                      f'fill="{c["card"]}" stroke="{c["line"]}"/>')
            inner += T(round(x + w / 2), y + 19, it, c["ink"], 12, 400, "middle")
            x += w + 8
        body += G(gi * 0.2, inner)
        y += 52
    return y, body

# ---------- 09 roadmap ----------
def roadmap(c):
    cols = [
        ("BUILDING", ["Crop Intelligence Rover polish", "Agentic tools with guardrails", "GSSoC '26 contributions", "C++ DSA, Striver A2Z roadmap"]),
        ("SEEKING", ["Product-company SWE internships", "AI/ML engineer roles", "Open source collaborations", "Deployed end-to-end AI projects"]),
        ("TARGET", ["200+ cold-solved DSA problems", "by Semester 6", "25-minute attempt rule first", "Production-grade AI systems"]),
    ]
    body = ""
    for i, (title, items) in enumerate(cols):
        x = i * 310
        inner = box(x, 0, 280, 180, c) + T(x + 20, 36, title, c["acc"], 14, 700)
        inner += f'<rect x="{x + 20}" y="46" width="40" height="2" fill="{c["acc"]}"/>'
        for j, it in enumerate(items):
            inner += T(x + 20, 80 + j * 28, "▸ " + it, c["ink"], 12)
        body += G(i * 0.3, inner)
    return 180, body

# ---------- status footer ----------
def status(c):
    body = box(0, 0, W, 120, c)
    body += (f'<circle cx="30" cy="34" r="5" fill="{c["ok"]}"/>'
             f'<circle cx="30" cy="34" r="5" fill="none" stroke="{c["ok"]}">'
             f'<animate attributeName="r" from="5" to="14" dur="1.6s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" from="0.7" to="0" dur="1.6s" repeatCount="indefinite"/></circle>')
    body += T(52, 39, "CURRENT STATUS", c["mut"], 12, 700)
    body += T(24, 72, "building: AI Powered Crop Intelligence Rover + agentic tools", c["ink"], 15, 700)
    body += T(24, 98, "open to: SWE internships  |  AI/ML roles  |  open source", c["acc"], 13, 700)
    return 120, body

SECTIONS = [(1, "whoami"), (2, "system map"), (3, "projects"), (4, "deep dives"), (5, "telemetry"),
            (6, "the route"), (7, "credentials"), (8, "stack"), (9, "roadmap")]
ASSETS = {f"s{n:02d}": (lambda c, n=n, t=t: section(c, n, t)) for n, t in SECTIONS}
ASSETS.update(whoami=whoami, ecosystem=ecosystem, projects=projects, rover=rover, agent=agent,
              gateway=gateway, telemetry=telemetry, timeline=route, credentials=credentials,
              academics=academics, stack=stack, roadmap=roadmap, footer=status)

if __name__ == "__main__":
    os.makedirs("assets/dark", exist_ok=True)
    for name, fn in ASSETS.items():
        for mode, folder in (("light", "assets"), ("dark", "assets/dark")):
            h, body = fn(THEMES[mode])
            with open(f"{folder}/{name}.svg", "w", encoding="utf-8") as f:
                f.write(svg(h, body))
    print(f"generated {len(ASSETS) * 2} svgs")
