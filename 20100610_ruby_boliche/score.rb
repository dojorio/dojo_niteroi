require 'array'
require 'frame'

class Score

  def initialize(frames)
    @frames = frames
  end

  def calculate
    score = 0
    @frames.each do |frame|
      frame = Frame.new(frame[0], frame[1])
      return 10 if frame.spare? or frame.strike?
      score += frame.sum
    end
    score
  end

end
