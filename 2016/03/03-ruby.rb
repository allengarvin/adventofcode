#!/opt/ruby3.0/bin/ruby

triangles = File.open("03-input.txt").readlines().map { |r| r.split().map(&:to_i) }

def valid(a,b,c) 
    a + b > c && a + c > b && b + c > a 
end

p triangles.filter { |r| valid *r }.length
p triangles.each_slice(3).map(&:transpose).reduce(:+).filter { |r| valid *r }.length
