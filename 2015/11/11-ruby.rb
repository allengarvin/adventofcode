#!/opt/ruby3.0/bin/ruby

tests = [
    ->(x) { 'a'.upto('z').each_cons(3).map(&:join).any? { |abc| x.index(abc) } },
    ->(x) { ['i', 'o', 'l'].none? { |c| x.index(c) } },
    ->(x) { 'a'.upto('z').map { |c| c+c }.to_a.select { |c| x.index(c) }.length > 1 } 
]
    
class String
    def from_26
        self.tr("a-z", "0-9a-p").to_i(26)
    end
end

class Integer
    def to_26
        self.to_s(26).tr("0-9a-p", "a-z")
    end
end
        
password = File.read("11-input.txt").chomp.from_26

flag = false

(password+1..Float::INFINITY).each do |p|
    if tests.all? { |x| x.(p.to_26) }
        puts p.to_26
        break if flag
        flag = true
    end
end
