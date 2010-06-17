function happyNumber(number){
    var aux;
    while (number != 1){
        aux = 1;
        while(aux<splitNumber(number).length){


        }
    }


    if (number == 1 || number == 7 || number == 10){
        return "I'm happy";
    }
    return "I'm sad";

}

function splitNumber(number){
    var _strNumber = new String(number);
    var _splittedNumber = new Array();
    for (var i = 0; i < _strNumber.length; i++)
    {
        _splittedNumber.push(parseInt(_strNumber[i]));
    }
    return _splittedNumber;
}

function sumPowArray(splittedNumber){
    var sum = 0;
    for (var i = 0; i < splittedNumber.length; i++)
    {
        sum += Math.pow(splittedNumber[i], 2);
    }
    return sum;
}
