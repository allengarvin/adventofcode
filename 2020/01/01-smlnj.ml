(* needs the 64 bit SML/NJ for part 2, else int overflow *)
open TextIO;
val infile = openIn("/home/agarvin/advent-2020/01-input.txt");

fun readList(file):int list = 
    if endOfStream(file) then nil 
    else valOf(Int.fromString(valOf(inputLine(file)))) :: readList(file);

fun member(lst: int list, elem: int):bool = List.exists (fn x => x = elem) lst;

fun mul(lst: int list): int =
    case lst of
        []   => 1
      | h::t => h * mul(t);

fun solve(xs: int list, ys: int list): int list =
    List.filter (fn x => member(ys, 2020 - x)) xs;

fun append(a: 'x list, b: 'x list) =
    if null a
    then b
    else (hd a) :: (append ((tl a), b));

fun comb_helper(x: int, lst: int list): (int*int) list =
    case lst of
      []   => nil
    | h::t => (x, h) :: comb_helper (x, t);

fun comb2(lst: int list): (int*int) list =
    case lst of
      []   => nil
    | h::t => append(comb_helper(h, t), comb2(t));

val numbers = readList(infile);
val pairs = comb2(numbers);
val pairsums = map (fn x => #1 x + #2 x) pairs;

print("Part 1: " ^ Int.toString (mul(solve(numbers, numbers))) ^ "\n");
print("Part 2: " ^ Int.toString (mul(solve(pairsums, numbers))) ^ "\n");



