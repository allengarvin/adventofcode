#!/opt/ruby3.0/bin/ruby

place = File.open("25-input.txt").read().scan(/\d+/).map(&:to_i)
start, p1, mod_p, up_to = 20151125, 252533, 33554393, (place.sum-1) * (place.sum-2) / 2 + place[1] - 1

up_to.times do
    start = (start * p1) % mod_p
end

p start
