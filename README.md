### code-alpha-python-tasks
## 1.chatbot-python
# 🤖 Basic Chatbot – Python

A simple **rule-based chatbot** built using Python.
The chatbot interacts with users through the command line and responds to predefined inputs such as greetings and basic questions.

---

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Python Programming Internship**.

The chatbot accepts user input and provides responses based on predefined rules using `if-elif` conditions.
It demonstrates how basic conversational logic can be implemented using Python.

---

## ⚙️ Features

* Simple command-line chatbot
* Responds to basic user inputs
* Continuous conversation using loops
* Exit command (`bye`) to stop the chatbot
* Easy to extend with more responses

---

## 🧠 Concepts Used

* Python **functions**
* **if-elif conditions**
* **loops**
* **input / output**
* **string processing**

---

## 📂 Project Structure

```id="cb1"
Basic_Chatbot
│
├── chatbot.py
└── README.md
```

---

## 💻 How to Run the Project

### 1️⃣ Clone the Repository

```id="cb2"
git clone https://github.com/your-username/Basic_Chatbot.git
```

### 2️⃣ Navigate to the Project Folder

```id="cb3"
cd Basic_Chatbot
```

### 3️⃣ Run the Python Script

```id="cb4"
python chatbot.py
```

---

## 🖥 Example Interaction

```id="cb5"
Simple Chatbot
Type 'bye' to exit

You: hello
Bot: Hi!

You: how are you
Bot: I'm fine, thanks!

You: what is your name
Bot: I'm a simple Python chatbot.

You: bye
Bot: Goodbye!
```
---

## 🎯 Objective

The objective of this project is to understand how **basic conversational systems** work by using simple Python logic and user input handling.

---

## 2. Humangame-python
# 🎮 Hangman Game – Python

A simple **text-based Hangman game** built using Python.
The player must guess the hidden word **one letter at a time** before running out of attempts.

---

## 📌 Project Overview

This project is part of the **CodeAlpha Python Programming Internship**.
The goal is to create a basic command-line Hangman game using core Python concepts.

The program randomly selects a word from a predefined list, and the player attempts to guess the word within **6 incorrect guesses**.

---

## ⚙️ Features

* Random word selection
* Letter-by-letter guessing
* 6 incorrect guess limit
* Displays current word progress
* Win / Lose game result

---

## 🧠 Concepts Used

* `random` module
* `while` loop
* `if-else` conditions
* `strings`
* `lists`
* `user input`

---

## 📂 Project Structure

```
Hangman_Game
│
├── hangman_game.py
└── README.md
```

---

## 💻 How to Run the Project

1. Clone the repository

```
git clone https://github.com/your-username/Hangman_Game.git
```

2. Navigate to the project folder

```
cd Hangman_Game
```

3. Run the Python program

```
python hangman_game.py
```

---

## 🖥 Example Output

```
Welcome to Hangman Game

Word: _ _ _ _ _ _
Guess a letter: p
Correct Guess!

Word: p _ _ _ _ _
Guess a letter:
```

---

## 🎯 Objective

The objective of this project is to practice:

* Python fundamentals
* Control flow
* Basic game logic
* User interaction through the console.

---

## 3. stack-tracker-python
# 📈 Stock Portfolio Tracker – Python

A simple **Stock Portfolio Tracker** built using Python that calculates the **total investment value** based on user input and predefined stock prices.

---

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Python Programming Internship**.
The program allows users to input stock names and quantities, then calculates the **total portfolio investment value** using predefined stock prices stored in a dictionary.

The final investment value is displayed in the console and saved to a text file.

---

## ⚙️ Features

* User inputs stock name and quantity
* Predefined dictionary of stock prices
* Calculates total portfolio value
* Displays individual stock investment value
* Saves final portfolio value to a `.txt` file

---

## 🧠 Concepts Used

* Python **dictionary**
* **User input / output**
* **Loops**
* **Basic arithmetic**
* **File handling**

---

## 📂 Project Structure

```id="stk1"
Stock_Portfolio_Tracker
│
├── stock_tracker.py
├── portfolio.txt
└── README.md
```

---

## 💻 How to Run the Project

### 1️⃣ Clone the Repository

```id="stk2"
git clone https://github.com/your-username/Stock_Portfolio_Tracker.git
```

### 2️⃣ Navigate to the Project Folder

```id="stk3"
cd Stock_Portfolio_Tracker
```

### 3️⃣ Run the Python Script

```id="stk4"
python stock_tracker.py
```

---

## 🖥 Example Output

```id="stk5"
Stock Portfolio Tracker

Enter stock name: AAPL
Enter quantity: 5
AAPL investment value = $900

Enter stock name: TSLA
Enter quantity: 2
TSLA investment value = $500

Enter stock name: done

Total Portfolio Value = $1400
Portfolio saved to portfolio.txt
```

---

## 📄 Generated File

After running the program, a file named:

```
portfolio.txt
```

will store the total investment value.

Example content:

```
Total Portfolio Value: $1400
```

---

## 🎯 Objective

The purpose of this project is to demonstrate:

* Basic **financial calculation using Python**
* Working with **dictionaries and loops**
* Handling **user input**
* Saving results using **file handling**

---

## 4. gmail-extract-python
# 📧 Email Extractor Automation Script – Python

A simple **Python automation script** that extracts all email addresses from a text file and saves them into another file automatically.

---

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Python Programming Internship**.

Manually finding email addresses in large text files can be time-consuming.
This Python script automates the process by scanning a text file, detecting email patterns using **Regular Expressions (Regex)**, and saving the extracted emails into a new file.

---

## ⚙️ Features

* Reads text data from a file
* Detects valid email addresses
* Extracts emails automatically
* Saves extracted emails to a new file
* Simple and efficient automation

---

## 🧠 Concepts Used

* Python **Regular Expressions (`re`)**
* **File handling**
* **Loops**
* **String processing**

---

## 📂 Project Structure

```id="em1"
Email_Extractor
│
├── email_extractor.py
├── emails.txt
├── extracted_emails.txt
└── README.md
```

---

## 💻 How to Run the Project

### 1️⃣ Clone the Repository

```id="em2"
git clone https://github.com/your-username/Email_Extractor.git
```

### 2️⃣ Navigate to the Project Folder

```id="em3"
cd Email_Extractor
```

### 3️⃣ Run the Python Script

```id="em4"
python email_extractor.py
```

---

## 📝 Example Input File

**emails.txt**

```id="em5"
hello@gmail.com
random text
contact@company.com
test@yahoo.com
info@website.org
```

---

## 🖥 Output

The script creates a new file:

```id="em6"
extracted_emails.txt
```

Example output:

```id="em7"
hello@gmail.com
contact@company.com
test@yahoo.com
info@website.org
```

---

## 🎯 Objective

The objective of this project is to demonstrate how **Python automation** can simplify repetitive tasks such as extracting structured information from text data.

---


## 👨‍💻 Author

**Yukesh**

---

## Connect
- LinkedIn: [www.linkedin.com/in/yukeshkanna022007]  
- GitHub: [https://github.com/yukeshkannayukeahkanna-afk]

---

## 📜 License

This project is created for **educational purposes** as part of the CodeAlpha Internship Program.
