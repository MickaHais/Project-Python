from train.models import Train

Train.objects.create(type="A", destination="Cergy-le-Haut", depart="08h49", plan="RERA.png")
Train.objects.create(type="A", destination="Marne-la-Vallée", depart="09h35", plan="RERA.png")
Train.objects.create(type="B", destination="Saint-Rémy-les-Chevreuses", depart="17h11", plan="RERB.png")
Train.objects.create(type="B", destination="Aéroport Charles de Gaulle", depart="18h09", plan="RERB.png")
Train.objects.create(type="C", destination="Saint-Quentin-en-Yvelines", depart="07h52", plan="RERC.png")
Train.objects.create(type="C", destination="Saint-Martin-d\'Etampes", depart="13h30", plan="RERC.png")
Train.objects.create(type="D", destination="Creil", depart="11h50", plan="RERD.png")
Train.objects.create(type="D", destination="Melun", depart="12h15", plan="RERD.png")
Train.objects.create(type="E", destination="Haussman-Saint-Lazare", depart="16h40", plan="RERE.png")
Train.objects.create(type="E", destination="Tournan", depart="20h11", plan="RERE.png")