# Efficient LLM Data Handling with Excel/CSV

## Why This Exists
This repo is a personal project to solve a very specific issue: using Large Language Models (LLMs) effectively for tasks involving Excel data processing and enabling LLMs to process Excel/CSV files efficiently.

## What This Does
1. **Excel Data Processing:** Prepares and processes Excel/CSV data specifically for LLM usage.
2. **LLM Agent Integration:** Handles LLM agent workflows and interactions with processed data.
3. **LLM-Specific Tasks:** Optimizes the way LLMs interact with structured data like Excel files for better results.

**Out of Scope:**
- Conversation UI (e.g., Streamlit)
- General-purpose Excel reading tools (this assumes you have the data ready to go).
- Broad data aggregation or non-LLM-related processing tasks.

## Tech Stack
This project plans to uses:
- **Python:** The backbone of it all.
- **Poetry:** For dependency management and keeping the project organized.
- **LangChain:** To streamline LLM workflows.


## Installation (WIP)

### What You Need
- Python 3.8 or newer.
- Poetry installed on your system.

### Get Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm-data-injection.git
   cd llm-data-injection
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```

## How to Use It
1. Prepare your Excel file (make sure it’s ready for processing—this repo assumes clean data).
2. Use the provided scripts to preprocess the data and inject it into the LLM pipeline.
3. Run the LLM agent to handle queries, summaries, or any task you define.

## Why You Might Like This
- You’re focused on integrating Excel data with LLM agents, not on building UI or generic tools.
- You want streamlined scripts for Excel-to-LLM workflows.
- You need a specialized solution, not a generic one.

## Contributing
Feel free to contribute. Fork the repo, make your changes, and submit a pull request!

## Roadmap
Here’s the narrowed-down focus:
1. Build rock-solid Excel data preprocessing for LLMs.
2. Develop and refine LLM agent workflows.
3. Add optimizations for common LLM tasks involving structured data.
