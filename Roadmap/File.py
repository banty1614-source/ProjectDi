from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, KeepTogether)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "/mnt/user-data/outputs/Banty_Kumar_AIML_Roadmap.pdf"

# ── Colour palette ──────────────────────────────────────────────────────────
C_DARK    = colors.HexColor("#0d1117")
C_BLUE    = colors.HexColor("#185FA5")
C_BLUE_LT = colors.HexColor("#E6F1FB")
C_GREEN   = colors.HexColor("#3B6D11")
C_GRN_LT  = colors.HexColor("#EAF3DE")
C_PURPLE  = colors.HexColor("#534AB7")
C_PUR_LT  = colors.HexColor("#EEEDFE")
C_AMBER   = colors.HexColor("#854F0B")
C_AMB_LT  = colors.HexColor("#FAEEDA")
C_TEAL    = colors.HexColor("#0F6E56")
C_TEAL_LT = colors.HexColor("#E1F5EE")
C_CORAL   = colors.HexColor("#993C1D")
C_CRL_LT  = colors.HexColor("#FAECE7")
C_GRAY    = colors.HexColor("#444441")
C_GRAY_LT = colors.HexColor("#F1EFE8")
C_TEXT    = colors.HexColor("#1a1a1a")
C_MUTED   = colors.HexColor("#6b6b6b")
C_BORDER  = colors.HexColor("#d0cfc7")
C_WHITE   = colors.white

W, H = A4
MARGIN = 18*mm

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN,
    topMargin=16*mm, bottomMargin=16*mm
)

styles = getSampleStyleSheet()

def sty(name, **kw):
    return ParagraphStyle(name, **kw)

S_TITLE  = sty("title",  fontName="Helvetica-Bold",   fontSize=22, textColor=C_DARK,   spaceAfter=2,  leading=26)
S_SUB    = sty("sub",    fontName="Helvetica",         fontSize=11, textColor=C_MUTED,  spaceAfter=8,  leading=14)
S_WK     = sty("wk",     fontName="Helvetica-Bold",   fontSize=13, textColor=C_WHITE,  leading=16)
S_WTITLE = sty("wtitle", fontName="Helvetica-Bold",   fontSize=11, textColor=C_TEXT,   leading=14)
S_DAY    = sty("day",    fontName="Helvetica-Bold",   fontSize=9,  textColor=C_MUTED,  spaceAfter=3,  spaceBefore=6, leading=12)
S_BODY   = sty("body",   fontName="Helvetica",         fontSize=9,  textColor=C_TEXT,   leading=13,    spaceAfter=1)
S_GOAL   = sty("goal",   fontName="Helvetica-Oblique", fontSize=9,  textColor=C_TEAL,   leading=12)
S_RULE   = sty("rule",   fontName="Helvetica-BoldOblique", fontSize=9, textColor=C_GREEN, leading=13)
S_SEC    = sty("sec",    fontName="Helvetica-Bold",   fontSize=10, textColor=C_MUTED,  spaceAfter=2, spaceBefore=4, leading=13)
S_SMALL  = sty("small",  fontName="Helvetica",         fontSize=8,  textColor=C_MUTED,  leading=11)

TAG_STYLES = {
    "watch":  (C_PUR_LT, C_PURPLE),
    "code":   (C_TEAL_LT, C_TEAL),
    "project":(C_CRL_LT,  C_CORAL),
    "resource":(C_GRAY_LT, C_GRAY),
    "deploy": (C_AMB_LT,  C_AMBER),
    "done":   (C_GRN_LT,  C_GREEN),
}

WEEK_COLORS = [C_BLUE, C_GREEN, C_PURPLE, C_AMBER]
WEEK_LT     = [C_BLUE_LT, C_GRN_LT, C_PUR_LT, C_AMB_LT]

# ── Content data ─────────────────────────────────────────────────────────────

