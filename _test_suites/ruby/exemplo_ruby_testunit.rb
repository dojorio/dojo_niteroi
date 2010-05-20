
require 'test/unit'

class Teste1 < Test::Unit::TestCase
  
  def test_passa
    assert_equal(1,1)
  end
  def nao_e_teste_pq_n_comeca_com_test
    assert_equal(1,1)
  end
  def test_nao_passa
    assert_equal(1,2)
  end
  
end

