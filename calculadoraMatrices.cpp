#include <iostream>

using namespace std;

char setOperation(){
    char oper;

    cout << "\n";
    while((oper != '+') & (oper != '-') & (oper != '=')){
        cout << "Introduce operacion: ";
        cin >> oper;
    }
    return oper;
}


int main()
{
    int matriz[100][100], filas, columnas;
    char operation;

    while(operation != '='){
        cout << "Introduce numero de filas: ";
        cin >> filas;
        cout << "Introduce numero de columnas: ";
        cin >> columnas;
        cout << "FILAS: " << filas << " COLUMNAS: " << columnas << endl;

        for(int i=0;i<filas;i++){
            for(int j=0;j<columnas;j++){
                cout << "Defina el elemento [" << i <<"][" << j << "]: ";
                cin >> matriz[i][j];
            }
        }

        cout << "\n" << "MATRIZ DEFINIDA" << "\n";
        for(int i=0;i<filas;i++){
            for(int j=0;j<columnas;j++){
                cout << " " << matriz[i][j];
            }
            cout << "\n";
        }
        operation = setOperation();
        cout << "\n";
        if(operation == '+'){
            cout << "La operacion seleccionada es una suma" << endl;
        }else if(operation == '-'){
            cout << "La opercion seleccionada es una resta" << endl;
        }else if(operation == '='){
            cout << "La opercion seleccionada es mostrar resultado y salir" << endl;
        }

        }
    return 0;
}
