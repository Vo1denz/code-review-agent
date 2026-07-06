# GitHub PR Review Agent

An AI-powered Pull Request Review Agent built using **LangChain**, **Groq LLM**, and the **GitHub REST API** that automatically analyzes GitHub Pull Requests for security vulnerabilities, code quality issues, and missing test coverage.

Instead of manually reviewing every line of code, this agent performs parallel AI-powered analysis and generates structured review comments that can be posted directly back to the GitHub Pull Request.

---

## Features

- Security vulnerability detection
- Code quality and maintainability analysis
- Test coverage suggestions
- Parallel multi-agent architecture using LangChain
- GitHub PR diff parsing
- Automatic Markdown review generation
- GitHub Review Comment integration
- Structured outputs using Pydantic models
- Rate limiting and retry handling
- LangSmith tracing support

---

## Architecture

```
                GitHub Pull Request URL
                        │
                        ▼
              PR URL Parser
                        │
                        ▼
             GitHub REST API Fetcher
                        │
                        ▼
               Unified Diff Parser
                        │
                        ▼
            RunnableParallel (LangChain)
        ┌──────────┬──────────────┬──────────────┐
        ▼          ▼              ▼
 Security Agent  Quality Agent  Test Agent
        └──────────┴──────────────┴──────────────┘
                        │
                        ▼
              Pydantic Structured Output
                        │
                        ▼
             Markdown Review Formatter
                        │
                        ▼
          GitHub Pull Request Comment
```

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | LangChain |
| LLM | Groq (Llama 3.3 70B) |
| API | GitHub REST API |
| Validation | Pydantic |
| Diff Parsing | unidiff |
| CLI | argparse |
| Environment | python-dotenv |
| Observability | LangSmith |

---

## Project Structure

```
github-pr-review-agent/
│
├── agents/
│   ├── security_agent.py
│   ├── code_quality_agent.py
│   ├── test_coverage_agent.py
│   └── orchestrator.py
│
├── middleware/
│   ├── rate_limiter.py
│   ├── retry_handler.py
│   └── langsmith_tracer.py
│
├── models/
│   └── schemas.py
│
├── tools/
│   ├── github_fetcher.py
│   ├── diff_parser.py
│   └── comment_poster.py
│
├── utils/
│   ├── pr_url_parser.py
│   └── markdown_formatter.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Workflow

1. User provides a GitHub Pull Request URL.
2. The PR URL is parsed to extract the repository details.
3. GitHub API fetches PR metadata and the unified diff.
4. The diff is parsed into individual file hunks.
5. LangChain runs three AI agents in parallel:
   - Security Agent
   - Code Quality Agent
   - Test Coverage Agent
6. Results are merged into a structured `PRReview` object.
7. The review is converted into GitHub-flavored Markdown.
8. The generated review can be posted back to the Pull Request.

---

## Security Checks

The Security Agent can identify issues such as:

- Hardcoded API keys
- Hardcoded passwords
- SQL Injection
- Command Injection
- Path Traversal
- Insecure Deserialization
- Weak Authentication
- Weak Cryptography
- Sensitive information exposure
- General security best practices

---

## Code Quality Checks

The Quality Agent reviews code for:

- Readability
- Maintainability
- Naming conventions
- Function complexity
- Duplicate code
- Large functions
- Poor code organization
- Best practices
- Performance improvements
- Clean code principles

---

## Test Coverage Checks

The Test Coverage Agent detects:

- Missing unit tests
- Untested edge cases
- Missing negative test cases
- Boundary condition coverage
- Error handling scenarios
- Regression risks

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/github-pr-review-agent.git

cd github-pr-review-agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```env
GITHUB_TOKEN=your_github_token
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
```

---

## Usage

```bash
python main.py \
--pr https://github.com/owner/repository/pull/15
```

---

## Example Output

```markdown
# AI Pull Request Review

## Security Issues

🔴 High
- Hardcoded API key detected in auth.py

🟠 Medium
- Potential SQL Injection in user_service.py

---

## Code Quality

🟡 Medium
- Function exceeds recommended complexity

🟢 Low
- Variable naming can be improved

---

## Test Coverage

🟠 Missing tests for invalid authentication flow

🟡 Boundary cases for empty input are not covered
```

---

## Future Improvements

- GitHub Action integration
- Inline code review comments
- Support for multiple LLM providers
- Repository-wide context retrieval
- RAG-based code understanding
- Multi-language support
- Severity scoring dashboard
- Web interface using Streamlit or FastAPI

---

## Learning Outcomes

This project demonstrates practical experience with:

- LangChain Agent Architecture
- AI-powered Code Review
- GitHub REST API Integration
- Parallel LLM Workflows
- Prompt Engineering
- Structured LLM Outputs
- Pydantic Validation
- Software Security Analysis
- Diff Parsing
- Production-ready Python Design

---

## License

This project is licensed under the MIT License.

---

## Author

**Void**

Passionate about AI, Agentic Systems, and Software Engineering.

Always building projects that solve real developer problems.