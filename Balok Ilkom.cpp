#include <iostream>
#include <bits/stdc++.h> 
#define pii pair<int, int> 
#define mp make_pair 
using namespace std;
int BFS (int aA, int aB, int mA, int mB){
	map<pii, int> m; 
    bool isSolvable = false; 
    vector<pii> path; 
  
    queue<pii> q;
    q.push({ 0, 0 });
	
	while (!q.empty()) { 
		//Kondisi Solusi
			if (u.first == u.second) { 
				isSolvable = true; 
				if (u.first >= 20 || u.second >=20) { 
					//berhenti karena mencapai batas
					path.push_back({ u.first, 0 }); 
				} 
				// cetak path solusi
				int sz = path.size(); 
				for (int i = 0; i < sz; i++) 
					cout << "(" << path[i].first 
						<< ", " << path[i].second << ")\n"; 
				break; 
				
			}
			for (int i = 0; u <= max(a, b); i++) {
				//wip
			}
		}
		
	q.push({ a, 0 }); // reset state A 
    q.push({ 0, b }); // reset state B 
	
}


int main() 
{ 
    int addA = 5, addB = 3, minA = 2, minB = 1; 
  
    //printf("Langkah Minimum  %d", 
           //minSteps(addA, addB, minA, minB)); 
    printf("Langkah Mininum %d",BFS(addA,addB,minA,minB));
    return 0; 
} 
