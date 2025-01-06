from services.pacienteServices import PacienteServices
from services.medicoServices import MedicoServices
from services.citaServices import CitaServices
from services.pacienteServices import PacienteServices
from services.habitacionServices import HabitacionServices
from services.historiaClinicaServices import HistoriaClinicaServices
from models import Medico, Paciente, Cita, HistoriaClinica, Habitacion



# Inicializar servicios
paciente_service = PacienteServices()
medico_service = MedicoServices()
cita_service = CitaServices()
habitacion_service = HabitacionServices()
historia_clinica_service = HistoriaClinicaServices()

def menu_principal():
    print("\n--- GESTOR HOSPITAL ---")
    print("1. Gestionar Pacientes")
    print("2. Gestionar Médicos")
    print("3. Gestionar Citas")
    print("4. Gestionar Habitaciones")
    print("5. Gestionar Historias Clínicas")
    print("0. Salir")

def gestionar_pacientes():
    print("\n--- GESTIÓN DE PACIENTES ---")
    print("1. Listar Pacientes")
    print("2. Agregar Paciente")
    print("3. Buscar Paciente por ID")
    print("4. Buscar Paciente por Nombre")
    print("5. Buscar Paciente por Apellido")
    print("6. Buscar Paciente por Telefono")
    print("7. Buscar Paciente por Direccion")
    print("8. Eliminar Paciente")
    print("9. Actualizar Paciente")
    print("0. Volver")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        pacientes = paciente_service.obtenerPacientes()
        print("\nLista de Pacientes:")
        for paciente in pacientes:
            print(paciente)
    elif opcion == "2":
        nombre = input("Ingrese nombre del paciente: ")
        apellido = input("Ingrese apellido del paciente: ")
        edad = int(input("Ingrese edad del paciente: "))
        direccion = input("Ingrese dirección del paciente: ")
        enfermedad = input("Ingrese enfermedad del paciente: ")     
        paciente = Paciente(nombre, apellido, edad, direccion, enfermedad)
        paciente_service.agregarPaciente(paciente)
        print("Paciente agregado exitosamente.")
    elif opcion == "3":
        id = int(input("Ingrese ID del paciente: "))
        paciente = paciente_service.obtenerPaciente(id)
        print(paciente if paciente else "Paciente no encontrado.")
    elif opcion == "4":
        nombre = input("Ingrese nombre del paciente: ")
        pacientes = paciente_service.obtenerPacientesPorNombre(nombre)
        print("\nLista de Pacientes con nombre", nombre)
        for paciente in pacientes:
            print(paciente)
    elif opcion == "5":
        apellido = input("Ingrese apellido del paciente: ")
        pacientes = paciente_service.obtenerPacientesPorApellido(apellido)
        print("\nLista de Pacientes con apellido", apellido)
        for paciente in pacientes:
            print(paciente)
    elif opcion == "6":
        telefono = input("Ingrese teléfono del paciente: ")
        pacientes = paciente_service.obtenerPacientesPorTelefono(telefono)
        print("\nLista de Pacientes con teléfono", telefono)
        for paciente in pacientes:
            print(paciente)
    elif opcion == "7":
        direccion = input("Ingrese dirección del paciente: ")
        pacientes = paciente_service.obtenerPacientesPorDireccion(direccion)
        print("\nLista de Pacientes con dirección", direccion)
        for paciente in pacientes:
            print(paciente)
    elif opcion == "8":
        id_paciente = int(input("Ingrese ID del paciente a eliminar: "))
        paciente_service.eliminarPaciente(id_paciente)
        print("Paciente eliminado")
    elif opcion == "9":
        id_paciente = int(input("Ingrese ID del paciente a actualizar: "))
        nombre = input("Ingrese nombre del paciente: ")
        apellido = input("Ingrese apellido del paciente: ")
        edad = int(input("Ingrese edad del paciente: "))
        direccion = input("Ingrese dirección del paciente: ")
        enfermedad = input("Ingrese enfermedad del paciente: ")
        paciente_service.actualizarPaciente(id_paciente, nombre, apellido, edad, direccion, enfermedad)
        print("Paciente actualizado exitosamente.")
    elif opcion == "0":
        return menu_principal()
    
    


