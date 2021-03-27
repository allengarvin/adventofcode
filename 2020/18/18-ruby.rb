#!/opt/ruby3.0/bin/ruby

expressions = File.readlines("18-input.txt").map(&:chomp)

class Integer
    def -(x)
        self * x
    end

    def /(x)
        self + x
    end
end

puts expressions.map { |x| eval(x.tr("*", "-")) }.sum, expressions.map { |x| eval(x.tr("*+", "-/")) }.sum
