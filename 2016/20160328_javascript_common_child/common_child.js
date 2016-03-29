exports.commonChild = function (fathers) {
	var a = fathers[0],
		b = fathers[1];
		// aSorted = fathers[0].sort(),
		// bSorted = fathers[1].sort(),

	
	if (a.length > b.length){
		var max = a,
			min = b;
	}else{
		var min = a,
			max = b;
	}

	var arrCount = []
	var count = 0


	var maxAux = 0,
		is = false;
	for (var i = max.length - 1; i >= 0; i--) {
		for (var j = min.length - 1; j >= 0; j--) {
			if(min[j] == max[i]){
				count++;
				is = true;
			}
		};
		if (is){
			continue
		}
		count = 0;
	};

	return maxAux
};
