#include <bits/stdc++.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <algorithm>



using namespace std;

typedef pair <int, int> P;
int dag_n;
const int N = 999999;
const int w = 15134;
map <int, int> anc[N];
vector <int> child[N];
map <int, int> mp_id;
int id[N], feq[N] = {}, indegree[N] = {};
int K;
double val[w][w] = {}, sumscore[N] = {};
int cnt = 0, root = 0;
map <int, int>::iterator ite;
queue<int> que;
vector<int> S;
set<int> result;
vector<int>tmp_q;
string name[N] = {};
FILE *fout, *fout_record;

typedef struct Score
{
	int id, round;
	double score;
}Score;

bool operator< (const Score& t1, const Score& t2) {
	return t1.score < t2.score;
}

string Trim(string& str)
{
	
	str.erase(0, str.find_first_not_of(" \t\r\n"));
	str.erase(str.find_last_not_of(" \t\r\n") + 1);
	return str;
}

priority_queue<Score, vector <Score> > candidate;

double SummaryImpact(int level, int feq) {
	return feq / level;

}

double update(int x, int y) {
	double sum = 0;
	for (int i = 0; i < cnt; i++)
		if (val[x][i] > 0 && val[y][i] > 0) {
			sum += val[y][i] - max(0.0, val[y][i] - val[x][i]);
			val[y][i] = max(0.0, val[y][i] - val[x][i]);
		}
	return sum;
}


void get_queue() {
	tmp_q.clear();
	for (int i = 0; i < cnt; i++) {
		
		if (indegree[i] == 0) {
			que.push(i);
			tmp_q.push_back(i);
		}
		anc[i].clear();
	}
	//get queue and ancestor
	while (!que.empty()) {
		int x = que.front();
		//printf("X=%d\n", x);
		anc[x][x] = 0;
		que.pop();
		for (int i = 0; i < child[x].size(); i++) {
			
			int y = child[x][i];
			indegree[y]--;
			if (indegree[y] == 0) {
				que.push(y);
				tmp_q.push_back(y);
			}
			for (ite = anc[x].begin(); ite != anc[x].end(); ite++) {
				
				if (anc[y].find((*ite).first) != anc[y].end())
				{
					anc[y][(*ite).first] = min(anc[y][(*ite).first], (*ite).second + 1);

				}
				else {
					anc[y][(*ite).first] = (*ite).second + 1;
				}
			}
		}
	}
}
void init() {
	//printf("------inside init 1---\n");
	get_queue();
	
	for (int i = 0; i < cnt; i++)
	{

		//printf("------inside init 2--- feq[%d]=%d\n",i, feq[i]);
		if (anc[i].size()>0 && feq[i]) {
			for (ite = anc[i].begin(); ite != anc[i].end(); ite++) {
				//��i���������� ����summary impact
				//up to down
				//val-->how anc[i] can summarize i, sumscore--> total score of anc[i]
				//printf("ANC[%d]:%d\n", (*ite).first,(*ite).second);
				val[(*ite).first][i] = SummaryImpact(((*ite).second + 1), feq[i]);//�൱��ĳnode�����Լ��ĳ�ʼ���� (*ite).second+1���ص��� ������ӵ�еĺ��ӵĸ���
				sumscore[(*ite).first] += SummaryImpact(((*ite).second + 1), feq[i]);
			}
		}
		else {
			val[i][i] = SummaryImpact(1000, feq[i]);
			sumscore[i] += SummaryImpact(1000, feq[i]);
		}

	}

	/*
	for (int i = 0; i < cnt; i++) {
		printf("Sumscore[%d]=%f\n", i, sumscore[i]);
	}
	printf("------inside init 3------\n");
	*/
	int round = 0;

	for (int i = 0; i < cnt; i++) {
		Score tmp;
		tmp.round = 1;
		tmp.id = i;
		tmp.score = sumscore[i];
		candidate.push(tmp);
	}
}



void select(int K) {
	double Total_Score = 0;
	int round = 0;
	S.clear();
	result.clear();

	while (!candidate.empty()) {
		Score tmp = candidate.top();
		candidate.pop();

		if (tmp.round > round) {
			round++;
			
			Total_Score += tmp.score;
			S.push_back(tmp.id);
			result.insert(tmp.id);
			for (int i = 0; i < cnt; i++) {
				Score up;
				if (i != tmp.id) {
					sumscore[i] -= update(tmp.id, i);
					up.score = sumscore[i];
					up.id = i;
					up.round = round + 1;
					candidate.push(up);
				}

			}


			update(tmp.id, tmp.id);
			sumscore[tmp.id] = 0;
		}
		if (round == K) break;

	}
	//fprintf(fout_record,"%s,%f\n", "Total Socre",Total_Score);

}

