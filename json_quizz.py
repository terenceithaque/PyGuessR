"""This script handles the JSON format used for the quizz and provides a JSONQuizzFormat class."""
import json
import random


class JSONQuestion:
    def __init__(self, content:str, answer:str, reward:int, widgets:list) -> None:
        """A specific question of the quizz.\n
        - content: the content of the question (ex. 'What is the capital of France ?')
        - answer: the correct answer to the question (ex. 'Paris')
        - reward: the number of points the player grants if he correctly answers
        - widgets: a list descripting widgets offered to the players (buttons, inputs, etc)."""

        self.content = content
        self.answer = answer
        self.reward = reward
        self.widgets = widgets


    def is_answer_correct(self, player_answer:str) -> bool:
        """Returns True if the given player answer is correct or False if it is not."""
        return player_answer == self.answer



class JSONQuizzFormat:
    

    def __init__(self, json_file:str) -> None:
        """This class acts as an abstraction for the JSON format which is used for the quizz.\n
        json_file: the JSON file from which the content of the quizz (questions, answers, etc.) is parsed using the json module."""

        self.file = json_file

        # Parse the content of the JSON file


        self.quizz_content = {}

        with open(json_file, "r", encoding="utf-8") as f:
            self.quizz_content = json.load(f)



        # Get the questions of the quizz
        self.questions = self.quizz_content["questions"]



    def get_points_sum(self, question_numbers:list) -> int:
        """Returns the points sum for all the selected questions of the quizz.
        - question_numbers: a list of question numbers used for the sum."""

        points_sum = 0 # Initialize the sum to 0

        for number in question_numbers:
            question = self.get_question(number)
            points_sum += question.reward

        return points_sum    

        

    def get_question_numbers(self) -> list:
        """Return the list of question numbers in crescent order."""

        numbers = [] # List of question numbers
        for number in self.questions.keys():
            numbers.append(int(number))

        return numbers


    def question_serie(self, length=10) -> list:
        """Returns a list of numbers representing the questions asked to the player.
        - length : the length of the list, 10 by default."""

        serie = [] # Question serie list

        question_numbers = self.get_question_numbers()

        while len(serie) < length:
            number = random.choice(question_numbers)
            print(number)
            print(serie)
            if number not in serie:
                serie.append(number)

        return serie        
        



    def get_question(self, number:int) -> JSONQuestion:
        """Returns the question identified by the given number."""

        assert number in self.get_question_numbers(), f"Invalid question number ({number})."

        question_data = self.questions[str(number)]

        return JSONQuestion(question_data["content"], question_data["answer"], question_data["reward"], question_data["widgets"])    

        




# Executed only if the scripted is runned directly
if __name__ == "__main__":
    quizz = JSONQuizzFormat("quizz/geographics/level_1.json")
    print("Question numbers :", quizz.get_question_numbers())
    print("Question n°1 :", quizz.get_question(1))
    print("Question serie :", quizz.question_serie(4))