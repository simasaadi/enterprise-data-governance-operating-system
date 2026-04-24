
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Enterprise Data Governance Control Tower",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parents[1]

WORKBOOKS = {
    "raci": {
        "path": ROOT / "02_roles_and_stewardship" / "raci-matrix.xlsx",
        "sheet": "RACI Matrix",
    },
    "issues": {
        "path": ROOT / "06_issue_and_change_management" / "issue-intake-log.xlsx",
        "sheet": "Issue Log",
    },
    "access": {
        "path": ROOT / "05_access_and_privacy" / "access-decision-log.xlsx",
        "sheet": "Decision Log",
    },
    "glossary": {
        "path": ROOT / "04_metadata_and_lineage" / "business-glossary.xlsx",
        "sheet": "Glossary",
    },
    "dictionary": {
        "path": ROOT / "04_metadata_and_lineage" / "data-dictionary.xlsx",
        "sheet": "Dictionary",
    },
}

OPTIONAL_IMAGES = {
    "raci_preview": ROOT / "assets" / "images" / "raci-matrix-preview.png",
    "issue_preview": ROOT / "assets" / "images" / "issue-intake-log-preview.png",
    "access_preview": ROOT / "assets" / "images" / "access-decision-log-preview.png",
    "kpi_preview": ROOT / "assets" / "images" / "governance-kpi-dashboard.png",
    "reporting_lineage": ROOT / "04_metadata_and_lineage" / "lineage-diagrams" / "reporting-lineage-diagram.png",
    "access_lineage": ROOT / "04_metadata_and_lineage" / "lineage-diagrams" / "access-request-lineage-diagram.png",
}


def apply_style() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1400px;
        }
        div[data-testid="metric-container"] {
            background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
            border: 1px solid #1f2937;
            padding: 14px 16px;
            border-radius: 16px;
        }
        .section-card {
            border: 1px solid #1f2937;
            background: linear-gradient(180deg, #0b1220 0%, #0f172a 100%);
            border-radius: 16px;
            padding: 18px;
            margin-bottom: 14px;
        }
        .subtle {
            color: #9ca3af;
            font-size: 0.94rem;
        }
        .pill {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            border: 1px solid #334155;
            background: #0f172a;
            margin-right: 8px;
            margin-bottom: 8px;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data
def load_sheet(path: Path, sheet_name: str) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        df = pd.read_excel(path, sheet_name=sheet_name, engine="openpyxl")
        df.columns = [str(col).strip() for col in df.columns]
        df = df.dropna(how="all")
        return df
    except Exception:
        return pd.DataFrame()


@st.cache_data
def load_all_data() -> dict[str, pd.DataFrame]:
    return {
        key: load_sheet(meta["path"], meta["sheet"])
        for key, meta in WORKBOOKS.items()
    }


def nonempty(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.strip().ne("")


def pct(part: int, whole: int) -> float:
    if whole == 0:
        return 0.0
    return round((part / whole) * 100, 1)


def load_image(path: Path) -> bool:
    return path.exists()


def build_kpis(
    issues: pd.DataFrame,
    access: pd.DataFrame,
    glossary: pd.DataFrame,
    dictionary: pd.DataFrame,
) -> dict[str, float | int]:
    owner_coverage = 0.0
    if not dictionary.empty and {"Owner", "Steward"}.issubset(dictionary.columns):
        owner_coverage = pct(
            ((nonempty(dictionary["Owner"])) & (nonempty(dictionary["Steward"]))).sum(),
            len(dictionary),
        )

    glossary_approval = 0.0
    if not glossary.empty and "Status" in glossary.columns:
        glossary_approval = pct(
            glossary["Status"].astype(str).str.strip().str.lower().eq("approved").sum(),
            len(glossary),
        )

    open_high_risk = 0
    assigned_issue_rate = 0.0
    recurring_issues = 0
    if not issues.empty:
        if {"Severity", "Status"}.issubset(issues.columns):
            sev = issues["Severity"].astype(str).str.strip().str.lower()
            stat = issues["Status"].astype(str).str.strip().str.lower()
            open_high_risk = int(
                ((sev.isin(["high", "critical"])) & (~stat.isin(["closed", "validated"]))).sum()
            )
        if "Assigned Owner" in issues.columns:
            assigned_issue_rate = pct(nonempty(issues["Assigned Owner"]).sum(), len(issues))
        if "Recurrence" in issues.columns:
            recurring_issues = int(
                issues["Recurrence"].astype(str).str.strip().str.lower().eq("yes").sum()
            )

    documented_access_rate = 0.0
    sensitive_requests = 0
    exception_requests = 0
    if not access.empty:
        if {"Decision", "Decision Owner"}.issubset(access.columns):
            documented_access_rate = pct(
                ((nonempty(access["Decision"])) & (nonempty(access["Decision Owner"]))).sum(),
                len(access),
            )
        if "Sensitive Data Involved" in access.columns:
            sensitive_requests = int(
                access["Sensitive Data Involved"].astype(str).str.strip().str.lower().eq("yes").sum()
            )
        if "Request Type" in access.columns:
            exception_requests = int(
                access["Request Type"].astype(str).str.strip().str.lower().str.contains("exception", na=False).sum()
            )

    maturity_score = 3.8
    training_completion = 88.0

    return {
        "Owner coverage %": owner_coverage,
        "Glossary approval %": glossary_approval,
        "Open high-risk issues": open_high_risk,
        "Issue owner assignment %": assigned_issue_rate,
        "Documented access decision %": documented_access_rate,
        "Sensitive requests": sensitive_requests,
        "Exception requests": exception_requests,
        "Recurring issues": recurring_issues,
        "Training completion %": training_completion,
        "Maturity score": maturity_score,
    }


def maturity_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Dimension": [
                "Operating model",
                "Roles and stewardship",
                "Data quality controls",
                "Metadata and definitions",
                "Access governance",
                "Issue and change management",
                "KPI monitoring",
                "Implementation and adoption",
            ],
            "Score": [4.0, 4.1, 3.8, 3.7, 4.0, 3.9, 3.6, 3.5],
            "Target": [4.2, 4.2, 4.1, 4.0, 4.1, 4.0, 4.0, 4.0],
        }
    )


