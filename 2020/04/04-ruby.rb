#!/opt/ruby3.0/bin/ruby

class String
    def isdigit?
        /^\d+$/
    end
end

validification = {
    'byr' => ->(x) { (1920..2002).member?(x.to_i) },
    'iyr' => ->(x) { (2010..2020).member?(x.to_i) },
    'eyr' => ->(x) { (2020..2030).member?(x.to_i) },
    'hcl' => ->(x) { x.length == 7 && /^#[0-9a-f]*$/.match(x) and true },
    'ecl' => ->(x) { ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].member?(x) },
    'pid' => ->(x) { x.isdigit? and x.length == 9 },
    'cid' => ->(x) { true },
    'hgt' => ->(x) {
        h, unit = x[0..-3], x[-2..-1]
        h.isdigit? && ( (unit == 'cm' && (150..193).member?(h.to_i)) || (unit == "in" && (59..76).member?(h.to_i)) )
    }
}

records = File.read("04-input.txt").split("\n\n").map { |x| x.split().map { |y| y.split(":") }.to_h}
part1 = records.select { |p| p.length == 8 || (p.length == 7 && !p.member?("cid")) }
part2 = part1.select { |h| h.map { |k,v| validification[k].(v) }.inject(:&) }

puts part1.count, part2.count
