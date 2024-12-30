# Browsing History Management

## Overview
This project implements a **Browsing History Manager** using a **Stack** data structure in Python. It simulates the behavior of a web browser's history, where users can:

1. **Add a new page** - Pushes a new page URL onto the stack.
2. **Remove the last visited page** - Pops the most recent page off the stack.
3. **View the total number of pages** - Displays the total count of pages stored in the browsing history.
4. **Check if the history is empty** - Determines whether the stack has any pages.
5. **Display browsing history** - Lists all pages in reverse order (last visited first).

## Why This Approach?
The **stack** structure (Last In, First Out - LIFO) was chosen because it closely models how browser navigation works:
- The most recently visited page is accessed first.
- Users often navigate backward through history, which aligns with stack behavior.

Using a stack simplifies operations like adding and removing pages, providing efficient performance for these tasks.

## Features
- **Input Validation**: Ensures URLs are non-empty strings.
- **Error Handling**: Handles attempts to remove pages from an empty stack gracefully.
- **Interactive Output**: Prints clear messages for each operation, making the system easy to test and debug.

## Usage
1. Initialize the browsing history manager.
2. Use the provided methods to simulate adding, removing, and viewing history.
3. Run the script, and outputs will display in the console.

## Future Enhancements
- Add a **forward navigation** feature to revisit removed pages.
- Implement **search functionality** to locate specific pages in history.
- Save browsing history to a file for persistence across sessions.

---
**Author:** Jose  
**Date:** December 30, 2024