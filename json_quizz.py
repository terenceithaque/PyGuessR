"""This script handles the JSON format used for the quizz and provides a JSONQuizzFormat class."""
import json


class JSONQuizzFormat:
    

    def __init__(self, json_file:str) -> None:
        """This class acts as an abstraction for the JSON format which is used for the quizz.\n
        json_file: the JSON file from which the content of the quizz (questions, answers, etc.) is parsed using the json module."""

        self.file = json_file

        # Parse the content of the JSON file


        self.quizz_content = {}

        with open(json_file, "r") as f:
            self.quizz_content = json.load(f)



        # Get the questions of the quizz
        self.questions = self.quizz_content["questions"]

        

    def get_question_numbers(self) -> list:
        """Return the list of question numbers in crescent order."""

        numbers = [] # List of question numbers
        for number in self.questions.keys():
            numbers.append(int(number))

        return numbers


    def get_question(self, number:int) -> dict:
        """Returns the dictionnary representing the data of a question identified by the given number."""

        assert number in self.get_question_numbers(), f"Invalid question number ({number})."

        return self.questions[str(number)]         

        




# Executed only if the scripted is runned directly
if __name__ == "__main__":
    quizz = JSONQuizzFormat("quizz/geographics/level_1.json")
    print("Question numbers :", quizz.get_question_numbers())
    print("Question n°1 :", quizz.get_question(1))