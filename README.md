<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/header.svg"/><img src="assets/header.svg" alt="Mohammad Fayas Khan — Software Engineer, AI/ML and embedded systems"/></picture>

<a href="https://github.com/MohammadFayasKhan"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/GITHUB-111111?style=flat-square&logo=github&logoColor=ffffff"/><img src="https://img.shields.io/badge/GITHUB-ffffff?style=flat-square&logo=github&logoColor=000000" alt="GitHub"/></picture></a>
<a href="https://linkedin.com/in/mohammadfayaskhan"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/LINKEDIN-111111?style=flat-square&logo=linkedin&logoColor=ffffff"/><img src="https://img.shields.io/badge/LINKEDIN-ffffff?style=flat-square&logo=linkedin&logoColor=000000" alt="LinkedIn"/></picture></a>
<a href="https://leetcode.com/u/fayaskhanx/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/LEETCODE-111111?style=flat-square&logo=leetcode&logoColor=ffffff"/><img src="https://img.shields.io/badge/LEETCODE-ffffff?style=flat-square&logo=leetcode&logoColor=000000" alt="LeetCode"/></picture></a>
<a href="mailto:fayaskhanmohammad@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/EMAIL-111111?style=flat-square&logo=gmail&logoColor=ffffff"/><img src="https://img.shields.io/badge/EMAIL-ffffff?style=flat-square&logo=gmail&logoColor=000000" alt="Email"/></picture></a>

</div>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/now.svg"/><img src="assets/now.svg" alt="Current focus"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s01.svg"/><img src="assets/s01.svg" alt="01 — whoami"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/whoami.svg"/><img src="assets/whoami.svg" alt="About Mohammad Fayas Khan"/></picture>

<details>
<summary><b>Profile and engineering approach</b></summary>

<br/>

I am a **Computer Science Engineering** student at **Lovely Professional University** (2024–2028), with a **9.66 CGPA**, University Honor Roll recognition, and an AI/ML Minor. I build systems that move beyond notebooks: vision-powered field robotics, browser agents, LLM applications, deployed ML services, and embedded products.

| | |
|---|---|
| **Core focus** | Computer vision, LLM applications, agentic workflows, RAG, applied ML on edge hardware |
| **Build style** | Model → validated API → usable interface → deployment, with deterministic logic outside the LLM |
| **Leadership** | Team Innovex leader; top 30 hardware teams out of 900+ at LPU GearUp Season 5 |
| **Open source** | Accepted contributor, GirlScript Summer of Code 2026 |
| **Open to** | Software engineering internships, AI/ML roles, and meaningful collaborations |

</details>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s02.svg"/><img src="assets/s02.svg" alt="02 — system map"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/ecosystem.svg"/><img src="assets/ecosystem.svg" alt="System map: edge, models, backend and apps"/></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s03.svg"/><img src="assets/s03.svg" alt="03 — projects"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/projects.svg"/><img src="assets/projects.svg" alt="Featured projects"/></picture>

<details>
<summary><b>Project links, architecture, and engineering decisions</b></summary>

<br/>

