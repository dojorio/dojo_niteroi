function encaixotar(lista_objetos, linha, coluna) {
    var caixa = gera_caixa_vazia(linha, coluna);

    var i = 0;
    for (var i = 0; i < lista_objetos.length; i++) {
        caixa[i] = lista_objetos[i];
    }

    var str_caixa = "";
    for(i = 0; i < caixa.length; i++)
        str_caixa = caixa[i].join('') +"\n";

    return str_caixa
}

function gera_caixa_vazia(linha, coluna) {
    var caixa = [];
    for (var i = 0; i < linha; i++) {
        caixa[i] = gera_linha_vazia(coluna)
    }
    return caixa;
}

function gera_linha_vazia(coluna) {
    var linha = []
    for (var i = 0;  i<coluna; i++) {
        linha[i] = '-'
    }
    return linha;
}
