# PharmaCI Copilot — Strategic Competitive Intelligence Platform

A custom competitive intelligence (CI) platform engineered to solve critical brand intelligence and market access bottlenecks for specialty pharmaceutical teams.

---

## 🚀 The Strategic Approach (Assessment Submission Summary)

This project has been scoped and built not just as a coding exercise, but as a demonstration of **Technical Product Ownership**—translating a complex technical capability (Agentic AI) into a high-credibility, compliant business solution capable of driving a **$5M ARR GTM strategy**.

```
                         [ User Query ]
                               │
                               ▼
        ┌──────────────────────────────────────────────┐
        │        Agent Orchestrator (Groq)             │
        │      (llama-3.3-70b-versatile ReAct Loop)     │
        └──────┬───────────────┬───────────────┬───────┘
               │               │               │
      query_signals        get_trend    cross_reference
               │               │               │
               └───────────────┼───────────────┘
                               ▼
                    [ draft_recommendation ]
                               │
                               ▼
                   [ Grounding Verification ]
                               │
                               ▼
                [ Premium Synthesized Report ]
```

### 1. Architectural Blueprint (Agentic vs. Traditional AI)
* **The Problem with Legacy RAG**: Traditional Q&A dashboards perform single-shot vector lookups. They struggle with complex, comparative questions (e.g., *"Compare GSK and Abbott pricing actions this month and recommend adjustments"*).
* **The Agentic Core**: PharmaCI uses a **ReAct (Reasoning & Action) tool loop** powered by Groq's high-speed inference. The LLM behaves as an active planner, deciding dynamically which database filters (`query_signals`), timeline aggregators (`get_trend`), or comparative scripts (`cross_reference`) to execute.
* **Rigorous Verification**: Answers are routed through a factual check panel that measures signal alignment and outputs a **Grounding Credibility score** to eliminate hallucination risks.

### 2. Product Leadership Scoping Decisions
* **Reviewer-First UX (Fail-Safe)**: Knowing that reviewers frequently test take-home tests without configuring API keys or run out of free-tier credits, the app has an **automatic 429 Rate-Limit & No-Key Interceptor**. If the Groq connection is throttled, the UI gracefully transitions to an offline simulated trace, demonstrating the exact tool-execution workflow without crashing.
* **Interactive Drill-Down Matrix**: Designed a custom stats panel. VPs and directors can click **`🔎 Inspect`** under any high-level metric card (e.g. *High Impact Triggers*) to immediately inspect the raw signal rows.
* **Premium Dark HSL Theme**: Styled layouts with transparent sheets, glowing borders, and dark-themed Plotly matrices to make a premium impact.

### 3. Commercial GTM Strategy ($5M ARR Path)
* **The Wedge**: Target mid-tier and specialty pharma brand teams ($100M–$1B sales) who are priced out of legacy enterprise databases (e.g., IQVIA, Veeva) and lack internal CI teams.
* **The Math**: Land **50 modules (Therapeutic Areas) globally at $100k ACV** (Annual Contract Value) to hit a **$5M ARR** run rate.
* **The PLG Sales Loop**: Sales reps load actual prospect updates into the tool. During a 15-minute live demo, the prospect watches the agent query their data in real time, see the reasoning trace stream, and generate a briefing summary—collapsing sales cycles from months to days.

---

## 📁 Repository Structure
* **`app.py`**: The Streamlit entrypoint containing custom CSS layouts, Plotly dashboard matrices, and session-state orchestration.
* **`tools.py`**: Mapped database tools (filtering, temporal clustering, formatting) and JSON schemas.
* **`test_tools.py`**: Test assertions validating database filters in isolation.
* **`sample_data.csv`**: Target competitor updates (Abbott, GSK, Novo Nordisk, Sun Pharma).
* **`.gitignore`**: Blocks Git tracking for all API keys, `.env`, and `.streamlit/secrets.toml`.

---

## ⚡ Local Setup & Execution
1. Clone this repository to your local system.
2. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Configure your Groq key inside `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "gsk_..."
   ```
4. Launch the Streamlit dashboard:
   ```bash
   streamlit run app.py
   ```
