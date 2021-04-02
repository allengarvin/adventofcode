#!/usr/bin/ruby

require 'prime'

p (108100..(108100+17000)).step(17).select { |n| !Prime.prime?(n) }.length

