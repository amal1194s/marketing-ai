# RivalSense AI - Hackathon Demo Guide

## 🎯 Quick Demo Script

Perfect for presenting your project in 5 minutes!

---

## 🚀 Before Demo

### Setup (Do this before presenting)

```bash
# 1. Install dependencies (only needed once)
.\install.ps1

# 2. Start both services
.\start.ps1

# 3. Wait 10 seconds for services to start

# 4. Open browser to http://localhost:3000
```

✅ **Checklist:**
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Browser open to localhost:3000
- [ ] No errors in terminals

---

## 🎤 Demo Script (5 Minutes)

### Slide 1: The Problem (30 seconds)
*"Small businesses lose customers to competitors because they don't know what's happening in the market until it's too late."*

**Show:** Landing page at `http://localhost:3000`

---

### Slide 2: The Solution (30 seconds)
*"RivalSense AI is your 24/7 market intelligence agent that monitors competitors and automatically generates strategies."*

**Show:** Click through to Dashboard
- Point out competitor cards
- Show threat levels
- Mention real-time monitoring

---

### Slide 3: The Magic - War Room (2 minutes)
*"Let me show you our AI agents in action."*

**Demo Steps:**
1. Click "War Room" in sidebar
2. Click "Start Analysis"
3. **While agents are running, explain each step:**
   - 🔍 **Scout Agent**: "Scans competitor pricing, promotions, new products"
   - 🔬 **Analyst Agent**: "Calculates threat scores, identifies pricing gaps"
   - 🎯 **Strategist Agent**: "Generates actionable strategies with marketing content"

4. **When complete:**
   - Show the threat score
   - Read a key insight
   - Show the marketing post that's ready to publish

---

### Slide 4: The Results (1 minute)
*"In seconds, business owners get:"*

**Point out on screen:**
- ✅ Threat assessment with clear urgency level
- ✅ Specific pricing recommendations
- ✅ Action steps they can implement today
- ✅ Ready-to-publish marketing content

*"This saves them hours of market research every week."*

---

### Slide 5: The Tech (1 minute)
*"Built with modern AI and web technologies:"*

**Show:** Architecture
- FastAPI backend with Python agents
- Next.js frontend with real-time UI
- Modular agent pipeline (extensible)
- Production-ready design

**Optional:** Show API docs at `http://localhost:8000/docs`

---

### Closing: The Ask (30 seconds)
*"We're looking for [funding/partners/early adopters] to help small businesses compete with enterprise-level market intelligence."*

**Show:** Navigate through pages
- Dashboard → Analysis → Strategy
- Demonstrate polish and completeness

---

## 🎬 Demo Tips

### Do's ✅
- **Practice the flow** several times before demo
- **Use real data** that tells a story
- **Pause during agent execution** to explain each step
- **Highlight the marketing post** - it's the most impressive output
- **Smile and be enthusiastic!**

### Don'ts ❌
- Don't rush through the War Room animation
- Don't ignore errors if they appear (acknowledge and move on)
- Don't get stuck in technical details unless asked
- Don't forget to close your other browser tabs
- Don't let background processes slow down the demo

---

## 💡 Talking Points

### Pain Point
- "78% of small businesses say they lose customers to competitors"
- "Most discover competitor moves weeks too late"
- "Market research costs $5K-$20K per month"

### Solution Value
- "Continuous monitoring, not one-time reports"
- "Actionable strategies, not just data"
- "Ready in seconds, not hours"

### Technical Differentiation
- "Multi-agent system that actually works together"
- "Generates marketing content automatically"
- "Built for small businesses, not enterprises"

---

## 🐛 Troubleshooting During Demo

### Backend not responding
```bash
# Restart quickly
python api_server.py
```

### Frontend error
```bash
# Clear and restart
cd rivalsense-ui
npm run dev
```

### War Room shows error
- Say: *"Let me restart that"*
- Click Reset, then Start Analysis again

### Complete failure
- Have screenshots ready as backup
- Say: *"Let me show you the results from our test run"*
- Show strategy output from a previous successful run

---

## 📸 Screenshot Backup

**Before demo, take screenshots of:**
1. Dashboard with data
2. War Room in progress
3. War Room results (analyst output)
4. Marketing post content
5. Strategy page

Store in: `demo-screenshots/`

---

## 🎯 Victory Metrics

After demo, you want people to say:
- "That was really fast!"
- "I love how it gives you marketing content"
- "The UI looks professional"
- "When can I use this?"

---

## 🚀 Post-Demo

**If they want to try it:**
```bash
# Share localhost link if on same network
http://[YOUR-IP]:3000
```

**If they want code:**
- GitHub repo ready
- README with setup instructions
- Docker container (if available)

---

## 📞 Q&A Prep

### "How do you get competitor data?"
*"Currently we use example data, but we're integrating with web scraping APIs and social media monitoring."*

### "What if a competitor isn't online?"
*"We focus on businesses with digital presence, which is 95%+ of modern competitors."*

### "How much does it cost?"
*"We're targeting $49-99/month for small businesses, 10x cheaper than traditional market research."*

### "Can it monitor more than 3 competitors?"
*"Absolutely! Our system is designed to scale. The demo shows 3 for clarity."*

### "Is this real AI or templated responses?"
*"Our agents use structured reasoning to analyze data and generate contextual strategies, not templates."*

---

**You got this! 🎉**

Break a leg! 🚀
