#include<bits/stdc++.h>
using namespace std;

int timer=1;

vector <int> start;
vector <int> endt;

void addedge(vector<int> A[],int u,int v)
{
    A[u].push_back(v);
    A[v].push_back(u);
}

int checkcycle(vector<int> A[],int v,int s)
{   // Using BFS
    queue <int> q;  

    vector<bool> visited(v+1,false);
    vector<int> parent(v+1,0);
    q.push(s);

    while(q.empty()==false)
    {
        int w = q.front();
        q.pop();
        cout<<w<<" ";
        visited[w]=true;

        for(int i=0;i<A[w].size();i++)
        {   

            if(visited[A[w][i]]==false)
            {   
                parent[A[w][i]]=w;
                q.push(A[w][i]);
                visited[A[w][i]]=true;
            }
            else
            {
                if(parent[w] != A[w][i])
                {
                cout<<"Cycle Detected at "<<A[w][i]<<" "<<w<<endl;
                //return 0;
                }
            }
            
        }

    }

    return 1;

}

int main()
{
int v=7;
vector <int> b[v];
/*
addedge(b,1,2);
addedge(b,2,3);
addedge(b,3,4);
addedge(b,3,5);
addedge(b,1,5);
addedge(b,5,6);
addedge(b,6,4);
*/

addedge(b,1,2);
//addedge(b,1,3);
addedge(b,1,4);
addedge(b,2,3);
addedge(b,3,4);

if(checkcycle(b,v,1))
{
    cout<<" NO Cycle \n";
}

    return 0;
}