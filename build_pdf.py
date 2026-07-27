import os
from fpdf import FPDF

class SimplifiedGuidePDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(128, 128, 128)
            # Avoid using cell with ln=0 and multi_cell on same line
            self.cell(100, 10, "PharmaCI Copilot - Presentation & Interview Defense Guide", 0, 0, "L")
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "R")
            self.ln(12)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 10, "Multiplier AI Technical Product Owner Assessment  |  Candidate: Alok Pandey", 0, 0, "C")

def create_guide_pdf():
    pdf = SimplifiedGuidePDF(orientation="P", unit="mm", format="A4")
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
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(11, 15, 23)
    pdf.multi_cell(0, 12, "PharmaCI Copilot\nPresentation & Defense Guide", 0, "L")
    pdf.ln(5)
    
    # Subtitle
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 8, "Simplifying Advanced Agentic AI for Executive Stakeholders", 0, 0, "L")
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
        "Target Assessment Goal: $5M ARR GTM Strategic Presentation Defense", 
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
    pdf.cell(0, 6, "ABOUT THIS PLAYBOOK:", 0, 0, "L")
    pdf.ln(8)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.set_x(12)
    pdf.multi_cell(186, 5,
        "This guide translates the advanced technical and business decisions behind the PharmaCI platform "
        "into clear, structured, and easy-to-understand language. It uses real-world analogies suitable for "
        "any audience (even an 8th-grade level) without compromising on the depth of the product case or roadmap, "
        "ensuring you are fully prepared for the panel interview.",
        0, "L"
    )
    
    # ----------------------------------------------------
    # CONTENT PAGE 1: TERMINOLOGY & ANALOGIES
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "1. Core Industry Concepts (Simple Terms)", 0, 0, "L")
    pdf.ln(12)
    
    concepts = [
        ("Competitive Intelligence (CI)", 
         "Keeping track of what your competitors are doing so you can win.",
         "Imagine you run a pizza shop. You want to know if the pizza shop across the street is lowering their prices, hiring new delivery drivers, or testing a new cheese recipe. That way, you can react quickly and not lose your customers. In medicine, pharma companies do the exact same thing."),
         
        ("Healthcare Professionals (HCPs)", 
         "Doctors, nurses, and pharmacists who prescribe medicine.",
         "These are the licensed medical experts who choose which drugs are prescribed to patients. Pharma companies focus their marketing on HCPs to convince them to prescribe their specific brand."),
         
        ("MLR Review (Medical, Legal, Regulatory)", 
         "The safety check committee inside a pharmaceutical company.",
         "Imagine writing an article for the school newspaper, but before it prints, a science teacher, a lawyer, and the principal must read every sentence to make sure you didn't print any lies, illegal things, or unproven claims. In pharma, every document shown to a doctor must be 'MLR-Approved' to avoid multi-million dollar regulatory fines.")
    ]
    
    for title, definition, analogy in concepts:
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(0, 212, 170)
        pdf.cell(0, 6, title, 0, 0, "L")
        pdf.ln(6)
        
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, f"What it means: {definition}", 0, "L")
        pdf.ln(1)
        
        pdf.set_font("Helvetica", "I", 10)
        pdf.set_text_color(80, 80, 80)
        pdf.multi_cell(0, 5, f"Analogy: {analogy}", 0, "L")
        pdf.ln(6)

    # ----------------------------------------------------
    # CONTENT PAGE 2: AGENTIC AI & REACTION LOOP
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "2. Understanding the Agentic Architecture", 0, 0, "L")
    pdf.ln(12)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "Regular AI (RAG Search) vs. Agentic AI (ReAct Loop)", 0, 0, "L")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "Regular AI is like a basic search bar: you ask a question, it fetches some rows, and prints an answer.\n\n"
        "Agentic AI is like hiring a smart detective. If you ask: 'Is our rival expanding?', the detective doesn't "
        "just guess. He makes a plan, queries the files, inspects the clues, finds that they hired 40 new sales reps, "
        "checks where they hired them, computes if they are hiring faster than last month, and writes a final report. "
        "This multi-step reasoning is called the ReAct (Reasoning + Action) Loop.",
        0, "L"
    )
    pdf.ln(8)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "The Detective's Tools (API Functions)", 0, 0, "L")
    pdf.ln(6)
    
    tools_list = [
        ("query_signals", "Looks up specific data rows matching filters (e.g. only GSK updates)."),
        ("get_trend", "Counts how many competitor events happened over weekly or monthly periods to show acceleration."),
        ("cross_reference", "Compares two or more companies side-by-side on specific criteria."),
        ("draft_recommendation", "Formulates what the brand team should do next based on the gathered evidence.")
    ]
    for name, desc in tools_list:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(11, 15, 23)
        pdf.cell(45, 5, f"  * {name}:", 0, 0, "L")
        # Ensure we call ln() to advance the line before multicell
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 5, desc, 0, "L")
        pdf.ln(2)

    # ----------------------------------------------------
    # CONTENT PAGE 3: DEMO SCRIPT & GTM MATH
    # ----------------------------------------------------
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(11, 15, 23)
    pdf.cell(0, 10, "3. Walkthrough Demo & The $5M Revenue Model", 0, 0, "L")
    pdf.ln(12)
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "The 5-Tab Live Demo Guide", 0, 0, "L")
    pdf.ln(6)
    
    demo_tabs = [
        ("Tab 1: Dashboard", "Show visual Plotly charts (Share of Voice donut, posture mix). Click 'Inspect' on metric cards to show interactive tables."),
        ("Tab 2: News Feed", "Show the cards, the AI-generated implication sentence, and expand the 'Audit Trace' to show compliance metrics."),
        ("Tab 3: Grounded Search", "Run a simple query to show how search bounds the AI from fabricating/hallucinating answers."),
        ("Tab 4: Agent Analyst", "Run a multi-step query. Point out the live st.status containers spinning step-by-step and the Grounding Confidence Meter."),
        ("Tab 5: Digest Export", "Click to compile all active views into a clean Markdown report ready to download for executive briefings.")
    ]
    for tab_title, tab_action in demo_tabs:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(11, 15, 23)
        pdf.cell(40, 5, f"  * {tab_title}:", 0, 0, "L")
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 5, tab_action, 0, "L")
        pdf.ln(2)
        
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 212, 170)
    pdf.cell(0, 6, "Defending the $5M ARR Math", 0, 0, "L")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 5,
        "  - How we reach $5M: We sell a single module (e.g. Oncology) for $100,000/year. We need to license 50 modules globally.\n"
        "  - The Land-and-Expand strategy: We do not need 50 different companies. We only need 10 companies. "
        "Large brands (like Abbott) operate multiple therapeutic pipelines. If 10 companies buy 5 modules each, we hit 50 modules ($5M ARR).\n"
        "  - Cost Justification: Hiring a human analyst costs $150k/year. Our digital analyst is $100k, saving them immediate budget.\n"
        "  - PLG Wedge: Pre-loading actual competitor data makes the live demo so impactful that pilots convert in 14 days.",
        0, "L"
    )
    
    # Save the output
    out_path = r"C:\Users\aloks\Downloads\PharmaCI_Presentation_Defense_Guide.pdf"
    pdf.output(out_path)
    print(f"PDF successfully compiled at: {out_path}")

if __name__ == "__main__":
    create_guide_pdf()
