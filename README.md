# Candidate Performance Analysis & Recommendation Tool

A Python and Streamlit web application that analyzes candidate performance data and generates actionable recommendations — built to help identify strengths, weaknesses, and improvement paths for a batch of candidates across multiple courses.

## 🌐 Live Demo

[Click here to open the Candidate Performance Analysis App](https://candidate-performance-analysis.streamlit.app/)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Overview

This project analyzes the performance of 100 candidates across different courses. It goes beyond simple score reporting — the system identifies each candidate's strengths and weaknesses, recommends specific courses for improvement, tracks performance across multiple attempts, and pairs poor performers with high-performing mentors to support peer learning.

The goal is to turn a raw spreadsheet of scores into a dashboard that a training coordinator, mentor, or evaluator can actually act on.

## Features

- 📁 **Flexible data upload** — accepts both CSV and Excel datasets
- 📊 **Class performance dashboard** — visual overview of how the entire batch is performing
- 📈 **Average performance calculation** — per-candidate and per-course averages
- 🟢🟡🔴 **Performance segmentation** — automatically classifies candidates as high, medium, or poor performers
- 💪 **Strength identification** — highlights the courses/areas each candidate excels in
- ⚠️ **Weakness identification** — flags courses/areas that need improvement
- 🎯 **Course recommendations** — suggests specific courses for a candidate to focus on
- 🔁 **Multi-attempt tracking** — compares performance across multiple attempts to show improvement or decline over time
- 🤝 **Mentor pairing** — matches poor performers with high-performing candidates for guided support
- 📥 **Downloadable reports** — exports the analysis for offline use or sharing

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Web Framework | Streamlit |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Development Environment | Google Colab |

## Project Structure

```text
candidate-performance-analysis/
├── Candidate_Performance_Analysis.ipynb   # Data analysis & exploration notebook
├── candidate_performance_app.py           # Main Streamlit web application
├── candidate_performance_analysis.csv     # Sample performance dataset
├── requirements.txt                       # Python dependencies
└── README.md                              # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/YogeshS-shanmugam/candidate-performance-analysis.git
cd candidate-performance-analysis
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run candidate_performance_app.py
```

4. The app will open automatically in your browser at:

```text
http://localhost:8501
```

## Usage

1. Launch the app locally or open the [Live Demo](https://candidate-performance-analysis.streamlit.app/).
2. Upload a CSV or Excel file containing candidate scores across courses and attempts.
3. View the auto-generated class performance dashboard.
4. Explore individual candidate breakdowns, including strengths, weaknesses, and recommended courses.
5. Review the poor-performer and high-performer mentor pairings.
6. Download the final performance report.

## How It Works

1. **Data Ingestion** — Uploaded CSV or Excel data is read and processed using Pandas.
2. **Performance Calculation** — Average scores are calculated for each candidate and course.
3. **Segmentation** — Candidates are classified into high, medium, and poor performance categories.
4. **Strength & Weakness Detection** — Course-level scores are analyzed to identify each candidate's strongest and weakest areas.
5. **Recommendation Engine** — Weak areas are used to suggest courses for improvement.
6. **Improvement Tracking** — Multiple attempts are compared to identify improvement or decline over time.
7. **Mentor Matching** — High performers are paired with poor performers to encourage peer mentoring.
8. **Reporting** — Performance insights are compiled into downloadable reports.

## Sample Output

The application generates:

- Class-wide performance statistics
- Performance distribution charts
- Course-wise average marks
- Individual candidate analysis
- Strength and weakness breakdowns
- Personalized course recommendations
- Performance improvement trends across attempts
- Mentor-mentee pairings
- Downloadable performance reports

## Future Improvements

- Add a machine learning model to predict candidates at risk of underperforming
- Support real-time score updates using API or database integration
- Add authentication for mentors and coordinators
- Add interactive visualizations using Plotly
- Improve the recommendation system using machine learning

## Author

**Yogesh S**

[GitHub](https://github.com/YogeshS-shanmugam) · [LinkedIn](https://linkedin.com/in/yogesh-s-9345a92a2)
