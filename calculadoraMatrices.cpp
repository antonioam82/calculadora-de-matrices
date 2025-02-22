#include <iostream>

using namespace std;

char continuar(){
    char conti;

    cout << "\n";
    while((conti != 'Y') & (conti != 'N')){
        cout << "Desea continuar? (N/Y): ";
        cin >> conti;
    }
    return conti;
}


int main()
{
    int matriz[100][100], filas, columnas;
    char conti = 'Y';

    while(conti == 'Y'){
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
        conti = continuar();
    }
    return 0;
}
