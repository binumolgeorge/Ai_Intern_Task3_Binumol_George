# Task3_Binumol_George
# Startup Matching Recommendation Engine

This project simulates intelligent matchmaking between **Founders** and **Service Providers / Mentors**, similar to platforms like ScaleDux. It uses AI-based scoring and semantic similarity to recommend the most relevant matches based on domain, skills, project type, and timeline fit.

---

## Objective

To answer:
- *For Founders:* "Who's the best person to help me at my current startup stage?"
- *For Service Providers:* "Which startup projects match my skills, experience, and timeline?"

---

## How It Works

We use a hybrid recommendation approach combining:
- **Structured matching** (industry, skill, availability)
- **Semantic similarity** (via Hugging Face Transformers)
- **Scoring system out of 100** for every match

The engine provides:
- Bi-directional recommendations (Founder → Provider and Provider → Founder)
- Match score + key matching reasons (e.g. "Skill Match, Timeline Fit")
- Interactive dashboard with visualizations

---

## Dataset

The dataset includes **100 users**:
- 50 Founders (`F001` to `F050`)
- 50 Service Providers or Mentors (`S001` to `S050`)

Each user profile includes fields such as:
- **Founders**: startup_stage, industry, project_need, tech_requirement, deadline
- **Providers**: user_type, expertise_area, industry_preference, core_skill, availability

---
Matching Logic

The engine computes a match score (out of 100) based on:

| Feature             | Description                                         | Weight |
|---------------------|-----------------------------------------------------|--------|
| **Skill Match**      | Semantic similarity between tech needs and skills  | 30     |
| **Project Type**     | Match between project need and preferred type      | 25     |
| **Industry Match**   | Same domain or sector alignment                    | 20     |
| **Timeline Fit**     | Availability vs project deadline                   | 15     |
| **Stage Alignment**  | Optional alignment of startup stage with expertise | 10     |

We use `sentence-transformers` from Hugging Face for skill and project matching using **cosine similarity** on embeddings.

---
## Example Output

| Founder ID | Matched Provider ID | Match Score | Key Matching Reasons                |
|------------|---------------------|-------------|-------------------------------------|
| F001       | S012                | 87.45       | Skill Match, Industry Match         |
| F001       | S009                | 82.32       | Skill Match, Project Type Match     |

| Provider ID | Matched Founder ID | Match Score | Key Matching Reasons                     |
|-------------|--------------------|-------------|------------------------------------------|
| S001        | F011               | 84.90       | Skill Match, Timeline Fit, Industry Match |

CSV files:
- `Top3_Founder_Matches_With_Reasons.csv`
- `Top3_Provider_Matches_With_Reasons.csv`

---

## Interactive Dashboard

We built a Streamlit dashboard for real-time exploration of matches.
## Live Demo (Streamlit Cloud)

**Try it live:**  
[Click here to open the dashboard](https://task3binumolgeorge-myzc66hefgkfx6b3t8shek.streamlit.app/)


### Features:
- View top 3 matches per founder or provider
- See match score + reasons
- Visual bar chart of match quality

---

