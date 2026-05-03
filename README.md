# trending_tags_system

📊 ShareChat APM Assignment — Trending Tags System
🔗 Live Demo

([Streamlit URL here](https://trendingtagssystem-prash.streamlit.app/))

📦 Repository Contents
sharechat_trending.ipynb — Data pipeline for generating trends
trending_tags_output.csv — Final output used by the app
app.py — Streamlit prototype (Part 2)
🧠 Problem Statement

Build a system that:

Automatically identifies trending topics in India (Hindi-first audience)
Outputs ranked trending tags with metadata
Displays them in an interactive, mobile-friendly UI
⚙️ Part 1 — Trending Tags System
🧩 Data Sources
Google News RSS (primary signal)
Real-time headlines representing current events
🔄 Pipeline Overview
News RSS → Topic Extraction → Cleaning → Deduplication → Scoring → Ranking → Hindi Output
🔍 Key Steps
1. Topic Extraction
Parse news headlines
Extract main topic (before - or :)
Normalize text
2. Cleaning & Deduplication
Remove noise, punctuation
Merge similar topics
Lowercase normalization
3. Scoring Logic
Trend Score = Frequency of topic in news feed
Higher frequency → higher trend rank
Recency is implicitly handled by RSS ordering
🏷 Output Format

Each trend contains:

Field	Description
tag	Hindi hashtag
description	Short explanation
category	(समाचार / खेल / etc.)
score	Heat (0–100)
source	Data source
posts	Estimated engagement
📌 Example Output
#आईपीएल2026 — क्रिकेट मैच ट्रेंड कर रहा है
#मुंबईबारिश — मौसम से जुड़ी खबरें
#चुनाव2026 — राजनीतिक गतिविधि बढ़ी
💡 Design Decisions
✅ Used News as proxy for trends (reliable, real-time)
✅ Avoided unstable Google Trends APIs
✅ Deterministic pipeline (no dependency on paid APIs)
✅ Hindi-first output for ShareChat audience
🤖 ML + Personalization Layer (Conceptual)

Although simplified, the system simulates:

ML Ranking
Input: trend score + category
Output: engagement likelihood
Personalization

Final score adjusted by:

User interest (e.g. क्रिकेट, समाचार)
Location (Delhi, Mumbai, etc.)
Final Score = Base Score × Personalization Boost
📱 Part 2 — App Prototype

Built using Streamlit

🎯 Features
📊 Feed-style UI
🔥 Trending tags with heat score
✨ “Recommended” personalized section
👆 Click → detailed view
🧠 AI-style summary (simulated)
🖥 UI Screens
Home
Personalized trends
All trends list
Detail View
Tag
Category
Description
Source
Summary
⚙️ How It Works

The app:

Loads CSV (trending_tags_output.csv)
Applies personalization logic
Ranks trends dynamically
Displays clickable cards
🚀 Run Locally
pip install streamlit pandas
python -m streamlit run app.py
🌐 Deployment

Deployed using Streamlit Cloud:

Connected via GitHub
Auto-deploy on push
🎨 UX Rationale
Mobile-first card design
Minimal clutter
High visibility for top trends
Quick navigation (tap → explore)

Optimized for:

Fast browsing
High engagement
Discoverability
🔮 Future Improvements (Next 4 Weeks)
1. Better Trend Detection
Add Twitter / YouTube signals
Use NLP clustering
2. ML Ranking Upgrade
Train model on engagement data
Predict CTR / dwell time
3. Personalization
Language-based feed
Region-specific trends
User behavior tracking
4. Content Integration
Show actual posts/videos under each trend



<img width="1509" height="940" alt="image" src="https://github.com/user-attachments/assets/33d5d2e0-7476-4371-a2b2-80cb2c1a7686" />

🎥 Loom Walkthrough

(Add your Loom link here)

📸 Screenshot

(Add screenshot of app here)

✅ Summary

This system:

Detects real-world trends reliably
Converts them into Hindi-first tags
Ranks and personalizes them
Displays them in an interactive UI
🙌 Thank You
