
class Solution {
public:
	string countAndSay(int n) {
		// see if i can solve this within O(n2); most others are doing in O(n3)

		// possible if i can process getting a new data using the old one in single for loop
		// Given: 21 -> acquire 1211
		string output = "1";
		string input0 = "11";
		char prevValue = input0[0];
		int count = 1;
		string outputTest = "";

		if (n == 1) return "1";
		else if (n == 2) return "11";

		for (int j = 2; j < n; j++) { // wtf is going on here

			for (int i = 1; i <= input0.length() - 1; i++) {
				if (prevValue != input0[i]) {
					outputTest += to_string(count) + prevValue;
					count = 1;
					prevValue = input0[i];
				}
				else {
					count++;
				}
			}
			outputTest += to_string(count) + prevValue;
			input0 = outputTest;
			outputTest = "";
			prevValue = input0[0]; 
			count = 1;
			cout << input0 << endl;
		}

		return input0;
	}
};
