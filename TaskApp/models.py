from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=20) #oopss :)  #we can extend length :)
    task_desc = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    #image = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')
    xml = models.FileField(upload_to='Xml/',default='Xml/None/No-xml.xml')

    def __str__(self):
        return  "%s" % self.task_name




