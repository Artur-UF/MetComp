#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define e 2.7182818
// $ gcc ising-2D.c -o ising-2D

int main () {
	
	double uniform (double min, double max);
	int indexprob (int del);
	
	// Aresta do sistema
	int l = 6;
	
	// Inicialização da matriz do sistema
	int sist[l*l];
	
	// Tudo up
	int c = 0;
	for (int i = 0; i < l*l; ++i) {
		sist[i] = 1;
	}
	/*
	// Random
	for (int i = 0; i < l*l; ++i) {
		if (random < 0.5){
			sist[i] = 1;
		}else{
			sist[i] = -1;
		}
	}
	*/
	
	// Geração da matriz de vizinhança
	int viz[l*l][5];
	int cc = 0;
	int cl = 0;
	for (int i = 0; i < l*l; ++i) {
		viz[i][0] = i;
		// Bordas
		if (cc == 0){
			viz[i][1] = i + (l-1); // Esquerda
			viz[i][2] = i + 1; // Direita
		}
		if (cc == l-1){
			viz[i][1] = i - 1; // Esquerda
			viz[i][2] = i - (l-1); // Direita
		}
		if (cl == 0){
			viz[i][3] = l*l - (l-cc); // Cima
			viz[i][4] = i + l; // Baixo
		}
		if (cl == l-1){
			viz[i][3] = i - l; // Cima
			viz[i][4] = cc; // Baixo
		}
		// Miolo
		if (cc > 0 & cc < l-1){
			viz[i][1] = i - 1; // Esquerda
			viz[i][2] = i + 1; // Direita
		}
		if (cl > 0 & cl < l-1){
			viz[i][3] = i - l; // Cima
			viz[i][4] = i + l; // Baixo
		}
		if (cc >= l-1){
			cc = 0;
			++cl;
		}else{
			++cc;
		}
	}	
	
	// Dinâmica
	int J = 1;
	int T = 0.5;	
	int dels[5] = {-8, -4, 0, 4, 8};
	double prob[5];
	
	// Vetor de probabilidades
	for (int i = 0; i < 5; ++i){
		prob[i] = pow(e, -dels[i]/T);
	}
	
	// Magnetização
	int M = 0;
	for (int i = 0; i < l*l; ++i){
		M += sist[i];
	}
	
	// Loop temporal
	int rep = l*l;
	int sort;
	int delE = 0;
	int soma =  0;

	int Ms[rep+1];
	Ms[0] = M;

	for (int i = 0; i < rep; ++i){
		// Sorteio		
		sort = uniform(0, l*l);
		
		// Calculo o delta E
		for (int j = 1; j < 4; ++j){
			soma += sist[viz[sort][j]];
		}
		delE = 2*J*sist[sort]*soma;

		// Decido
		if (delE <= 0){
			sist[sort] *= -1;
			if (sist[sort] < 0){
				M -= 2;
				Ms[i+1] = M;
			}else{
				M += 2;
				Ms[i+1] = M;
			}
			// Falta atualizar aqui
		}else{
			if (uniform(0, 1) < prob[indexprob(delE)]){
				sist[sort] *= -1;
				if (sist[sort] < 0){
					M -= 2;
					Ms[i+1] = M;
				}else{
					M += 2;
					Ms[i+1] = M;
				}
				// Falta atualizar aqui
			}
		}
	}
	
	for (int i = 0; i < l*l; ++i){
		printf ("%i\n", Ms[i]);
	}
	
	
	return 0;
}

double uniform (double min, double max) {
	/*
	Função que gera um número aleatório em uma distribuição uniforme
	*/
	double random  = ((double) rand()) / RAND_MAX;
	double range = (max - min) * random;
	double n = range + min;	
	
	return n;
}

int indexprob (int del){
	switch (del) {
		case -8:
			return 0;
		case -4:
			return 1;
		case 0:
			return 2;
		case 4:
			return 3;
		case 8:
			return 4;
	}
}

