"""
questions.py  -  the quiz content.

Each question tests ONE well-known bias from behavioural finance
(the field where psychology meets money, made famous by Kahneman & Tversky).

For every question:
  - "options": the answers shown to the user
  - "biased": the answer(s) that show the bias
  - "bias", "explain", "tip": what we show on the results page
"""

QUESTIONS = [
    {
        "id": "loss_aversion",
        "bias": "Loss Aversion",
        "question": "A friend offers a coin toss. Heads: you win ₹600. Tails: you lose ₹500. Do you play?",
        "options": ["Yes, I'll play", "No, I'd rather not"],
        "biased": ["No, I'd rather not"],
        "explain": "On average this bet earns you ₹50 per toss, yet most people refuse. "
                   "Losing ₹500 feels about twice as painful as winning ₹500 feels good.",
        "tip": "Judge a bet by its average outcome, not by how bad the loss would feel.",
    },
    {
        "id": "disposition",
        "bias": "Disposition Effect",
        "question": "You own two stocks. Stock A is up 20%, Stock B is down 20%. You need cash. Which do you sell?",
        "options": ["Sell A (the winner)", "Sell B (the loser)", "Look at each company's future first"],
        "biased": ["Sell A (the winner)"],
        "explain": "Investors love to 'lock in' gains and hold losers hoping they'll come back. "
                   "Selling only winners often leaves you holding the weakest companies.",
        "tip": "Ask: 'Would I buy this stock today?' Keep the one you'd still buy.",
    },
    {
        "id": "anchoring",
        "bias": "Anchoring",
        "question": "A share traded at ₹1,000 last year and is now ₹600. What's your first thought?",
        "options": ["It's a bargain, it was ₹1,000!", "I need to check if the business is still good"],
        "biased": ["It's a bargain, it was ₹1,000!"],
        "explain": "The old price of ₹1,000 acts like an 'anchor' in your mind. "
                   "But the price may have fallen for a good reason.",
        "tip": "A past price tells you nothing about what a share is worth today.",
    },
    {
        "id": "herding",
        "bias": "Herd Behaviour",
        "question": "Everyone in your office is applying for a hot new IPO. You haven't read anything about the company. What do you do?",
        "options": ["Apply too, everyone can't be wrong", "Read about the company first, then decide"],
        "biased": ["Apply too, everyone can't be wrong"],
        "explain": "Following the crowd feels safe, but crowds also create bubbles.",
        "tip": "If you can't explain why you're buying in one sentence, don't buy yet.",
    },
    {
        "id": "overconfidence",
        "bias": "Overconfidence",
        "question": "Compared to the average person who invests, how good are you at picking stocks?",
        "options": ["Better than average", "About average", "Below average / not sure"],
        "biased": ["Better than average"],
        "explain": "In surveys, most people rate themselves above average, which is mathematically impossible. "
                   "Overconfident investors trade more and usually earn less.",
        "tip": "Keep a record of your past picks and compare them honestly with an index fund.",
    },
    {
        "id": "sunk_cost",
        "bias": "Sunk Cost Fallacy",
        "question": "You paid ₹5,000 (non-refundable) for a 10-week course. After 3 weeks you find it useless. What do you do?",
        "options": ["Finish it, I already paid", "Stop and use the time for something better"],
        "biased": ["Finish it, I already paid"],
        "explain": "The ₹5,000 is gone whatever you do. Continuing only adds wasted time on top of the lost money.",
        "tip": "Decide based on future costs and benefits only. Past money is 'sunk'.",
    },
    {
        "id": "recency",
        "bias": "Recency Bias",
        "question": "The stock market has gone up for three years in a row. What do you expect next year?",
        "options": ["It will most likely go up again", "Nobody can reliably predict one year"],
        "biased": ["It will most likely go up again"],
        "explain": "We give too much weight to what happened recently and assume it will continue.",
        "tip": "Look at long-term history (10–20 years), not the last few years.",
    },
    {
        "id": "mental_accounting",
        "bias": "Mental Accounting",
        "question": "You get a ₹20,000 Diwali bonus. You also owe ₹20,000 on a credit card charging 36% a year. What do you do with the bonus?",
        "options": ["Treat myself, it's bonus money!", "Pay off the credit card"],
        "biased": ["Treat myself, it's bonus money!"],
        "explain": "We put money into mental 'boxes' (salary, bonus, gift) and treat each box differently. "
                   "But every rupee is the same, and the card costs you 36% a year.",
        "tip": "Money is money, whatever its source. Clear expensive debt first.",
    },
    {
        "id": "present_bias",
        "bias": "Present Bias",
        "question": "Would you rather have ₹10,000 today or ₹11,000 in one month?",
        "options": ["₹10,000 today", "₹11,000 in one month"],
        "biased": ["₹10,000 today"],
        "explain": "Waiting one month earns 10%, more than a bank FD pays in a whole year. "
                   "Yet 'now' feels much more valuable than 'later'.",
        "tip": "Automate saving (like an SIP) so your present self can't overrule your future self.",
    },
    {
        "id": "gamblers_fallacy",
        "bias": "Gambler's Fallacy",
        "question": "The Nifty has fallen five days in a row. Is it more likely to rise tomorrow?",
        "options": ["Yes, it's due for a rise", "No, each day is roughly independent"],
        "biased": ["Yes, it's due for a rise"],
        "explain": "Markets have no memory. A losing streak doesn't make a rise 'due', just like a coin isn't 'due' for heads.",
        "tip": "Don't time trades on streaks. Base decisions on fundamentals.",
    },
]