def overview_snapshot_df(kpis: dict[str, float | int]) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Metric": [
                "Owner assignment coverage",
                "Approved glossary coverage",
                "Issue owner assignment",
                "Documented access decisions",
                "Training completion",
                "Governance maturity score",
            ],
            "Value": [
                kpis["Owner coverage %"],
                kpis["Glossary approval %"],
                kpis["Issue owner assignment %"],
                kpis["Documented access decision %"],
                kpis["Training completion %"],
                kpis["Maturity score"],
            ],
            "Target": [95.0, 90.0, 95.0, 100.0, 90.0, 4.0],
        }
    )


def status_badge(loaded: bool) -> str:
    return "✅ Loaded" if loaded else "⚠️ Missing"


def show_overview(
    issues: pd.DataFrame,
    access: pd.DataFrame,
    glossary: pd.DataFrame,
    dictionary: pd.DataFrame,
) -> None:
    st.title("Enterprise Data Governance Control Tower")
    st.caption(
        "Interactive governance dashboard built from the operating artifacts already stored in this repository."
    )

    st.markdown(
        """
        <div class="section-card">
        <strong>What this dashboard does:</strong><br>
        It turns governance artifacts into a management-facing control tower covering stewardship accountability,
        issue handling, access traceability, metadata discipline, KPI monitoring, maturity scoring, and a real end-to-end workflow example.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <span class="pill">Operating model</span>
        <span class="pill">Stewardship</span>
        <span class="pill">Data quality controls</span>
        <span class="pill">Metadata and definitions</span>
        <span class="pill">Access governance</span>
        <span class="pill">Issue and change management</span>
        <span class="pill">KPIs and maturity</span>
        """,
        unsafe_allow_html=True,
    )

    kpis = build_kpis(issues, access, glossary, dictionary)

    a, b, c, d, e, f = st.columns(6)
    a.metric("Owner coverage", f"{kpis['Owner coverage %']}%")
    b.metric("Glossary approval", f"{kpis['Glossary approval %']}%")
    c.metric("Open high-risk issues", int(kpis["Open high-risk issues"]))
    d.metric("Access decisions logged", f"{kpis['Documented access decision %']}%")
    e.metric("Recurring issues", int(kpis["Recurring issues"]))
    f.metric("Maturity score", float(kpis["Maturity score"]))

    left, right = st.columns((1.15, 1))

    with left:
        st.subheader("Governance KPI snapshot")
        snapshot = overview_snapshot_df(kpis)
        fig = px.bar(
            snapshot,
            x="Metric",
            y="Value",
            text="Value",
            title="Illustrative governance management scorecard",
        )
        fig.add_scatter(
            x=snapshot["Metric"],
            y=snapshot["Target"],
            mode="lines+markers",
            name="Target",
        )
        fig.update_layout(height=460, xaxis_title="", yaxis_title="Value")
        fig.update_traces(textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Issue severity mix")
        if not issues.empty and "Severity" in issues.columns:
            sev = (
                issues["Severity"]
                .astype(str)
                .str.strip()
                .value_counts()
                .rename_axis("Severity")
                .reset_index(name="Count")
            )
            fig2 = px.pie(sev, names="Severity", values="Count", hole=0.45)
            fig2.update_layout(height=300)
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("Issue sheet not available.")

        st.subheader("Access request mix")
        if not access.empty and "Request Type" in access.columns:
            req = (
                access["Request Type"]
                .astype(str)
                .str.strip()
                .value_counts()
                .rename_axis("Request Type")
                .reset_index(name="Count")
            )
            fig3 = px.bar(req, x="Request Type", y="Count", text="Count")
            fig3.update_layout(height=300, xaxis_title="", yaxis_title="Count")
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("Access sheet not available.")

    if load_image(OPTIONAL_IMAGES["kpi_preview"]):
        st.subheader("Dashboard preview asset")
        st.image(str(OPTIONAL_IMAGES["kpi_preview"]), use_container_width=True)


def show_raci(raci: pd.DataFrame) -> None:
    st.title("RACI and Stewardship")
    st.caption("Governance accountability across the operating model.")

    if raci.empty:
        st.warning("RACI workbook could not be loaded.")
        return

    search = st.text_input("Filter governance activity", placeholder="Type an activity name")
    table = raci.copy()

    if search and "Governance Activity" in table.columns:
        table = table[
            table["Governance Activity"].astype(str).str.contains(search, case=False, na=False)
        ]

    c1, c2 = st.columns((1.2, 1))

    with c1:
        st.dataframe(table, use_container_width=True, hide_index=True)

    with c2:
        st.markdown("### Role concentration")
        raci_cols = [col for col in table.columns if col not in ["Governance Activity", "Notes"]]
        counts = []
        for col in raci_cols:
            counts.append(
                {
                    "Role": col,
                    "A count": table[col].astype(str).str.contains(r"\bA\b", regex=True, na=False).sum(),
                    "R count": table[col].astype(str).str.contains(r"\bR\b", regex=True, na=False).sum(),
                    "C count": table[col].astype(str).str.contains(r"\bC\b", regex=True, na=False).sum(),
                }
            )

        summary = pd.DataFrame(counts)
        fig = go.Figure()
        fig.add_bar(name="Accountable", x=summary["Role"], y=summary["A count"])
        fig.add_bar(name="Responsible", x=summary["Role"], y=summary["R count"])
        fig.add_bar(name="Consulted", x=summary["Role"], y=summary["C count"])
        fig.update_layout(barmode="group", height=430, xaxis_title="", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)

    if load_image(OPTIONAL_IMAGES["raci_preview"]):
        st.subheader("RACI artifact preview")
        st.image(str(OPTIONAL_IMAGES["raci_preview"]), use_container_width=True)


def show_issues(issues: pd.DataFrame) -> None:
    st.title("Issue Management")
    st.caption("Structured issue intake, triage, ownership, and remediation tracking.")

    if issues.empty:
        st.warning("Issue log workbook could not be loaded.")
        return

    left, mid, right = st.columns(3)

    with left:
        severity = st.multiselect(
            "Severity",
            sorted(issues["Severity"].dropna().astype(str).unique()) if "Severity" in issues.columns else [],
        )
    with mid:
        category = st.multiselect(
            "Category",
            sorted(issues["Category"].dropna().astype(str).unique()) if "Category" in issues.columns else [],
        )
    with right:
        status = st.multiselect(
            "Status",
            sorted(issues["Status"].dropna().astype(str).unique()) if "Status" in issues.columns else [],
        )

    table = issues.copy()

    if severity and "Severity" in table.columns:
        table = table[table["Severity"].astype(str).isin(severity)]
    if category and "Category" in table.columns:
        table = table[table["Category"].astype(str).isin(category)]
    if status and "Status" in table.columns:
        table = table[table["Status"].astype(str).isin(status)]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Issues shown", len(table))
    m2.metric(
        "High / Critical",
        int(table["Severity"].astype(str).str.lower().isin(["high", "critical"]).sum()) if "Severity" in table.columns else 0,
    )
    m3.metric(
        "Recurring",
        int(table["Recurrence"].astype(str).str.lower().eq("yes").sum()) if "Recurrence" in table.columns else 0,
    )
    m4.metric(
        "Assigned owners",
        int(nonempty(table["Assigned Owner"]).sum()) if "Assigned Owner" in table.columns else 0,
    )

    st.dataframe(table, use_container_width=True, hide_index=True)

    chart_left, chart_right = st.columns(2)

    with chart_left:
        if "Category" in table.columns:
            cat = (
                table["Category"]
                .astype(str)
                .value_counts()
                .rename_axis("Category")
                .reset_index(name="Count")
            )
            fig = px.bar(cat, x="Category", y="Count", text="Count", title="Issues by category")
            st.plotly_chart(fig, use_container_width=True)

    with chart_right:
        if "Status" in table.columns:
            stat = (
                table["Status"]
                .astype(str)
                .value_counts()
                .rename_axis("Status")
                .reset_index(name="Count")
            )
            fig = px.bar(stat, x="Status", y="Count", text="Count", title="Issues by status")
            st.plotly_chart(fig, use_container_width=True)

    if load_image(OPTIONAL_IMAGES["issue_preview"]):
        st.subheader("Issue log artifact preview")
        st.image(str(OPTIONAL_IMAGES["issue_preview"]), use_container_width=True)


def show_access(access: pd.DataFrame) -> None:
    st.title("Access Governance")
    st.caption("Decision traceability, minimum-necessary logic, and access request monitoring.")

    if access.empty:
        st.warning("Access decision log workbook could not be loaded.")
        return

    left, mid, right = st.columns(3)

    with left:
        classification = st.multiselect(
            "Classification",
            sorted(access["Classification"].dropna().astype(str).unique()) if "Classification" in access.columns else [],
        )
    with mid:
        request_type = st.multiselect(
            "Request Type",
            sorted(access["Request Type"].dropna().astype(str).unique()) if "Request Type" in access.columns else [],
        )
    with right:
        decision = st.multiselect(
            "Decision",
            sorted(access["Decision"].dropna().astype(str).unique()) if "Decision" in access.columns else [],
        )

    table = access.copy()

    if classification and "Classification" in table.columns:
        table = table[table["Classification"].astype(str).isin(classification)]
    if request_type and "Request Type" in table.columns:
        table = table[table["Request Type"].astype(str).isin(request_type)]
    if decision and "Decision" in table.columns:
        table = table[table["Decision"].astype(str).isin(decision)]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Requests shown", len(table))
    c2.metric(
        "Sensitive data involved",
        int(table["Sensitive Data Involved"].astype(str).str.lower().eq("yes").sum()) if "Sensitive Data Involved" in table.columns else 0,
    )
    c3.metric(
        "High risk",
        int(table["Risk Level"].astype(str).str.lower().eq("high").sum()) if "Risk Level" in table.columns else 0,
    )
    c4.metric(
        "Exception requests",
        int(table["Request Type"].astype(str).str.lower().str.contains("exception", na=False).sum()) if "Request Type" in table.columns else 0,
    )

    st.dataframe(table, use_container_width=True, hide_index=True)

    left_chart, right_chart = st.columns(2)

    with left_chart:
        if "Decision" in table.columns:
            dec = (
                table["Decision"]
                .astype(str)
                .value_counts()
                .rename_axis("Decision")
                .reset_index(name="Count")
            )
            fig = px.bar(dec, x="Decision", y="Count", text="Count", title="Decision outcomes")
            st.plotly_chart(fig, use_container_width=True)

    with right_chart:
        if "Risk Level" in table.columns:
            risk = (
                table["Risk Level"]
                .astype(str)
                .value_counts()
                .rename_axis("Risk Level")
                .reset_index(name="Count")
            )
            fig = px.pie(risk, names="Risk Level", values="Count", hole=0.45, title="Risk distribution")
            st.plotly_chart(fig, use_container_width=True)

    if load_image(OPTIONAL_IMAGES["access_preview"]):
        st.subheader("Access decision log preview")
        st.image(str(OPTIONAL_IMAGES["access_preview"]), use_container_width=True)


def show_metadata(glossary: pd.DataFrame, dictionary: pd.DataFrame) -> None:
    st.title("Metadata and Definitions")
    st.caption("Business glossary and data dictionary coverage for governed assets.")

    left, right = st.columns(2)

    with left:
        st.subheader("Business glossary")
        if glossary.empty:
            st.warning("Glossary workbook could not be loaded.")
        else:
            if "Status" in glossary.columns:
                status_df = (
                    glossary["Status"]
                    .astype(str)
                    .value_counts()
                    .rename_axis("Status")
                    .reset_index(name="Count")
                )
                fig = px.pie(status_df, names="Status", values="Count", hole=0.45, title="Glossary status")
                st.plotly_chart(fig, use_container_width=True)
            st.dataframe(glossary, use_container_width=True, hide_index=True)

    with right:
        st.subheader("Data dictionary")
        if dictionary.empty:
            st.warning("Dictionary workbook could not be loaded.")
        else:
            if "Classification" in dictionary.columns:
                cls_df = (
                    dictionary["Classification"]
                    .astype(str)
                    .value_counts()
                    .rename_axis("Classification")
                    .reset_index(name="Count")
                )
                fig = px.bar(cls_df, x="Classification", y="Count", text="Count", title="Dictionary classification mix")
                st.plotly_chart(fig, use_container_width=True)
            st.dataframe(dictionary, use_container_width=True, hide_index=True)


def show_kpis_and_maturity(
    issues: pd.DataFrame,
    access: pd.DataFrame,
    glossary: pd.DataFrame,
    dictionary: pd.DataFrame,
) -> None:
    st.title("KPIs and Maturity")
    st.caption("Governance measurement view for management follow-up.")

    kpis = build_kpis(issues, access, glossary, dictionary)
    snapshot = overview_snapshot_df(kpis)
    maturity = maturity_df()

    st.subheader("Governance KPI table")
    st.dataframe(snapshot, use_container_width=True, hide_index=True)

    left, right = st.columns(2)

    with left:
        fig = px.bar(
            maturity,
            x="Dimension",
            y="Score",
            text="Score",
            title="Current maturity by dimension",
        )
        fig.add_scatter(
            x=maturity["Dimension"],
            y=maturity["Target"],
            mode="lines+markers",
            name="Target",
        )
        fig.update_layout(height=460, xaxis_title="", yaxis_title="Score")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=float(maturity["Score"].mean()),
                title={"text": "Average maturity score"},
                gauge={
                    "axis": {"range": [0, 5]},
                    "bar": {"thickness": 0.35},
                    "steps": [
                        {"range": [0, 2], "color": "#7f1d1d"},
                        {"range": [2, 3], "color": "#78350f"},
                        {"range": [3, 4], "color": "#1e3a8a"},
                        {"range": [4, 5], "color": "#14532d"},
                    ],
                },
            )
        )
        gauge.update_layout(height=460)
        st.plotly_chart(gauge, use_container_width=True)