WEEKS = [
  dict(
    num=1, col=0,
    title="Classical ML — Foundations to Ensemble Methods",
    hours="5–6 hrs/day  |  Days 1–7",
    goal="Complete StatQuest videos 1–28 + implement every algorithm on real Indian data",
    days=[
      dict(label="Days 1–2 · ML basics + Linear models", items=[
        ("watch",   "StatQuest #1–7: ML fundamentals, cross validation, confusion matrix, bias-variance, ROC-AUC, entropy, odds & log-odds"),
        ("watch",   "StatQuest #8–12: Linear regression (x2), multiple regression, logistic regression (x2)"),
        ("code",    "Scikit-learn: LinearRegression on commodity price data — evaluate with R2, MAE, plot residuals"),
        ("code",    "Scikit-learn: LogisticRegression to predict Gold direction — confusion matrix + ROC curve"),
        ("resource","ML with Python — Programming with Mosh (Scikit-learn syntax alongside StatQuest concepts)"),
      ]),
      dict(label="Days 3–4 · Regularization + Dimensionality reduction", items=[
        ("watch",   "StatQuest #13–15: Ridge L2, Lasso L1, Ridge vs Lasso visualized"),
        ("watch",   "StatQuest #16–19: PCA step-by-step, PCA 5 min, PCA in Python, t-SNE"),
        ("code",    "Add Ridge + Lasso to commodity regression, compare coefficients, see which features vanish"),
        ("code",    "Run PCA on 1000 Monte Carlo country simulation paths — visualise clusters with t-SNE"),
      ]),
      dict(label="Days 5–6 · Clustering + Trees + Ensembles", items=[
        ("watch",   "StatQuest #20–21: K-means, Hierarchical clustering"),
        ("watch",   "StatQuest #22–28: Decision trees (x2), Random forests, AdaBoost, Gradient boost, XGBoost"),
        ("code",    "K-means cluster commodity price regimes (bull/bear/sideways) from real yfinance data"),
        ("code",    "Random Forest vs XGBoost on India AQI data — compare accuracy, plot feature importance"),
      ]),
      dict(label="Day 7 · Remaining algorithms + Week 1 project", items=[
        ("watch",   "StatQuest #29–32: SVM pt1, Naive Bayes, One-hot encoding, Feature importance"),
        ("code",    "Hyperparameter tuning with GridSearchCV on your best model"),
        ("project", "PROJECT 1: End-to-end ML notebook — real Indian dataset (AQI or NSE stock), EDA to model comparison, pushed to GitHub with README"),
      ]),
    ]
  ),
  dict(
    num=2, col=1,
    title="Neural Networks + Deep Learning",
    hours="5–6 hrs/day  |  Days 8–14",
    goal="Build first neural network, understand backpropagation, train on real tabular + image data",
    days=[
      dict(label="Days 8–9 · Neural network intuition + TensorFlow setup", items=[
        ("watch",   "3Blue1Brown: Essence of Neural Networks (4 videos, ~1 hr) — watch all in one sitting"),
        ("watch",   "DeepLearning.AI Specialization Week 1–2 (audit free on Coursera) — Andrew Ng on forward/backprop"),
        ("code",    "Build neural network from scratch in NumPy — matrix multiplications + sigmoid, solve XOR"),
        ("code",    "TensorFlow + Keras: first Sequential model on commodity data, compare vs XGBoost from Week 1"),
        ("resource","Google Colab — use free GPU for all deep learning, no local setup needed"),
      ]),
      dict(label="Days 10–11 · Deep learning with TensorFlow/Keras", items=[
        ("watch",   "Deep Learning with TensorFlow — freeCodeCamp (6-hour video, split across 2 days)"),
        ("code",    "Tabular classifier on India income/credit dataset — dropout, batch norm, proper val/test split"),
        ("code",    "Experiment: vary layers, learning rate, optimizers (Adam vs SGD) — log results in a table"),
        ("resource","CampusX: Neural Networks playlist (Hindi/English) for any re-explanation needed"),
      ]),
      dict(label="Days 12–13 · Real neural network project", items=[
        ("code",    "Upgrade commodity simulator: replace Logistic Regression with Keras neural network"),
        ("code",    "Train on real NSE/BSE data via yfinance — walk-forward validation (time series split)"),
        ("code",    "Plot learning curves, loss curves, implement early stopping"),
      ]),
      dict(label="Day 14 · Week 2 project", items=[
        ("project", "PROJECT 2: Neural net on real financial or AQI data — compare classical ML vs neural net. Write 1-page analysis of when each wins. Push to GitHub."),
      ]),
    ]
  ),
  dict(
    num=3, col=2,
    title="Computer Vision + NLP + Transformers",
    hours="5–6 hrs/day  |  Days 15–21",
    goal="Build an image classifier and a text model — the two most in-demand deep learning skills",
    days=[
      dict(label="Days 15–16 · CNNs + Computer Vision", items=[
        ("watch",   "CNN for Computer Vision — Aladdin Persson (PyTorch from scratch, 2–3 hours)"),
        ("watch",   "Transfer Learning Tutorial — Daniel Bourke (fine-tuning ResNet on custom data)"),
        ("code",    "Build CNN on CIFAR-10 in PyTorch — Conv layers, MaxPool, ReLU, Dropout from scratch"),
        ("code",    "Fine-tune ResNet18 (pretrained) on a small custom dataset — e.g. Indian currency notes"),
        ("resource","Stanford CS231n free notes — read Conv layer section alongside coding"),
      ]),
      dict(label="Days 17–18 · NLP foundations + Transformers", items=[
        ("watch",   "HuggingFace NLP Course — Chapters 1–3 (tokenization, models, fine-tuning)"),
        ("watch",   "Attention Mechanism Explained — Yannic Kilcher (watch twice, it's dense)"),
        ("code",    "Text classification: classify Indian news headlines sentiment using BERT + HuggingFace"),
        ("code",    "Fine-tune small model on Hindi/English mixed dataset using HuggingFace Trainer API"),
      ]),
      dict(label="Days 19–20 · Build GPT intuition + LLM tools", items=[
        ("watch",   "Let's Build GPT — Andrej Karpathy (2.5 hrs — most important ML video of last 3 years)"),
        ("code",    "Follow Karpathy: build character-level language model on Indian text (Hindi poems, Constitution)"),
        ("code",    "HuggingFace pipeline API — build Q&A or summarization app on Indian dataset in <50 lines"),
      ]),
      dict(label="Day 21 · Week 3 project", items=[
        ("project", "PROJECT 3 (choose one): (A) CNN classify electrical components for TESLA society, or (B) Sentiment analysis on Indian financial news feeding buy/sell signal into commodity simulator. Push to GitHub."),
      ]),
    ]
  ),
  dict(
    num=4, col=3,
    title="MLOps + Deployment + Portfolio Sprint",
    hours="5–6 hrs/day  |  Days 22–30",
    goal="Deploy 2 projects as live apps, build GitHub portfolio, apply to internships",
    days=[
      dict(label="Days 22–23 · Streamlit deployment", items=[
        ("watch",   "Deploy ML Model with Streamlit — Nicholas Renotte (1 hour, then build immediately)"),
        ("deploy",  "Deploy Project 1 as Streamlit app — user inputs parameters, model predicts, shows chart"),
        ("deploy",  "Deploy commodity simulator with ML prediction as interactive Streamlit dashboard"),
        ("resource","Streamlit docs — components, layout, caching (st.cache_data)"),
      ]),
      dict(label="Days 24–25 · MLOps basics + experiment tracking", items=[
        ("watch",   "MLOps Crash Course — freeCodeCamp (MLflow, model versioning sections)"),
        ("code",    "Add MLflow tracking to best project — log params, metrics, model artifacts"),
        ("code",    "FastAPI: build REST endpoint that serves your ML model — POST request returns prediction"),
        ("resource","Made With ML — MLOps course (free) — read design and monitoring sections"),
      ]),
      dict(label="Days 26–27 · GitHub portfolio + LinkedIn", items=[
        ("deploy",  "Clean all 3+ repos: proper README with problem statement, approach, results, screenshots"),
        ("deploy",  "Add requirements.txt, .gitignore, project structure to every repo"),
        ("deploy",  "Write 3 LinkedIn posts (one per project). Tag NIT Patna. Pin best 3 repos on GitHub profile."),
      ]),
      dict(label="Days 28–30 · Capstone + Internship applications", items=[
        ("project", "PROJECT 4 (Capstone): Bihar AQI Health Risk Predictor — real Patna data from data.gov.in, XGBoost + neural net, deployed as Streamlit app. Your flagship project."),
        ("deploy",  "Apply to 5 ML/data internships on Internshala + Unstop using new portfolio"),
        ("deploy",  "Update resume: all 4 projects, Forage certificates, skills (Python, Scikit-learn, TensorFlow, PyTorch, HuggingFace, Streamlit, MLflow)"),
      ]),
    ]
  ),
]

