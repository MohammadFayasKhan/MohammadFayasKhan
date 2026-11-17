from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]


def t(x, y, value, size=13, color="bone", weight="400", anchor="start", spacing=None, cls="rise", length=None):
    attrs = [f'x="{x}"', f'y="{y}"', f'font-size="{size}"', f'fill="var(--{color})"']
    if weight != "400":
        attrs.append(f'font-weight="{weight}"')
    if anchor != "start":
        attrs.append(f'text-anchor="{anchor}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    if length:
        attrs.append(f'textLength="{length}" lengthAdjust="spacingAndGlyphs"')
    if cls:
        attrs.append(f'class="mono {cls}"')
    else:
        attrs.append('class="mono"')
    return f'<text {" ".join(attrs)}>{escape(value)}</text>'


def frame(title, width, height, body, dark=False):
    if dark:
        colors = ("#DDDDDD", "#777777", "#666666", "#444444", "#AAAAAA", "#1A1A1A", "#222222")
    else:
        colors = ("#444444", "#888888", "#AAAAAA", "#C0C0C0", "#555555", "#F0F0F0", "#E8E8E8")
    bone, muted, dim, rule, accent, node, core = colors
    return f"""<svg viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(title)}">
<style>
:root{{--bone:{bone};--muted:{muted};--dim:{dim};--rule:{rule};--accent:{accent};--node:{node};--core:{core}}}
.mono{{font-family:ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,"Liberation Mono",monospace}}
.card{{fill:var(--node);stroke:var(--rule);stroke-width:1}}
.soft{{fill:var(--core);stroke:var(--rule);stroke-width:1}}
.gridline{{stroke:var(--rule);stroke-width:1;opacity:.32}}
.bar{{stroke:var(--accent);stroke-width:3;stroke-linecap:round}}
.dot{{fill:var(--accent)}}
.rise{{opacity:1;animation:rise .7s cubic-bezier(.2,.7,.2,1) forwards}}
.r1{{animation-delay:.1s}}.r2{{animation-delay:.2s}}.r3{{animation-delay:.3s}}.r4{{animation-delay:.4s}}.r5{{animation-delay:.5s}}.r6{{animation-delay:.6s}}.r7{{animation-delay:.7s}}.r8{{animation-delay:.8s}}.r9{{animation-delay:.9s}}.r10{{animation-delay:1s}}
.draw{{stroke-dasharray:1200;stroke-dashoffset:1200;animation:draw 1.5s cubic-bezier(.6,0,.2,1) forwards}}
.wire{{stroke:var(--rule);stroke-width:1;stroke-dasharray:500;stroke-dashoffset:500;animation:draw 1.4s cubic-bezier(.6,0,.2,1) forwards}}
.pulse{{animation:pulse 2.4s ease-in-out infinite}}
.ring{{animation:ring 2.4s ease-out infinite;transform-origin:60px 64px}}
.blink{{animation:blink 1.1s steps(2,end) infinite}}
.scan{{animation:scan 4s ease-in-out infinite}}
.float{{animation:float 3.2s ease-in-out infinite}}
@keyframes rise{{from{{transform:translateY(8px)}}to{{transform:translateY(0)}}}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
@keyframes ring{{0%{{transform:scale(.4);opacity:.8}}80%,100%{{transform:scale(2.6);opacity:0}}}}
@keyframes blink{{0%,45%{{opacity:1}}46%,100%{{opacity:0}}}}
@keyframes scan{{0%{{transform:translateX(0);opacity:.15}}50%{{opacity:.8}}100%{{transform:translateX(900px);opacity:.15}}}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
@media(prefers-reduced-motion:reduce){{.rise,.draw,.wire,.pulse,.ring,.blink,.scan,.float{{animation:none;opacity:1;stroke-dashoffset:0}}}}
</style>
<title>{escape(title)}</title>
<g>{body}</g>
</svg>"""


def save_pair(name, title, width, height, body):
    for dark in (False, True):
        path = ROOT / ("assets/dark" if dark else "assets") / name
        path.write_text(frame(title, width, height, body, dark), encoding="utf-8")


def heading(label, right):
    return (
        t(48, 34, label, 11, "muted", spacing="3", cls="")
        + t(952, 34, right, 11, "accent", anchor="end", spacing="1", cls="")
        + '<line class="draw" x1="48" y1="52" x2="952" y2="52"/>'
    )


def divider(number, label, route):
    body = (
        t(48, 58, number, 42, "bone", cls="")
        + t(116, 56, label, 11, "muted", spacing="3", cls="")
        + t(952, 56, route, 10, "accent", anchor="end", spacing="2", cls="")
        + '<line class="draw" x1="238" y1="48" x2="900" y2="48"/>'
    )
    save_pair(f"s{number}.svg", f"Section {number} — {label}", 1000, 92, body)


for number, label, route in [
    ("01", "WHOAMI", "~/01-whoami"),
    ("02", "SYSTEM MAP", "~/02-system-map"),
    ("03", "PROJECTS", "~/03-projects"),
    ("04", "TELEMETRY", "~/04-telemetry"),
    ("05", "THE ROUTE", "~/05-the-route"),
    ("06", "STACK", "~/06-stack"),
]:
    divider(number, label, route)


header = (
    '<rect class="soft" x="28" y="20" width="944" height="372" rx="4"/>'
    + t(48, 44, "PORTFOLIO — INDEX Nº 001", 11, "muted", spacing="3", cls="")
    + t(952, 44, "PHAGWARA, IN — 31.25° N", 11, "muted", anchor="end", spacing="3", cls="")
    + '<line class="scan" x1="48" y1="76" x2="48" y2="330" stroke="var(--accent)" stroke-width="1"/>'
    + t(46, 176, "Mohammad Fayas Khan", 62, "bone", weight="700", spacing="-2", cls="rise r1", length=900)
    + '<rect class="blink" x="952" y="130" width="7" height="46" fill="var(--accent)"/>'
    + t(48, 214, "CSE Student & Applied AI Builder — Phagwara, India.", 19, "muted", cls="rise r2")
    + t(48, 274, "focus  ▸", 12, "dim", spacing="1", cls="rise r3")
    + t(128, 274, "AI/ML · computer vision · LLM systems · backend · IoT", 12, "accent", spacing="1", cls="rise r3")
    + t(48, 300, "building practical systems with software, models, automation and hardware", 12, "dim", spacing="1", cls="rise r4")
    + '<line class="draw" x1="48" y1="342" x2="952" y2="342"/>'
    + t(48, 374, "B.TECH CSE @ LPU · GRADUATING 2028", 11, "muted", spacing="3", cls="rise r5")
    + t(952, 374, "TEAM INNOVEX · OPEN TO COLLABORATION", 11, "muted", anchor="end", spacing="2", cls="rise r5")
)
save_pair("header-v1.svg", "Mohammad Fayas Khan — CSE student and applied AI builder", 1000, 400, header)


whoami = (
    t(48, 32, "B.Tech Computer Science and Engineering student at Lovely Professional University.", 16, cls="r1")
    + t(48, 60, "building practical systems where AI, software, automation and hardware meet.", 16, cls="r2")
    + t(48, 88, "interested in models that become useful products: APIs, interfaces, devices and feedback loops.", 15, "muted", cls="r3")
    + '<line class="rise r4" x1="48" y1="116" x2="952" y2="116"/>'
    + t(48, 148, "FOCUS", 11, "muted", spacing="2", cls="r4")
    + t(154, 148, "Applied AI/ML · computer vision · LLMs and agents · backend engineering · IoT", 14, cls="r4")
    + t(48, 182, "FOUNDATION", 11, "muted", spacing="2", cls="r5")
    + t(154, 182, "AI/ML minor · C++ DSA · competitive programming · software fundamentals", 14, cls="r5")
    + t(48, 216, "NOW", 11, "muted", spacing="2", cls="r6")
    + t(154, 216, "Team Innovex · hackathon systems · transparent evaluation · continuous learning", 14, "accent", cls="r6")
)
save_pair("whoami.svg", "whoami — identity, focus and foundations", 1000, 236, whoami)


ecosystem = (
    heading("SYSTEM MAP", "ONE PIPELINE / MANY LAYERS")
    + t(48, 84, "FAYAS.SYS", 16, "bone", weight="700", spacing="2", cls="r1")
    + t(48, 108, "sense signals · frame context · validate decisions · serve people · learn from reality", 12, "muted", cls="r1")
    + '<line class="wire" x1="500" y1="126" x2="500" y2="590"/>'
    + '<line class="wire" x1="160" y1="198" x2="840" y2="198"/>'
    + '<line class="wire" x1="160" y1="338" x2="840" y2="338"/>'
    + '<line class="wire" x1="160" y1="478" x2="840" y2="478"/>'
)
nodes = [
    (80, 156, "SIGNAL", "cameras · sensors"),
    (380, 156, "CONTEXT", "DOM · telemetry"),
    (680, 156, "DATA", "datasets · evidence"),
    (80, 296, "INFER", "ML · vision · LLM"),
    (380, 296, "GROUND", "retrieval · rules"),
    (680, 296, "EXPLAIN", "metrics · traces"),
    (80, 436, "SERVE", "FastAPI · APIs"),
    (380, 436, "SHIP", "React · MV3 · Docker"),
    (680, 436, "DEVICE", "ESP32 · IoT"),
]
for i, (x, y, name, desc) in enumerate(nodes, 1):
    ecosystem += f'<rect class="rise r{i}" x="{x}" y="{y}" width="240" height="70" fill="var(--node)" stroke="var(--rule)"/>'
    ecosystem += t(x + 18, y + 28, name, 13, "bone", weight="700", spacing="1", cls=f"r{i}")
    ecosystem += t(x + 18, y + 51, desc, 11, "muted", cls=f"r{i}")
ecosystem += '<rect x="370" y="516" width="260" height="48" fill="var(--core)" stroke="var(--accent)"/>'
ecosystem += '<circle class="ring" style="transform-origin:500px 540px" cx="500" cy="540" r="18" stroke="var(--accent)" fill="none"/>'
ecosystem += '<circle class="pulse" cx="500" cy="540" r="5" fill="var(--accent)"/>'
ecosystem += t(500, 538, "PRACTICAL SYSTEMS", 12, "bone", weight="700", anchor="middle", spacing="2", cls="r10")
ecosystem += t(500, 592, "BUILD → TEST → EXPLAIN → SHIP → OBSERVE", 11, "accent", anchor="middle", spacing="2", cls="r10")
save_pair("ecosystem.svg", "System map — AI, software and hardware ecosystem", 1000, 620, ecosystem)


project_rows = [
    ("01", "AGRIROVER / SMARTCROPVISION", "SIH26180 · Team Innovex · AI smart farming assistant", "Random Forest crop recommendation · 2,200 records · 22 classes", "Lab 99.01% acc / 98.74% bal acc / 98.58% F1 · field 47.46% acc", "ACTIVE"),
    ("02", "LPU AGENT", "Student assistant · UMS workflows · active development", "Playwright · Chrome extension architecture · manual authentication", "IndexedDB local-first history · Cloudflare verification remains user-controlled", "WIP"),
    ("03", "CODEEXPLAIN", "Plain-English code tutor for programming education", "React · TypeScript · Monaco · FastAPI · Pydantic", "Uvicorn · HTTPX · Tailwind · Framer Motion · Render", "BUILT"),
    ("04", "FAYASAI", "ESP32 voice assistant with an animated OLED interface", "C++ · ESP32 · Groq Whisper STT · Llama response loop", "Embedded AI exploration · active development", "WIP"),
    ("05", "CPUSCHED", "Interactive CPU scheduling simulator", "React · Vite · Tailwind · Zustand · Gantt visualisation", "FCFS · SJF · SRTF · Round Robin · Priority", "TEAM"),
    ("06", "ESPBOT", "ESP8266 Wi-Fi robot with browser control panel", "C++ · ESP8266 · responsive controls · robotics", "Open-source hardware and software exploration", "BUILD"),
    ("07", "JOY MOUSE", "Joystick-controlled desktop pointing device", "Arduino Nano · Python · serial communication · signal filtering", "Dead-zone handling · acceleration · human-interface experiment", "BUILD"),
    ("08", "SMART HOME SOCKET", "Cloud-free ESP8266 home automation socket", "C++ · ESP8266 · HomeKit Accessory Protocol · relay control", "Active-LOW safety state · device-first integration", "WIP"),
]
projects = heading("PROJECTS", "SELECTED BUILDS / OUTCOMES / ENGINEERING CHOICES")
projects += '<line class="scan" x1="48" y1="66" x2="48" y2="990" stroke="var(--accent)" stroke-width="1" opacity=".35"/>'
for i, (num, title, line1, line2, line3, status) in enumerate(project_rows, 1):
    y = 82 + (i - 1) * 114
    projects += f'<rect class="card rise r{i}" x="48" y="{y - 20}" width="904" height="96" rx="3"/>'
    projects += t(70, y + 8, f"{num}", 12, "accent", weight="700", spacing="1", cls=f"r{i}")
    projects += t(116, y + 8, title, 16, "bone", weight="700", spacing=".7", cls=f"r{i}")
    projects += t(930, y + 8, status, 10, "muted", anchor="end", spacing="2", cls=f"r{i}")
    projects += t(116, y + 32, line1, 12, cls=f"r{i}")
    projects += t(116, y + 52, line2, 11, "muted", cls=f"r{i}")
    projects += t(116, y + 72, line3, 11, "accent", spacing=".2", cls=f"r{i}")
    projects += f'<circle class="pulse dot r{i}" cx="76" cy="{y + 3}" r="3"/>'
save_pair("projects.svg", "Selected projects by Mohammad Fayas Khan", 1000, 1040, projects)


links = heading("PROJECT LINKS", "REPOSITORIES / DECISIONS / STATUS")
links += t(48, 82, "SYSTEM", 10, "muted", spacing="2", cls="")
links += t(390, 82, "PROOF / DECISION", 10, "muted", spacing="2", cls="")
links += t(952, 82, "SURFACE", 10, "muted", anchor="end", spacing="2", cls="")
link_rows = [
    ("AGRIROVER", "lab vs field evaluation · proposed edge pipeline", "REPO"),
    ("LPU AGENT", "manual auth · local-first persistence · WIP", "REPO"),
    ("CODEEXPLAIN", "education · validated API contracts · Render", "REPO"),
    ("FAYASAI", "embedded voice loop · OLED interface · WIP", "REPO"),
    ("CPUSCHED", "algorithm visualisation · team build", "REPO"),
    ("ESPBOT", "Wi-Fi robotics · browser controls", "REPO"),
    ("JOY MOUSE", "serial input · filtering · acceleration", "REPO"),
    ("SMART HOME", "on-device HAP · active-LOW relay safety", "REPO"),
]
for i, (name, proof, surface) in enumerate(link_rows, 1):
    y = 114 + (i - 1) * 42
    links += f'<rect class="rise r{i}" x="48" y="{y - 19}" width="904" height="30" fill="var(--node)" opacity=".55"/>'
    links += t(48, y, name, 11, cls=f"r{i}")
    links += t(390, y, proof, 11, "muted", cls=f"r{i}")
    links += t(952, y, surface, 10, "accent", anchor="end", spacing="1", cls=f"r{i}")
links += '<line class="draw" x1="48" y1="462" x2="952" y2="462"/>'
links += t(48, 492, "ENGINEERING DECISIONS", 10, "muted", spacing="2", cls="r8")
links += t(48, 518, "transparent evaluation · deterministic rules · validated contracts · local-first privacy", 12, cls="r8")
links += t(48, 542, "sensor-measurable features · user-controlled auth · observable interfaces", 12, "muted", cls="r9")
save_pair("project-links.svg", "Project links and engineering decisions", 1000, 560, links)


telemetry = heading("TELEMETRY", "WHAT THE ACCOUNT SHOWS")
telemetry += t(48, 82, "REPOSITORY SIGNALS", 11, "muted", spacing="2", cls="r1")
telemetry += t(48, 108, "LANGUAGES / ACTIVITY / LEARNING", 14, "bone", weight="700", cls="r1")
for i, label in enumerate(["PYTHON + NOTEBOOKS", "JAVASCRIPT + TYPESCRIPT", "C + C++ + EMBEDDED", "HTML + CSS + OTHER"], 1):
    y = 140 + (i - 1) * 29
    telemetry += t(48, y, label, 11, cls=f"r{i}")
    telemetry += f'<line class="rise r{i}" x1="250" y1="{y - 4}" x2="480" y2="{y - 4}" stroke="var(--rule)"/>'
    telemetry += f'<circle class="rise r{i}" cx="{270 + i * 42}" cy="{y - 4}" r="3" fill="var(--accent)"/>'
telemetry += t(570, 82, "ACTIVITY", 11, "muted", spacing="2", cls="r5")
telemetry += t(570, 108, "CONTRIBUTION TELEMETRY", 14, "bone", weight="700", cls="r5")
telemetry += '<polyline class="draw" points="570,220 620,190 670,204 720,150 770,178 820,122 870,145 920,96" fill="none" stroke="var(--accent)" stroke-width="2"/>'
for i, x in enumerate([570, 620, 670, 720, 770, 820, 870, 920], 1):
    telemetry += f'<circle class="pulse" cx="{x}" cy="{220 - [0,30,16,70,42,98,75,124][i-1]}" r="3" fill="var(--accent)"/>'
telemetry += t(570, 250, "LIVE CONTRIBUTION GRAPH RENDERED BELOW", 11, "muted", cls="r9")
telemetry += t(48, 270, "No hardcoded percentages, streaks, stars or solve counts.", 10, "accent", spacing="1", cls="r10")
save_pair("telemetry.svg", "GitHub development telemetry", 1000, 300, telemetry)


stats = (
    '<rect x="24" y="20" width="456" height="270" fill="none" stroke="var(--rule)"/>'
    '<rect x="520" y="20" width="456" height="270" fill="none" stroke="var(--rule)"/>'
    + t(52, 58, "PROFILE METRICS", 15, weight="700", spacing="2", cls="r1")
    + t(52, 96, "LATEST RECORDED TGPA", 11, "muted", spacing="1", cls="r2")
    + t(452, 98, "9.76", 18, "accent", weight="700", anchor="end", cls="r2")
    + t(52, 136, "CSE RANK IN TGPA", 11, "muted", spacing="1", cls="r3")
    + t(452, 138, "14TH", 18, "accent", weight="700", anchor="end", cls="r3")
    + t(52, 176, "GRADUATION TARGET", 11, "muted", spacing="1", cls="r4")
    + t(452, 178, "2028", 18, "accent", weight="700", anchor="end", cls="r4")
    + t(52, 226, "GITHUB ACCOUNT", 11, "muted", spacing="1", cls="r5")
    + t(52, 252, "MohammadFayasKhan", 15, weight="700", cls="r5")
    + t(548, 58, "LANGUAGES / ACTIVITY", 15, weight="700", spacing="2", cls="r6")
    + t(548, 104, "LIVE PROFILE GRAPH BELOW", 12, "accent", weight="700", cls="r7")
    + t(548, 140, "Repository language views and contribution", 13, cls="r8")
    + t(548, 164, "activity use the GitHub account directly.", 13, cls="r8")
    + t(548, 212, "No hardcoded stars, streaks or solve counts.", 12, "muted", cls="r9")
)
save_pair("github-stats.svg", "Profile metrics and repository languages", 1000, 310, stats)


timeline = (
    '<line class="draw" x1="70" y1="126" x2="1130" y2="126"/>'
    + t(70, 52, "2024", 12, "accent", cls="r1")
    + t(70, 82, "LPU BEGINS", 13, weight="700", cls="r1")
    + t(70, 170, "B.Tech CSE · foundations", 11, "muted", cls="r1")
    + t(270, 52, "2025", 12, "accent", cls="r2")
    + t(270, 82, "SYSTEMS", 13, weight="700", cls="r2")
    + t(270, 170, "IoT · web · ML projects", 11, "muted", cls="r2")
    + t(490, 52, "2026", 12, "accent", cls="r3")
    + t(490, 82, "TEAM INNOVEX", 13, weight="700", cls="r3")
    + t(490, 170, "GearUp selection · SIH work", 11, "muted", cls="r3")
    + t(710, 52, "2026", 12, "accent", cls="r4")
    + t(710, 82, "AI SYSTEMS", 13, weight="700", cls="r4")
    + t(710, 170, "AgriRover · LPU Agent · CodeExplain", 11, "muted", cls="r4")
    + t(930, 52, "NOW", 12, "accent", cls="r5")
    + t(930, 82, "NEXT ITERATION", 13, weight="700", cls="r5")
    + t(930, 170, "C++ DSA · backend · AI engineering", 11, "muted", cls="r5")
)
for x in [70, 270, 490, 710, 930]:
    timeline += f'<circle class="rise r5" cx="{x}" cy="126" r="5" fill="var(--accent)"/>'
timeline += '<circle class="ring" style="transform-origin:930px 126px" cx="930" cy="126" r="10" stroke="var(--accent)" fill="none"/>'
save_pair("timeline.svg", "Academic and technical development route", 1200, 220, timeline)


experience = (
    '<line x1="120" y1="10" x2="120" y2="360" stroke="var(--rule)" opacity=".4"/>'
    + t(48, 42, "2026", 12, "accent", spacing="2", cls="r1")
    + t(136, 42, "TEAM INNOVEX · TECHNICAL TEAM LEAD", 15, cls="r1")
    + t(136, 68, "AI, IoT and hardware-oriented development for hackathon systems.", 13, "muted", cls="r1")
    + t(136, 92, "LPU GearUp Season 5 selection · SIH26180 preparation.", 12, cls="r1")
    + t(48, 142, "2026", 12, "accent", spacing="2", cls="r2")
    + t(136, 142, "PROJECT ENGINEERING · APPLIED AI", 15, cls="r2")
    + t(136, 168, "AgriRover, LPU Agent and CodeExplain connect models to usable systems.", 13, "muted", cls="r2")
    + t(136, 192, "FastAPI · Playwright · React · computer vision · local-first architecture.", 12, cls="r2")
    + t(48, 242, "2024 →", 12, "accent", spacing="2", cls="r3")
    + t(136, 242, "LPU · B.TECH COMPUTER SCIENCE AND ENGINEERING", 15, cls="r3")
    + t(136, 268, "Latest TGPA 9.76 · CSE rank 14th in TGPA · graduation target 2028.", 13, "muted", cls="r3")
    + t(136, 292, "Class Representative during third semester · Team Innovex collaboration.", 12, cls="r3")
)
save_pair("experience.svg", "Experience, leadership and education", 1000, 330, experience)


credentials = heading("CREDENTIALS", "LEADERSHIP / ACADEMIC RECORD / CERTIFICATIONS")
credentials += t(48, 84, "ACADEMIC RECORD", 11, "muted", spacing="2", cls="r1")
credentials += t(48, 112, "TGPA 9.76 · CSE RANK 14TH · GRADUATING 2028", 15, weight="700", cls="r1")
credentials += t(48, 138, "AI/ML MINOR · >95% IN CLASS 10 AND CLASS 12 · INSPIRE MANAK TWICE", 11, "muted", cls="r1")
credentials += '<line class="draw" x1="48" y1="162" x2="952" y2="162"/>'
credentials += t(48, 194, "LEADERSHIP AND SELECTION", 11, "muted", spacing="2", cls="r2")
credentials += t(48, 222, "TEAM INNOVEX LEAD · LPU GEARUP SEASON 5", 14, weight="700", cls="r2")
credentials += t(48, 246, "SELECTED AMONG 30 HARDWARE TEAMS FROM 900+ PARTICIPATING TEAMS", 12, "muted", cls="r2")
credentials += '<line class="draw" x1="48" y1="270" x2="952" y2="270"/>'
credentials += t(48, 302, "CERTIFICATIONS", 11, "muted", spacing="2", cls="r3")
credentials += t(48, 330, "IBM SKILLSBUILD · HP LIFE · AGILE ACADEMY", 14, weight="700", cls="r3")
credentials += t(48, 354, "AGILE EXPLORER · PROJECT MANAGEMENT · AGILE FUNDAMENTALS · SCRUM FOUNDATIONS", 11, "muted", cls="r3")
credentials += t(48, 378, "30 AUG · 8 SEP · 30 SEP · 1 OCT 2026", 10, "accent", spacing="1", cls="r3")
save_pair("credentials.svg", "Credentials, leadership and academic record", 1000, 410, credentials)


stack = (
    '<line x1="138" y1="8" x2="138" y2="230" stroke="var(--rule)" opacity=".4"/>'
    + t(48, 32, "LANGUAGES", 12, "muted", spacing="2", cls="r1")
    + t(154, 32, "C · C++ · Python · Java · JavaScript", 15, cls="r1")
    + t(48, 64, "AI / ML", 12, "muted", spacing="2", cls="r2")
    + t(154, 64, "machine learning · deep learning · computer vision · NLP", 15, cls="r2")
    + t(48, 96, "LLM", 12, "muted", spacing="2", cls="r3")
    + t(154, 96, "Transformers · RAG · embeddings · prompt engineering · agents", 15, cls="r3")
    + t(48, 128, "WEB", 12, "muted", spacing="2", cls="r4")
    + t(154, 128, "FastAPI · Django · Node.js · React · REST APIs", 15, cls="r4")
    + t(48, 160, "IOT", 12, "muted", spacing="2", cls="r5")
    + t(154, 160, "ESP32 · ESP8266 · Arduino · Raspberry Pi · RFID · sensors", 15, cls="r5")
    + t(48, 192, "TOOLING", 12, "muted", spacing="2", cls="r6")
    + t(154, 192, "Git · Docker · Postman · Kaggle · Hugging Face · Jupyter", 15, cls="r6")
    + t(48, 224, "METHOD", 12, "muted", spacing="2", cls="r7")
    + t(154, 224, "measure honestly · validate outputs · ship useful interfaces", 15, "accent", cls="r7")
)
save_pair("stack.svg", "Technical stack — languages, AI, web, IoT and tooling", 1000, 238, stack)


focus = (
    heading("STACK FOCUS", "CURRENT WORK / NEXT BUILD")
    + t(48, 84, "C++ DSA", 12, "muted", spacing="2", cls="r1")
    + t(220, 84, "complexity · patterns · systematic LeetCode practice", 15, cls="r1")
    + t(48, 124, "AI ENGINEERING", 12, "muted", spacing="2", cls="r2")
    + t(220, 124, "RAG · structured outputs · model integration · agents", 15, cls="r2")
    + t(48, 164, "VISION", 12, "muted", spacing="2", cls="r3")
    + t(220, 164, "field robustness · domain shift · explainability", 15, cls="r3")
    + t(48, 204, "BACKEND", 12, "muted", spacing="2", cls="r4")
    + t(220, 204, "APIs · deployment · cloud infrastructure · maintainability", 15, cls="r4")
    + t(48, 244, "NEXT", 12, "muted", spacing="2", cls="r5")
    + t(220, 244, "privacy-conscious automation · evaluated systems · reliable products", 15, "accent", cls="r5")
)
save_pair("stack-focus.svg", "Current technical focus and next build", 1000, 280, focus)


footer = (
    '<line class="draw" x1="48" y1="24" x2="952" y2="24"/>'
    + '<circle class="ring" cx="60" cy="64" r="5" stroke="var(--accent)" fill="none"/>'
    + '<circle class="pulse" cx="60" cy="64" r="4" fill="var(--accent)"/>'
    + t(82, 62, "STATUS — BUILDING", 12, spacing="3", cls="")
    + t(82, 86, "AI systems · software foundations · hardware experiments", 11, "muted", cls="")
    + t(952, 86, "github.com/MohammadFayasKhan · Phagwara, IN · © 2026", 11, "accent", anchor="end", cls="")
)
save_pair("footer.svg", "Status — Mohammad Fayas Khan is building", 1000, 110, footer)
