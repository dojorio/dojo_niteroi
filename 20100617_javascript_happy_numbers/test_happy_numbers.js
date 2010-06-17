describe('Happy Numbers', {
    happy:"I'm happy", sad:"I'm sad",

    'return "I\'m happy" for 1': function() {
        value_of(happy(1)).should_be(happy);
    },

    'return "I\'m sad" for 2': function() {
        value_of(happy(2)).should_be("I'm sad");
    },

});
