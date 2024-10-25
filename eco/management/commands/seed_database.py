from django.core.management.base import BaseCommand
from eco.models import Tiposmateriales, Puntos, Ordenes, Materiales

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        
        Tiposmateriales.objects.all().delete()
        Puntos.objects.all().delete()
        Ordenes.objects.all().delete()
        Materiales.objects.all().delete()

        self.stdout.write(self.style.WARNING('All tables cleared.'))

        # Tiposmateriales
        material1 = Tiposmateriales.objects.create(nombre="Plástico")
        material2 = Tiposmateriales.objects.create(nombre="Vidrio")
        material3 = Tiposmateriales.objects.create(nombre="Metal")
        material4 = Tiposmateriales.objects.create(nombre="Madera")
        material5 = Tiposmateriales.objects.create(nombre="Papel")
        material6 = Tiposmateriales.objects.create(nombre="Cartón")
        
        # Puntos
        punto1 = Puntos.objects.create(nombre="Punto Norte")
        punto1.materiales_posibles.set([material1, material2, material6])
        
        punto2 = Puntos.objects.create(nombre="Punto Sur")
        punto2.materiales_posibles.set([material2, material3, material4, material5])

        punto3 = Puntos.objects.create(nombre="Punto Este")
        punto3.materiales_posibles.set([material1, material2, material3, material4, material5, material6])
        
        punto4 = Puntos.objects.create(nombre="Punto Oeste")
        punto4.materiales_posibles.set([material1, material3, material6, material4])
        
        # Ordenes
        orden1 = Ordenes.objects.create(cantidad=10, tipo=material1, reservado=True, entregado=False, proveedor=punto1)
        orden2 = Ordenes.objects.create(cantidad=15, tipo=material2, reservado=False, entregado=False)
        orden3 = Ordenes.objects.create(cantidad=1, tipo=material4, reservado=False, entregado=False)
        orden4 = Ordenes.objects.create(cantidad=3, tipo=material6, reservado=True, entregado=True, proveedor=punto3)
        orden5 = Ordenes.objects.create(cantidad=50, tipo=material1, reservado=False, entregado=False)
        orden6 = Ordenes.objects.create(cantidad=4, tipo=material2, reservado=False, entregado=False)
        orden7 = Ordenes.objects.create(cantidad=15, tipo=material5, reservado=False, entregado=False)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
