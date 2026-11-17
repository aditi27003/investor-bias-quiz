# 🧠 Investor Bias Quiz

**🚀 [Try the live app here](https://aditi-investor-bias-quiz.streamlit.app)**. No installation needed, it opens in your browser.

A behavioural-finance quiz that combines psychology with personal finance.
People answer 10 everyday money scenarios. The app shows which well-known **cognitive biases**
they display, explains each one in plain language with a practical tip, and gives a
"rational investor score" and investor personality.

Every completed quiz is saved, so the **Group Results** page can show how common each bias
is in a class, team or survey group. That makes the app usable as a small research tool.

## Biases tested

| Bias | What it means |
|---|---|
| Loss Aversion | Losses hurt about twice as much as equal gains feel good |
| Disposition Effect | Selling winners too early and holding losers too long |
| Anchoring | Judging value by an old or irrelevant number |
| Herd Behaviour | Following the crowd without your own analysis |
| Overconfidence | Rating your own skill above average |
| Sunk Cost Fallacy | Letting money already spent drive future choices |
| Recency Bias | Expecting recent trends to continue |
| Mental Accounting | Treating money differently depending on its source |
| Present Bias | Over-valuing "now" compared with "later" |
| Gambler's Fallacy | Believing a streak makes the opposite outcome "due" |

Based on the work of Daniel Kahneman, Amos Tversky (Prospect Theory) and Richard Thaler.

## Tech used
- **Python** and **Streamlit** for the web app
- **pandas** to save and analyse responses (`responses.csv`)

## How to run

```bash
pip install -r requirements.txt
streamlit run app.py
```

On Windows you can also double-click `start_app.bat`.

## Files
- `questions.py`: the 10 scenarios, the biases they test, explanations and tips
- `app.py`: the quiz page and the group results page
