## Step 2: Shuruat Karein – Installation Aur Pehli Dafa Chalana
(Getting Started – Installation and First Run)

Assalam-o-Alaikum, dost! 👋 Ab jab humne **OpenAI Agents SDK** ki bunyadi baatein samajh li hain, toh ab waqt hai isko apne system mein dalne aur iske saath thora khelne ka. Yeh step-by-step guide aapko asani se shuru karne mein madad karegi.

### 2.1: SDK Ki Installation
(Installation of the SDK)

Sab se pehle, humein **OpenAI Agents SDK** ko apne computer par install karna hoga. Yeh bohat asaan hai, aapko bas `pip` command istemal karni hai.

```bash
# Terminal (Command Prompt / PowerShell / Git Bash) mein yeh command likhiye:
pip install openai-agents
```
*   `pip install openai-agents`: Yeh command Python package manager `pip` ko istemal karti hai taake `openai-agents` naam ka package aapke system mein download aur install ho jaye. Jab yeh command poori ho jaye, toh samajh lijiye ke SDK ab aapke istemal ke liye tayaar hai!

### 2.2: OPENAI_API_KEY Set Karna
(Setting the OPENAI_API_KEY)

Ab yeh aik **bohat zaroori qadam** hai. Jab aap OpenAI ke models istemal karte hain (jaisay GPT-3.5, GPT-4, etc.), toh aapko aik **API Key** ki zaroorat hoti hai. Yeh aapki shanakht (identity) hoti hai aur billing ke liye istemal hoti hai. Is key ko apne system ke **environment variables** mein set karna zaroori hai taake SDK usay istemal kar sake.

```bash
# Terminal mein yeh command likhiye:
# 'sk-...' ki jagah apni asal OpenAI API Key daliye.
export OPENAI_API_KEY=sk-...
```
*   `export OPENAI_API_KEY=sk-...`: Yeh command `OPENAI_API_KEY` naam ka **environment variable** set karti hai. Iska matlab hai ke jab aap Python script chalayenge jo SDK istemal kar rahi hogi, toh woh automatic tor par is variable se aapki API key utha legi. **Yaad rakhiye, apni asal API key `sk-...` ki jagah dalna mat bhooliyega!** Yeh key aapko OpenAI ki website par account banane ke baad mil jayegi (agr aapka account nahi hai to).

**Note**: Agar aap Windows istemal kar rahe hain, toh `export` ki jagah `set` ya PowerShell mein `$env:OPENAI_API_KEY="..."` istemal ho sakta hai. Lekin bunyadi maqsad aik hi hai: environment variable set karna.

### 2.3: "Hello World" Example – Pehla Agent Chalana
(First Agent Run)

Ab hum tayaar hain apna pehla Agent banane aur chalane ke liye! Yeh bohat seedha saadha sa code hai jo aapko dikhayega ke aik basic Agent kaise kaam karta hai.

Aik nai Python file banaiye, maslan `hello_agent.py`, aur ismein neechay diya gaya code paste karein:

```python
# hello_agent.py

from agents import Agent, Runner #

# Step 1: Agent banayiye
# Agent woh LLM (Large Language Model) hai jise hum instructions aur tools dete hain.
agent = Agent(
    name="Assistant", # Agent ka naam. Koi bhi naam de sakte hain.
    instructions="You are a helpful assistant" #
    # Yeh instructions LLM ko batati hain ke uska role kya hai aur usay kya karna hai.
)

# Step 2: Agent ko chalayiye
# Runner.run_sync() Agent ko synchronously chalata hai.
# Hum Agent ko aik task de rahe hain: "Write a haiku about recursion in programming."
result = Runner.run_sync(
    agent, # Jis Agent ko chalana hai.
    "Write a haiku about recursion in programming." #
)

# Step 3: Nateeja (output) dekhiye
# result.final_output se Agent ka final jawab milta hai.
print(result.final_output) #

# Umeed hai ke aapko yeh haiku milega:
# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

Ab is file ko **terminal** mein chalayiye jahan aapne apni API key set ki thi:

```bash
# Terminal mein:
python hello_agent.py
```

Aap dekhenge ke Agent aapko recursion par aik haiku likh kar dega! Hai na mazedar? Yeh bata raha hai ke **Agent loop** built-in hai, jo tools ko call karta hai, results ko LLM tak bhejta hai, aur yeh tab tak loop karta hai jab tak LLM apna kaam mukammal na karle.

### 2.4: Doosre Models (Jaisay Gemini) Ke Liye Configuration
(Configuration for Other Models like Gemini)

Aapne theek kaha, OpenAI ke APIs paid hain. Achi baat yeh hai ke **OpenAI Agents SDK** aapko sirf OpenAI models tak mehdood nahi rakhta. Yeh aapko **kisi bhi model (any model) ko LiteLLM ke zariye istemal karne ki ijazaat deta hai**.

*   **LiteLLM Kya Hai?**
    LiteLLM aik library hai jo mukhtalif LLM providers (jaisay Google Gemini, Anthropic Claude, Cohere, vagerah) ke APIs ko aik single, consistent interface ke zariye istemal karne ki sahoolat deti hai. Yani, aapko har model ke liye alag se code nahi likhna parta.

*   **Kaise Configure Karein?**
    SDK ke andar **`Models`** module mein yeh functionality maujood hai. Jab aap SDK ko configure kar rahe honge, aap LiteLLM ko point kar sakte hain taake woh aapke pasandeeda models (jaisay Gemini) ko load kar sake.

*   **Yeh Kaise Faidamand Hai?**
    Yeh design aapko **cost effective** hone mein madad karta hai. Agar aapko OpenAI ke models se kam kharche par ya kisi khaas feature ke liye doosra model istemal karna hai, toh **LiteLLM** ke zariye aap usay asani se **OpenAI Agents SDK** ke saath integrate kar sakte hain. Yani, aap flexibility aur choice ka lutf utha sakte hain!

**Note**: Sources mein LiteLLM ke zariye Gemini ko specifically configure karne ka code nahi diya gaya hai. Lekin yeh bataya gaya hai ke aap **LiteLLM Models** ke option ke zariye kisi bhi model ko istemal kar sakte hain. Iska matlab hai ke aapko LiteLLM ki documentation dekhni parhegi ke Gemini model ko kaise configure kiya jata hai, aur phir us configuration ko **OpenAI Agents SDK** ke `Models` module mein apply karna hoga. Yeh aik **bahar ki maloomat (information from outside of the given sources)** hai ke aapko LiteLLM ki documentation dekhni parhegi, lekin yeh batana zaroori hai kyunki sources khud LiteLLM ko "any model" ke liye zikar karte hain.

Umeed hai ke yeh tafseeli Step 2 aapke liye mufeed sabit hoga. Ab aap tayaar hain mazeed advanced features explore karne ke liye! 🎉
```