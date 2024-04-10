from django.db import models

class Train(models.Model):
    trainID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30)
    destination = models.TextField()
    depart = models.CharField(max_length=30)
    plan = models.CharField(max_length=30)
    
    def __str__(self):
        return self.trainID

# DESTINATIONS_BY_RER = {
#     'A': ['Cergy-le-Haut', 'Marne-la-Vallée'],
#     'B': ['Saint-Rémy-les-Chevreuses', 'Aéroport Charles de Gaulle'],
#     'C': ['Saint-Quentin-en-Yvelines', 'Saint-Martin-d\'Etampes'],
#     'D': ['Creil', 'Melun'],
#     'E': ['Haussman-Saint-Lazare', 'Tournan']
# }