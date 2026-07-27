import os
from fpdf import FPDF

class PlaybookPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(128, 128, 128)
            self.cell(100, 10, "PharmaCI Copilot - Presentation & Defense Playbook", 0, 0, "L")
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "R")
            self.ln(12)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 10, "Multiplier AI Technical Product Owner Assessment  |  Candidate: Alok Pandey", 0, 0, "C")

def create_playbook_pdf():
    pdf = PlaybookPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # ----------------------------------------------------
    # COVER PAGE
    # ----------------------------------------------------
    pdf.add_page()
    
    # Large colored top bar
    pdf.set_fill_color(11, 15, 23) # Deep Navy
    pdf.rect(0, 0, 210, 40, "F")
    
    # Accent color line
    pdf.set_fill_color(0, 212, 170) # Teal
    pdf.rect(0, 40, 210, 4, "F")
    
    pdf.ln(45)
    
    # Document Title
    pdf.set_font("Helvetica", "B", 26)
    pdf.set_text_color(11, 15, 23)
    pdf.multi_cell(0, 12, "PharmaCI Copilot\nPresentation & Interview Defense Playbook", 0, "L")
    pdf.ln(5)
    
    # Subtitle
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 8, "How to Walkthrough the Presentation & Handle Panel QA", 0, 0, "L")
    pdf.ln(15)
    
    # Horizontal Divider Line
    pdf.set_draw_color(220, 220, 220)
    pdf.set_line_width(0.5)
    pdf.line(10, 105, 200, 105)
    
    # Role Details
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 7, 
        "Position: AI Technical Product Owner (Pharma AI Platforms)\n"
        "Candidate: Alok Pandey\n"
        "Date: July 2026\n"
        "Target Goal: Executive Presentation Hook, Demo Scripts, & FAQ Preparations", 
        0, "L"
    )
    
    # Executive Intro Box
    pdf.ln(25)
    pdf.set_fill_color(245, 247, 250)
    pdf.set_draw_color(0, 212, 170)
    pdf.set_line_width(0.5)
    pdf.rect(10, 155, 190, 45, "DF")
    
    pdf.set_xy(12, 157)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 6, "PLAYBOOK OBJECTIVES:", 0, 0, "L")
    pdf.ln(8)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.set_x(12)
    pdf.multi_cell(186, 5,
        "This playbook prepares you for the panel presentation. It outlines exactly what to say to hook the "
        "reviewers, how to structure the live demo tab-by-tab, how to justify the $5M ARR GTM math, and how to "
        "comfortably handle technical curveballs regarding security, rate limits, and database structures.",
        0, "L"
    )
    
    # ----------------------------------------------------
    # CONTENT PAGE 1: THE 2-MINUTE HOOK
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "Part 1: The 2-Minute Presentation Hook (Opening Script)", 0, 0, "L")
    pdf.ln(12)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "Read this opening speech at the beginning of the presentation to establish authority:",
        0, "L"
    )
    pdf.ln(4)
    
    # Speech block quote styling
    pdf.set_fill_color(245, 247, 250)
    pdf.set_draw_color(200, 200, 200)
    pdf.rect(10, 36, 190, 85, "DF")
    pdf.set_xy(12, 38)
    
    pdf.set_font("Helvetica", "I", 10.5)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(186, 5.5,
        "\"Good morning, team. Today I am showing you PharmaCI Copilot, an automated market-scouting "
        "helper for brand managers.\n\n"
        "A common mistake candidates make is treating this assignment like a coding test. I treated it "
        "as a business decision. Large pharmaceutical giants spend millions of dollars on legacy database "
        "systems and analyst teams to scout their competitors. But mid-sized specialty brand teams ($100M - $1B "
        "sales) cannot afford that. Their brand directors waste 15 hours every week manually parsing trials, "
        "filings, and news feeds.\n\n"
        "PharmaCI is an automated 'Analyst-in-a-Box.' It uses a smart AI detective to scout, compare, and "
        "draft action plans in 10 seconds. Today, I will walk you through our prototype, show you how we sell "
        "this to achieve $5 Million in sales this year, and outline the product roadmap.\"",
        0, "L"
    )
    
    # ----------------------------------------------------
    # CONTENT PAGE 2: WHAT, WHY, HOW
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "Part 2: The 'What, Why, and How' of the Build", 0, 0, "L")
    pdf.ln(12)
    
    # Question 1
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "1. What did you build?", 0, 0, "L")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "A visual dark-themed web dashboard with 5 tabs. The main feature is the Agent Analyst tab - a smart "
        "AI detective powered by Groq's high-speed chips that dynamically decides how to gather data and write summaries.",
        0, "L"
    )
    pdf.ln(4)

    # Question 2
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "2. Why did you build it this way?", 0, 0, "L")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "  * Groq llama-3.3-70b: Chosen because the AI detective needs to make multiple decisions sequentially. "
        "Groq runs so fast that these thinking steps stream live in under 5 seconds, preventing user drop-off.\n"
        "  * Stateless Runs: The AI doesn't remember previous questions once the search is done. This prevents "
        "context contamination with outdated data and minimizes API token costs.\n"
        "  * Dynamic Ingestion Enrichment: The app programmatically tags signals with impact severity (High/Medium/Low) "
        "and posture (Offensive/Defensive) at startup, adding immediate value to raw competitor feeds.",
        0, "L"
    )
    pdf.ln(4)

    # Question 3
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "3. How does the ReAct (Reasoning + Action) Loop work?", 0, 0, "L")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "We gave the AI detective four tools: query_signals (filters data), get_trend (counts events over time), "
        "cross_reference (compares rivals), and draft_recommendation (suggests next actions). The AI writes down a "
        "Thought, takes an Action (calls a tool), receives the Observation (data output), and repeats. We enforce a "
        "5-step limit to prevent infinite loops.",
        0, "L"
    )

    # ----------------------------------------------------
    # CONTENT PAGE 3: DEMO & GTM MATH
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "Part 3: Demo Script & GTM Business Math", 0, 0, "L")
    pdf.ln(12)
    
    # Demo Script
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "Live Demo Flow (Tab-by-Tab):", 0, 0, "L")
    pdf.ln(6)
    
    demo_flow = [
        ("Dashboard (Tab 1)", "Explain the SOV donut and posture charts. Click the Inspect button under metrics to show popup data tables."),
        ("News Feed (Tab 2)", "Show signal cards, AI business implications, and expand the Audit Trace panel to show MLR metrics."),
        ("RAG Search (Tab 3)", "Run a search. Point out that answers are restricted to local signals to prevent hallucinations."),
        ("Agent Analyst (Tab 4)", "Click a preset button. Watch the st.status boxes load live, followed by the Grounding Credibility Check."),
        ("Digest Export (Tab 5)", "Click to compile all active views into a clean, downloadable report ready for weekly meetings.")
    ]
    for name, action in demo_flow:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(11, 15, 23)
        pdf.cell(40, 5, f"  * {name}:", 0, 0, "L")
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 5, action, 0, "L")
        pdf.ln(2)
        
    pdf.ln(4)
    # GTM Math
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "Defending the $5M ARR Revenue Math:", 0, 0, "L")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "  - The Price: We charge $100,000/year per Therapeutic Area (TA) module. We need to license 50 modules globally.\n"
        "  - The Customers: We don't need 50 companies. We only need 10. Large pharma brands operate multiple therapeutic divisions. "
        "If 10 companies license 5 modules each, we reach our goal of 50 modules ($5M ARR).\n"
        "  - The Savings: Hiring an analyst costs $150k/year. Our digital assistant is $100k, saving them immediate budget.\n"
        "  - The PLG Wedge: Pre-loading actual competitor data makes the live demo so impactful that pilots convert in 14 days.",
        0, "L"
    )

    # ----------------------------------------------------
    # CONTENT PAGE 4: INTERVIEW CURVEBALLS
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "Part 4: Defending Against Panel Curveballs (FAQ)", 0, 0, "L")
    pdf.ln(12)
    
    faqs = [
        ("Q: Why use simple text matching instead of vector databases (like FAISS)?",
         "For a small 21-signal prototype, vector databases introduce unnecessary API calls, storage overhead, and latency. Simple text matching runs in under 1ms. On the Q1-Q2 roadmap, we will implement hybrid search (keywords + dense embeddings) as we scale to larger PDF documents."),
         
        ("Q: How do you handle API key security when deploying?",
         "I configured a strict .gitignore to prevent local key files from ever being uploaded to GitHub. When hosting on Streamlit, we input the key in the Secrets dashboard. The app reads it securely in the background, keeping it completely hidden from the public."),
         
        ("Q: What happens if the Groq API key is rate-limited (Error 429) during review?",
         "I built an active Rate Limit Interceptor. If the Groq connection is throttled, the app catches the error and automatically triggers a local simulated trace. The reviewer sees the exact same visual trace and answers without experiencing any errors or crashes.")
    ]
    
    for q, a in faqs:
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(0, 212, 170)
        pdf.cell(0, 6, q, 0, 0, "L")
        pdf.ln(6)
        
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 5, a, 0, "L")
        pdf.ln(6)

    # Save the output
    out_path = r"C:\Users\aloks\Downloads\PharmaCI_Presentation_Playbook.pdf"
    pdf.output(out_path)
    print(f"PDF successfully compiled at: {out_path}")

if __name__ == "__main__":
    create_playbook_pdf()
