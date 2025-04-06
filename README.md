# learn-ai

This repository is for learning and experimenting with Artificial Intelligence concepts and technologies, with a current focus on Google Generative AI Large Language Models (LLMs).

## Getting Started

1.  **Prerequisites:** Ensure you have Python 3.x, pip, and Git installed on your system.

2.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd learn-ai
    ```
    (Replace `<repository_url>` with your repository's URL)

3.  **Set Up Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(This command installs the necessary packages listed in `requirements.txt`.)*

5.  **Create `requirements.txt` (if it doesn't exist or to update):**
    ```bash
    pip freeze > requirements.txt
    ```
    *(This command captures the currently installed packages in your virtual environment.)*

6.  **Configure API Key:**
    * Create a `.env` file: `touch .env`
    * Add your Google Generative AI API key to `.env`:
      ```
      GOOGLE_API_KEY=<YOUR_API_KEY>
      ```

## Code Structure

* **`hello_llm.py`**: Demonstrates interaction with a Google Generative AI LLM using LangChain.
* **`.env`**: Stores environment variables, like your API key (not to be committed to version control).
* **`requirements.txt`**: Lists project dependencies for easy installation.

## Running the Example

1.  Activate your virtual environment:
    ```bash
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```
2.  Navigate to the repository directory:
    ```bash
    cd learn-ai
    ```
3.  Execute the script:
    ```bash
    python hello_llm.py
    ```

## `hello_llm.py` Explained

This script initializes and uses the `ChatGoogleGenerativeAI` model from the `langchain-google-genai` library to generate a response to a simple prompt.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Error: GOOGLE_API_KEY environment variable is not set.")

# Initialize Google Generative AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    max_output_tokens=256,
    top_p=0.9,
    top_k=40,
    api_key=api_key
)

# Generate and print the response
response = llm.invoke("Hello, How are your, please Introduce yourself!")
print(response)
```

# Python packages to install
pip install langchain-google-genai
pip install python-dotenv

# Basic git usage
```
1. Initialize a Git repository (if you haven't already):
git init

2. Add files to staging:
git add .

3. Commit changes:
git commit -m "Your descriptive commit message here"
e.g. git commit -m "Initial commit with LLM integration"

4.a Create a new branch (e.g., develop):
git checkout main  # Or master
git branch develop
git checkout develop

4.b Create a new local branch based on another existing branch:
git checkout -b <new_branch_name> <base_branch_name>
e.g git checkout -b feature-branch main
This will create a new local branch named feature-branch that is a copy of your current main branch and immediately switch you to the feature-branch.

4.c Clone from a remote branch (origin/develop)
git checkout -b bugfix-branch origin/develop
This will create a new local branch named bugfix-branch that is based on the develop branch from the remote repository named origin, and switch you to bugfix-branch. Git will also set up a tracking relationship with origin/develop.

5. Push your local branch to the remote repository (e.g., origin):
git push -u origin develop
(The -u flag sets up tracking between your local and remote branch.)

6. Switch between branches:
git checkout main  # Or develop

7. Merge branches (e.g., merge develop into main):
git checkout main
git merge develop

8. List local branches:
git branch
(* marked branch is your current branch)
eg.   main
    * develop
In this example, develop is the currently active branch.

9. List remote branches: 
git branch -r

The output will show the remote branches, typically prefixed with the remote name (e.g., origin/main, origin/develop).
  origin/HEAD -> origin/main   // HEAD here is Remote's Default: It generally reflects the default branch configured on the remote repository.
  origin/main
  origin/develop

10. List local & remote branches:
git branch -a

* develop
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
  remotes/origin/develop

11. Verify Your Staged Changes (Optional but Recommended):
git status
This will show you files that are staged for commit under the "Changes to be committed" section. It will also show you unstaged changes.
