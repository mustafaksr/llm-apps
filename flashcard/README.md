# Flashcard App

The Flashcard App is a web application that allows you to create and display interactive flashcards. It provides a user-friendly interface to create a grid of flashcards with customizable rows and columns. Each flashcard has a front and back side that can be flipped to reveal the information on the other side.

## Features

- Dynamic grid: Specify the number of rows and columns for the flashcard grid.
- Interactive flip animation: Click on a flashcard to flip it and reveal the information on the back side.
- Customize flashcard content: Enter your own text for the front and back sides of the flashcards.

## Technologies Used

- Front-end: HTML, CSS, JavaScript
- Back-end: Python, Flask

## Getting Started

### 1.Prerequisites

requirements.txt

### 2.Installation

 Clone the repository:

```bash
git clone https://github.com/mustafaksr/llm-apps.git
cd ~/llm-apps/flashcard
```

### 3.Navigate to the project directory:
```bash
cd ~/llm-apps/flashcard
```

### 4.Create env:
```bash
virtualenv llm
```

```bash
source llm/bin/activate
```


### 5.Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 6.Auth for test:
```bash
gcloud auth login
```


### 7.Usage
Start the Flask development server:
```bash
export PORT=5000
python3 main.py
```
Open your web browser and visit http://localhost:5000 to access the Flashcard App.
Enter the desired number of rows and columns in the input fields and click the "Create" button to generate the flashcards.
Hover on a flashcard to flip it and reveal the information on the back side.

