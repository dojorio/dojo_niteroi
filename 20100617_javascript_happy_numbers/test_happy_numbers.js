var happy = "I'm happy";
var sad = "I'm sad";

describe('Happy Numbers', {

    "1 says: I'm happy": function() {
        value_of(happyNumber(1)).should_be(happy);
    },

    "2 says: I'm sad": function() {
        value_of(happyNumber(2)).should_be(sad);
    },

    "3 says: I'm sad": function() {
        value_of(happyNumber(3)).should_be(sad);
    },

    "7 says: I'm happy": function() {
        value_of(happyNumber(7)).should_be(happy);
    },

    "10 says: I'm happy": function() {
        value_of(happyNumber(10)).should_be(happy);
    },

});

describe('Split numbers', {

    "1 becomes [1]": function() {
        value_of(splitNumber(1)).should_be([1]);
    },

    "2 becomes [2]": function() {
        value_of(splitNumber(2)).should_be([2]);
    },

    "23 becomes [2, 3]": function() {
        value_of(splitNumber(23)).should_be([2, 3]);
    },

    "2334 becomes [2, 3, 3, 4]": function() {
        value_of(splitNumber(2334)).should_be([2, 3, 3, 4]);
    },
});

describe('Sum Pow Array', {

    "[7] becomes 49": function() {
        value_of(sumPowArray([7])).should_be([49]);
    },
});