# ── Build story ───────────────────────────────────────────────────────────────

story = []

# Cover / header
story.append(Spacer(1, 4*mm))
story.append(Paragraph("AI & ML in 1 Month", S_TITLE))
story.append(Paragraph("Banty Kumar  ·  NIT Patna  ·  B.Tech Electrical Engineering (Year 1)", S_SUB))

# Stats row
stat_data = [["4 Weeks","5–6 hrs/day","32 StatQuest videos","6+ Projects","$0 Cost"]]
stat_table = Table(stat_data, colWidths=[(W-2*MARGIN)/5]*5)
stat_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), C_DARK),
    ("TEXTCOLOR",  (0,0), (-1,-1), C_WHITE),
    ("FONTNAME",   (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,-1), 10),
    ("ALIGN",      (0,0), (-1,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING",(0,0),(-1,-1),8),
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[C_DARK]),
    ("ROUNDEDCORNERS",[4]),
]))
story.append(stat_table)
story.append(Spacer(1, 4*mm))

# Rule box
rule_data = [["One non-negotiable rule: watch a concept → open VS Code → implement before sleeping. Every single day. This separates people who finish with a portfolio from people who finish with notes."]]
rule_table = Table(rule_data, colWidths=[W-2*MARGIN])
rule_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(0,0), C_GRN_LT),
    ("TEXTCOLOR",     (0,0),(0,0), C_GREEN),
    ("FONTNAME",      (0,0),(0,0), "Helvetica-BoldOblique"),
    ("FONTSIZE",      (0,0),(0,0), 9),
    ("TOPPADDING",    (0,0),(0,0), 8),
    ("BOTTOMPADDING", (0,0),(0,0), 8),
    ("LEFTPADDING",   (0,0),(0,0), 12),
    ("RIGHTPADDING",  (0,0),(0,0), 12),
    ("LINEAFTER",     (0,0),(0,0), 3, C_GREEN),  # left border trick via line
    ("BOX",           (0,0),(0,0), 0.5, C_BORDER),
    ("ROUNDEDCORNERS",[4]),
]))
story.append(rule_table)
story.append(Spacer(1, 5*mm))

