# 📘 Automated Book Publication Workflow System

## 🎯 Objective

Develop a system that automates the process of fetching web-based book content, transforms it through AI-driven iterations, and manages versioned content with human-in-the-loop refinements and intelligent retrieval.

---

## 🚀 Key Features

### 1. 📥 Scraping & Screenshots
- Fetch content from [The Gates of Morning - Chapter 1](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1).
- Capture full-page screenshots using `Playwright`.

### 2. 🤖 AI Writing & Reviewing
- Use a Large Language Model (e.g., Gemini or GPT) to:
  - **Spin** the raw content (AI Writer).
  - Review and refine the spun content (AI Reviewer).

### 3. 👥 Human-in-the-Loop Iteration
- Enable human writers, reviewers, and editors to:
  - Suggest edits.
  - Track review comments.
  - Finalize content after multiple iterations.

### 4. 🧠 Agentic API Integration
- Use a modular system for content flow:
  - `WriterAgent` → `ReviewerAgent` → `EditorAgent`
- Agents communicate using clean, version-tracked APIs.

### 5. 🗂️ Versioning & Retrieval
- Store all content versions using **ChromaDB**.
- Use a **Reinforcement Learning (RL) Search Algorithm** for context-aware, consistent retrieval of the latest/finalized versions.

---

## 🛠️ Core Technologies

| Tool       | Role                                  |
|------------|---------------------------------------|
| Python     | Primary development language          |
| Playwright | Web scraping & screenshot capture     |
| LLM        | AI content generation & editing       |
| ChromaDB   | Versioned vector storage              |
| RL Search  | Consistent content retrieval          |

---

## 🛠️ Recommended: Use a Virtual Environment

It's recommended to run this project inside a Python virtual environment.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

## 📹 Demo Video

## 📹 Demo Video

A complete demo video is available on Google Drive.

🎥 [Click here to watch the demo](https://drive.google.com/file/d/1hxatRDXVUPevo2N1zg1kRcMTIIewcp3l/view?usp=sharing)


🎥 The video demonstrates:
- Web scraping and screenshot capturing  
- AI-based spinning and reviewing of chapters  
- Human-in-the-loop feedback integration  
- Content versioning with ChromaDB  
- Final retrieval using RL-based search


## 📁 Project Structure

automated-book-workflow/
├── ai_writer.py # WriterAgent: Generates spun content using LLM
├── reviewer.py # ReviewerAgent: Reviews and refines AI-generated content
├── editor.py #  EditorAgent: Final refinement and approval
├── fetcher.py # Orchestrates the agent flow: Writer → Reviewer → Editor
├── scrape_chapter.py # Scrapes book content from the web using Playwright
├── screenshot.py # Captures full-page screenshots of the chapter
├── version_manager.py # Handles versioning and ChromaDB storage
├── requirements.txt # Python dependencies list
├── README.md # Project overview and documentation
├── LICENSE 
├── .gitignore # Git ignored files (e.g., env/, pycache)
├── .env # Environment variables (e.g., API keys)
├── chroma_store/ # Stores ChromaDB index and versioned content
├── output/ # Output folder for screenshots and content files
├── env/ # Python virtual environment (should be ignored)
└── pycache/ # Python cache files (auto-generated; should be ignored)


## 📦 Dependencies

All dependencies are listed in `requirements.txt`. To install:

```bash
pip install -r requirements.txt


