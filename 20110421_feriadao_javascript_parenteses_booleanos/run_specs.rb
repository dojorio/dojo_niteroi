require 'rubygems'  
require 'jazz_money'  
  
javascript_files = [  
  'spec/SpecHelper.js',  
  'spec/BooleanSpec.js'  
]  
  
jasmine_spec_files = [  
  'src/boolean.js'
]  
  
a = JazzMoney::Runner.new(javascript_files, jasmine_spec_files)
a.call 

exit ((a.results.include? "expected")? 1 : 0)

