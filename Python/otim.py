import scipy
from scipy.optimize import linprog
from tkinter import *
from PySimpleGUI import PySimpleGUI as sg

def solve_diet(Qp_s=3, Qp_i=2, Qg_s=1, Qg_i=0.6, Cdu=2000, Pkg=72):
    #ordem Qp Qc Qg 
    c = [-(Pkg*4), -(Pkg*4), -(Pkg*9)] # coeficientes da função objetivo
    A = [[(Pkg*4), (Pkg*4), (Pkg*9)]] #matriz de coeficientes das restrições
    b = [Cdu] #termos independentes 

    qp_bounds = (Qp_i, Qp_s) 
    qc_bounds = (None, None)
    qg_bounds = (Qg_i, Qg_s)

    #Método padrão: simplex.
    res = scipy.optimize.linprog(c, A_ub=A, b_ub=b, bounds=(qp_bounds, qc_bounds, qg_bounds),
               options={"disp": True})

    #print(res)
    x=res.x
    print(x[0], x[1], x[2])
    Qp=round(x[0], 3)
    Qc=round(x[1], 3)
    Qg=round(x[2], 3)
    Qcal=(Qp*Pkg*4)+(Qc*Pkg*4)+(Qg*Pkg*9)
    Qf = 15*(Cdu//1000)
    return round((Qp*Pkg),3), round((Qc*Pkg),3), round((Qg*Pkg),3), Qcal, Qf

def interface():

    sg.theme('Reddit')
    layout = [
        [sg.Text('Peso em kg do usuário',size=(35,1)), sg.Input(key='Pkg',size=(10,1))],
        [sg.Text('Calorias diárias a serem ingeridas',size=(35,1)), sg.Input(key='Cdu',size=(10,1))],
        [sg.Text('Quantidade mínima de proteína por kg',size=(35,1)), sg.Input(key='Qp_i',size=(10,1))],
        [sg.Text('Quantidade máxima de proteína por kg',size=(35,1)), sg.Input(key='Qp_m',size=(10,1))],
        [sg.Text('Quantidade mínima de gordura por kg',size=(35,1)), sg.Input(key='Qg_i',size=(10,1))],
        [sg.Text('Quantidade máxima de gordura por kg',size=(35,1)), sg.Input(key='Qg_s',size=(10,1))],
        [sg.Button('Calcular Macronutrientes')]
        #[sg.Output(size=(75,3))]
    ]

    janela=sg.Window('Trabalho Prático Otimização',layout)

    while True:
        eventos, valores = janela.read()
        if(eventos == sg.WINDOW_CLOSED):
            break

        if(eventos == 'Calcular Macronutrientes'):
            pkg_user = valores['Pkg']
            cdu_user = valores['Cdu']
            qp_i_user = valores['Qp_i']
            qp_s_user = valores['Qp_m']
            qg_i_user = valores['Qg_i']
            qg_s_user = valores['Qg_s']
            Qp_user, Qc_user, Qg_user, total_calories, Qf_user = solve_diet(float(qp_s_user), float(qp_i_user), float(qg_s_user), float(qg_i_user), float(cdu_user), float(pkg_user))
            sg.Print('Quantidade de proteína (em gramas) a ser consumida: ', Qp_user)
            sg.Print('Quantidade de carboidrato (em gramas) a ser consumida: ', Qc_user)
            sg.Print('Quantidade de gordura (em gramas) a ser consumida: ', Qg_user)
            sg.Print('Quantidade de fibras (em gramas) a ser consumida: ', Qf_user)
            sg.Print('Total de calorias a ser consumida: ', total_calories)


   

def main():
    interface()

if __name__ == '__main__':
   main()