#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	char name[4][10];
	double score[4];
	char a[10];
	char b[10];
	double awin, asame, alose;
	double bestscore = 0;
	int bestscoreindex;
	double endscore[4];
	int samebestscorecount=0;
	scanf("%s %s %s %s", name[0], name[1], name[2], name[3]);

	for(int i=0;i<6;i++){
		scanf("%s %s %lf %lf %lf", a, b, &awin, &asame, &alose);
		for(int j=0;j<4;j++){
			if(strcmp(a, name[j]) == 0){
				score[j] += 3*awin + asame;
			}
			if(strcmp(b, name[j]) == 0){
				score[j] += asame + 3*alose;
			}
		}
	}

	for(int i=0;i<4;i++){
		if(score[i] >= bestscore){
			bestscore = score[i];
			bestscoreindex = i;
		}
	}
	for(int i=0;i<4;i++){
		if(samebestscorecount == score[i])
			samebestscorecount++;
	}

	if(samebestscorecount == 4){
		for(int i=0;i<4;i++)
			endscore[i] = (double)0.5;
	}else if(samebestscorecount == 3){
		for(int i=0;i<4;i++){
			if(score[i] == bestscore){
				endscore[i] = (double)2/3;
			}else{
				endscore[i] = 0;
			}
		}
	}else if(samebestscorecount == 2){
		for(int i=0;i<4;i++){
			if(score[i] == bestscore){
				endscore[i] = 1;
			}else{
				endscore[i] = 0;
			}
		}
	}else{
		int bestscoreindex2;
		double bestscore2=0;
		int samebestscorecount2=0;
		for(int i=0;i<4;i++){
			if(score[i] >= bestscore2 && score[i] < bestscore){
				bestscore2 = score[i];
				bestscoreindex2 = i;
			}
		}
		for(int i=0;i<4;i++){
				if(bestscore2 == score[i])
					samebestscorecount2++;
			}
		if(samebestscorecount2 == 3){
			for(int i=0;i<4;i++){
				if(score[i] == bestscore2)
					endscore[i] = (double)1/3;
			}
		}else if(samebestscorecount2 == 2){
			for(int i=0;i<4;i++){
				if(score[i] == bestscore2)
					endscore[i] = (double)1/2;
				else
					endscore[i] = 0;
			}
		}else{
			for(int i=0;i<4;i++){
				if(score[i] == bestscore2)
					endscore[i] = 1;
				else
					endscore[i] = 0;
			}
		}
		for(int i=0;i<4;i++){
			if(score[i] == bestscore){
				endscore[i] = 1;
			}
		}
	}

	for(int i=0;i<4;i++){
		printf("%.10lf\n", endscore[i]);
	}

	return 0;
}