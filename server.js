const express = require('express');
const cors = require('cors');
const { Configuration, OpenAIApi } = require("openai");

const app = express();
app.use(cors());
app.use(express.json());

const openai = new OpenAIApi(new Configuration({ apiKey: process.env.OPENAI_API_KEY }));

app.get('/api/status', (req, res) => {
  res.json({
    activeExperiments: 4,
    parallelSimulations: 25,
    nodesOnline: 5,
    lastUpdate: new Date().toISOString()
  });
});

app.post('/api/agi/chat', async (req, res) => {
  const { prompt } = req.body;
  const response = await openai.createChatCompletion({
    model: "gpt-4o",
    messages: [{ role: "user", content: prompt }]
  });
  res.json({ reply: response.data.choices[0].message.content });
});

app.listen(3001, () => console.log("API running on port 3001"));
