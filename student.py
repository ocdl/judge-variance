class Student(object):

    name = ""
    scores = []
    id_num = 0

    def __init__(self, name, id_num, scores):
        self.name = name
        self.scores = scores
        self.id_num = id_num

    def __str__(self):
        return "Student: {}\nScores: {}\n".format(self.name, [score.__str__() for score in self.scores])
