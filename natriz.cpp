#include <iostream>
#include <vector>

using namespace std;

char setOperation() {
    char oper;

    cout << "\n";
    while ((oper != '+') && (oper != '-') && (oper != '=')) {
        cout << "Introduce operacion (+, -, =): ";
        cin >> oper;
    }
    return oper;
}

// Función para ingresar una matriz
void defineMatriz(vector<vector<int>>& matriz, int filas, int columnas) {
    cout << "Ingresa los elementos de la matriz (" << filas << "x" << columnas << "):" << endl;
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            cout << "Elemento [" << i + 1 << "][" << j + 1 << "]: ";
            cin >> matriz[i][j];
        }
    }
}

// Función para imprimir una matriz
void printMatriz(const vector<vector<int>>& matriz, int filas, int columnas) {
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            cout << " " << matriz[i][j];
        }
        cout << "\n";
    }
}

int main() {
    int filas, columnas;
    char operation;

    // Mantener el programa corriendo hasta que se elija "="
    while (operation != '=') {
        cout << "Introduce numero de filas: ";
        cin >> filas;
        cout << "Introduce numero de columnas: ";
        cin >> columnas;

        // Crear matrices dinámicas
        vector<vector<int>> matriz(filas, vector<int>(columnas));
        vector<vector<int>> resultMatriz(filas, vector<int>(columnas));

        // Ingresar los elementos de la matriz
        defineMatriz(matriz, filas, columnas);

        // Mostrar la matriz definida
        cout << "\nMATRIZ DEFINIDA:" << "\n";
        printMatriz(matriz, filas, columnas);

        // Solicitar la operación
        operation = setOperation();

        if (operation == '+') {
            // Sumar el escalar 2 a cada elemento de la matriz
            cout << "La operacion seleccionada es una suma con el escalar 2." << endl;
            for (int i = 0; i < filas; ++i) {
                for (int j = 0; j < columnas; ++j) {
                    resultMatriz[i][j] = matriz[i][j] + 2;
                }
            }

            // Mostrar el resultado de la operación
            cout << "Resultado de la suma con el escalar 2:" << endl;
            printMatriz(resultMatriz, filas, columnas);
        } else if (operation == '-') {
            cout << "La operacion seleccionada es una resta." << endl;
            // Aquí puedes implementar la resta si lo deseas
        } else if (operation == '=') {
            cout << "La operacion seleccionada es mostrar resultado y salir." << endl;
            cout << "Matriz final:" << endl;
            printMatriz(resultMatriz, filas, columnas);
        }
    }

    return 0;
}
