require 'rubygems'
require 'rspec'
require './split_word'

  def check_break_words(opts)
    it "should return '#{opts[:expected]}' if text is '#{opts[:text]}' and columns is '#{opts[:cols]}'" do
      break_words(opts[:text], opts[:cols]).should == opts[:expected]
    end
  end

describe "Split Words" do

  check_break_words(text: "a", cols: 1, expected: "a")

  check_break_words(text: "b", cols: 1, expected: "b")

  check_break_words(text: "ab", cols: 1, expected: "a\nb")

  check_break_words(text: "a b", cols: 1, expected: "a\nb")

  check_break_words(text: "cd", cols: 1, expected: "c\nd")

  check_break_words(text: "a ", cols: 1, expected: "a")

  check_break_words(text: "abc", cols: 2, expected: "ab\nc")

  check_break_words(text: "ab ", cols: 3, expected: "ab")

end
