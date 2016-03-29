//https://www.hackerrank.com/challenges/common-child

var assert = require ('assert'),
    commonChild = require('./common_child').commonChild;

describe('commonChild', function() {
    it('["AA", "BB"]', function () {
        var fathers = ["AA", "BB"];
        assert.equal(commonChild(fathers), 0);
    });
    it('["AABB", "BB"]', function () {
        var fathers = ["AABB", "BB"];
        assert.equal(commonChild(fathers), 2);
    });
    it('["AAABB", "BB"]', function () {
        var fathers = ["AAABB", "BB"];
        assert.equal(commonChild(fathers), 2);
    });
    it('["BB", "AAABB"]', function () {
        var fathers = ["BB", "AAABB"];
        assert.equal(commonChild(fathers), 2);
    });
    it('["BBB", "AAABB"]', function () {
        var fathers = ["BBB", "AAABB"];
        assert.equal(commonChild(fathers), 2);
    });
    it('["CCC", "AAACC"]', function () {
        var fathers = ["CCC", "AAACC"];
        assert.equal(commonChild(fathers), 2);
    });
    it('["CCC", "AAAACC"]', function () {
        var fathers = ["CCC", "AAAACC"];
        assert.equal(commonChild(fathers), 2);
    });
    it('["CCCA", "AAAACC"]', function () {
        var fathers = ["CCCA", "AAAACC"];
        assert.equal(commonChild(fathers), 2);
    });
})