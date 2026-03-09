from strategist_agent import strategist_agent

analysis_data = {
    "competitor_price": 799,
    "our_price": 950,
    "competitor_offer": "20% Summer Sale"
}

result = strategist_agent(analysis_data)

print(result)