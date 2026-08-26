# CISC 4080 Lab 0

## Goal

1. Get familiar with Python programming;
2. Practice using basic data structures in Python: list



## Preparation

1. Download Python IDE ([VS Code](https://code.visualstudio.com/download?_exp_download=fb315fc982) or [Pycharm](https://www.jetbrains.com/pycharm/)). If you want to use the interactive code block shown in the first class, you can also download the **Jupyter** extension in VS code.

2. Download lab0.py in this repo.



## Overall requirements

Please write comments for your functions. Test your functions by using manually created list, and lists created using the RandomList function provided in the code.



## Detailed Requirements

1. Implement a function **`BubbleSort`** to sort a list in ascending order. Call this function on some short lists to test it.

2. Implement a function **`SortedCheck`** to test if the list(s) you sorted using BubbleSort is in ascending order or not. The function shall return True or False. 

3. Implement a function **`CheckDuplicate_Sorted`** to test if a sorted list contain duplicates or not. The function return True or False based upon the checking result. Call this function on some short lists to test it.

4. Implement a function **`CheckDUplicate_Unsorted`**to test if an unsorted list contnain duplicates or not. And also call this function on selveral short lists to test it.

5. Implement a function **`IsPalindrome`** that determines whether a given string is a palindrome.

   A **palindrome** is a word or sequence that reads the same forward and backward. For example, `"kayak"` is a palindrome because reversing it gives the same string, while `"Welcome"` is not.

   Test your function on several strings. For example:

   ```python
   IsPalindrome("Welcome")   # False
   IsPalindrome("kayak")     # True
   ```

    Please review [this](https://python.pages.doc.ic.ac.uk/cpp/lessons/cpp/04-seq/07-strseq.html) to familarize yourself with **str** in Python. Essenntnially, a string (str) in Python is a list of char. So you can use the list slicing to index a character or a sequence of characters in a string.



## Deadline

11:59 PM, September 2, 2026



**Note:**

1. Please name your python file as **lab0_{your_name}.py** and submit on Blackboard.
2. Please do not use any python built-in function such as ``sorted()`` to write your code. 