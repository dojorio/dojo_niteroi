require './miojo'

describe "Preparo de miojo" do
  it 'com ampulhetas de 10 e 1, com uma no menor tempo necessário' do
    ampulhetas = [10,1]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(false)
  end
  it 'com ampulhetas de 5 e 7' do
    ampulhetas = [5,7]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(10)
  end
  it 'com ampulhetas de 7 e 7' do
    ampulhetas = [7,7]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(false)
  end
  it 'com ampulhetas de 6 e 9' do
    ampulhetas = [6,9]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(9)
  end
  it 'com ampulhetas de 9 e 6' do
    ampulhetas = [9,6]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(9)
  end
  it 'com ampulhetas de 4 e 7' do
    ampulhetas = [4,7]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(7)
  end
  it 'com ampulhetas de 4 e 4' do
    ampulhetas = [4,4]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(false)
  end
  it 'com ampulhetas de 13 e 10' do
    ampulhetas = [13,10]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(13)
  end
  it 'com ampulhetas de 5 e 9' do
    ampulhetas = [5,9]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(18)
  end
  it 'com ampulhetas de 9 e 5' do
    ampulhetas = [9,5]
    tempo_necessario = 3

    expect(prepara_miojo(tempo_necessario, ampulhetas)).to eq(18)
  end
end