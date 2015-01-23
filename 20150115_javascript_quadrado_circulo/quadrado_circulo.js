var naoTemIntersecao = function( circulo,  quadrado ) {
  return ( circulo.y < quadrado.y - quadrado.l
      || circulo.y > quadrado.y
      || circulo.x < quadrado.x
      || circulo.x > quadrado.x + quadrado.l );
}

var circuloNaBorda = function( circulo, quadrado ) {
  return circulo.x === quadrado.x + quadrado.l
      || circulo.x === quadrado.x
      || circulo.y === quadrado.y;
};

var areaIntersecao = function( circulo, quadrado ) {
  if (naoTemIntersecao(circulo, quadrado)) {
    return 0;
  }

  if (circuloNaBorda(circulo, quadrado)) {
    return Math.PI / 2;
  }

  return Math.PI;
}

exports.areaIntersecao = areaIntersecao;