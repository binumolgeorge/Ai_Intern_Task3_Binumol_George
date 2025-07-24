# Task3_Binumol_George
# Startup Matching Recommendation Engine

This project simulates intelligent matchmaking between **Founders** and **Service Providers**, similar to platforms like ScaleDux. It uses AI-based scoring and semantic similarity to recommend the most relevant matches based on domain, skills, project type, and timeline fit.

---

## Objective

To answer:
- *For Founders:* "Who's the best person to help me at my current startup stage?"
- *For Service Providers:* "Which startup projects match my skills, experience, and timeline?"

---

## How It Works

Uses a hybrid recommendation approach combining:
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

Uses `sentence-transformers` from Hugging Face for skill and project matching using **cosine similarity** on embeddings.

---
## Outputs
Below are the outputs generated from the Google Colab notebook:

### CSV Files (Uploaded in this repo):

| File Name                                        | Description                                              |
|--------------------------------------------------|----------------------------------------------------------|
| `Top3_Founder_Matches.csv`                      | Top 3 matches per Founder (without key reasons)          |
| `Top3_Provider_Matches.csv`                     | Top 3 matches per Provider (without key reasons)         |
| `Top3_Founder_Matches_With_Reasons.csv`         | Top 3 Founder matches with scores + key matching reasons |
| `Top3_Provider_Matches_With_Reasons.csv`        | Top 3 Provider matches with scores + key matching reasons |
| `Full_Match_Matrix.csv`                         | All scores between all Founder–Provider combinations     |

### 📊 Visual Output (in Colab notebook):

- **Heatmap** 'heatmap.png' showing all Founder ↔ Provider match scores (`match_matrix`)
  - Generated using `seaborn` in the `.ipynb` notebook
  - Helps visualize which combinations score higher
    
[Click here to open the Colab notebook](https://colab.research.google.com/drive/12ufl2nO8MxiudkO3lxrcpsuovVpOChAy?usp=sharing)

---
## Example Output

| Founder ID | Matched Provider ID | Match Score | Key Matching Reasons                |
|------------|---------------------|-------------|-------------------------------------|
| F001       | S008                | 69.43       | Industry Match, Skill Match, Timeline Fit     |
| F001       | S015                | 66.38       | Industry Match, Skill Match, Timeline Fit     |


| Provider ID | Matched Founder ID | Match Score | Key Matching Reasons                     |
|-------------|--------------------|-------------|------------------------------------------|
| S001	      | F043               |	70         | Skill Match, Project Type Match, Timeline Fit   |
| S001        |	F044               |	46.02      | Industry Match, Project Type Match              |

CSV files:
- `Top3_Founder_Matches_With_Reasons.csv`
- `Top3_Provider_Matches_With_Reasons.csv`

---

## Interactive Dashboard

Built a Streamlit dashboard for real-time exploration of matches.
## Live Demo (Streamlit Cloud)

**Try it live:**  
[Click here to open the dashboard](https://task3binumolgeorge-myzc66hefgkfx6b3t8shek.streamlit.app/)


### Features:
- View top 3 matches per founder or provider
- See match score + reasons
- Visual bar chart of match quality

---

