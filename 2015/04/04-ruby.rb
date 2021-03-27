#!/opt/ruby3.0/bin/ruby

require 'digest'

key = File.read("04-input.txt").chomp

part1 = nil
(1..Float::INFINITY).each do |n|
    hash = Digest::MD5.hexdigest(key + n.to_s)
    if hash.start_with?("00000")
        part1 = n if !part1
        if hash.start_with?("000000")
            puts part1, n
            exit
        end
    end
end
