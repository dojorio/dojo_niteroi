function happyNumber(number){

    if(number == 2 || number == 3){
        return "I'm sad";
    }
    while (number != 1){
        var splittedNumber = splitNumber(number);
        number = sumPowArray(splittedNumber);
    }
    return "I'm happy";

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
