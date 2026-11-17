"""
app.py  -  Investor Bias Quiz (Streamlit web app).

Run with:  streamlit run app.py

Two pages (pick in the sidebar):
  1. Take the Quiz   - answer 10 money scenarios, see your bias profile
  2. Group Results   - see how everyone who took the quiz on this
                       computer answered (great for a class survey!)

Every finished quiz is saved as one row in responses.csv.
"""

import os
from datetime import datetime

import pandas as pd
import streamlit as st

from questions import QUESTIONS

RESPONSES_FILE = "responses.csv"

st.set_page_config(page_title="Investor Bias Quiz", page_icon="🧠", layout="centered")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def save_response(name: str, answers: dict, biased: dict) -> None:
    """Add one person's answers to responses.csv (creates the file if needed)."""
    row = {"time": datetime.now().strftime("%Y-%m-%d %H:%M"), "name": name or "Anonymous"}
    for q in QUESTIONS:
        row[q["id"]] = int(biased[q["id"]])        # 1 = showed the bias, 0 = didn't
    pd.DataFrame([row]).to_csv(
        RESPONSES_FILE, mode="a", index=False, header=not os.path.exists(RESPONSES_FILE)
    )


def profile_label(score: int) -> tuple[str, str]:
    """Turn a 'rational score' (0-100) into a friendly investor type."""
    if score >= 80:
        return "🦉 The Wise Owl", "You mostly think like a textbook rational investor. Rare!"
    if score >= 60:
        return "🐢 The Steady Tortoise", "You're fairly balanced, with a few mental shortcuts to watch."
    if score >= 40:
        return "🐒 The Curious Monkey", "Your instincts often take over. Very human, and very fixable."
    return "🐑 The Friendly Sheep", "Emotions and the crowd drive many of your money choices."


# ---------------------------------------------------------------------------
# Page 1: the quiz
# ---------------------------------------------------------------------------

def quiz_page():
    st.title("🧠 Investor Bias Quiz")
    st.write("Answer 10 quick money questions honestly. There are no 'right' answers to "
             "feel bad about. The quiz shows which **mental shortcuts (biases)** psychologists "
             "have found in most investors.")

    name = st.text_input("Your first name (optional)")

    with st.form("quiz"):
        answers = {}
        for i, q in enumerate(QUESTIONS, start=1):
            answers[q["id"]] = st.radio(f"**{i}. {q['question']}**", q["options"],
                                        index=None, key=q["id"])
        submitted = st.form_submit_button("See my results", type="primary")

    if not submitted:
        return
    if any(a is None for a in answers.values()):
        st.warning("Please answer all 10 questions first.")
        return

    biased = {q["id"]: answers[q["id"]] in q["biased"] for q in QUESTIONS}
    save_response(name, answers, biased)

    n_biased = sum(biased.values())
    score = round((len(QUESTIONS) - n_biased) / len(QUESTIONS) * 100)
    label, blurb = profile_label(score)

    st.divider()
    st.header("Your results")
    c1, c2 = st.columns(2)
    c1.metric("Rational investor score", f"{score} / 100")
    c2.metric("Biases spotted", f"{n_biased} of {len(QUESTIONS)}")
    st.subheader(label)
    st.write(blurb)

    st.subheader("Bias by bias")
    for q in QUESTIONS:
        if biased[q["id"]]:
            with st.expander(f"🔴 {q['bias']}: you showed this one", expanded=True):
                st.write(q["explain"])
                st.info(f"💡 Tip: {q['tip']}")
        else:
            with st.expander(f"🟢 {q['bias']}: you avoided this one"):
                st.write(q["explain"])


# ---------------------------------------------------------------------------
# Page 2: group results
# ---------------------------------------------------------------------------

def group_page():
    st.title("📊 Group Results")
    if not os.path.exists(RESPONSES_FILE):
        st.info("No one has taken the quiz yet. Share it with friends or classmates!")
        return

    df = pd.read_csv(RESPONSES_FILE)
    st.write(f"**{len(df)} people** have taken the quiz on this computer.")

    # % of people who showed each bias
    names = {q["id"]: q["bias"] for q in QUESTIONS}
    pct = (df[list(names)].mean() * 100).rename(index=names).sort_values(ascending=False)
    st.subheader("How common is each bias? (% of people)")
    st.bar_chart(pct)

    top = pct.index[0]
    st.success(f"The most common bias in your group is **{top}** ({pct.iloc[0]:.0f}% of people).")

    df["Rational score"] = (1 - df[list(names)].mean(axis=1)) * 100
    st.metric("Average rational score", f"{df['Rational score'].mean():.0f} / 100")

    with st.expander("See all responses (1 = showed the bias)"):
        st.dataframe(df.rename(columns=names), use_container_width=True)
    st.download_button("Download responses as CSV", df.to_csv(index=False), "responses.csv")


# ---------------------------------------------------------------------------
page = st.sidebar.radio("Go to", ["Take the Quiz", "Group Results"])
st.sidebar.caption("Based on behavioural finance research (Kahneman, Tversky, Thaler).")
quiz_page() if page == "Take the Quiz" else group_page()
