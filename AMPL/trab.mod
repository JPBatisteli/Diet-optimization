param Pkg = 60;
param Cdu = 2500;
var Qp >= 0;
var Qc >= 0;
var Qg >= 0;
var Qf >= 0;
maximize Qcal: (Pkg * Qp * 4) + (Pkg * Qc * 4) + (Pkg * Qg * 9);

subject to total_cal: (Pkg * Qp * 4) + (Pkg * Qc * 4) + (Pkg * Qg * 9) <= Cdu;
subject to Limite_Qp_1: Qp<=5;
subject to Limite_Qp_2: Qp>=3;
subject to Limite_Qg_1: Qg<=0.6;
subject to Limite_Qg_2: Qg>=0.3;
subject to Valor_Qf: Qf = 15 * (Cdu div 1000);


#subject to Resticao_Qp: Cdu - (Pkg*Qp*4) + (Pkg*Qg*9);
