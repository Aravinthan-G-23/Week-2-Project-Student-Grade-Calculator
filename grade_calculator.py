{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "15261aca-1815-4e13-8890-d4ba01d4305a",
   "metadata": {},
   "source": [
    "### *Week 2 Project: Student Grade Calculator*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c7b37bf-fa3e-4386-bfc6-69fd99db0582",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter student name:  Aravinthan G\n",
      "Enter marks (0-100):  88\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " RESULT FOR ARAVINTHAN G\n",
      "--------------------------\n",
      "Marks: 88 /100\n",
      "Grade: B\n",
      "Message: Very Good! Keep it up!\n"
     ]
    }
   ],
   "source": [
    "# Student Grade Calculator\n",
    "\n",
    "def calculate_grade(marks):\n",
    "    \"\"\"Returns grade and encouraging message\"\"\"\n",
    "\n",
    "    if marks >= 90:\n",
    "        return \"A\", \"Excellent! Outstanding work!\"\n",
    "\n",
    "    elif marks >= 80:\n",
    "        return \"B\", \"Very Good! Keep it up!\"\n",
    "\n",
    "    elif marks >= 70:\n",
    "        return \"C\", \"Good Job! You can do even better!\"\n",
    "\n",
    "    elif marks >= 60:\n",
    "        return \"D\", \"Nice effort! Keep practicing!\"\n",
    "\n",
    "    else:\n",
    "        return \"F\", \"Don't give up! Success comes with practice!\"\n",
    "\n",
    "\n",
    "# Input student name\n",
    "name = input(\"Enter student name: \")\n",
    "\n",
    "# Validate marks\n",
    "while True:\n",
    "    try:\n",
    "        marks = int(input(\"Enter marks (0-100): \"))\n",
    "\n",
    "        if 0 <= marks <= 100:\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid input! Marks should be between 0 and 100.\")\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"Please enter numbers only.\")\n",
    "\n",
    "\n",
    "# Calculate grade\n",
    "grade, message = calculate_grade(marks)\n",
    "\n",
    "# Display result\n",
    "print(\"\\n RESULT FOR\", name.upper())\n",
    "print(\"--------------------------\")\n",
    "print(\"Marks:\", marks, \"/100\")\n",
    "print(\"Grade:\", grade)\n",
    "print(\"Message:\", message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea317322-c9f1-4edd-9d49-e180e638326e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