story.append(HRFlowable(width="100%", thickness=0.5, color=C_BORDER))
story.append(Spacer(1, 4*mm))

# Weeks
for wk in WEEKS:
    ci = wk["col"]
    wc = WEEK_COLORS[ci]
    wl = WEEK_LT[ci]

    # Week header bar
    hdr_data = [[
        Paragraph(f"Week {wk['num']}", S_WK),
        Paragraph(wk['title'], ParagraphStyle("wt2", fontName="Helvetica-Bold", fontSize=11, textColor=C_WHITE, leading=14)),
        Paragraph(wk['hours'], ParagraphStyle("wh2", fontName="Helvetica", fontSize=8, textColor=colors.HexColor("#c0d8f0"), leading=11, alignment=2)),
    ]]
    hdr_table = Table(hdr_data, colWidths=[22*mm, (W-2*MARGIN-22*mm-38*mm), 38*mm])
    hdr_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), wc),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(0,0),  10),
        ("LEFTPADDING",   (1,0),(1,0),   6),
        ("ROUNDEDCORNERS",[5]),
    ]))
    story.append(KeepTogether([hdr_table]))
    story.append(Spacer(1, 1*mm))

    # Goal line
    goal_data = [[Paragraph(f"Goal: {wk['goal']}", S_GOAL)]]
    goal_table = Table(goal_data, colWidths=[W-2*MARGIN])
    goal_table.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(0,0), wl),
        ("TOPPADDING",    (0,0),(0,0), 5),
        ("BOTTOMPADDING", (0,0),(0,0), 5),
        ("LEFTPADDING",   (0,0),(0,0), 10),
        ("BOX",           (0,0),(0,0), 0.5, C_BORDER),
    ]))
    story.append(goal_table)
    story.append(Spacer(1, 2*mm))

    # Days
    for day in wk["days"]:
        day_items = []
        day_items.append(Paragraph(day["label"], S_DAY))

        for tag, text in day["items"]:
            bg, fg = TAG_STYLES.get(tag, (C_GRAY_LT, C_GRAY))
            tag_label = Paragraph(tag, ParagraphStyle(
                "tg", fontName="Helvetica-Bold", fontSize=7,
                textColor=fg, alignment=TA_CENTER, leading=9
            ))
            tag_cell = Table([[tag_label]], colWidths=[14*mm])
            tag_cell.setStyle(TableStyle([
                ("BACKGROUND",    (0,0),(0,0), bg),
                ("TOPPADDING",    (0,0),(0,0), 2),
                ("BOTTOMPADDING", (0,0),(0,0), 2),
                ("LEFTPADDING",   (0,0),(0,0), 2),
                ("RIGHTPADDING",  (0,0),(0,0), 2),
                ("ROUNDEDCORNERS",[3]),
            ]))
            body_p = Paragraph(text, S_BODY)
            row = Table([[tag_cell, body_p]], colWidths=[16*mm, W-2*MARGIN-16*mm])
            row.setStyle(TableStyle([
                ("VALIGN",        (0,0),(-1,-1), "TOP"),
                ("TOPPADDING",    (0,0),(-1,-1), 1),
                ("BOTTOMPADDING", (0,0),(-1,-1), 2),
                ("LEFTPADDING",   (0,0),(0,0),   0),
                ("LEFTPADDING",   (1,0),(1,0),   4),
            ]))
            day_items.append(row)

        story.append(KeepTogether(day_items))
        story.append(Spacer(1, 1*mm))

    story.append(Spacer(1, 4*mm))

# Footer note
story.append(HRFlowable(width="100%", thickness=0.5, color=C_BORDER))
story.append(Spacer(1, 3*mm))

footer_cols = [
    "Week 1 already complete (Python + NumPy + Pandas + 2 simulation projects)",
    "StatQuest videos 1–32 mapped week-by-week above",
    "Kaggle replaced by: Zindi, DrivenData, data.gov.in, yfinance",
    "Month 2 deep learning compressed into Weeks 3–4 using extra hours",
]
for f in footer_cols:
    story.append(Paragraph(f"• {f}", S_SMALL))

story.append(Spacer(1, 3*mm))
story.append(Paragraph("Built for Banty Kumar · NIT Patna · June 2026  ·  All resources free", 
    ParagraphStyle("ft", fontName="Helvetica", fontSize=7, textColor=C_MUTED, alignment=TA_CENTER)))

doc.build(story)
print("PDF saved.")