from django.core.management.base import BaseCommand
from eco.models import Tiposmateriales, Puntos, Ordenes, Materiales

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Tiposmateriales.objects.all().delete()
        Puntos.objects.all().delete()
        Ordenes.objects.all().delete()
        Materiales.objects.all().delete()

        self.stdout.write(self.style.WARNING('All tables cleared.'))

        # Tiposmateriales (reciclables)
        material1 = Tiposmateriales.objects.create(nombre="Plástico")
        material2 = Tiposmateriales.objects.create(nombre="Vidrio")
        material3 = Tiposmateriales.objects.create(nombre="Metal")
        material4 = Tiposmateriales.objects.create(nombre="Madera")
        material5 = Tiposmateriales.objects.create(nombre="Papel")
        material6 = Tiposmateriales.objects.create(nombre="Cartón")
        material7 = Tiposmateriales.objects.create(nombre="Aluminio")
        material8 = Tiposmateriales.objects.create(nombre="Caucho")
        material9 = Tiposmateriales.objects.create(nombre="Cobre")

        # Puntos
        punto1 = Puntos.objects.create(nombre="Punto Norte")
        punto1.materiales_posibles.set([material1, material2, material6])

        punto2 = Puntos.objects.create(nombre="Punto Sur")
        punto2.materiales_posibles.set([material2, material3, material4, material5])

        punto3 = Puntos.objects.create(nombre="Punto Este")
        punto3.materiales_posibles.set([material1, material2, material3, material4, material5, material6])

        punto4 = Puntos.objects.create(nombre="Punto Oeste")
        punto4.materiales_posibles.set([material1, material3, material6, material4])

        punto5 = Puntos.objects.create(nombre="Punto Central")
        punto5.materiales_posibles.set([material7, material8, material9])

        punto6 = Puntos.objects.create(nombre="Punto Reciclaje Avanzado")
        punto6.materiales_posibles.set([material7, material1, material8])

        # Ordenes
        ordenes = [
            Ordenes(cantidad=10, tipo=material1, reservado=False, entregado=False),
            Ordenes(cantidad=15, tipo=material2, reservado=True, entregado=False, proveedor=punto2),
            Ordenes(cantidad=1, tipo=material4, reservado=False, entregado=False),
            Ordenes(cantidad=3, tipo=material6, reservado=True, entregado=True, proveedor=punto3),
            Ordenes(cantidad=50, tipo=material1, reservado=False, entregado=False),
            Ordenes(cantidad=4, tipo=material2, reservado=False, entregado=False),
            Ordenes(cantidad=15, tipo=material5, reservado=False, entregado=False),
            Ordenes(cantidad=8, tipo=material7, reservado=True, entregado=False, proveedor=punto5),
            Ordenes(cantidad=20, tipo=material8, reservado=False, entregado=False),
            Ordenes(cantidad=25, tipo=material3, reservado=True, entregado=False, proveedor=punto4),
            Ordenes(cantidad=30, tipo=material6, reservado=True, entregado=False, proveedor=punto1),
            Ordenes(cantidad=6, tipo=material5, reservado=False, entregado=False),
            Ordenes(cantidad=18, tipo=material7, reservado=False, entregado=False),
            Ordenes(cantidad=7, tipo=material2, reservado=True, entregado=False, proveedor=punto2),
            Ordenes(cantidad=12, tipo=material8, reservado=True, entregado=True, proveedor=punto6),
            Ordenes(cantidad=5, tipo=material4, reservado=False, entregado=False),
            Ordenes(cantidad=14, tipo=material1, reservado=True, entregado=False, proveedor=punto3),
            Ordenes(cantidad=11, tipo=material3, reservado=False, entregado=False),
            Ordenes(cantidad=22, tipo=material2, reservado=False, entregado=False),
            Ordenes(cantidad=9, tipo=material5, reservado=False, entregado=False),
            Ordenes(cantidad=13, tipo=material6, reservado=False, entregado=False),
            Ordenes(cantidad=17, tipo=material7, reservado=False, entregado=False),
            Ordenes(cantidad=21, tipo=material9, reservado=True, entregado=False, proveedor=punto6),
            Ordenes(cantidad=19, tipo=material4, reservado=True, entregado=False, proveedor=punto2),
            Ordenes(cantidad=2, tipo=material1, reservado=True, entregado=True, proveedor=punto1),
        ]
        Ordenes.objects.bulk_create(ordenes)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
