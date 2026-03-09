def strategist_agent(data):

    competitor_price = data["competitor_price"]
    our_price = data["our_price"]
    competitor_offer = data["competitor_offer"]

    if our_price > competitor_price:
        recommendation = "Competitor is cheaper. Consider giving a discount."
    else:
        recommendation = "Your pricing is competitive."

    result = f"""
Market Strategy Report

Competitor Price: {competitor_price}
Our Price: {our_price}
Competitor Offer: {competitor_offer}

Recommendation:
{recommendation}

Marketing Idea:
🔥 Weekend Sale! Flat 10% OFF on all products!
"""

    return result