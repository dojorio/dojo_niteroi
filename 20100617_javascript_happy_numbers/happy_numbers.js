function happyNumber(number){

    var _olderNumbers = new Array()

    while (number != 1 && _olderNumbers.indexOf(number) != -1){
        _olderNumbers.push(number);
        var splittedNumber = splitNumber(number);
        number = sumPowArray(splittedNumber);
    }

    if (number == 1){
        return "I'm happy";
    } else {
        alert(number)
        return "I'm sad";
    }

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