double Distance(int x, set<int>ans) {
	vector<int> H;
	set<int> check;
	H.clear();
	H.push_back(x);
	check.insert(x);
	int size = H.size();
	double depth = 0;
	int height = 0;
	
	while (height < H.size()) {
		int y = H[height];
		height++;
		
		if (ans.find(y) != ans.end()) {
			return depth;
		}
		
		for (ite = anc[y].begin(); ite != anc[y].end(); ite++) {
			if (check.find((*ite).first) == check.end()) {
				H.push_back((*ite).first);
				check.insert((*ite).first);
				//printf("ite.first=%d, ite.second = %d\n", (*ite).first, (*ite).second);
			}
		}

		for (int i = 0; i < child[y].size(); i++) {
			int a = child[y][i];
			if (check.find(a) == check.end()) {
				H.push_back(a);
				check.insert(a);
			}
		}
		if (height == size) {
			size = H.size();
			depth++;
		}
	}
	return depth;

}
double Evaluation_Distance(vector<int> Q, set <int> ans)
{
	double dsum = 0;
	for (int i = 0; i<Q.size(); i++)
	{
		int x = Q[i];
		dsum += Distance(x, ans);
	}
	
	fprintf(fout_record,"%d,%f\n",(int)ans.size(), dsum);
	//fprintf(fout_score, "Total Distance: %.0lf\n", dsum);
	return dsum;
}

vector<int> find_parent(int x, set<int>tmp)
{
	vector<int> item;
	for (int i = 0; i < cnt; i++) {
		for (int k = 0; k < child[i].size(); k++) {
			int y = child[i][k];
			if (y == x) {
				
				item.push_back(i);
			}
		}
	}
	if (item.size() == 0) {
		item.push_back(0);
	}
	return item;
	
}

