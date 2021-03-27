#!/opt/ruby3.0/bin/ruby

keys = File.readlines("25-input.txt").map(&:to_i)

def transform(subj, keys, setloops)
    val = 1
    (1..Float::INFINITY).each do |cnt|
        val = (val * subj) % 20201227
        if keys.empty?
            return val if cnt == setloops
        else
            keys.each_with_index { |k, i| return cnt, keys[1-i] if val == k }
        end
    end
end

m, k = transform(7, keys, false)
puts transform(k, [], m)
