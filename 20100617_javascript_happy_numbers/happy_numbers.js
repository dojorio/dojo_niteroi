function happyNumber(number){

    if (number == 1 || number == 7 || number == 10){
        return "I'm happy";
    }
    return "I'm sad";

}

function splitNumber(number){
    var _tmp = new String(number);
    var _return = new Array();
    for (var i = 0; i < _tmp.length; i++)
    {
        _return.push(parseInt(_tmp[i]));
    }
    return _return;
}
