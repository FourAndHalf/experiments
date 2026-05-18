# Code Reviewer Agent Workflow (CodeRabbit Style)

This document outlines the operational flow the Code Reviewer agent follows when tasked with reviewing code, modeled after CodeRabbit's automated PR review process.

## 1. Context & Diff Gathering
1.  **Identify Changes:** Use `run_shell_command` (`git diff --cached` or `git diff HEAD`) to identify modified files and line-level changes.
2.  **Analyze Context:** Read project-level documentation (`GEMINI.md`) and use `read_file` to fetch the surrounding functions and classes for the modified lines. Ensure you understand the state of the code *before* and *after* the change.

## 2. Comprehensive Analysis Phase
1.  **Bug Detection:** Look for logic flaws, off-by-one errors, unhandled exceptions, and race conditions.
2.  **Security Audit:** Check for unsanitized inputs, hardcoded secrets, and insecure dependencies.
3.  **Code Quality:** Verify naming conventions, adherence to DRY/SOLID principles, and maintainability.

## 3. CodeRabbit-Style Generation
The agent synthesizes its findings into a highly structured markdown report containing four mandatory sections:

### 📝 Summary
A high-level overview of the entire changeset. Answers "What is the purpose of this review?"

### 🚀 Release Notes
A bulleted, changelog-ready summary of the architectural and user-facing changes.

### 💻 Walkthrough
A file-by-file summary of the modifications. Provides the reviewer with a map of where changes occurred.

### 💬 Review Comments (Inline Simulation)
Instead of a wall of text, the agent simulates inline PR comments. Each comment targets a specific file and line number, categorized by severity:
*   🔴 **Critical:** Must-fix bugs and security flaws.
*   🟡 **Suggestion:** Best-practice improvements.
*   🔵 **Nitpick:** Minor stylistic tweaks.
*   🟢 **Praise:** Highlighting good engineering practices.

*Actionable Suggestions & AI Prompts:* Where applicable, the agent provides a `suggestion` code block. Additionally, it provides an **🤖 AI Action** prompt for each issue, and a combined **🤖 AI Auto-Fix Summary** at the end of the report, enabling the user to easily automate the application of the review feedback using their main AI assistant.