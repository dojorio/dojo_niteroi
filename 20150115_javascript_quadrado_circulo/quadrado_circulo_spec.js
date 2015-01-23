//http://dojopuzzles.com/problemas/exibe/quadrados-e-circulos/

var assert = require('assert'),
    areaIntersecao = require('./quadrado_circulo').areaIntersecao;

describe('Quadrado Circulo', function() {
    it('Circulo dentro de um quadrado', function() {
      var circulo  = {x: 4, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r
      );
    });

    it('Circulo fora de um quadrado', function() {
      var circulo  = {x: 6, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });

    it('Circulo x++ fora de um quadrado', function() {
      var circulo  = {x: 7, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });

    it('Circulo fora de um quadrado antes', function() {
      var circulo  = {x: 2, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });

    it('Circulo fora de um quadrado antes e x negativo', function() {
      var circulo  = {x: -2, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });

    it('Circulo mexendo no y fora de um quadrado', function() {
      var circulo  = {x: 4, y: 4, r: 1},
          quadrado = {x: 3, y: 3, l: 2};


      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });

    it('Circulo mexendo no y fora de um quadrado pra baixo', function() {
      var circulo  = {x: 4, y: 0, r: 1},
          quadrado = {x: 3, y: 3, l: 2};


      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });
    it('Mexendo tudo', function() {
      var circulo  = {x: 5, y: 1, r: 1},
          quadrado = {x: 4, y: 4, l: 2};


      assert.equal(
        areaIntersecao( circulo, quadrado ),
        0
      );
    });

    it('Mexendo tudo com circulo dentro do quadrado', function() {
      var circulo  = {x: 5, y: 3, r: 1},
          quadrado = {x: 4, y: 4, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r
      );
    });

    it('Aumentando o quadrado com circulo dentro', function() {
      var circulo  = {x: 5, y: 3, r: 1},
          quadrado = {x: 4, y: 4, l: 3};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r
      );
    });

    it('Aumentando o quadrado com circulo dentro', function() {
      var circulo  = {x: 5, y: 3, r: 1},
          quadrado = {x: 4, y: 4, l: 3};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r
      );
    });

    it('Circulo com centro do lado direito do quadrado', function() {
      var circulo  = {x: 5, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r / 2
      );
    });

    it('Circulo com centro no lado esquerdo do quadrado', function() {
      var circulo  = {x: 3, y: 2, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r / 2
      );
    });

    it('Circulo com centro acima do quadrado', function() {
      var circulo  = {x: 4, y: 3, r: 1},
          quadrado = {x: 3, y: 3, l: 2};

      assert.equal(
        areaIntersecao( circulo, quadrado ),
        Math.PI * circulo.r * circulo.r / 2
      );
    });
});