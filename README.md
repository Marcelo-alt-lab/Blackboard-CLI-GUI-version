# 🎓 Blackboard CLI (UPC) — AI Study Notebook Sync

Modern and professional console tool for **Blackboard Ultra (UPC)**. Synchronize your courses, weekly materials, assessments, and official announcements, organizing them into **Markdown Study Notebooks** ready to be read by you or any Artificial Intelligence (Antigravity, Claude, ChatGPT, Gemini, etc.).

---

## ⚡ Quick Start (Hassle-free)

You don't need to manually configure environments. The program includes automatic managers for Windows and macOS/Linux.

1. **Download and unzip:**
   - Download the [Blackboard-CLI.zip](https://github.com/jwd3t/Blackboard-CLI/releases) file from the **Releases** section of this repository and unzip it into any folder on your computer.
2. **Run:**
   - **On Windows:** Double-click on **`BlackboardCLI-v*.bat`** (e.g., `BlackboardCLI-v2.2.0-Windows.bat`).
   - **On Mac:** Double-click on **`BlackboardCLI-v*.command`** (or in the terminal: `./BlackboardCLI-v*.command`).
   - **On Linux:** Open the terminal in the folder and run **`./BlackboardCLI-v*.sh`**.
   - *First time note:* On its first boot, the program will automatically create an isolated virtual environment (`.venv`) and install the necessary libraries. **It will not leave any residue on your system.**
3. **Log in:**
   - In the main menu, select the `[5] login` option.
   - A browser window will open where you can log in with your UPC email (`@upc.edu.pe`), institutional password, and confirm your two-step verification (2FA).
   - Done! Your session will be securely saved locally.

---

## 🖥️ Interactive Menu

When you start the application, you will see the interactive console with the following options:

| Option | Command | Description |
| :---: | :--- | :--- |
| `[1]` | `sync` | **Synchronizer:** Allows downloading the entire semester or choosing a specific course and week. |
| `[2]` | `agenda` | **Assessment Radar:** Lists exams, assignments, and due dates ordered chronologically. |
| `[3]` | `cursos` | **Subjects:** Table with your active courses of the cycle and their codes. |
| `[4]` | `status` | **Diagnostics:** Check the connection status with the Ultra server and your student profile. |
| `[5]` | `login` | **Log In:** Opens the browser to authenticate via Microsoft 365 / SSO. |
| `[6]` | `logout` | **Log Out:** Immediately deletes your local credentials and cookies from your PC. |
| `[7]` | `notebook`| **Export to Gemini Notebook:** Generates a flat folder (`gemini_notebook/`) optimized for NotebookLM. |
| `[0]` | `exit` | Closes the application. |

> 💡 **Navigation Tip:** Inside the synchronization menus, you can type **`v`** at any time to return to the previous screen without closing the program.

---

## 📁 Structure of Generated "Study Notebooks"

When synchronizing, a folder named `cuadernos/` (notebooks) will be created with a clean and standardized structure:

```text
cuadernos/
├── RESUMEN_SEMESTRE_IA.md        <-- 🧠 General index of the cycle with exam radar
└── [CODE] Course Name/
    ├── CUADERNO_CURSO.md         <-- 📓 Master course notebook with formulas and links
    ├── 00_INFORMACION_GENERAL/   <-- 📄 Syllabi, course rules, and calendar plan
    ├── 01_EVALUACIONES_Y_EXAMENES/
    │   └── agenda_evaluaciones.md <-- 📅 Dates, assessment topics, and weights
    ├── 02_MATERIALES_Y_CLASES/   <-- 📚 Content organized by Weeks or Units
    │   ├── Semana 01/
    │   └── Semana 02/
    ├── 03_ANUNCIOS/
    │   └── historial_anuncios.md <-- 📢 Official announcements from the professor
    └── gemini_notebook/          <-- 🤖 (Optional) Flat folder generated with the `notebook` command ready to drag to NotebookLM
```

---

## 🤖 How to study with AI using these notebooks?

Once your notebooks are downloaded, you can open the folder in your favorite editor (Cursor, VS Code, Obsidian) or drag the files to any AI:

* **Ask about assessments:**
  > *"What assessments do I have in the next two weeks and which one has the highest percentage weight?"*
  *(The AI will read `cuadernos/RESUMEN_SEMESTRE_IA.md` and the agendas).*
* **Study weekly topics:**
  > *"Explain simply the theoretical content of Week 03 of this course."*
  *(The AI will consult the Markdown files of the selected week).*
* **Consult grading formulas:**
  > *"How much do I need to score on the final exam to pass the course according to the syllabus formula?"*

---

## 🔒 Privacy and Security

* **Your credentials are never shared:** Neither your passwords nor your session cookies are uploaded to any external server. Everything runs 100% locally on your machine.
* **The `package` command is secure:** If you want to share the tool with a friend, the `[7] package` option generates a ZIP that automatically excludes your personal files, notes, and sessions.

---

## 🛠️ System Requirements

* **Windows:** Windows 10 or Windows 11 (64-bit).
* **macOS:** macOS Catalina (10.15) or higher.
* Have Python 3.9 or higher installed (Python 3.10+ recommended; on Windows check *"Add python.exe to PATH"*; on Mac install via `brew install python` or python.org). The startup scripts will handle everything else.

---

## 📄 License

This project is protected under the **GNU General Public License v3.0 (GPLv3)**.
See the [LICENSE](LICENSE) file for more details.

*Free use, study, and improvement of the code is allowed, but any derivative must remain under the same open license, always guaranteeing credit to the original author and prohibiting the appropriation or closing of the software.*
