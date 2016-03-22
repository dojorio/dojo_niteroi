require 'spec_helper'
require 'romanos'

describe "Romanos" do
	it "1 retorna I" do
		expect(1.romano).to eq "I"
	end

	it "2 retorna II" do
		expect(2.romano).to eq "II"
	end

	it "3 retorna III" do
		expect(3.romano).to eq "III"
	end

	it "10 retorna X" do
		expect(10.romano).to eq "X"
	end

	it "20 retorna XX" do
		expect(20.romano).to eq "XX"
	end

	it "30 retorna XXX" do
		expect(30.romano).to eq "XXX"
	end

	it "5 retorna V" do
		expect(5.romano).to eq "V"
	end

	it "6 retorna VI" do
		expect(6.romano).to eq "VI"
	end

	it "7 retorna VII" do
		expect(7.romano).to eq "VII"
	end

	it "8 retorna VIII" do 
		expect(8.romano).to eq "VIII"
	end

	it "15 retorna XV" do
		expect(15.romano).to eq "XV"
	end

	it "16 retorna XVI" do
		expect(16.romano).to eq "XVI"
	end

	it "11 retorna XI" do
		expect(11.romano).to eq "XI"
	end

	it "4 retorna IV" do
		expect(4.romano).to eq "IV"
	end

	it "14 retorna XIV" do 
		expect(14.romano).to eq "XIV"
	end

	it "34 retorna XXXIV" do
		expect(34.romano).to eq "XXXIV"
	end

	it "9 retorna IX" do
		expect(9.romano).to eq "IX"
	end

	it "50 retorna L" do
		expect(50.romano).to eq "L" 
	end

	it "59 retorna LIX" do
		expect(59.romano).to eq "LIX"
	end

	it "47 retorna XLVII" do
		expect(47.romano).to eq "XLVII"
	end

	it "68 retorna LXVIII" do
		expect(68.romano).to eq "LXVIII"
	end

	it "99 retorna XCIX" do
		expect(99.romano).to eq "XCIX"
	end
end