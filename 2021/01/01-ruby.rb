#!/opt/ruby3.0/bin/ruby

def count_asc(ls)
   return ls[..-2].zip(ls[1..]).filter { |a,b| b>a }.length
end

nums = File.open("01-input.txt").readlines().map(&:to_i)
puts count_asc(nums)
puts count_asc(nums[..-3].zip(nums[1..-2], nums[2..]).map(&:sum))