def show_flows() -> None:
    st.title("Flows and Lineage")
    st.caption("Governance process flow and reporting lineage views.")

    left, right = st.columns(2)

    with left:
        st.subheader("Reporting lineage")
        if load_image(OPTIONAL_IMAGES["reporting_lineage"]):
            st.image(str(OPTIONAL_IMAGES["reporting_lineage"]), use_container_width=True)
        else:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    node [shape=box, style="rounded,filled", color="#334155", fillcolor="#0f172a", fontcolor="white"];
                    CRM [label="CRM"];
                    ERP [label="ERP"];
                    SVC [label="Service Request System"];
                    STG [label="Staging / Integration"];
                    RULES [label="Business Rules + Validation"];
                    MART [label="Certified Reporting Mart"];
                    KPI [label="KPI Dashboard"];
                    EXEC [label="Executive Reporting"];

                    CRM -> STG;
                    ERP -> STG;
                    SVC -> STG;
                    STG -> RULES;
                    RULES -> MART;
                    MART -> KPI;
                    KPI -> EXEC;
                }
                """
            )

    with right:
        st.subheader("Access request governance flow")
        if load_image(OPTIONAL_IMAGES["access_lineage"]):
            st.image(str(OPTIONAL_IMAGES["access_lineage"]), use_container_width=True)
        else:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    node [shape=box, style="rounded,filled", color="#334155", fillcolor="#0f172a", fontcolor="white"];
                    RQ [label="Request Submitted"];
                    CL [label="Classification Check"];
                    MN [label="Minimum Necessary Review"];
                    OW [label="Data Owner Approval"];
                    PR [label="Provisioning"];
                    LG [label="Decision Logged"];
                    RV [label="Periodic Review"];

                    RQ -> CL -> MN -> OW -> PR -> LG -> RV;
                }
                """
            )

    st.markdown(
        """
        <div class="section-card">
        These views show governance as an operational flow: requests move through classification, review, approval,
        fulfilment, and monitoring, while reporting assets move through source systems, validation, marts, dashboards, and executive use.
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_example() -> None:
    st.title("End-to-End Example")
    st.caption("How the operating system handles a sensitive access request from intake to review.")

    st.markdown("## Scenario")
    st.write(
        "A business analyst requests access to a restricted reporting extract containing operational and employee-linked data for a time-sensitive management reporting need."
    )

    st.markdown("## Governance problem")
    st.write(
        "The organization must balance business need, privacy, minimum necessary access, decision accountability, fulfilment traceability, and later review."
    )

    st.markdown("## Step-by-step artifact sequence")
    example_df = pd.DataFrame(
        {
            "Step": [
                "Request submitted",
                "Classification reviewed",
                "Minimum necessary assessed",
                "Decision authority confirmed",
                "Approval recorded",
                "Provisioning completed",
                "Decision logged",
                "Review date assigned",
            ],
            "Artifact / File": [
                "05_access_and_privacy/access-request-workflow.md",
                "05_access_and_privacy/data-classification-model.md",
                "05_access_and_privacy/minimum-necessary-policy.md",
                "01_operating-model/decision-rights-framework.md",
                "02_roles_and_stewardship/data-owner-steward-model.md",
                "05_access_and_privacy/access-control-matrix.xlsx",
                "05_access_and_privacy/access-decision-log.xlsx",
                "06_issue_and_change_management/issue-intake-log.xlsx",
            ],
            "Why it matters": [
                "Starts a governed process",
                "Confirms sensitivity and handling expectations",
                "Prevents over-permissioned access",
                "Ensures the correct approver makes the decision",
                "Creates business accountability",
                "Links approval to technical execution",
                "Creates traceability",
                "Supports later expiry review and follow-up",
            ],
        }
    )
    st.dataframe(example_df, use_container_width=True, hide_index=True)

    st.markdown("## Example decision outcome")
    st.success(
        "Approved for time-limited read-only access to a masked extract for 30 days, restricted to the reporting purpose stated in the request. Export and onward sharing prohibited."
    )

    st.markdown("## Why this makes the repo stronger")
    st.write(
        "This connects policy, workflow, stewardship, decision rights, access logging, and later review into one practical governance case. It shows how the repository operates as a management system rather than a static document library."
    )


def sidebar_status(data: dict[str, pd.DataFrame]) -> str:
    st.sidebar.title("Control Tower Navigation")
    page = st.sidebar.radio(
        "Go to",
        [
            "Overview",
            "RACI & Stewardship",
            "Issue Management",
            "Access Governance",
            "Metadata & Definitions",
            "KPIs & Maturity",
            "Flows & Lineage",
            "End-to-End Example",
        ],
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Workbook status")
    st.sidebar.write(f"RACI workbook: {status_badge(not data['raci'].empty)}")
    st.sidebar.write(f"Issue log: {status_badge(not data['issues'].empty)}")
    st.sidebar.write(f"Access log: {status_badge(not data['access'].empty)}")
    st.sidebar.write(f"Glossary: {status_badge(not data['glossary'].empty)}")
    st.sidebar.write(f"Dictionary: {status_badge(not data['dictionary'].empty)}")

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        '<div class="subtle">This app reads the governance workbooks already stored in the repository and turns them into an interactive management-facing dashboard.</div>',
        unsafe_allow_html=True,
    )
    return page


def main() -> None:
    apply_style()
    data = load_all_data()
    page = sidebar_status(data)

    if page == "Overview":
        show_overview(data["issues"], data["access"], data["glossary"], data["dictionary"])
    elif page == "RACI & Stewardship":
        show_raci(data["raci"])
    elif page == "Issue Management":
        show_issues(data["issues"])
    elif page == "Access Governance":
        show_access(data["access"])
    elif page == "Metadata & Definitions":
        show_metadata(data["glossary"], data["dictionary"])
    elif page == "KPIs & Maturity":
        show_kpis_and_maturity(data["issues"], data["access"], data["glossary"], data["dictionary"])
    elif page == "Flows & Lineage":
        show_flows()
    elif page == "End-to-End Example":
        show_example()


if __name__ == "__main__":
    main()
