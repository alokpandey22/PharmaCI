import pandas as pd
import json
from tools import query_signals, get_trend, cross_reference, draft_recommendation, enrich_dataframe

def get_sample_df():
    data = [
        {"date": "2026-06-02", "company": "GSK", "drug": "Nucala", "therapeutic_area": "Respiratory", "signal_type": "Pricing & Reimbursement", "headline": "GSK adjusts list price", "detail": "Details here", "source_type": "Payer Filing"},
        {"date": "2026-06-04", "company": "Sun Pharma", "drug": "Ilumya", "therapeutic_area": "Dermatology", "signal_type": "Sales Force Effectiveness", "headline": "Field force expansion", "detail": "Details here", "source_type": "Field Intelligence"},
        {"date": "2026-06-07", "company": "Abbott", "drug": "FreeStyle Libre 4", "therapeutic_area": "Diabetes", "signal_type": "Pipeline", "headline": "Files CGM sensor", "detail": "Details here", "source_type": "Regulatory Filing"},
        {"date": "2026-06-09", "company": "Novo Nordisk", "drug": "Ozempic", "therapeutic_area": "Diabetes/Obesity", "signal_type": "Pricing & Reimbursement", "headline": "Lowers price", "detail": "Details here", "source_type": "News"},
        {"date": "2026-06-11", "company": "GSK", "drug": "Jemperli", "therapeutic_area": "Oncology", "signal_type": "Clinical Trial", "headline": "Positive Phase III", "detail": "Details here", "source_type": "Clinical Trial Registry"}
    ]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    return df

def test_enrichment():
    df = get_sample_df()
    enriched = enrich_dataframe(df)
    assert "impact_level" in enriched.columns
    assert "strategic_focus" in enriched.columns
    # Check that "adjusts" maps to Defensive
    assert enriched.iloc[0]["strategic_focus"] == "Defensive"
    print("test_enrichment passed!")

def test_query_signals():
    df = get_sample_df()
    # Test filtering by company
    res = query_signals(df, company="GSK")
    data = json.loads(res)
    assert len(data) == 2, "GSK count should be 2"
    assert all(x['company'] == 'GSK' for x in data)

    # Test filtering by impact_level
    res = query_signals(df, impact_level="High")
    data = json.loads(res)
    # lowers price contains "lower" -> High impact
    assert len(data) >= 1
    print("test_query_signals passed!")

def test_get_trend():
    df = get_sample_df()
    res = get_trend(df, entity="GSK", granularity="week")
    data = json.loads(res)
    assert data['entity'] == 'GSK'
    assert len(data['trends']) > 0
    print("test_get_trend passed!")

def test_cross_reference():
    df = get_sample_df()
    res = cross_reference(df, companies=["GSK", "Novo Nordisk"], signal_type="Pricing & Reimbursement")
    data = json.loads(res)
    assert "GSK" in data
    assert "Novo Nordisk" in data
    print("test_cross_reference passed!")

def test_draft_recommendation():
    res = draft_recommendation("Novo Nordisk lowers Ozempic prices")
    data = json.loads(res)
    assert "so_what" in data
    assert len(data["commercial_actions"]) == 3
    print("test_draft_recommendation passed!")

if __name__ == "__main__":
    test_enrichment()
    test_query_signals()
    test_get_trend()
    test_cross_reference()
    test_draft_recommendation()
    print("All tests passed successfully!")
