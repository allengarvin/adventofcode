#!/opt/ruby3.0/bin/ruby

previous = {}
File.read("15-input.txt").split(",").map(&:to_i).each_with_index { |n,i| previous[n] = i }

next_seq = 0
(previous.length..Float::INFINITY).each do |n|
    puts next_seq if n + 1 == 2020
    if n + 1 == 30000000
        puts next_seq
        exit
    end

    last = { next_seq => n }
    next_seq = n - previous.fetch(next_seq, n)
    previous.update(last)
end
