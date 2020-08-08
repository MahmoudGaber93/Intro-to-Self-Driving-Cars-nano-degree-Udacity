#include "headers/blur.h"
#include "headers/zeros.h"
using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector < vector <float> > blur(vector < vector < float> > &grid, float blurring) {

	// OPTIMIZATION: window, DX and  DY variables have the 
    // same value each time the function is run.
  	// It's very inefficient to recalculate the vectors
    // every time the function runs. 
    // 
    // The const and/or static operator could be useful.
  	// Define and declare window, DX, and DY using the
    // bracket syntax: vector<int> foo = {1, 2, 3, 4} 
    // instead of calculating these vectors with for loops 
    // and push back
  static vector < vector < float> > window;
	vector < vector <float> > newGrid;
	vector <float> row;
	int height;
	int width;

	height = grid.size();
	width = grid[0].size();

	static	float center = 1.0 - blurring;
	static	float corner = blurring / 12.0;
	static	float adjacent = blurring / 6.0;

	int i, j;
	float val;

	for (i=0; i<3; i++) {
		row.clear();
		for (j=0; j<3; j++) {
			switch (i) {
				case 0: 
				switch (j) {
					case 0: 
					val = corner;
					break;

					case 1: 
					val = adjacent;
					break;

					case 2: 
					val = corner;
					break;
				}
				break; 

				case 1:
				switch (j) {
					case 0: 
					val = adjacent;
					break;

					case 1: 
					val = center;
					break;
					
					case 2: 
					val = adjacent;
					break;
				}
				break;

				case 2:
				switch(j) {
					case 0: 
					val = corner;
					break;

					case 1: 
					val = adjacent;
					break;
					
					case 2: 
					val = corner;
					break;
				}
				break;
			}
			row.push_back(val);
		}
		window.push_back(row);
	}


	static vector < int> DX = {-1,0,1};
	static vector < int> DY  =  {-1,0,1};



	int ii;
	int jj;
	int new_i;
	int new_j;


	// OPTIMIZATION: Use your improved zeros function
	
  newGrid= zeros(height,width);

	for (i=0; i< height; i++ ) {
		for (j=0; j<width; j++ ) {
			for (ii=0; ii<3; ii++) {
				for (jj=0; jj<3; jj++) {
					newGrid[ (i + DY[ii] + height) % height][(j + DX[jj] + width) % width] += grid[i][j] *  window[ii][jj];
				}
			}
		}
	}

	return newGrid;
}
