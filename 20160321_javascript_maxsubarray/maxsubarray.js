var maxsubarray = function(list) {
  var sumContiguous = 0,
      sumNonContiguous = 0,
      sumAux = 0
      // allNegatives = list.reduce(function(memo, current){ 
      //   if(current < 0){
      //     return memo.push(current);
      //   }
      //   return memo;
      // }, []),
      // maxBellowZero = Math.max.apply(undefined, allNegatives);
  //sumContiguous
  for (var i = 0; i <= list.length - 1; i++) {
    if(list[i] >= 0){
      sumContiguous += list[i];
    }else if (sumContiguous > sumAux) { //negative
        sumAux = sumContiguous;
        sumContiguous = 0; //zerar pra prox
        continue;
    }
  };
  if(sumAux > sumContiguous){
    sumContiguous = sumAux;
  }
  // if (maxBellowZero > sumContiguous) {
  //   sumContiguous = maxBellowZero;
  // };

  //sumNonContiguous
  for (var i = 0; i <= list.length - 1; i++) {
    if(list[i] >= 0){
      sumNonContiguous += list[i];
    }
  };
  return [sumContiguous, sumNonContiguous];
}

exports.maxsubarray = maxsubarray;