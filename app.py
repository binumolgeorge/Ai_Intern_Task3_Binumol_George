import streamlit as st
import pandas as pd
import altair as alt

# Load precomputed match data
founder_df = pd.read_csv("Top3_Founder_Matches_With_Reasons.csv")
provider_df = pd.read_csv("Top3_Provider_Matches_With_Reasons.csv")

st.set_page_config(page_title="Startup Matching Engine", layout="wide")

st.title(" Startup Recommendation Engine Dashboard")
st.markdown("Matchmaking between **Founders** and **Service Providers and Mentors** based on skills, domains, and timeline fit.")

tab1, tab2 = st.tabs([" Founder Recommendations", " Provider Recommendations"])

with tab1:
    st.subheader(" Top Matches for a Founder")
    founder_ids = sorted(founder_df["Founder ID"].unique())
    selected_founder = st.selectbox("Select a Founder ID", founder_ids)

    f_matches = founder_df[founder_df["Founder ID"] == selected_founder]

    st.write(" Top 3 Matches:")
    st.dataframe(f_matches[["Matched Provider ID", "Match Score", "Key Matching Reasons"]])

    # Visualization
    bar_chart = alt.Chart(f_matches).mark_bar().encode(
        x=alt.X('Matched Provider ID', sort='-y'),
        y='Match Score',
        tooltip=['Key Matching Reasons']
    ).properties(title=" Match Scores with Providers")
    st.altair_chart(bar_chart, use_container_width=True)

with tab2:
    st.subheader(" Top Matches for a Service Provider or Mentor")
    provider_ids = sorted(provider_df["Provider ID"].unique())
    selected_provider = st.selectbox("Select a Provider ID", provider_ids)

    p_matches = provider_df[provider_df["Provider ID"] == selected_provider]

    st.write(" Top 3 Matches:")
    st.dataframe(p_matches[["Matched Founder ID", "Match Score", "Key Matching Reasons"]])

    # Visualization
    bar_chart2 = alt.Chart(p_matches).mark_bar().encode(
        x=alt.X('Matched Founder ID', sort='-y'),
        y='Match Score',
        tooltip=['Key Matching Reasons']
    ).properties(title=" Match Scores with Founders")
    st.altair_chart(bar_chart2, use_container_width=True)