def gestionar_medicos():
    print("\n--- GESTIÓN DE MÉDICOS ---")
    print("1. Listar Médicos")
    print("2. Agregar Médico")
    print("3. Buscar Médico por ID")
    print("4. Buscar Médico por Especialidad")
    print("5. Buscar Médico por Nombre")
    print("6. Buscar Médico por Apellido")
    print("7. Eliminar Médico")
    print("8. Actualizar Médico")
    print("0. Volver")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        medicos = medico_service.obtenerMedicos()
        print("\nLista de Médicos:")
        for medico in medicos:
            print(medico)
    elif opcion == "2":
        nombre = input("Ingrese nombre del médico: ")
        apellido = input("Ingrese apellido del médico: ")
        especialidad = input("Ingrese especialidad: ")
        telefono = input("Ingrese teléfono del médico: ")
        medico = Medico(nombre, apellido, especialidad, telefono)
        medico_service.agregarMedico(medico)
        print("Médico agregado exitosamente.")
    elif opcion == "3":
        id_medico = int(input("Ingrese ID del médico: "))
        medico = medico_service.obtenerMedico(id_medico)
        print(medico if medico else "Médico no encontrado.")
    elif opcion == "4":
        especialidad = input("Ingrese especialidad del médico: ")
        medicos = medico_service.obtenerMedicosPorEspecialidad(especialidad)
        print("\nLista de Médicos con especialidad", especialidad)
        for medico in medicos:
            print(medico)
    elif opcion == "5":
        nombre = input("Ingrese nombre del médico: ")
        medicos = medico_service.obtenerMedicosPorNombre(nombre)
        print("\nLista de Médicos con nombre", nombre)
        for medico in medicos:
            print(medico)
    elif opcion == "6":
        apellido = input("Ingrese apellido del médico: ")
        medicos = medico_service.obtenerMedicosPorApellido(apellido)
        print("\nLista de Médicos con apellido", apellido)
        for medico in medicos:
            print(medico)
    elif opcion == "7":
        id_medico = int(input("Ingrese ID del médico a eliminar: "))
        medico_service.eliminarMedico(id_medico)
        print("Médico eliminado exitosamente.")
    elif opcion == "8":
        id_medico = int(input("Ingrese ID del médico a actualizar: "))
        nombre = input("Ingrese nombre del médico: ")
        apellido = input("Ingrese apellido del médico: ")
        especialidad = input("Ingrese especialidad: ")
        medico_service.actualizarMedico(id_medico, nombre, apellido, especialidad)
        print("Médico actualizado exitosamente.")
    elif opcion == "0":
        return menu_principal()
    

def gestionar_citas():
    print("\n--- GESTIÓN DE CITAS ---")
    print("1. Listar Citas")
    print("2. Agregar Cita")
    print("3. Buscar Cita por ID")
    print("4. Buscar Cita por Fecha")
    print("5. Buscar Cita por Paciente")
    print("6. Buscar Cita por Médico")
    print("7. Eliminar Cita")
    print("8. Actualizar Cita")
    print("0. Volver")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        citas = cita_service.obtenerCitas()
        print("\nLista de Citas:")
        for cita in citas:
            print(cita)
    elif opcion == "2":
        id_paciente = int(input("Ingrese ID del paciente: "))
        id_medico = int(input("Ingrese ID del médico: "))
        fecha = input("Ingrese fecha de la cita (YYYY-MM-DD): ")
        hora = input("Ingrese hora de la cita (HH:MM): ")
        cita = Cita(id_paciente, id_medico, fecha , hora)
        cita_service.agregarCita(cita)
        print("Cita agregada exitosamente.")
    elif opcion == "3":
        id_cita = int(input("Ingrese ID de la cita: "))
        cita = cita_service.obtenerCita(id_cita)
        print(cita if cita else "Cita no encontrada.")
    elif opcion == "4":
        fecha = input("Ingrese fecha de la cita (YYYY-MM-DD): ")
        citas = cita_service.obtenerCitasPorFecha(fecha)
        print("\nLista de Citas para la fecha", fecha)
        for cita in citas:
            print(cita)
    elif opcion == "5":
        id_paciente = int(input("Ingrese ID del paciente: "))
        citas = cita_service.obtenerCitasPorPaciente(id_paciente)
        print("\nLista de Citas para el paciente", id_paciente)
        for cita in citas:
            print(cita)
    elif opcion == "6":
        id_medico = int(input("Ingrese ID del médico: "))
        citas = cita_service.obtenerCitasPorMedico(id_medico)
        print("\nLista de Citas para el médico", id_medico)
        for cita in citas:
            print(cita)
    elif opcion == "7":
        id_cita = int(input("Ingrese ID de la cita a eliminar: "))
        cita_service.eliminarCita(id_cita)
        print("Cita eliminada exitosamente.")
    elif opcion == "8":
        id_cita = int(input("Ingrese ID de la cita a actualizar: "))
        id_paciente = int(input("Ingrese ID del paciente: "))
        id_medico = int(input("Ingrese ID del médico: "))
        fecha = input("Ingrese fecha de la cita (YYYY-MM-DD): ")
        cita_service.actualizarCita(id_cita, id_paciente, id_medico, fecha)
        print("Cita actualizada exitosamente.")
    elif opcion == "0":
        return menu_principal()


