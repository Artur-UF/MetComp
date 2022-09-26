#include <stdio.h>
#include <stdlib.h>
# include <time.h>
#include <math.h>

#define E 2.7182818
#define T 2
#define J 1
#define L 6
#define L2 (L * L)
#define REP 100

// $ gcc ising-2D.c -o ising-2D -lm

int main () {
	srand (time(NULL));
	
	double uniform (double min, double max);
	int indexprob (int del);
	
	// Inicialização da matriz do sistema
    int *sist;    

    sist = (int *) malloc(L2 * sizeof(int));
    
	// Tudo up
	int c = 0;
	for (int i = 0; i < L2; ++i) {
		sist[i] = 1;
	}
	
	/*
	// Random
	for (int i = 0; i < L2; ++i) {
		if (random < 0.5){
			sist[i] = 1;
		}else{
			sist[i] = -1;
		}
	}
	*/
	
	// Geração da matriz de vizinhança
    int **viz;
    viz = (int**) malloc(L2 * sizeof(int*));
    for (int i = 0; i < L2; i++){
        viz[i] = (int*) malloc(5 * sizeof(int));
    }
    
	int cc = 0;
	int cl = 0;
	for (int i = 0; i < L2; i++) {
        //printf ("i = %i  p = %i \n", i, (cl*L) + cc);
        
		viz[i][0] = i;
		// Bordas
		if (cc == 0){
			viz[i][1] = i + (L-1); // Esquerda
			viz[i][2] = i + 1; // Direita
		}
		if (cc == L-1){
			viz[i][1] = i - 1; // Esquerda
			viz[i][2] = i - (L-1); // Direita
		}
		if (cl == 0){
			viz[i][3] = L2 - (L-cc); // Cima
			viz[i][4] = i + L; // Baixo
		}
		if (cl == L-1){
			viz[i][3] = i - L; // Cima
			viz[i][4] = cc; // Baixo
		}
		// Miolo
		if (cc > 0 & cc < L-1){
			viz[i][1] = i - 1; // Esquerda
			viz[i][2] = i + 1; // Direita
		}
		if (cl > 0 & cl < L-1){
			viz[i][3] = i - L; // Cima
			viz[i][4] = i + L; // Baixo
		}
		if (cc >= L-1){
			cc = 0;
			++cl;
		}else{
			++cc;
		}
		//printf ("%i %i %i %i %i\n", viz[i][0], viz[i][1], viz[i][2], viz[i][3], viz[i][4]);
	}	
	
	// Deltas E possíveis
	int dels[5] = {-8, -4, 0, 4, 8};
	double prob[5];
	
	// Vetor de probabilidades
	for (int i = 0; i < 5; ++i){
		prob[i] = pow(E, -dels[i]/T);
		//printf ("Prob (%i) = %lf\n", dels[i], prob[i]);
	}
	
	
	// Magnetização
	int M = 0;
	for (int i = 0; i < L2; ++i){
		M += sist[i];
	}
	
	// Variáveis necessárias para o loop temporal
	int sort;		// Spin sorteado
	int delE = 0;	
	int soma =  0;	// Soma dos vizinhos
	
	// Vetor com as magnetizações (por sítio) em cada passo
    int *Ms;    
    Ms = (int *) malloc((REP+1) * sizeof(int));
    Ms[0] = M;
    
    double teste = uniform(0, 1);
    
    printf ("teste random %lf\n", teste);
	for (int i = 0; i < REP; ++i){
		// Sorteio		
		sort = uniform(0, L2);
		
		// Calculo o delta E
		for (int j = 1; j <= 4; ++j){
			soma += sist[viz[sort][j]];
		}
		delE = 2*J*sist[sort]*soma;

		// Decido
		if (delE <= 0){
			sist[sort] *= -1;
			M += sist[sort]*2;
			Ms[i+1] = M;
		}else{ // É POSSÍVEL QUE O SINAL AQUI ESTEJA ERRADO
			if (uniform(0, 1) > prob[indexprob(delE)]){
				sist[sort] *= -1;
				M += sist[sort]*2;
				Ms[i+1] = M;
			}else{
				Ms[i+1] = M;
			}
		}
		soma = 0;
		delE = 0;
	}
	
	for (int i = 0; i < REP+1; ++i){
		printf ("%i %i\n", i, Ms[i]);
	}
	
	// Escrita do arquivo
	FILE *ark = fopen("plotising2d.txt", "w");
	for (int i = 0; i < REP+1; ++i){
		fprintf (ark, "%i %i\n", i, Ms[i]);
	}
	fclose(ark);
	
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

