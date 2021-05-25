param Pkg ;
param Cdu ;
param Qg_s ;
param Qg_i ;
param Qp_s ;
param Qp_i ;
var Qp >= 0;
var Qc >= 0;
var Qg >= 0;
var Qf >= 0;
maximize Qcal: (Pkg * Qp * 4) + (Pkg * Qc * 4) + (Pkg * Qg * 9);

subject to total_cal: (Pkg * Qp * 4) + (Pkg * Qc * 4) + (Pkg * Qg * 9) <= Cdu;
subject to Limite_Qp_1: Qp<=Qp_s;
subject to Limite_Qp_2: Qp>=Qp_i;
subject to Limite_Qg_1: Qg<=Qp_s;
subject to Limite_Qg_2: Qg>=Qp_i;
subject to Valor_Qf: Qf = 15 * (Cdu div 1000);
