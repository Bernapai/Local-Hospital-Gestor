from services.pacienteServices import PacienteServices
from services.medicoServices import MedicoServices
from services.citaServices import CitaServices
from services.habitacionServices import HabitacionServices
from services.historiaClinicaServices import HistoriaClinicaServices

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
        dni = input("Ingrese DNI del paciente: ")
        direccion = input("Ingrese dirección del paciente: ")
        telefono = input("Ingrese teléfono del paciente: ")
        paciente_service.agregarPaciente(nombre, apellido, dni, direccion, telefono)
        print("Paciente agregado exitosamente.")
    elif opcion == "3":
        id_paciente = int(input("Ingrese ID del paciente: "))
        paciente = paciente_service.obtenerPaciente(id_paciente)
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
        dni = input("Ingrese DNI del paciente: ")
        direccion = input("Ingrese dirección del paciente: ")
        telefono = input("Ingrese teléfono del paciente: ")
        paciente_service.actualizarPaciente(id_paciente, nombre, apellido, dni, direccion, telefono)
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
        medico_service.agregarMedico(nombre, apellido, especialidad)
        print("Médico agregado exitosamente.")
    elif opcion == "3":
        id_medico = int(input("Ingrese ID del médico: "))
        medico = medico_service.obtenerMedico(id_medico)
        print(medico if medico else "Médico no encontrado.")
    elif opcion == "4":
        especialidad = input("Ingrese especialidad del médico: ")
        medicos = medico_service.obtenerMedicoPorEspecialidad(especialidad)
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
    
    


def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestionar_pacientes()
        elif opcion == "2":
            gestionar_medicos()
        elif opcion == "3":
            print("Gestión de Citas (en desarrollo).")
        elif opcion == "4":
            print("Gestión de Habitaciones (en desarrollo).")
        elif opcion == "5":
            print("Gestión de Historias Clínicas (en desarrollo).")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