def gestionar_habitaciones():
    print("\n--- GESTIÓN DE HABITACIONES ---")
    print("1. Listar Habitaciones")
    print("2. Agregar Habitación")
    print("3. Buscar Habitación por ID")
    print("4. Buscar Habitación por Tipo")
    print("5. Buscar Habitación por Numero")
    print("6. Eliminar Habitación")
    print("7. Actualizar Habitación")
    print("0. Volver")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        habitaciones = habitacion_service.obtenerHabitaciones()
        print("\nLista de Habitaciones:")
        for habitacion in habitaciones:
            print(habitacion)
    elif opcion == "2":
        numero = int(input("Ingrese número de la habitación: "))
        tipo = input("Ingrese tipo de la habitación: ")
        capacidad = int(input("Ingrese capacidad de la habitación: "))
        estado = input("Ingrese estado de la habitación: ")
        habitacion = Habitacion(numero, tipo, capacidad, estado)
        habitacion_service.agregarHabitacion(habitacion)
        print("Habitación agregada exitosamente.")
    elif opcion == "3":
        id_habitacion = int(input("Ingrese ID de la habitación: "))
        habitacion = habitacion_service.obtenerHabitacion(id_habitacion)
        print(habitacion if habitacion else "Habitación no encontrada.")
    elif opcion == "4":
        tipo = input("Ingrese tipo de la habitación: ")
        habitaciones = habitacion_service.obtenerHabitacionesPorTipo(tipo)
        print("\nLista de Habitaciones de tipo", tipo)
        for habitacion in habitaciones:
            print(habitacion)
    elif opcion == "5":
        numero = int(input("Ingrese número de la habitación: "))
        habitaciones = habitacion_service.obtenerHabitacionesPorNumero(numero)
        print("\nLista de Habitaciones con número", numero)
        for habitacion in habitaciones:
            print(habitacion)
    elif opcion == "6":
        id_habitacion = int(input("Ingrese ID de la habitación a eliminar: "))
        habitacion_service.eliminarHabitacion(id_habitacion)
        print("Habitación eliminada exitosamente.")
    elif opcion == "7":
        id_habitacion = int(input("Ingrese ID de la habitación a actualizar: "))
        numero = int(input("Ingrese número de la habitación: "))
        tipo = input("Ingrese tipo de la habitación: ")
        precio = float(input("Ingrese precio de la habitación: "))
        habitacion_service.actualizarHabitacion(id_habitacion, numero, tipo, precio)
        print("Habitación actualizada exitosamente.")
    elif opcion == "0":
        return menu_principal()


