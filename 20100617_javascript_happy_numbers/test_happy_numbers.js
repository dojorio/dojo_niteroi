describe('Happy Numbers', {

    'return "I\'m happy" for 1': function() {
        value_of(happy(1)).should_be("I'm happy");
    },

    'return "I\'m sad" for 2': function() {
        value_of(happy(2)).should_be("I'm sad");
    },

});