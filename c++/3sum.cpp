#include<bits/stdc++.h>
using namespace std;

vector<int> solution(vector<int> vals, int target){
	
	vector<int> res(3);
	
	sort(vals.begin(),vals.end());
	for(int i=0;i<vals.size();i++)
	{
		int x = vals[i];
		int l = i+1;
		int r = vals.size()-1;
		while(l<r)
		{
			if(x+vals[l]+vals[r]==target)
			{
				res[0] = x;
				res[1] = vals[l]
				res[2] = vals[r]
				return res;
			}
			if(x+vals[l]+vals[r]>target)
			{
				r--;
			}
			else
			{
				l++;
			}
		}
	}

	
	return res;
}

int main()
{
	vector<int> vals={2,6,3,11,7,4,9,7,10,6};
	int target = 20;

	vector<int> res = solution(vals, target);

	
	if(res.size() == 0)
		cout<<"No triplet"<<endl;
	else
		cout << res[0] << " " << res[1] << " " << res[2] << endl; 
	return 0;
}