void translate_dag() {
	fprintf(fout,"%s,%s,%s\n","parent","name","value");
	fprintf(fout,"%s,%s,%d\n","null","Anime",30);
	printf( "%s,%s,%s\n", "parent", "name", "value");
	printf( "%s,%s,%d\n", "null", "Anime", 30);
	set<int> tmp;
	for (int i = 0; i < S.size(); i++) {
		tmp.insert(S[i]);
	}
	queue <int>plist;
	vector<int>*rela = new vector<int>[N+1];

	for (int i = 0; i < S.size(); i++) {
		int x = S[i];
		vector<int> a = find_parent(x,tmp);
		//printf("a.size=%d\n", a.size());
		if (a.size() > 1) {
			for (int k = 0; k < a.size(); k++) {
				
				int t = a[k];
				plist.push(t);
				//printf("a[k]=%d\n", a[k]);
				rela[x].push_back(t);
			}
		}
		else {
			plist.push(a[0]);
			//printf("a[k]=%d\n", a[0]);
			rela[x].push_back(a[0]);
		}
		
	}
	
	int k;
	while (!plist.empty()) {
		k = plist.front();
		plist.pop();
		vector<int> p;
		if (tmp.find(k) == tmp.end()) {
			p = find_parent(k, tmp);
			if (p.size() > 1) {
				for (int k = 1; k < p.size(); k++) {
					plist.push(p[k]);
				}
			}
		}
		else {
			for (int i = 0; i < S.size(); i++) {
				int x = S[i];
				for (int z = 0; z < rela[x].size(); z++) {
					if (k != rela[x][z]) {
						rela[x].erase(rela[x].begin() + z);
					}
				}
			}
		}
	}
	for (int i = 0; i < S.size(); i++) {
		int x = S[i];
	
		fprintf(fout, "%s,%s,%d\n", name[rela[x][0]].c_str(), name[x].c_str(), feq[x]);
		printf("%s,%s,%d\n", name[rela[x][0]].c_str(), name[x].c_str(), feq[x]);
		//printf("parent=%s\nchild=%s\nvalue=%d\n", name_p.c_str(), name_c.c_str(), feq[x]);
	}

}
int main(int argc, char* argv[])
{



	FILE *fin;



	int n;
	int num;
	
	//n=������ num=node���id
	if (argv[2] != NULL){
		fin = fopen(argv[2], "r");
	}
	else {
		fin = fopen("D:/For-F-drive/school/comp/FYP/TSL/code/rela_for_Kvdo_Japan.txt", "r");
	//	fin = fopen("D:/For-F-drive/school/comp/FYP/TSL/code/DAG_LATT20.txt", "r");
	//	fin = fopen("dag-data.txt", "r");
	}
	
	fscanf(fin, "%d %d", &n, &num);
	
	//printf("Total records and nodes: %d %d\n", n, num);

	cnt = 0;
	dag_n = num;
	
	mp_id.clear();
	memset(indegree, 0, sizeof indegree);
	memset(val, 0, sizeof val);
	memset(sumscore, 0, sizeof sumscore);
	memset(feq, 0, sizeof feq);

	for (int i = 0; i < num; i++) child[i].clear();
	for (int i = 0; i < n; i++)
	{
		int x, y;
		fscanf(fin, "%d %d", &x, &y);
		//printf("%d %d\n", x, y);
		//��=cnt ��cnt++��cnt��ʾһ���м���node��id-->�ڼ�λ�����nodeΪx��y
		if (mp_id.find(x) == mp_id.end())
		{
			mp_id[x] = cnt++;
			id[mp_id[x]] = x;
		}
		if (mp_id.find(y) == mp_id.end()) {
			mp_id[y] = cnt++;
			id[mp_id[y]] = y;
		}
		child[mp_id[x]].push_back(mp_id[y]);
		indegree[mp_id[y]]++;
	//	printf("in the initisual x=%d, mp_id[x]=%d, y=%d, mp_id[y]=%d cnt=%d, du[mp_id[y]]=%d\n", x, mp_id[x], y, mp_id[y], cnt, indegree[mp_id[y]]);
	}

	fclose(fin);
	//fin = fopen("freq-dag.txt", "r");
	//fin = fopen("D:/For-F-drive/school/comp/FYP/TSL/code/feq-dag-latt.txt", "r");
	if (argv[3] != NULL) {
		fin = fopen(argv[3], "r");
	}
	else {
		fin = fopen("E:/school/comp/FYP/TSL/code/rela_for_Kvdo_Japan.txt", "r");
		//	fin = fopen("D:/For-F-drive/school/comp/FYP/TSL/code/DAG_LATT20.txt", "r");
		//	fin = fopen("dag-data.txt", "r");
	}

	fscanf(fin, "%d %d", &n, &num);

	fin = fopen("E:/school/comp/FYP/TSL/code/freq_for_Kvdo_Japan.txt", "r");
	
	int m;
	fscanf(fin, "%d", &m);
	K = 10;
	if (argv[1] != NULL) {
	K = atoi(argv[1]);
	}
	//printf("K = %d\n", K);
	//int sum = 0;
	for (int i = 0; i < m; i++)
	{
		int x, y;
		fscanf(fin, "%d %d", &x, &y);

		if (y != 0) {
			feq[mp_id[x]] = y;
		}
		//printf("node and freq: %d %d\n", mp_id[x], feq[mp_id[x]]);
	}

	fclose(fin);
	ifstream infile("E:/school/comp/eclipse-workspace/test/WebContent/name_and_ID_Japan.csv",ios::in );
	string line;
	while (getline(infile, line)) {
		//cout << line << endl;
		istringstream ss(line);
		string str;
		vector<string>lineArray;
		while (getline(ss, str, ',')) {
			lineArray.push_back(str);//lineArray[0]-->id, lineArray[1]-->name
			
		}
		if (lineArray[0] == "ID") {
			continue;
		}
		int x = stoi(lineArray[0], nullptr, 10);
		if (name[mp_id[x]] =="") {
			name[mp_id[x]] = Trim(lineArray[1]);
		}
		
	}

	fout_record = fopen("E:/school/comp/eclipse-workspace/test/WebContent/ScoreResult.csv", "w");
	init();
	//printf("----------end init-----------\n");
	select(K);
	//printf("============= Answers ============\n");
	
	sort(S.begin(), S.end());
	
	fout = fopen("E:/school/comp/eclipse-workspace/test/WebContent/dag-result.csv", "w");

	translate_dag();
	fclose(fout);
	//Analysis
	int add = 1;
	int init = 1;
	if (K > 10 && K < 30) {
		add = 5;
		init = 5;
	}
	else if (K >= 30 && K < 60) {
		add = 10;
		init = 10;
	}
	else if(K>=60){
		add = 20;
		init = 10;
	}
	else if (K <= 10 && K>5) {
		add = 2;
		init = 2;
	}
	fprintf(fout_record, "%s,%s\n", "Item", "Value");
	for (int k = init; k <= K; k +=add)
	{
		result.clear();
		for (int i = 0; i<k && i<S.size(); i++)
		{
			result.insert(S[i]);
		}
		//printf( "#%d ", (int)result.size());
		Evaluation_Distance(tmp_q, result);
	}
	fclose(fout_record);

	return 0;
}