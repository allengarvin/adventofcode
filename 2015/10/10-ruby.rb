#!/opt/ruby3.0/bin/ruby

class String
    def look_say
        gsub(/(.)\1*/){|s| s.size.to_s + s[0]}
    end
end

number = File.open("10-input.txt").read.chomp

(1..50).each do |n|
    number = number.look_say
    puts number.length if n == 40 || n == 50
end
