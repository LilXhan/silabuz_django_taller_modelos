from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        abstract = True


class Teacher(Person):
    salary = models.FloatField(default=0.0)

    class Meta:
        db_table = 'teachers'


class Classroom(models.Model):
    idTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    class Meta:
        db_table = 'classrooms'


class Student(Person):
    idClassroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        db_table = 'students'

    
class OrderedAlumn(Student):
    class Meta: 
        proxy = True 
        ordering = ["last_name"]


# Tarea

class Evaluation(models.Model):
    date = models.DateTimeField(auto_now=True)
    course = models.CharField(max_length=30)
    evaluator = models.CharField(max_length=50)

    class Meta:
        abstract = True


class ExamFinal(Evaluation):
    exam_duration = models.IntegerField(default=0)
    questions = models.IntegerField(default=0)
    score = models.IntegerField(default=0)


    def question_score(self):
        return self.questions / self.score
    

class Project(Evaluation):
    project_theme = models.CharField(max_length=100)
    groups_numbers = models.IntegerField(default=0)


class ProjectProxy(Project):
    class Meta:
        proxy = True
        ordering = ["project_theme"]