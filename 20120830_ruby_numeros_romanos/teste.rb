require "romano"

describe Romano do

	it "passa I e retorna 1" do
		romano = Romano.new
		romano.to_numero("I").should == 1
	end
	
	it "passa II e retorna 2" do
		romano = Romano.new
		romano.to_numero("II").should == 2
	end
	it "passa III e retorna 3" do
		romano = Romano.new
		romano.to_numero("III").should == 3
	end
	it "passa IV e retorna 4" do
		romano = Romano.new
		romano.to_numero("IV").should == 4
	end
	it "passa V e retorna 5" do
		romano = Romano.new
		romano.to_numero("V").should == 5
	end
	it "passa VI e retorna 6" do
		romano = Romano.new
		romano.to_numero("VI").should == 6
	end
		it "passa VII e retorna 7" do
		romano = Romano.new
		romano.to_numero("VII").should == 7
	end
		it "passa VIII e retorna 8" do
		romano = Romano.new
		romano.to_numero("VIII").should == 8
	end
		it "passa IX e retorna 9" do
		romano = Romano.new
		romano.to_numero("IX").should == 9
	end
		it "passa X e retorna 10" do
		romano = Romano.new
		romano.to_numero("X").should == 10
	end
		it "passa XIV e retorna 14" do
		romano = Romano.new
		romano.to_numero("XIV").should == 14
	end
	it "passa XIII e retorna 13" do
		romano = Romano.new
		romano.to_numero("XIII").should == 13
	end
	it "passa CDXLVI e retorna 446" do
		romano = Romano.new
		romano.to_numero("CDXLVI").should == 446
	end
	
end