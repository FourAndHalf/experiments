# Code Reviewer Agent Architecture

## Overview
The Code Reviewer agent is a specialized subagent designed for the Gemini CLI. Its primary role is to provide automated, high-fidelity code reviews by analyzing changes within a git repository. It is a **local** agent, meaning it operates within the user's environment and has access to local tools.

## System Components

### 1. Interaction Model
*   **Invocation:** Can be called explicitly via `@code-reviewer` or delegated to by the main agent when a request for a code review is detected.
*   **Delegation Logic:** The main agent delegates tasks to `code-reviewer` when it identifies a need for in-depth analysis of code quality, security, or architectural alignment.

### 2. Capabilities & Toolset
The agent is granted a specific set of tools to perform its duties:
*   `run_shell_command`: Essential for fetching git diffs (`git diff`, `git log`), running linters, or checking branch status.
*   `read_file`: Used to read the content of files identified in diffs or for exploring project-wide configuration.
*   `grep_search`: Used to search for patterns (e.g., checking for consistent usage of a library across the project).

### 3. Intelligence Model
*   **Persona:** Senior Staff Software Engineer / Lead Architect.
*   **Analytical Focus:** 
    *   Logic correctness and edge case handling.
    *   Security vulnerabilities (OWASP Top 10 focus).
    *   Maintainability and adherence to DRY/SOLID principles.
    *   Compliance with project-specific `GEMINI.md` instructions.

## Security & Privacy
As a local subagent, it respects all user-defined policies and does not transmit code outside the local environment unless explicitly configured for a remote model. It is bound by the same safety constraints as the main Gemini CLI agent.
