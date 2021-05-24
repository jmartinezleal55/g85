

#students = 'jose,david,'
students = ['jose', 'david']


def create_student(student_name):
    global students

    if student_name not in students:
        students.append(student_name)
    else:
        print('El estudiante se encuentra en lista')


def list_students():
    global students
    
    for idx, student in enumerate(students):
        print(f'{idx}: {student}')


def delete_student(student_name):
    global students

    if student_name in students:
        students.remove(student_name)
    else:
        print(f'El estudiante {student_name} NO se encuentra en lista')


def update_student(student_name, update_student_name):
    global students

    if student_name in students:
        idx = students.index(student_name)
        students[idx] = update_student_name
    else:
        print(f'El estudiante {student_name} NO se encuentra en lista')


def search_student(student_name):
    global students

    if student_name in students:
        print(f"El estudiante {student_name} se encuentra en lista")
    else:
        print(f"El estudiante {student_name} No se encuentra en lista")


def print_menu():
    print("--APLICACION CRUD: INSCRIPCION ESTUDIANTES--")
    print("="*50)
    print("Escoja su opcion: ")
    print("[C] - Crear estudiante")
    print("[R] - Listar estudiantes")
    print("[U] - Actualizar estudiante")
    print("[D] - Borrar estudiante")
    print("[S] - Buscar estudiante")
    print("[E] - Salir.")


def get_student_name():

    student_name = None

    while not student_name:
        student_name = input('Nombre estudiante: ')

    return student_name


if __name__ == '__main__':


    mainlopp = True

    while mainlopp:
        print_menu()

        command = input()
        command = command.upper()

        if command == 'C':
            student_name = get_student_name()
            create_student(student_name)
            list_students()
        elif command == 'R':
            list_students()
        elif command == 'U':
            list_students()
            student_name = get_student_name()
            update_student_name = input('Nuevo Nombre: ')
            update_student(student_name, update_student_name)
            list_students()
        elif command == 'D':
            list_students()
            student_name = get_student_name()
            delete_student(student_name)
            list_students()
        elif command == 'S':
            student_name = get_student_name()
            search_student(student_name)
        elif command == 'E':
            mainlopp = False
        else:
            print("OPCION INVALIDA")
