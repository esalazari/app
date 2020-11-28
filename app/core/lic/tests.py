#Traer todos los usuario de la tabla Usuario
#query = Usuario.objects.all()
#print(query)

#Traer datos con filtro
#t = Usuario.objects.filter(usuario_nombre='buscar')
#print(t)

#Ingresar usuario
#t = Usuario()
#t.usuario_nombre = 'Esteban'
#t.save()

#Modificar
#try:
    #t = Usuario.objects.get(usuario_nombre)
    #t.usuario_nombre = 'nuevo nombre'
    #t.save()
#except Exception as e:
    #print(e)

#Eliminar
#t = Usuario.objects.get(usuario_nombre='nombre')
#t.delete()