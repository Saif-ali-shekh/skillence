import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillence.settings')
django.setup()

from App_Models.models import Question, Option

def populate_data():
    questions = [
        "What is the output of 'print(2 ** 3)' in Python?",
        "Which keyword is used to define a function in Python?",
        "What does 'len()' function do in Python?",
        "How do you create a list in Python?",
        "What is a dictionary in Python?",
        "How do you add an element to a set in Python?",
        "Which operator is used for integer division in Python?",
        "What is a lambda function in Python?",
        "How do you handle exceptions in Python?",
        "What is a list comprehension in Python?",
        "How do you import a module in Python?",
        "What is a tuple in Python?",
        "How do you check the data type of a variable in Python?",
        "What does 'break' do in a loop in Python?",
        "What is slicing in Python?",
        "How do you define a class in Python?",
        "What is the purpose of '__init__' in a class?",
        "How do you inherit a class in Python?",
        "What is a generator in Python?",
        "How do you create a virtual environment in Python?",
        "What is the use of 'pass' statement in Python?",
        "What is the 'self' keyword in Python?",
        "How do you read a file in Python?",
        "What is the difference between '==' and 'is' in Python?",
        "How do you convert a string to an integer in Python?",
        "What does 'map()' function do in Python?",
        "How do you remove an item from a list in Python?",
        "What is the purpose of 'with' statement in Python?",
        "How do you get the current date and time in Python?",
        "What is PEP 8 in Python?",
    ]

    options = [
        ["8", "6", "9", "7"],
        ["def", "function", "fun", "define"],
        ["Returns length", "Concatenates strings", "Splits strings", "None"],
        ["Using brackets", "Using parentheses", "Using braces", "Using quotes"],
        ["Key-value pairs", "List of elements", "Set of elements", "Tuple of values"],
        ["add()", "append()", "insert()", "update()"],
        ["//", "/", "%", "**"],
        ["Anonymous function", "Normal function", "Class method", "Built-in function"],
        ["try-except", "catch-throw", "handle-catch", "begin-rescue"],
        ["Compact way to create lists", "Way to sort lists", "Way to reverse lists", "Way to shuffle lists"],
        ["import module_name", "include module_name", "require module_name", "using module_name"],
        ["Immutable list", "Mutable list", "Unordered list", "Dictionary"],
        ["type()", "check()", "var_type()", "dtype()"],
        ["Exits the loop", "Continues the loop", "Skips an iteration", "Returns a value"],
        ["Accessing parts of strings/lists", "Joining strings", "Removing elements", "Sorting lists"],
        ["class ClassName:", "def ClassName:", "function ClassName:", "create ClassName:"],
        ["Initializes class", "Deletes class", "Modifies class", "Defines methods"],
        ["Using parentheses", "Using 'inherit' keyword", "Using 'extends' keyword", "Using '->' symbol"],
        ["Function that returns iterator", "Function that sorts lists", "Function that filters lists", "Function that maps lists"],
        ["Using 'venv'", "Using 'env'", "Using 'virtual'", "Using 'env_manager'"],
        ["Does nothing", "Ends the program", "Starts a loop", "Starts a function"],
        ["Reference to instance", "Reference to class", "Reference to method", "Reference to function"],
        ["open() and read()", "file() and read()", "read() and openfile()", "readfile()"],
        ["Checks value equality", "Checks memory location", "Checks type", "Checks both value and type"],
        ["int()", "str()", "float()", "convert()"],
        ["Applies a function to elements", "Maps elements to new list", "Merges two lists", "Finds max element"],
        ["remove()", "delete()", "pop()", "discard()"],
        ["Used for resource management", "Used for exception handling", "Used for defining functions", "Used for defining loops"],
        ["datetime.now()", "time.now()", "date.now()", "current.date()"],
        ["Python Enhancement Proposal", "Python Execution Protocol", "Python Example Program", "Python Error Protocol"],
    ]

    correct_answers = [
        0,  # 8
        0,  # def
        0,  # Returns length
        0,  # Using brackets
        0,  # Key-value pairs
        0,  # add()
        0,  # //
        0,  # Anonymous function
        0,  # try-except
        0,  # Compact way to create lists
        0,  # import module_name
        0,  # Immutable list
        0,  # type()
        0,  # Exits the loop
        0,  # Accessing parts of strings/lists
        0,  # class ClassName:
        0,  # Initializes class
        0,  # Using parentheses
        0,  # Function that returns iterator
        0,  # Using 'venv'
        0,  # Does nothing
        0,  # Reference to instance
        0,  # open() and read()
        0,  # Checks value equality
        0,  # int()
        0,  # Applies a function to elements
        0,  # remove()
        0,  # Used for resource management
        0,  # datetime.now()
        0,  # Python Enhancement Proposal
    ]

    for i, question_text in enumerate(questions):
        question = Question.objects.create(text=question_text)
        for j, option_text in enumerate(options[i]):
            is_correct = j == correct_answers[i]
            Option.objects.create(question=question, text=option_text, is_correct=is_correct)

    print("Data populated successfully.")

if __name__ == "__main__":
    populate_data()