def gestionar_historias_clinicas():
    print("\n--- GESTIÓN DE HISTORIAS CLÍNICAS ---")
    print("1. Listar Historias Clínicas")
    print("2. Agregar Historia Clínica")
    print("3. Buscar Historia Clínica por ID")
    print("4. Buscar Historia Clínica por Paciente")
    print("5. Buscar Historia Clínica por Médico")
    print("6. Buscar Historia Clínica por Fecha")
    print("7. Buscar Historia Clínica por Diagnóstico")
    print("8. Buscar Historia Clínica por Tratamiento")
    print("9. Eliminar Historia Clínica")
    print("10. Actualizar Historia Clínica")
    print("0. Volver")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        historias_clinicas = historia_clinica_service.obtenerHistoriasClinicas()
        print("\nLista de Historias Clínicas:")
        for historia_clinica in historias_clinicas:
            print(historia_clinica)
    elif opcion == "2":
        id_paciente = int(input("Ingrese ID del paciente: "))
        fecha = input("Ingrese fecha de la historia clínica (YYYY-MM-DD): ")
        diagnostico = input("Ingrese diagnóstico: ")
        tratamiento = input("Ingrese tratamiento: ")
        id_medico = int(input("Ingrese ID del médico: "))
        historia_clinica = HistoriaClinica(id_paciente, fecha, diagnostico, tratamiento, id_medico)
        historia_clinica_service.agregarHistoriaClinica(historia_clinica)
        print("Historia Clínica agregada exitosamente.")
    elif opcion == "3":
        id_historia_clinica = int(input("Ingrese ID de la historia clínica: "))
        historia_clinica = historia_clinica_service.obtenerHistoriaClinica(id_historia_clinica)
        print(historia_clinica if historia_clinica else "Historia Clínica no encontrada.")
    elif opcion == "4":
        id_paciente = int(input("Ingrese ID del paciente: "))
        historias_clinicas = historia_clinica_service.obtenerHistoriasClinicasPorPaciente(id_paciente)
        print("\nLista de Historias Clínicas para el paciente", id_paciente)
        for historia_clinica in historias_clinicas:
            print(historia_clinica)
    elif opcion == "5":
        id_medico = int(input("Ingrese ID del médico: "))
        historias_clinicas = historia_clinica_service.obtenerHistoriasClinicasPorMedico(id_medico)
        print("\nLista de Historias Clínicas para el médico", id_medico)
        for historia_clinica in historias_clinicas:
            print(historia_clinica)
    elif opcion == "6":
        fecha = input("Ingrese fecha de la historia clínica (YYYY-MM-DD): ")
        historias_clinicas = historia_clinica_service.obtenerHistoriasClinicasPorFecha(fecha)
        print("\nLista de Historias Clínicas para la fecha", fecha)
        for historia_clinica in historias_clinicas:
            print(historia_clinica)
    elif opcion == "7":
        diagnostico = input("Ingrese diagnóstico: ")
        historias_clinicas = historia_clinica_service.obtenerHistoriasClinicasPorDiagnostico(diagnostico)
        print("\nLista de Historias Clínicas con diagnóstico", diagnostico)
        for historia_clinica in historias_clinicas:
            print(historia_clinica)
    elif opcion == "8":
        tratamiento = input("Ingrese tratamiento: ")
        historias_clinicas = historia_clinica_service.obtenerHistoriasClinicasPorTratamiento(tratamiento)
        print("\nLista de Historias Clínicas con tratamiento", tratamiento)
        for historia_clinica in historias_clinicas:
            print(historia_clinica)
    elif opcion == "9":
        id_historia_clinica = int(input("Ingrese ID de la historia clínica a eliminar: "))
        historia_clinica_service.eliminarHistoriaClinica(id_historia_clinica)
        print("Historia Clínica eliminada exitosamente.")
    elif opcion == "10":
        id_historia_clinica = int(input("Ingrese ID de la historia clínica a actualizar: "))
        id_paciente = int(input("Ingrese ID del paciente: "))
        fecha = input("Ingrese fecha de la historia clínica (YYYY-MM-DD): ")
        diagnostico = input("Ingrese diagnóstico: ")
        tratamiento = input("Ingrese tratamiento: ")
        id_medico = int(input("Ingrese ID del médico: "))
        historia_clinica_service.actualizarHistoriaClinica(id_historia_clinica, id_paciente, fecha, diagnostico, tratamiento, id_medico)
        print("Historia Clínica actualizada exitosamente.")
    elif opcion == "0":
        return menu_principal()


def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestionar_pacientes()
        elif opcion == "2":
            gestionar_medicos()
        elif opcion == "3":
            gestionar_citas()
        elif opcion == "4":
            gestionar_habitaciones()
        elif opcion == "5":
            gestionar_historias_clinicas()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
