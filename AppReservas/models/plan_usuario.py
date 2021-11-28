""" el modelo de la tabla plan usuario para la base de datos, tiene los siguientes campos: 
la jornada de la reserva diurno y nocturno, el id único por cada plan, el nombre del plan, 
la descripción y el precio """


from django.db    import models


JORNADAS = (("Diurno","diurno"),("Nocturno","nocturno"))
class Plan_usuario(models.Model): 
    id_plan            = models.AutoField(primary_key=True)
    jornada            = models.CharField('Jornada',choices=JORNADAS, max_length=10, default="Diurno")
    nombre_plan        = models.CharField('Nombre del plan', max_length=50)
    descripcion       = models.CharField('Nombre del plan', max_length=100)
    precio             = models.FloatField('Precio', default= 0.00)
    
