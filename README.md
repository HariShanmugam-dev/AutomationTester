
# 📦 Automation Tester

An intelligent desktop application UI testing solution built in Python — designed to automate, validate, and report on end-to-end user interactions through screen-based validation and active window management.

## 📖 Overview

**Automation Tester** is a lightweight, modular, and highly extensible automated testing framework for desktop applications. Whether testing static UIs or highly dynamic interfaces, Automation Tester captures user actions, replays them, validates application state via screenshots, and generates detailed reports — all with minimal human intervention.

---

## 🏗️ Architecture Summary

The system is composed of 4 key modules:

- **Recorder**: Captures mouse movements, clicks, keyboard inputs, and precise time intervals.
- **Test Executor**: Replays recorded test scripts simulating real user behavior.
- **Validator**: Compares screenshots and monitors active window titles for reliable execution.
- **Reporter**: Generates structured, PDF-format reports on test outcomes.

---

## 📊 High-Level Workflow

1. **Recording Phase**
   - Launch the recorder, interact with the application.
   - Every interaction and UI screenshot is logged into a JSON-based test script.

2. **Test Execution Phase**
   - Load a recorded test case.
   - Replay all actions sequentially with exact delays.
   - Capture screenshots and verify against recorded references.

3. **Validation Phase**
   - Compare UI screenshots step-by-step.
   - Validate active window focus.
   - Mark discrepancies or application window losses.

4. **Reporting Phase**
   - Generate a polished PDF report including:
     - Test Case ID & Description
     - Pass/Fail status per step
     - Visual diff screenshots for failed steps
     - Error explanations

---

## 📦 Tech Stack

| Purpose                 | Library         |
|:------------------------|:----------------|
| GUI Framework           | `PySide6`       |
| Mouse/Keyboard Control  | `pyautogui`      |
| Input Listener          | `pynput`         |
| Active Window Management| `pygetwindow`    |
| Screenshot Comparison   | `scikit-image`   |
| PDF Report Generation   | `reportlab`      |

---

## 📝 Installation

> **Prerequisites**: Python 3.9+

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automation-tester.git
   cd automation-tester
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## 📄 Test Case Structure (JSON)

Each test case is stored as a structured JSON file:

```json
{
  "TestCaseID": "TC001",
  "TestCaseDescription": "Login form validation test",
  "TestCaseSteps": [
    "pyautogui.moveTo(200, 300)",
    "pyautogui.click()",
    "pyautogui.typewrite('testuser')"
  ]
}
```

---

## 📑 Report Format

- PDF report generated post-execution
- Includes:
  - Test Case ID & description
  - Pass/Fail status
  - Screenshot comparisons for failed steps
  - Active window validation outcomes

---

## 🚀 Planned Improvements

- **Dynamic UI Handling**
  - Implement adjustable delay capture or event-listening triggers to replace fixed 300ms screenshot delays.

- **Masking for Dynamic Data**
  - Exclude volatile regions (like timestamps or transaction IDs) from visual validation.

- **OCR Integration**
  - Incorporate OCR (Optical Character Recognition) to verify dynamic textual data behind masked UI components.

---

## 📌 Limitations

- Currently optimized for single-monitor setups.
- Designed for Windows-based applications (Linux/macOS support possible with minor adjustments).

---

## 📢 Contribution Guidelines

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature: your feature"
   ```
4. Push and open a pull request.

---

## 🧑‍💻 Author

**Hari Hara Sudhan Shanmugam**  
📧 [contacthari.dev@gmail.com](mailto:contacthari.dev@gmail.com)  
🌐 [harishanmugam.com](https://harishanmugam.com](https://harishanmugam-dev.github.io/portfolio/))

---

## 📃 License

MIT License — free to use, modify, and distribute.
