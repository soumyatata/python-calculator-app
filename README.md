# **Python Calculator App**

A simple calculator app built with **Python** using the `tkinter` library for the graphical user interface. This app supports basic arithmetic operations (addition, subtraction, multiplication, division), exponentiation (`x²`), percentage, and more. It also provides a clear history, a backspace feature, and limits decimal results to 2 places.

## **Features**

- **Basic Operations**: Addition, subtraction, multiplication, and division.
- **Exponentiation**: Using `x²` to raise a number to the power of 2.
- **Percentage**: Use `%` to calculate percentages.
- **Clear (AC)**: Clears the input field.
- **Backspace**: Allows removing the last entered digit or operator.
- **Decimal**: Supports decimal points for operations.
- **Formatted Results**: Results are rounded to 2 decimal places for division.

## **Installation**

1. **Clone the repository to your machine:**
    ```bash
    git clone https://github.com/yourusername/python-calculator-app.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd python-calculator-app
    ```

3. **Install Python if you haven't already.** You can download it from [python.org](https://www.python.org/).

4. This project requires the `tkinter` library, which comes pre-installed with Python. If it's not installed, you can install it using:
    ```bash
    pip install tk
    ```

## **Usage**

1. **Run the app:**
    After installation, navigate to the project folder and run the Python script:
    ```bash
    python calculator.py
    ```

2. **Using the calculator:**

    - **Input numbers**: Click on the number buttons (0-9).
    - **Operations**: Use `+`, `-`, `x`, `/` to perform basic arithmetic.
    - **Exponentiation**: Click `x²` to square the number.
    - **Percentage**: Use `%` to perform percentage calculations.
    - **Decimal**: Click `.` to input decimal numbers.
    - **Clear**: Click `AC` to clear the input screen.
    - **Backspace**: Use `<-` to remove the last character.

3. **Results**: The results are displayed at the top of the window, and for divisions, results are rounded to 2 decimal places.

## **Example Usage**

- To calculate the square of `5`, press `5`, then `x²`, and the result `25` will appear.
- To calculate `5 + 7`, press `5`, `+`, `7`, and `=` to get the result `12`.
- To calculate 10% of 50, press `50`, `%`, and the result `0.5` will appear.

## **Project Structure**

```bash
python-calculator-app/
│
├── calculator_app.py          # Main application script
└── README.md                  # This README file
```