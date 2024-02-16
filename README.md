👉 [picsou.streamlit.app](https://b-picsou.streamlit.app)

1. open repo in a new **Code space** (or create a **dedicated VM** and clone repo)
2. install useful **VSCode extensions**
    - Pylint
    - Jupyter TOC
    - Rust-Analyzer (rust-lang.org)
    - Github Copilot
3. define a [**devcontainer**](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
4. **create venv** in home : `cd ~ && virtualenv venv`
5. **activate** venv : `source venv/bin/activate`
6. **automate venv activation** by adding it to .bashrc : `nano ~/.bashrc` et ajout `source venv/bin/activate`
7. **restart** shell
8. **check** venv automation worked and you are in venv
9. **check requirements.txt** is up-to-date
10. **install project dependencies** : `make install`

# App overview

A very simple and interactive compound interests calculator.  
Designed in Euro € with account taken of French taxation (PFL).
