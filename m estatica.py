class MemoriaEstatica:
  caificaciones = [0] * 5

  @staticmethod
  def calificaciones():
    for i in range(5):
      calificacion = int(input(f"Ingrese calificación {i+1}: "))
      MemoriaEstatica.caificaciones[i] = calificacion

MemoriaEstatica.calificaciones()