| Project | Outcome | Links |
|---|---|---|
| **AI Powered Crop Intelligence Rover** | EfficientNetV2-S on ~54K images / 38 classes; 95.13% accuracy, 0.9354 macro F1; YOLO, Mobile-UNet, Grad-CAM, ESP32 rover, 4-DOF arm | [Repo](https://github.com/MohammadFayasKhan/AIPoweredCropIntelligenceRover) · [Live](https://aipoweredcropintelligencerover.dpdns.org) · [Demo](https://youtu.be/BdzizjHH6jI) |
| **LPU UMS Agent** | MV3 browser agent for attendance, date-sheet, and seating workflows; closed-loop grounding; IndexedDB privacy; 139 tests | [Repo](https://github.com/MohammadFayasKhan/LpuUmsAgent) |
| **Code Explain** | React/Monaco code tutor with five FastAPI endpoints, Pydantic validation, self-repair, Groq/Gemini fallback, and Docker deployment | [Repo](https://github.com/MohammadFayasKhan/CodeExplain) |
| **Smart Crop Intelligence** | RandomForest crop advisor with 93.18% accuracy, 93.10% macro F1, 27.61ms latency, and ESP8266 telemetry | [Repo](https://github.com/MohammadFayasKhan/smart-crop-intelligene-system) · [Live](https://fayasx-smart-plant.hf.space) |
| **CPU Sched** | React/Vite simulator for FCFS, SJF, SRTF, Round Robin, and Priority Scheduling with animated Gantt charts | [Repo](https://github.com/MohammadFayasKhan/cpuSched) · [Live](https://cpu-sched.vercel.app) |
| **Smart Home Automation Socket** | Native Apple HomeKit HAP server on ESP8266; active-LOW safety; no cloud or bridge | [Repo](https://github.com/MohammadFayasKhan/SmartHomeAutomationSocket) |
| **Face Attendance System** | dlib recognition, geotagging, FastAPI, React, Tailwind CSS, and SQLite | [Repo](https://github.com/MohammadFayasKhan/Face-Attendance-System) · [Live](https://studentsfaceattendancesystem.vercel.app/) |

### Why these systems are reliable

- **Rover:** Grad-CAM explains predictions and field-risk insights combine vision with live telemetry.
- **UMS Agent:** attendance calculations remain deterministic; CAPTCHA and security steps stay human-controlled.
- **Code Explain:** model output is schema-validated, repaired once, then routed through a fallback provider.
- **Smart Crop:** the model trains only on variables the hardware can actually measure.
- **HomeKit Socket:** active-LOW relay logic defaults both outputs to OFF at power-up.

</details>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s04.svg"/><img src="assets/s04.svg" alt="04 — deep dives"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/rover.svg"/><img src="assets/rover.svg" alt="Crop rover inference pipeline"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/agent.svg"/><img src="assets/agent.svg" alt="UMS Agent closed-loop control"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/gateway.svg"/><img src="assets/gateway.svg" alt="Code Explain provider gateway"/></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s05.svg"/><img src="assets/s05.svg" alt="05 — telemetry"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/telemetry.svg"/><img src="assets/telemetry.svg" alt="Development telemetry"/></picture>

<div align="center">
<picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=MohammadFayasKhan&show_icons=true&theme=dark&bg_color=00000000&hide_border=true&include_all_commits=true&count_private=true"/><img src="https://github-readme-stats.vercel.app/api?username=MohammadFayasKhan&show_icons=true&theme=default&bg_color=00000000&hide_border=true&include_all_commits=true&count_private=true" height="175" alt="GitHub statistics"/></picture>
&nbsp;
<picture><source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammadFayasKhan&layout=compact&theme=dark&bg_color=00000000&hide_border=true&langs_count=8"/><img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammadFayasKhan&layout=compact&theme=default&bg_color=00000000&hide_border=true&langs_count=8" height="175" alt="Top languages"/></picture>
</div>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s06.svg"/><img src="assets/s06.svg" alt="06 — the route"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/timeline.svg"/><img src="assets/timeline.svg" alt="Development timeline"/></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s07.svg"/><img src="assets/s07.svg" alt="07 — credentials"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/credentials.svg"/><img src="assets/credentials.svg" alt="Credentials and recognition"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/academics.svg"/><img src="assets/academics.svg" alt="Academic record"/></picture>

<details>
<summary><b>Credentials, recognition, and academic record</b></summary>

<br/>

| Period | Milestone |
|---|---|
| Jun–Jul 2026 | LPU AI Engineer Launchpad: 50 hours covering LLMs, RAG, tool calling, LoRA/QLoRA, FastAPI, guardrails, and evaluation |
| Sep 2026 | Led Team Innovex into the top 30 hardware teams out of 900+ at LPU GearUp Season 5 |
| 2026 | Accepted contributor, GirlScript Summer of Code |
| 2025 | University Honor Roll; JPMorgan Chase Code For Good HackerRank round cleared |
| 2025–2026 | Oracle AI Foundations, Agentic AI Foundations, NASSCOM ML/Image Processing, Infosys C++, Google Analytics, and n8n certifications |

| Term | TGPA | Core subjects |
|---|---:|---|
| Semester 1 | 9.55 | Python, Computing, Engineering Mathematics |
| Semester 2 | 9.63 | DBMS, Software Engineering, Programming, Discrete Mathematics |
| Semester 3 | 9.76 | OOP, DSA, Computer Networks, Probability and Statistics |
| Semester 4 | 9.72 | Operating Systems, DAA, Theory of Computation, Computer Organization |
| **Overall** | **9.66** | **University Honor Roll · AI/ML Minor** |

</details>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s08.svg"/><img src="assets/s08.svg" alt="08 — stack"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/stack.svg"/><img src="assets/stack.svg" alt="Technical stack"/></picture>

<details>
<summary><b>Technical stack</b></summary>

<br/>

**Languages:** C++ · Python · C · Java · JavaScript · TypeScript · SQL  
**AI/ML:** PyTorch · scikit-learn · OpenCV · YOLO · EfficientNetV2-S · Mobile-UNet · dlib · Pandas · NumPy  
**LLM systems:** LangChain · LangGraph · RAG · tool calling · structured outputs · guardrails · LoRA/QLoRA  
**Product:** React · Vite · Tailwind · FastAPI · Pydantic · Node.js · Chrome MV3 · Monaco Editor  
**Data and delivery:** PostgreSQL · MySQL · SQLite · Firebase · Supabase · IndexedDB · Docker · Linux · Vercel · Render · Hugging Face Spaces  
**Hardware:** ESP32 · ESP32-CAM · ESP8266 · Arduino · Blynk · DHT11 · rain and soil-moisture sensors

</details>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/s09.svg"/><img src="assets/s09.svg" alt="09 — roadmap"/></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/roadmap.svg"/><img src="assets/roadmap.svg" alt="Current roadmap"/></picture>

<details>
<summary><b>Current focus</b></summary>

<br/>

```yaml
primary: C++ DSA using the Striver A2Z roadmap
practice: 25-minute cold-solve attempt before hints
target: 200+ problems by Semester 6
building:
  - Crop Intelligence Rover improvements
  - Agentic tools with deterministic guardrails
  - GSSoC '26 open-source contributions
  - Reliable backend APIs and intelligent applications
```

</details>

<div align="center">

**Open to building useful software at the intersection of AI, full-stack engineering, and embedded systems.**

<a href="mailto:fayaskhanmohammad@gmail.com"><img src="https://img.shields.io/badge/EMAIL-REACH_OUT-333333?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://linkedin.com/in/mohammadfayaskhan"><img src="https://img.shields.io/badge/LINKEDIN-CONNECT-333333?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>

</div>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/footer.svg"/><img src="assets/footer.svg" alt="Current status"/></picture>

<!-- One responsive picture per visual; inspired by the reference structure, with profile-specific content. -->
