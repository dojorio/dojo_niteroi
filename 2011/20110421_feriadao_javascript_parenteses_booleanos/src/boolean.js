function checkBool(expression) {
    if(operandsArray(expression).length == 3) {
        var expressionsArray = putParenthesis(expression)
        return trueCount(expressionsArray[0]) + trueCount(expressionsArray[1]);
    }

    return trueCount(expression)
}

function trueCount(expression){
    return eval(replaceOperators(expression)) ? 1 : 0;
}

function replaceOperators(expression) {
    return expression.replace(/and/g, "&&").replace(/xor/g, "^").replace(/or/g, "||")
}

function operandsArray(expression) {
    return expression.split(/and|xor|or/i)
}

function operatorsArray(expression){
    return expression.split(/true|false/i)
}

function putParenthesis(expression) {
    var operators = operatorsArray(expression);
    var operands = operandsArray(expression);

    var expressionsArray = new Array()
    expressionsArray.push(operands[0] + " " + operators[1] + " (" + operands[1] + " " + operators[2] + " " + operands[2] + " )")
    expressionsArray.push("( " + operands[0] + " " + operators[1] + " " + operands[1] + ") " + operators[2] + " " + operands[2])
    return expressionsArray;
}

function bruteForce(expression) {
    positions = expression.split(" ")
    buildPossibilities(positions)
}

function buildPossibilities(positions){
    for (var position = 0; position < positions.length; position++ )
    {
        var newArray = new Array()
        positions.pop()
        newArray.push("(" + buildPossibilities(positions) + ")")
        newArray.push(buildPossibilities(positions))
        return newArray;
    }
}

