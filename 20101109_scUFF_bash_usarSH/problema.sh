#e^ln((n)/2)
#!/bin/bash
operacao() {
  op="$3"
  if [ "$op" == '%' ] ; then
    echo $(($1$op$2))
  elif [ "$op" == 'rt' ] ; then
      echo `echo -e "scale=6\ne(l($1)/$2)+0.000001" | bc -l`
  else
    if [ "$op" == '**' ] ; then
      op='^'   
    fi
    echo `echo -e "scale=6\n$1$op$2" | bc -l`
  fi
}

test_soma_1_com_2() {
  assertEquals "$(operacao 1 2 '+')" '3'
}

test_soma_2_com_2() {
  assertEquals "$(operacao 2 2 '+')" '4'
}

test_subtrai_2_com_1() {
  assertEquals "$(operacao 2 1 '-')" '1'
}

test_divide_4_com_2() {
  assertEquals "$(operacao 4 2 '/')" '2.000000'
}

test_divide_3_com_2() {
  assertEquals "$(operacao 3 2 '/')" '1.500000'
}

test_resto_8_com_3() {
  assertEquals "$(operacao 8 3 '%')" '2'
}

test_multiplicacao_8_com_3() {
  assertEquals "$(operacao 8 3 '*')" '24'
}

test_exponencial_2_com_3() {
  assertEquals "$(operacao 2 3 '^')" '8'
}

test_exponencial_vezes_vezes_2_com_3() {
  assertEquals "$(operacao 2 3 '**')" '8'
}

test_raiz_de_4_com_2() {
  assertEquals "$(operacao 4 2 'rt')" '2.000000'
}

test_raiz_cubica_de_12() {
  assertEquals '2.289428' "$(operacao 12 3 'rt')" 
}




source "/home/joao/shunit2/build/shunit2"
 
