from django.core.management.base import BaseCommand
from eco.models import Tiposmateriales, Puntos, Ordenes, Materiales

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Tiposmateriales
        material1 = Tiposmateriales.objects.create(nombre="Plástico")
        material2 = Tiposmateriales.objects.create(nombre="Vidrio")
        material3 = Tiposmateriales.objects.create(nombre="Metal")
        
        # Puntos
        punto1 = Puntos.objects.create(nombre="Punto Norte")
        punto1.materiales_posibles.set([material1, material2])
        
        punto2 = Puntos.objects.create(nombre="Punto Sur")
        punto2.materiales_posibles.set([material2, material3])
        
        # Ordenes
        orden1 = Ordenes.objects.create(cantidad=10, tipo=material1, reservado=True, entregado=False, proveedor=punto1)
        orden2 = Ordenes.objects.create(cantidad=15, tipo=material2, reservado=False, entregado=True, proveedor=punto2)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
