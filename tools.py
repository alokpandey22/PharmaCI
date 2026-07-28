import pandas as pd
import json

# Define the tools schemas for Groq Tool Calling
TOOLS_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "query_signals",
            "description": "Filters and retrieves individual competitive intelligence signals from the tracked dataset.",
            "parameters": {
                "type": "object",
                "properties": {
                    "company": {
                        "type": "string",
                        "description": "Optional competitor name to filter by (e.g., GSK, Abbott, Sun Pharma, Novo Nordisk). OMIT this parameter if not filtering by company (do not pass empty string)."
                    },
                    "therapeutic_area": {
                        "type": "string",
                        "description": "Optional therapeutic area (e.g., Diabetes, Oncology, Dermatology, Respiratory, Vaccines). OMIT this parameter if not filtering by therapeutic area (do not pass empty string)."
                    },
                    "signal_type": {
                        "type": "string",
                        "description": "Optional signal category (e.g., Pricing & Reimbursement, Sales Force Effectiveness, Pipeline, Clinical Trial, Regulatory). OMIT this parameter if not filtering by signal type (do not pass empty string)."
                    },
                    "impact_level": {
                        "type": "string",
                        "enum": ["High", "Medium", "Low"],
                        "description": "Optional impact level filter. OMIT this parameter if not filtering by impact level (do not pass empty string)."
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_trend",
            "description": "Calculates the weekly or monthly trend/volume of competitor activities or therapeutic area shifts over time.",
            "parameters": {
                "type": "object",
                "properties": {
                    "entity": {
                        "type": "string",
                        "description": "A company name or therapeutic area to calculate signals count over time for."
                    },
                    "granularity": {
                        "type": "string",
                        "enum": ["week", "month"],
                        "description": "Time unit for grouping. Defaults to 'week'."
                    }
                },
                "required": ["entity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cross_reference",
            "description": "Compares multiple competitor companies on specific signal types to reveal direct competitive pressure or moves.",
            "parameters": {
                "type": "object",
                "properties": {
                    "companies": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of company names to compare (e.g. ['GSK', 'Novo Nordisk'])."
                    },
                    "signal_type": {
                        "type": "string",
                        "description": "Optional signal type to focus the comparison."
                    }
                },
                "required": ["companies"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draft_recommendation",
            "description": "Generates a structured commercial implication ('So-what') and recommended action from synthesized evidence.",
            "parameters": {
                "type": "object",
                "properties": {
                    "evidence_summary": {
                        "type": "string",
                        "description": "Brief summary of evidence collected through previous tool calls."
                    }
                },
                "required": ["evidence_summary"]
            }
        }
    }
]

# --- Helper function for dynamic signal enrichment ---
def enrich_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Enriches raw CSV signals data with strategic metrics for enterprise credibility."""
    if df.empty:
        return df
        
    enriched = df.copy()
    
    # Assign Impact Levels
    impacts = []
    focuses = []
    for _, r in enriched.iterrows():
        st_type = str(r["signal_type"])
        hl = str(r["headline"]).lower()
        detail = str(r["detail"]).lower()
        
        # Determine Impact
        if "fda" in hl or "approval" in hl or "lower" in hl or "undercut" in hl or "inquiry" in hl:
            impacts.append("High")
        elif "expand" in hl or "positive" in hl or "Phase III" in hl:
            impacts.append("Medium")
        else:
            impacts.append("Low")
            
        # Determine Strategic Focus
        if "adjust" in hl or "restructures" in hl or "consolidates" in hl:
            focuses.append("Defensive")
        elif "expand" in hl or "undercut" in hl or "initiates" in hl or "launches" in hl:
            focuses.append("Offensive")
        else:
            focuses.append("Neutral")
            
    enriched["impact_level"] = impacts
    enriched["strategic_focus"] = focuses
    return enriched

# --- Tool Implementations working on the DataFrame ---

def query_signals(df: pd.DataFrame, company: str = None, therapeutic_area: str = None, signal_type: str = None, impact_level: str = None) -> str:
    """Filters signals dataset."""
    filtered = enrich_dataframe(df)
    
    if company:
        filtered = filtered[filtered['company'].str.lower() == company.lower()]
    if therapeutic_area:
        filtered = filtered[filtered['therapeutic_area'].str.lower() == therapeutic_area.lower()]
    if signal_type:
        filtered = filtered[filtered['signal_type'].str.lower() == signal_type.lower()]
    if impact_level:
        filtered = filtered[filtered['impact_level'].str.lower() == impact_level.lower()]
            
    if filtered.empty:
        return "No signals matching the filters were found in the database."
        
    records = []
    for _, r in filtered.iterrows():
        records.append({
            "date": str(r['date'].date()) if hasattr(r['date'], 'date') else str(r['date']),
            "company": r['company'],
            "drug": r['drug'],
            "therapeutic_area": r['therapeutic_area'],
            "signal_type": r['signal_type'],
            "headline": r['headline'],
            "detail": r['detail'],
            "source_type": r['source_type'],
            "impact_level": r['impact_level'],
            "strategic_focus": r['strategic_focus']
        })
    return json.dumps(records, indent=2)

def get_trend(df: pd.DataFrame, entity: str, granularity: str = 'week') -> str:
    """Calculates signals counts grouped by date periods (week/month)."""
    # Check if entity is a company or therapeutic area
    is_company = entity.lower() in [c.lower() for c in df['company'].unique()]
    is_ta = entity.lower() in [t.lower() for t in df['therapeutic_area'].unique()]
    
    if not (is_company or is_ta):
        # Fuzzy match attempt
        company_matches = [c for c in df['company'].unique() if entity.lower() in c.lower()]
        ta_matches = [t for t in df['therapeutic_area'].unique() if entity.lower() in t.lower()]
        if company_matches:
            is_company = True
            entity = company_matches[0]
        elif ta_matches:
            is_ta = True
            entity = ta_matches[0]
        else:
            return f"Entity '{entity}' not found in companies or therapeutic areas."
            
    filtered = df.copy()
    if is_company:
        filtered = filtered[filtered['company'].str.lower() == entity.lower()]
    else:
        filtered = filtered[filtered['therapeutic_area'].str.lower() == entity.lower()]
        
    if filtered.empty:
        return f"No signal history found for entity: {entity}."
        
    freq = 'W' if granularity.lower() == 'week' else 'ME'
    
    filtered['date'] = pd.to_datetime(filtered['date'])
    grouped = filtered.groupby(pd.Grouper(key='date', freq=freq)).size().reset_index(name='count')
    
    trends = []
    for _, row in grouped.iterrows():
        trends.append({
            "period": str(row['date'].date()),
            "count": int(row['count'])
        })
    return json.dumps({"entity": entity, "granularity": granularity, "trends": trends}, indent=2)

def cross_reference(df: pd.DataFrame, companies: list, signal_type: str = None) -> str:
    """Compares multiple companies on a signal type."""
    companies_lower = [c.lower() for c in companies]
    filtered = enrich_dataframe(df)
    filtered = filtered[filtered['company'].str.lower().isin(companies_lower)].copy()
    
    if signal_type:
        filtered = filtered[filtered['signal_type'].str.lower() == signal_type.lower()]
        
    if filtered.empty:
        return f"No common signals found for companies {companies} with signal type '{signal_type}'."
        
    comparison = {}
    for comp in companies:
        comp_df = filtered[filtered['company'].str.lower() == comp.lower()]
        comparison[comp] = []
        for _, r in comp_df.iterrows():
            comparison[comp].append({
                "date": str(r['date'].date()) if hasattr(r['date'], 'date') else str(r['date']),
                "drug": r['drug'],
                "therapeutic_area": r['therapeutic_area'],
                "signal_type": r['signal_type'],
                "headline": r['headline'],
                "detail": r['detail'],
                "impact_level": r['impact_level'],
                "strategic_focus": r['strategic_focus']
            })
            
    return json.dumps(comparison, indent=2)

def draft_recommendation(evidence_summary: str) -> str:
    """Format and return a structured recommendation."""
    structured = {
        "so_what": f"Key competitive shift detected: {evidence_summary[:120]}...",
        "commercial_actions": [
            "Initiate defensive messaging briefing for medical science liaisons (MSLs).",
            "Audit commercial contract structures with national accounts/PBMs to block competitor expansion.",
            "Realign field representative territory mapping targeting high-opportunity accounts."
        ],
        "kpi_to_monitor": "Share-of-Voice (SOV), formulary Tier status, and NBRx velocity."
    }
    return json.dumps(structured, indent=2)
