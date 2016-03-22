describe("Parenteses booleanos", function() {

  it("Deve retornar 1 possibilidade para true", function() {   
    expect(checkBool("true")).toEqual(1); 
  });

  it("Deve retornar nenhuma possibilidade para false", function() {   
    expect(checkBool("false")).toEqual(0); 
  });

  it("Deve retornar nenhuma possibilidade para true and false", function() {   
    expect(checkBool("true and false")).toEqual(0); 
  });

  it("Deve retornar 1 possibilidade para true or false", function() {   
    expect(checkBool("true or false")).toEqual(1); 
  });

  it("Deve retornar 1 possibilidade para true xor false", function() {   
    expect(checkBool("true xor false")).toEqual(1); 
  });

  it("Deve retornar nenhuma possibilidade para true xor true", function() {   
    expect(checkBool("true xor true")).toEqual(0); 
  });

  it("Deve retornar nenhuma possibilidade para false xor false", function() {   
    expect(checkBool("false xor false")).toEqual(0); 
  });

  it("Deve retornar 2 possibilidades para true and true and true", function() {   
    expect(checkBool("true and true and true")).toEqual(2);
  });

  it("Deve retornar 2 possibilidades para true or true or true", function() {   
    expect(checkBool("true or true or true")).toEqual(2);
  });

  it("Deve retornar 2 possibilidades para true or true and true", function() {   
    expect(checkBool("true or true and true")).toEqual(2);
  });

  it("Deve retornar 2 possibilidades para true xor true xor true", function() {   
    expect(checkBool("true xor true xor true")).toEqual(2);
  });

  it("Deve retornar 1 possibilidade para true or true xor true", function() {   
    expect(checkBool("true or true xor true")).toEqual(1);
  });

  it("Deve retornar 1 possibilidade para true or true and false", function() {   
    expect(checkBool("true or true and false")).toEqual(1);
  });

  it("Deve retornar nenhuma possibilidade para false or true and false", function() {   
    expect(checkBool("false or true and false")).toEqual(0);
  });

  it("Deve retornar nenhuma possibilidade para true and true and true and true", function() {   
    expect(checkBool("true and true and true and true")).toEqual(5);
  });

  it("Coloca Parenteses", function() {   
    expect(bruteForce("true and true and true")).toEqual(["true and (true and true)", "(true and true) and true"]);
  });

});
