import numpy as np
from numpy.linalg import inv, det, solve

def input_matrix(rows, cols):
    matrix = []
    print("Masukkan elemen matriks:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Masukkan elemen baris {i + 1} kolom {j + 1}: "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix):
    print("Matriks:")
    print(matrix)

def add_matrix(matrix_a, matrix_b):
    return matrix_a + matrix_b

def subtract_matrix(matrix_a, matrix_b):
    return matrix_a - matrix_b

def transpose_matrix(matrix):
    return matrix.T

def determinant_2x2(matrix):
    return np.linalg.det(matrix)

def determinant_3x3(matrix):
    return np.linalg.det(matrix)

def inverse_2x2(matrix):
    return np.linalg.inv(matrix)

def inverse_3x3(matrix):
    return np.linalg.inv(matrix)

def solve_linear_system_2x2(coefficients, constants):
    return np.linalg.solve(coefficients, constants)

def solve_linear_system_3x3(coefficients, constants):
    return np.linalg.solve(coefficients, constants)

def main():
    while True:
        print("MENU")
        print("1. Penjumlahan dan Pengurangan Matriks")
        print("2. Matriks Transpose")
        print("3. Matriks Balikan")
        print("4. Determinan")
        print("5. Sistem Persamaan Linier")
        print("6. Keluar")

        menu = int(input("Pilih menu (1-6): "))

        if menu == 1:
            sub_menu = int(input("Pilih sub-menu untuk penjumlahan/pengurangan matriks (1/2): "))
            rows, cols = map(int, input("Masukkan ukuran matriks (baris kolom): ").split())

            matrix_a = input_matrix(rows, cols)
            matrix_b = input_matrix(rows, cols)

            if sub_menu == 1:
                result = add_matrix(matrix_a, matrix_b)
                print("Hasil penjumlahan matriks A dan B:")
                display_matrix(result)
            elif sub_menu == 2:
                result = subtract_matrix(matrix_a, matrix_b)
                print("Hasil pengurangan matriks A dan B:")
                display_matrix(result)
            else:
                print("Sub-menu tidak valid.")

        elif menu == 2:
            sub_menu = int(input("Pilih sub-menu untuk matriks transpose (1/2): "))
            rows, cols = map(int, input("Masukkan ukuran matriks (baris kolom): ").split())
            matrix = input_matrix(rows, cols)

            result = transpose_matrix(matrix)
            print("Hasil transpose matriks:")
            display_matrix(result)

        elif menu == 3:
            sub_menu = int(input("Pilih sub-menu untuk matriks balikan (1/2): "))

            if sub_menu == 1:
                matrix = input_matrix(2, 2)
                result = inverse_2x2(matrix)
                print("Hasil matriks balikan 2x2:")
                display_matrix(result)
            elif sub_menu == 2:
                matrix = input_matrix(3, 3)
                result = inverse_3x3(matrix)
                print("Hasil matriks balikan 3x3:")
                display_matrix(result)
            else:
                print("Sub-menu tidak valid.")

        elif menu == 4:
            sub_menu = int(input("Pilih sub-menu untuk determinan (1/2): "))

            if sub_menu == 1:
                matrix = input_matrix(2, 2)
                result = determinant_2x2(matrix)
                print(f"Determinan matriks 2x2: {result}")
            elif sub_menu == 2:
                matrix = input_matrix(3, 3)
                result = determinant_3x3(matrix)
                print(f"Determinan matriks 3x3: {result}")
            else:
                print("Sub-menu tidak valid.")

        elif menu == 5:
            sub_menu = int(input("Pilih sub-menu untuk sistem persamaan linier (2/3): "))

            if sub_menu == 2:
                coefficients = input_matrix(2, 2)
                constants = np.array(list(map(int, input("Masukkan konstanta (baris 1, baris 2): ").split())))
                result = solve_linear_system_2x2(coefficients, constants)
                print("Hasil sistem persamaan linier 2x2:")
                print(f"x = {result[0]}")
                print(f'y = {result[1]}')
            elif sub_menu == 3:
                coefficients = input_matrix(3, 3)
                constants = np.array(list(map(int, input("Masukkan konstanta (baris 1, baris 2, baris 3): ").split())))
                result = solve_linear_system_3x3(coefficients, constants)
                print("Hasil sistem persamaan linier 3x3:")
                print(f"x = {result[0]}")
                print(f'y = {result[1]}')
                print(f'z = {result[2]}')
            else:
                print("Sub-menu tidak valid.")

        elif menu == 6:
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()

