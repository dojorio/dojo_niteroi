$LOAD_PATH.unshift(File.dirname(__FILE__))
$LOAD_PATH.unshift(File.join(File.dirname(__FILE__), '..', 'lib'))
require 'quadrado_vazio'
require 'quadrado_preenchido'
require 'spec'
require 'spec/autorun'
require 'grade'

Spec::Runner.configure do |config|
  
end
