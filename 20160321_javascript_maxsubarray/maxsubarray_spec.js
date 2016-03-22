//https://www.hackerrank.com/challenges/maxsubarray

var assert = require('assert'),
    maxsubarray = require('./maxsubarray').maxsubarray;

describe('maxsubarray', function() {
    it('[1, 2, 3, 4]', function() {
      var listInput = [1, 2, 3, 4],
          listOutput = [ 10, 10 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
    it('[1, 2, 3]', function() {
      var listInput = [1, 2, 3],
          listOutput = [ 6, 6 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
    it('[1, 2, 3, -1]', function() {
      var listInput = [1, 2, 3, -1],
          listOutput = [ 6, 6 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
    it('[1, 2, -1, 3]', function() {
      var listInput = [1, 2, -1, 3],
          listOutput = [ 3, 6 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
    it('[-1, 2, 3]', function() {
      var listInput = [-1, 2, 3],
          listOutput = [ 5, 5 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
    it('[2, -1, 3]', function() {
      var listInput = [2, -1, 3],
          listOutput = [ 3, 5 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
    it('[-1, -2, -3]', function() {
      var listInput = [-1, -2, -3],
          listOutput = [ -1, -1 ];
      assert.deepEqual(maxsubarray(listInput), listOutput);
    });
});